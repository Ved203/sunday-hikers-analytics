import requests
import psycopg2 
from bs4 import BeautifulSoup
import re
from datetime import datetime

SITE_API = "https://public-api.wordpress.com/rest/v1.1/sites/sundayhikerspune.wordpress.com/posts?type=page&number=50"
TARGET_SLUG = "past-hikes"

DB_CONFIG = {
    "host": "DB_hostname",
    "database": "postgres",
    "user": "DB_username",
    "password": "DB_password",
    "port": DBport_number
}

print("Fetching website data...")


# 1️ Fetch data from WordPress API
response = requests.get(SITE_API, timeout=30)
response.raise_for_status()
data = response.json()

# 2️ Find the "Past Hikes" page
target_page = None
for post in data["posts"]:
    if post["slug"] == TARGET_SLUG:
        target_page = post
        break

if not target_page:
    raise Exception(" Past Hikes page not found")

print(" Found Past Hikes page")

# 3️ Parse HTML
soup = BeautifulSoup(target_page["content"], "html.parser")

# 4️ Connect to database
conn = psycopg2.connect(**DB_CONFIG)
cursor = conn.cursor()

#5 create table if not exist 
cursor.execute("""
CREATE TABLE IF NOT EXISTS past_hikes_summary (
    year INTEGER,
    event_type TEXT,
    count INTEGER,
    specifics TEXT,
    last_updated TIMESTAMP,
    PRIMARY KEY (year, event_type)
);
""")
conn.commit()

#6 Load existing data for change detection
cursor.execute("SELECT year, event_type, count FROM past_hikes_summary")
old_data = {(r[0], r[1]): r[2] for r in cursor.fetchall()}

new_rows = []


# 7 Extract tables and detect years

tables = soup.find_all("table")

for table in tables:
    year = None
    prev = table.find_previous(["h1", "h2", "h3", "h4", "p", "strong"])
    steps = 0
    skip_table = False

    while prev and steps < 7:
        heading_text = prev.get_text(strip=True).lower()

        # Skip cumulative / summary section
        if "total" in heading_text and "since" in heading_text:
            skip_table = True
            break

        # Extract explicit year headings only
        match = re.search(r"\b(2022|2023|2024|2025|2026)\b", heading_text)
        if match:
            year = int(match.group())
            break

        prev = prev.find_previous(["h1", "h2", "h3", "h4", "p", "strong"])
        steps += 1

    #  Skip summary tables or tables without year
    if skip_table or year is None:
        print(" Skipping non-year table")
        continue

    #  Process valid year tables
    rows = table.find_all("tr")
    for row in rows:
        cols = row.find_all("td")
        if len(cols) >= 3:
            event_type =  cols[0].get_text(strip=True)
            count =       cols[1].get_text(strip=True)
            specifics =   cols[2].get_text(strip=True)

            if not count.isdigit():
                continue

            count = int(count)
           

            

            new_rows.append((
                year,
                event_type,
                count,
                specifics,
                datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            ))


# 6️ Update database
for r in new_rows:
    cursor.execute("""
        INSERT INTO past_hikes_summary
        (year, event_type, count, specifics, last_updated)
        VALUES (%s, %s, %s, %s, %s)
        ON CONFLICT(year, event_type)
        DO UPDATE SET
            count = excluded.count,
            specifics = excluded.specifics,
            last_updated = excluded.last_updated
    """, r)

conn.commit()
cursor.close()
conn.close()


print(" Completed Sucessfully ")

