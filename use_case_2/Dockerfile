FROM python:3.12-slim
WORKDIR /app
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
COPY clean_data.py .
COPY sample_data.csv .
CMD ["python", "clean_data.py"]
