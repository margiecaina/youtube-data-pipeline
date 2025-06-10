# YouTube Trending Data Engineering Pipeline (AWS Serverless)

This project simulates a real-world data engineering workflow for ingesting, processing, and analyzing YouTube trending video category data using serverless architecture on AWS.

It is inspired by Darshil Parmar’s YouTube Data Engineering series and showcases how to work with semi-structured data at scale using cloud-native tools.

---

## 🚀 Project Objectives

- Ingest and process JSON metadata of trending YouTube video categories (~40K rows per region).
- Build a scalable, serverless ETL pipeline on AWS.
- Convert semi-structured JSON to Parquet and enable query access via Amazon Athena.
- Store and catalog data efficiently using S3 and AWS Glue.
- Simulate a basic data lake architecture with raw, processed, and analytics zones.

---

## 🛠️ Tools & Services Used

| Tool/Service       | Purpose                                       |
|--------------------|-----------------------------------------------|
| **AWS Lambda**     | Serverless compute for data ingestion & ETL   |
| **Amazon S3**      | Scalable object storage for data lake         |
| **AWS Glue**       | Data cataloging and schema management         |
| **Amazon Athena**  | SQL-based querying on S3-stored datasets      |
| **awswrangler**    | Pandas + AWS glue integration                 |
| **Python**         | Data ingestion, transformation, orchestration |

---

## 📁 Architecture Overview

```plaintext
    +--------------------------+
    |  JSON video data (mock)  |
    +------------+-------------+
                 |
        Triggered by file upload
                 ↓
         +---------------+
         | AWS S3 (Raw)  |
         +---------------+
                 ↓
        +------------------+
        | AWS Lambda (ETL) |
        +------------------+
                 ↓
         +---------------+
         | S3 (Processed)|
         +---------------+
                 ↓
        +-----------------+
        | AWS Glue Catalog|
        +-----------------+
                 ↓
        +----------------+
        | Amazon Athena  |
        +----------------+
```


## 📊 Dataset

This project uses the [Trending YouTube Video Statistics dataset](https://www.kaggle.com/datasets/datasnaek/youtube-new) from Kaggle.

The dataset contains daily records of trending YouTube videos across multiple regions (e.g., US, CA, GB, etc.).

Each region has its own CSV file (~40K rows), including metadata like video title, channel, tags, views, likes, and comment count.

A separate JSON file contains `category_id` mappings to category names for each region.

The data was ingested from raw `.csv` and `.json` formats and processed through an AWS-based ETL pipeline.

**Credit:** [Datasnaek on Kaggle](https://www.kaggle.com/datasets/datasnaek/youtube-new)

