import pickle

import click
import pandas as pd


@click.command()
@click.option("--input_file", type=click.Path(exists=True))
def predict(input_file):
    print(f"Loading data from {input_file}")
    with open("model.bin", "rb") as f_in:
        dv, model = pickle.load(f_in)

    categorical = ["PULocationID", "DOLocationID"]

    def read_data(filename):
        df = pd.read_parquet(filename)

        df["duration"] = df.tpep_dropoff_datetime - df.tpep_pickup_datetime
        df["duration"] = df.duration.dt.total_seconds() / 60

        df = df[(df.duration >= 1) & (df.duration <= 60)].copy()

        df[categorical] = df[categorical].fillna(-1).astype("int").astype("str")

        return df

    df = read_data(input_file)

    # In[8]:

    dicts = df[categorical].to_dict(orient="records")
    X_val = dv.transform(dicts)
    y_pred = model.predict(X_val)

    # In[10]:

    y_pred.std()

    # In[ ]:

    df["ride_id"] = f"{2023:04d}/{3:02d}_" + df.index.astype("str")

    # In[ ]:

    df_result = df[["ride_id"]].copy(deep=True)
    df_result["prediction"] = y_pred

    df_result.to_parquet(
        "predictions.parquet",
        engine="pyarrow",
        compression=None,
        index=False,
    )

    print(y_pred.mean())


if __name__ == "__main__":
    predict()
    print("Done!")