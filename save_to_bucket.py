from google.cloud import storage
import pandas as pd 
import os
from secret_getter import get_service_account_credentials
import logging

logging.basicConfig(level=logging.INFO)

# def delete_existing_files(bucket_name):

#     """Delete all files in the specified GCS bucket."""
#     # creds = get_service_account_credentials()
#     client = storage.Client()
#     bucket = client.bucket(bucket_name)
#     # List and delete all blobs in the bucket
#     blobs = bucket.list_blobs()
#     for blob in blobs:
#         print(f"Deleting file: {blob.name}")
#         logging.info(f"deleting file ....: {blob.name}")
#         blob.delete()

def upload_to_gcs(bucket_name, source_file_name, destination_blob_name):
    # creds = get_service_account_credentials()
    client = storage.Client()
    bucket = client.bucket(bucket_name)
    blob = bucket.blob(destination_blob_name)
    blob.upload_from_filename(source_file_name)
    print(f"Uploaded {source_file_name} to {destination_blob_name}")
    logging.info(f"Uploaded {source_file_name} to {destination_blob_name}")

def save_to_storage(df, term, username):
    logging.info(f"Saving data for term: {term}")
    try:
        today_date = pd.to_datetime('today').strftime('%Y-%m-%d-%h')
        file_name = f"tenders_{term}_{today_date}_{username}.xlsx"
        #f.to_excel(file_name, index=False)
        #logging.info(f"File saved locally: {file_name}")

        bucket_name = "tenders-excel-files"
        logging.info(f"deleting file ....: {term}/{file_name}")
        # delete_existing_files(bucket_name)
        logging.info(f"file deleted ....: {term}/{file_name}")
        upload_to_gcs(bucket_name, file_name, f"{term}/{file_name}")
        logging.info(f"File uploaded to GCS: {term}/{file_name}")

        os.remove(file_name)
    except Exception as e:
        logging.error(f"Error in save_to_storage: {str(e)}")
        raise
