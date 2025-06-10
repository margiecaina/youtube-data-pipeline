import awswrangler as wr
import pandas as pd
import urllib.parse
import os

# Environment variables
os_input_s3_cleansed_layer = os.environ['s3_cleansed_layer']
os_input_glue_catalog_db_name = os.environ['glue_catalog_db_name']
os_input_glue_catalog_table_name = os.environ['glue_catalog_table_name']
os_input_write_data_operation = os.environ['write_data_operation']


def lambda_handler(event, context):
    for record in event['Records']:
        bucket = record['s3']['bucket']['name']
        key = urllib.parse.unquote_plus(record['s3']['object']['key'], encoding='utf-8')
        
        try:
            # Only process JSON files
            if not key.endswith('.json'):
                print(f"Skipping non-JSON file: {key}")
                continue

            print(f"Processing file: s3://{bucket}/{key}")

            # Read JSON
            df_raw = wr.s3.read_json(f's3://{bucket}/{key}')

            # If it's a dictionary with 'items', normalize it
            if isinstance(df_raw, dict) and 'items' in df_raw:
                df_step_1 = pd.json_normalize(df_raw['items'])
            else:
                # Fallback: try normalizing full object or treating as flat
                df_step_1 = pd.json_normalize(df_raw)

            # Write to S3 and Glue Catalog
            wr_response = wr.s3.to_parquet(
                df=df_step_1,
                path=os_input_s3_cleansed_layer,
                dataset=True,
                database=os_input_glue_catalog_db_name,
                table=os_input_glue_catalog_table_name,
                mode=os_input_write_data_operation
            )

            print(f"Write successful for file: {key}")
            return wr_response
        
        except Exception as e:
            print(f"Error processing file: {key}")
            print(e)
            raise e
