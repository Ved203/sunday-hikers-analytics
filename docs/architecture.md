# System Architecture

## Overview

The Sunday Hikers Analytics Pipeline is an end-to-end ETL (Extract, Transform, Load) solution designed to collect hiking event data from the Sunday Hikers website, process and store it in a structured database, and generate interactive analytics dashboards.

The architecture consists of four main layers: Data Source, Data Extraction & Transformation, Data Storage, and Data Visualization.

---

## Architecture Diagram

<img width="486" height="577" alt="image" src="https://github.com/user-attachments/assets/bc931b98-07e6-4876-b2a5-ad764ea61c44" />

---

## 1. Data Source Layer

### WordPress REST API

The Sunday Hikers website serves as the primary data source for the project. Data is accessed through the WordPress REST API, which provides structured information about hiking events, including event titles, dates, categories, locations, and participant details.

The API enables automated data retrieval without requiring manual data collection, ensuring scalability and consistency.

**Responsibilities:**

* Provide event data through REST endpoints
* Deliver structured JSON responses
* Support automated data extraction

---

## 2. Data Extraction and Transformation Layer

### Python ETL Pipeline

The ETL pipeline is developed using Python and is responsible for extracting, cleaning, and transforming the data before loading it into the database.

The extraction process utilizes the Requests library to communicate with the WordPress REST API. HTML content embedded within API responses is parsed using BeautifulSoup to extract detailed event information.

After extraction, the data undergoes several transformation steps:

* Removal of unwanted HTML tags
* Handling of missing or inconsistent values
* Standardization of event categories
* Data validation and formatting
* Duplicate record detection

**Technologies Used:**

* Python
* Requests
* BeautifulSoup
* Pandas

**Responsibilities:**

* Extract data from WordPress API
* Parse and clean HTML content
* Transform raw data into structured format
* Prepare records for database storage

---

## 3. Data Storage Layer

### PostgreSQL Database (Supabase)

The transformed data is stored in a PostgreSQL database hosted on Supabase. PostgreSQL serves as the centralized repository for all hiking event records.

The database schema is designed to support efficient querying, reporting, and future scalability. UPSERT operations are implemented to prevent duplicate entries and maintain data integrity during repeated ETL executions.

**Responsibilities:**

* Store structured hiking event data
* Maintain data consistency
* Support analytical queries
* Enable secure cloud-based storage

**Technology Used:**

* PostgreSQL
* Supabase

---

## 4. Data Visualization Layer

### Power BI Dashboard

Power BI is used to connect directly to the PostgreSQL database and create interactive dashboards for data analysis and reporting.

The dashboard provides visual insights into hiking activities through charts, KPIs, filters, and trend analyses.

Key analytics include:

* Total hiking events
* Monthly and yearly event trends
* Popular hiking routes
* Event category distribution
* Seasonal participation patterns
* Geographic analysis of hiking locations

**Responsibilities:**

* Data visualization
* Business intelligence reporting
* Trend analysis
* Interactive exploration of data

---

## Data Flow

1. Data is fetched from the Sunday Hikers WordPress REST API.
2. The Python ETL pipeline extracts and processes the data.
3. Cleaned data is loaded into PostgreSQL (Supabase).
4. Power BI retrieves data from PostgreSQL.
5. Interactive dashboards generate insights and reports.

---

## Key Features

* Automated data extraction from WordPress
* Data cleaning and transformation using Python
* Cloud-based PostgreSQL storage with Supabase
* Interactive Power BI dashboards
* Scalable ETL architecture
* Automated duplicate handling using UPSERT operations
* Support for future data expansion and advanced analytics

---

## Benefits of the Architecture

* Reduces manual data collection effort
* Ensures consistent and accurate data processing
* Enables centralized data management
* Provides real-time analytical insights
* Supports future enhancements and scalability

This architecture demonstrates the integration of Data Engineering, Database Management, and Business Intelligence technologies to build a complete analytics solution for hiking event data.


