import numpy as np
import matplotlib.pyplot as plt
import sqlite3

conn = sqlite3.connect('combined_data.db')
c = conn.cursor()

sql_command = "SELECT f.zip_code, f.one_km_sm, f.three_km_sm, f.one_km_ff, f.three_km_ff, e.income from food_security as f INNER JOIN economic_health_la as e on f.zip_code = e.zip_code;"
c.execute(sql_command)
result = c.fetchall()

data = {}
for r in result:
    data[r[5]] = [r[1], r[2], r[3], r[4]]

avg_income = sorted(data.keys())
one_km_sm = [data[i][0] for i in avg_income]
three_km_sm = [data[i][1] for i in avg_income]
one_km_ff = [data[i][2] for i in avg_income]
three_km_ff = [data[i][3] for i in avg_income]


# PLOT DATA

plt.scatter(avg_income, one_km_sm, label="1km supermarkets", c='#639df9', alpha=0.8)
plt.scatter(avg_income, one_km_ff, label="1km fast food", c='#ce4646', alpha=0.8)
# plt.plot(avg_income, one_km_sm, label="1km supermarkets", color='blue', marker='o', linestyle='solid', linewidth=1, markersize=5)
# plt.plot(avg_income, one_km_ff, label="1km fast food", color='red', marker='o', linestyle='solid', linewidth=1, markersize=5)

# plt.plot(avg_income, three_km_sm, '-b', label="3km supermarkets")
# plt.plot(avg_income, three_km_ff, label="3km fast food")

plt.xlabel('food security', fontsize=12)
plt.ylabel('number of establishments', fontsize=12)
plt.legend()
plt.show()





