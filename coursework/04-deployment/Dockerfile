FROM agrigorev/zoomcamp-model:mlops-2024-3.10.13-slim

WORKDIR /app

COPY . .

RUN pip install click pandas scikit-learn pyarrow

CMD ["python", "starter.py", "--input_file", "yellow_tripdata_2023-05.parquet"]