# Sunday Hikers Analytics
### End-to-End Data Analytics Project using Python, PostgreSQL (Supabase), and Power BI

This project automates the collection, processing, storage, and visualization of historical hiking event data from the Sunday Hikers website.
The solution leverages the WordPress REST API, Python-based ETL workflows, PostgreSQL cloud storage, and Power BI dashboards to transform unstructured web data into actionable business insights.



---


## Business Problem

Historical hiking event data was stored in HTML tables across multiple WordPress pages, making trend analysis difficult and time-consuming.

The objective was to create an automated analytics platform that centralizes historical event data and provides interactive insights through dashboards.

---


## System Architecture


<img width="492" height="587" alt="image" src="https://github.com/user-attachments/assets/68cfd5fa-39b7-4d21-b827-17e6f6a39ddc" />

---

## Key Features

✔ Automated data extraction from WordPress REST API

✔ HTML table parsing using BeautifulSoup

✔ Dynamic year-wise event classification

✔ Cloud-based PostgreSQL storage

✔ UPSERT logic for incremental updates

✔ Interactive Power BI dashboards

✔ End-to-End ETL workflow

---

## Tech Stack

| Category | Technologies |
|-----------|--------------|
| Language | Python |
| Data Extraction | Requests, BeautifulSoup |
| Database | PostgreSQL, Supabase |
| Data Validation | SQLite |
| Visualization | Power BI |
| Version Control | Git, GitHub |


---

## ETL Workflow

### Extract
- Fetch data using WordPress REST API
- Retrieve archived hike pages

### Transform
- Parse HTML tables using BeautifulSoup
- Remove summary tables
- Standardize event information

### Load
- Store validated records in PostgreSQL
- Perform UPSERT operations

---

## Dashboard Preview

<img width="1280" height="720" alt="image" src="https://github.com/user-attachments/assets/48c42bc1-221b-478c-bc44-0fb3fea05ad3" />



## Insights Generated

- Year-wise hiking activity trends



- Monthly event distribution
- Popular trekking locations
- Seasonal hiking patterns
- Historical participation analysis


## Future Enhancements

- Automated scheduling using GitHub Actions
- Real-time dashboard refresh

