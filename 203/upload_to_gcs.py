from pathlib import Path
from prefect import flow, task
from prefect_gcp.cloud_storage import GcsBucket


@flow()
def upload_to_gcs(color: str, year: int, month: int) -> None:
    """The main flow function to upload taxi data"""
    path = Path(f"data/{color}/{year}/{color}_tripdata_{year}-{month:02}.parquet")
    gcs_block = GcsBucket.load("pacc-gcs-bucket")
    gcs_block.upload_from_path(from_path=path, to_path=path)


if __name__ == "__main__":
    upload_to_gcs(color="green", year=2020, month=1)
