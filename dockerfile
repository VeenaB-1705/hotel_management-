FROM python:3.12

WORKDIR /app

COPY hotel_management.py .

CMD ["python", "hotel_management.py"]