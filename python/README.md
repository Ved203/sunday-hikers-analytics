## Python Data Pipeline

This folder contains Python scripts used to extract, clean, and store
Sunday Hikers data from the WordPress website into databases used for analysis.

---

### SQLite Version (Initial Prototype)
**Path:** `python/sqlite_extraction/`

- Script: `extract_past_hikes_sqlite.py`
- Purpose:
  - Initial validation of data extraction logic
  - Parsing HTML tables from the WordPress "Past Hikes" page
  - Storing year-wise event data in a local SQLite database
- Note:
  - SQLite was used only for early testing
  - It is system-dependent and not suitable for shared BI dashboards

---

### PostgreSQL Version (Production Pipeline)
**Path:** `python/postgres_extraction/`

- Script: `extract_past_hikes_postgres.py`
- Purpose:
  - Extract structured data from WordPress REST API
  - Identify correct year for each event table
  - Exclude cumulative summary sections to avoid incorrect counts
  - Store and update data in a cloud PostgreSQL database (Supabase)
- Key Features:
  - Idempotent inserts using `ON CONFLICT` (UPSERT)
  - Cloud-based storage for multi-user access
  - Designed for Power BI integration

---

### Execution Notes
- Database credentials are not hardcoded in the repository
- Credentials should be supplied via environment variables or secure configuration
- Scripts are intended to be run manually or via scheduling (future enhancement)
