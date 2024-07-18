from fastapi import APIRouter, HTTPException
from app.api.deps import DBSESSIONDEPS, PRODUCERDEPS
from app.core.crud import (
    get_product,
    get_record_product,
    get_records,
    get_suppliers,
    single_product,
    update_inventory,
    get_inventory,
    add_supplier,
    update_record,
)
from app import product_pb2
from app.core.controllers import verify_admin_key
from app.models import Inventory, Product, Record, Suppliers
from app.settings import KAFKA_TOPIC

endpoint_router = APIRouter(tags=["Endpoint Routes"])


@endpoint_router.get("/get/stock/products")
def get_products_route(session: DBSESSIONDEPS):
    products = get_product(session=session)
    return products


@endpoint_router.post("/admin/add/stock/product", response_model=Product)
async def add_product_route(admin_key: str, product: Product , producer:PRODUCERDEPS):
    is_admin = verify_admin_key(key=admin_key)
    if not admin_key:
        raise HTTPException(status_code=404, detail="Admin Key Is Invalid")
    else:
        product_proto =  product_pb2.Product(id=product.id , name=product.name , price=product.price , description = product.description , category_id=product.category_id) # type: ignore
        serialized_string = product_proto.SerializeToString()
        await producer.send_and_wait(KAFKA_TOPIC, serialized_string)
        return {"message": "Product added successfully"}


@endpoint_router.get("/get-stock-product{id}")
def get_product_route(id: int, session: DBSESSIONDEPS):
    product = single_product(session, id)
    return product


@endpoint_router.put("/admin/update-inventory")
def update_inventory_route(
    admin_key: str, inventory: Inventory, session: DBSESSIONDEPS
):
    is_admin = verify_admin_key(key=admin_key)
    if not is_admin:
        raise HTTPException(status_code=404, detail="Admin Key Is Invalid")
    else:
        update_inventory(inventory, session)
        return inventory


@endpoint_router.get("/admin/get-inventory-record")
def get_inventory_record(admin_key: str, session: DBSESSIONDEPS):
    is_admin = verify_admin_key(key=admin_key)
    if not is_admin:
        raise HTTPException(status_code=404, detail="Admin Key Is Invalid")
    else:
        inventory = get_inventory(session)
        return inventory


@endpoint_router.post("/admin/add-supplier")
def add_supplier_route(admin_key: str, supplier: Suppliers, session: DBSESSIONDEPS):
    is_admin = verify_admin_key(key=admin_key)
    if not is_admin:
        raise HTTPException(status_code=404, detail="Admin Key Is Invalid")
    else:
        add_supplier(supplier=supplier, session=session)
        return supplier


@endpoint_router.get("/admin/get-suppliers")
def get_suppliers_route(admin_key: str, session: DBSESSIONDEPS):
    is_admin = verify_admin_key(key=admin_key)
    if not is_admin:
        raise HTTPException(status_code=404, detail="Admin Key Is Invalid")
    else:
        suppliers = get_suppliers(session)
        return suppliers


@endpoint_router.put("/admin/update-record")
def update_record_route(admin_key: str, record: Record, session: DBSESSIONDEPS):
    is_admin = verify_admin_key(key=admin_key)
    if not is_admin:
        raise HTTPException(status_code=404, detail="Admin Key Is Invalid")
    else:
        update_record(record, session)
        return record


@endpoint_router.get("/admin/get-records")
def get_record_route(admin_key: str, session: DBSESSIONDEPS):
    is_admin = verify_admin_key(key=admin_key)
    if not is_admin:
        raise HTTPException(status_code=404, detail="Admin Key Is Invalid")
    else:
        records = get_records(session)
        return records


@endpoint_router.get("/admin/get-product-record/{product_id}")
def get_product_record_route(product_id: int, admin_key: str, session: DBSESSIONDEPS):
    is_admin = verify_admin_key(key=admin_key)
    if not is_admin:
        raise HTTPException(status_code=404, detail="Admin Key Is Invalid")
    else:
        record = get_record_product(product_id, session)
        return record
