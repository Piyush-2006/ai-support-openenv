FROM python:3.9

WORKDIR /app

COPY . .

RUN pip install pydantic

CMD ["python", "inference.py"]