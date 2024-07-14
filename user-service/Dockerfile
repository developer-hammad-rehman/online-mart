FROM python:3.12


WORKDIR /code/


RUN pip install poetry


COPY ./pyproject.toml ./poetry.lock /code/

RUN poetry config virtualenvs.create false

RUN poetry install

COPY ./ /code/


EXPOSE 8081

CMD ["poetry" , "run" , "uvicorn" , "app.main:app" , "--reload" , "--host" , "0.0.0.0" , "--port"  , "8081"]