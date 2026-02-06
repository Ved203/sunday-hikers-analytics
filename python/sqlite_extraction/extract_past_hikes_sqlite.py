import requests
import sqlite3
import re
from html import unescape

PAGE_ID = 340
API_URL = f"https://public-api.wordpress.com/wp/v2/sites/sundayhikerspune.wordpress.com/pages/{PAGE_ID}"
DB_NAME = "past_hikes.db"

conn = sqlite3.connect(DB_NAME)
cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS past_hikes_summary (
    year INTEGER NOT NULL,
    event_type TEXT NOT NULL,
    count INTEGER NOT NULL,
    specifics TEXT,
    PRIMARY KEY (year, event_type)
)
""")
conn.commit()

response = requests.get(API_URL)
response.raise_for_status()
page_data = response.json()

html_content = unescape(page_data["content"]["rendered"])

year_blocks = re.split(r"(20\d{2})", html_content)

records = []
current_year = None

for block in year_blocks:
    if re.fullmatch(r"20\d{2}", block):
        current_year = int(block)
    elif current_year:
        rows = re.findall(
            r"<tr>.*?<td.*?>(.*?)</td>.*?"
            r"<td.*?>(\d+)</td>.*?"
            r"<td.*?>(.*?)</td>.*?</tr>",
            block,
            re.DOTALL
        )

        for event_type, count, specifics in rows:
            records.append((
                current_year,
                re.sub("<.*?>", "", event_type).strip(),
                int(count),
                re.sub("<.*?>", "", specifics).strip()
            ))

for rec in records:
    cursor.execute("""
        INSERT INTO past_hikes_summary (year, event_type, count, specifics)
        VALUES (?, ?, ?, ?)
        ON CONFLICT(year, event_type)
        DO UPDATE SET
            count = excluded.count,
            specifics = excluded.specifics
    """, rec)

conn.commit()
conn.close()

print(" Data stored successfully")


import sqlite3

conn = sqlite3.connect("past_hikes.db")
cursor = conn.cursor()

cursor.execute("SELECT * FROM past_hikes_summary LIMIT 10;")
rows = cursor.fetchall()

for row in rows:
    print(row)

conn.close()
