from fastapi import APIRouter, HTTPException, Request
import stripe
from app.depends import PRODUCER
from fastapi.responses import RedirectResponse
from app.settings import KAFKA_TOPIC, STRIPE_KEY
from stripe._error import SignatureVerificationError
from app import payment_pb2


stripe.api_key = STRIPE_KEY


router = APIRouter()

# =========================================================================================================================================


@router.get("/checkout")
async def create_checkout_session(
    amount: int,
    quantity: int,
    product_name: str,
    is_online_mart_assistant: bool = False,
):
    try:
        # Create a new checkout session
        session = stripe.checkout.Session.create(
            payment_method_types=["card", "link"],
            line_items=[
                {
                    "price_data": {
                        "currency": "usd",
                        "product_data": {
                            "name": product_name,
                        },
                        "unit_amount": amount * 100,
                    },
                    "quantity": quantity,
                },
            ],
            mode="payment",
            success_url=f"https://martnest.vercel.app/payment/sucess?amount={amount}",
            cancel_url="https://martnest.vercel.app/payment/fail",
        )

        if not is_online_mart_assistant:
            return RedirectResponse(session.url)  # type: ignore

        return f"Redirect to this url {session.url} for payment"

    except Exception as e:
        print("Payment Session Failed")
        raise HTTPException(status_code=400, detail=str(e))


# ======================================================================================================================================================================


@router.post("/webhook")
async def stripe_webhook_route(request: Request, producer: PRODUCER):
    payload = await request.json()
    try:
        event = stripe.Event.construct_from(payload, stripe.api_key)
    except ValueError as ve:
        print(f"Value error: {str(ve)}")
        raise HTTPException(status_code=400, detail=str(ve))
    except SignatureVerificationError as e:
        print(f"Signature verification error: {str(e)}")
        raise HTTPException(status_code=400, detail=str(e))

    if event["type"] == "checkout.session.completed":
        session = event["data"]["object"]
        print(session)
        proto_buf = payment_pb2.Payment(amount=session["amount_total"]/100, currency="usd", status="succeded", type="card")  # type: ignore
        encode_string = proto_buf.SerializeToString()
        await producer.send_and_wait(KAFKA_TOPIC, encode_string)
    return {"status": "success"}

#=========================================================================================================================================================================== 