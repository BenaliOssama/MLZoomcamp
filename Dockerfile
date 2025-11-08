FROM agrigorev/zoomcamp-model:2025

WORKDIR /app

# Copy project files and the model
COPY requirements.txt .
COPY app.py .
COPY pipeline_v1.bin .

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Expose FastAPI port
EXPOSE 8000

# Run FastAPI
CMD ["uvicorn", "app:app", "--host", "0.0.0.0", "--port", "8000"]

