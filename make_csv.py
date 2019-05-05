import csv
import sqlite3
from glob import glob; from os.path import expanduser

conn = sqlite3.connect('data-science-term-project/combined_data.db')
cursor = conn.cursor()
cursor.execute("select * from economic_health_la LEFT OUTER JOIN food_security on economic_health_la.zip_code = food_security.zip_code ;")

with open("out.csv", "w", newline='') as csv_file:  # Python 3 version    
# with open("out.csv", "wb") as csv_file:              # Python 2 version
    csv_writer = csv.writer(csv_file)
    csv_writer.writerow([i[0] for i in cursor.description]) # write headers
    csv_writer.writerows(cursor)