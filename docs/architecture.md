## System Architecture

### Phase 1
WordPress API → Python → SQLite -> PowerBI file
(Purpose: data validation and schema design)

### Phase 2
WordPress API → Python → PostgreSQL -> PowerBI file

The Sunday Hikers Analytics Pipeline follows an ETL (Extract, Transform, Load) architecture to collect, process, store, and visualize hiking event data.

WordPress REST API (Data Source)
The system retrieves hiking event data from the Sunday Hikers website using the WordPress REST API.

The API provides structured information about past hiking events, including event names, dates, locations, and participant details.

Python ETL Pipeline (Data Processing Layer)

A Python-based ETL pipeline extracts data from the WordPress REST API using the Requests library.

BeautifulSoup is used to parse HTML content and extract relevant information from event tables.

The extracted data is cleaned, transformed, and standardized to ensure consistency and accuracy before storage.

PostgreSQL (Supabase) (Data Storage Layer)

The processed data is loaded into a PostgreSQL database hosted on Supabase.

The database stores structured hiking event records and supports efficient querying.

UPSERT operations are used to prevent duplicate records and maintain data integrity.

Power BI Dashboard (Visualization Layer)

Power BI connects directly to the PostgreSQL database through ODBC.

Interactive dashboards are created to analyze hiking trends, participant statistics, seasonal patterns, route popularity, and event categories.

The dashboard provides actionable insights through charts, KPIs, and filters.
