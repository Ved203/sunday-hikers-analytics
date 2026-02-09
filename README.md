# Sunday Hikers Data Pipeline

## Overview
This project builds an automated data pipeline that extracts structured data from the Sunday Hikers WordPress website, stores it in a database, and enables analytical visualization through Power BI.

The objective is to create a scalable and shareable analytics workflow for historical hiking events.

---

## Data Source
- **Source:** Sunday Hikers WordPress Website
- **Access Method:** WordPress REST API
- **Target Page:** "Past Hikes"

---

## System Architecture

WordPress API → Python ETL → PostgreSQL (Supabase) → Power BI Dashboard

### Initial Validation Architecture
WordPress API → Python → SQLite (Local)

---

## Project Progress

### Phase 1 – Data Extraction & Validation
- Extracted data using WordPress REST API
- Parsed HTML tables using BeautifulSoup
- Classified events year-wise
- Stored structured data in SQLite for initial validation

### Phase 2 – Database Migration
- Identified SQLite limitations (system-dependent, non-shareable)
- Migrated storage to cloud-based PostgreSQL (Supabase)
- Implemented UPSERT logic for reliable updates
- Designed normalized table structure

### Phase 3 – BI Integration
- Connected PostgreSQL database to Power BI using ODBC
- Enabled centralized and shareable analytics access

---

## Current Features
- Automated data extraction from WordPress
- Dynamic year detection from page structure
- Exclusion of cumulative summary tables
- Cloud database storage (PostgreSQL)
- Power BI integration for visualization

---

## Repository Structure

