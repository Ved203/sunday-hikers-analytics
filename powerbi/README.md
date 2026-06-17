# Power BI Dashboard

## Overview

The Sunday Hikers Activity Analytics Dashboard is an interactive Business Intelligence solution developed using Power BI. It provides insights into hiking activities conducted by the Sunday Hikers community by transforming historical event data into meaningful visualizations and performance metrics.

The dashboard enables users to analyze activity trends, monitor category-wise performance, and identify the most popular hiking activities over time.

---

## Dashboard Objectives

* Analyze hiking activities conducted over multiple years.
* Identify the most popular activity categories.
* Monitor yearly activity trends.
* Provide data-driven insights for future event planning.
* Enable interactive exploration through filters and slicers.

---

## Data Source

The dashboard is powered by data collected from the Sunday Hikers website through an automated ETL pipeline.

### Data Flow

```text
WordPress REST API
        │
        ▼
Python ETL Pipeline
(Requests + BeautifulSoup)
        │
        ▼
PostgreSQL (Supabase)
        │
        ▼
Power BI Dashboard
```

---

## Key Performance Indicators (KPIs)

The dashboard highlights the following key metrics:

| KPI                        | Value           |
| -------------------------- | --------------- |
| Total Activities Conducted | 429             |
| Activity Categories        | 10              |
| Top Performing Activity    | City Hill Hikes |

---

## Dashboard Components

### 1. Total Activities Conducted

Displays the total number of hiking and community activities recorded in the dataset.

**Insight:**
A total of 429 activities have been conducted and analyzed.

---

### 2. Activity Categories

Shows the total number of unique activity categories.

**Insight:**
The dataset contains 10 distinct activity categories.

---

### 3. Top Performing Activity

Highlights the activity category with the highest number of events.

**Insight:**
City Hill Hikes is the most frequently conducted activity.

---

### 4. Activity Distribution by Category

A bar chart showing the number of activities conducted for each category.

Key categories include:

* City Hill Hikes
* Fort Hikes
* Range Treks
* Eco-Birthdays and Tree Plantation Activities
* Inspirational Talks and Health Sessions
* Divine Walks
* Historical Theme Programs

**Purpose:**

* Compare category popularity
* Identify high-engagement activities
* Support future event planning

---

### 5. Category-wise Activity Summary

A detailed table displaying activity counts for each category.

**Purpose:**

* Provide precise activity counts
* Enable category-level analysis
* Support reporting requirements

---

### 6. Year-wise Activity Trend

A line chart visualizing activity growth over time.

| Year | Activities |
| ---- | ---------- |
| 2022 | 50         |
| 2023 | 82         |
| 2024 | 97         |
| 2025 | 136        |
| 2026 | 64         |

**Insights:**

* Activity participation increased steadily from 2022 to 2025.
* The highest activity count was recorded in 2025.
* The lower count for 2026 reflects partial-year data collection.

---

## Interactive Features

The dashboard includes dynamic filters that allow users to explore data based on:

### Year Filter

Analyze activities for a specific year.

### Event Filter

Focus on a particular activity category.

These filters automatically update all visualizations and KPIs.

---

## Key Insights

* City Hill Hikes is the most popular activity category with 179 events.
* Fort Hikes is the second most popular category with 130 events.
* More than 70% of all activities belong to City Hill Hikes and Fort Hikes.
* Activity participation has shown consistent growth over recent years.
* The organization has successfully diversified activities across 10 categories.

---

## Technologies Used

* Power BI Desktop
* Power Query
* DAX
* PostgreSQL
* Supabase
* Python ETL Pipeline

---

## Dashboard Preview

### Main Dashboard


<img width="1272" height="711" alt="image" src="https://github.com/user-attachments/assets/1edbd683-dca0-4e97-b27c-40fffc346786" />


---

## Future Enhancements

Planned improvements include:

* Route-wise hiking analytics
* Geographic map visualizations
* Participant trend analysis
* Real-time dashboard refresh
* Predictive trend forecasting using machine learning

---

## File

```text
sunday_updates.pbix
```

Open the PBIX file using Power BI Desktop to explore the complete interactive dashboard.


