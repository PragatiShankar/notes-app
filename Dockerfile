FROM python:3.12-slim
WORKDIR /app
COPY requirements.txt .
RUN pip install -r requirement.txt
COPY . .
EXPOSE 5000
CMD ["python", "app.py"]