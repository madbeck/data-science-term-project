import numpy as np
import matplotlib.pyplot as plt
import sqlite3
import numpy as np

conn = sqlite3.connect('combined_data.db')
c = conn.cursor()

sql_command = "SELECT f.zip_code, f.one_km_sm, f.three_km_sm, f.one_km_ff, f.three_km_ff, e.income from food_security as f INNER JOIN economic_health_la as e on f.zip_code = e.zip_code;"
c.execute(sql_command)
result = c.fetchall()

data = {}
for r in result:
    data[r[5]] = [r[1], r[2], r[3], r[4]]

avg_income = sorted(data.keys())


buckets = {}
for i in data:
	rounded = int(i / 1000) * 1000

	if rounded in buckets:
		buckets[rounded].append(data[i])
	else:
		buckets[rounded] = [data[i]]

output = {}
for i in buckets:
	total = len(buckets[i])
	a = sum([j[0] for j in buckets[i]]) / total
	b = sum([j[1] for j in buckets[i]]) / total
	c = sum([j[2] for j in buckets[i]]) / total
	d = sum([j[3] for j in buckets[i]]) / total
	output[i] = [a, b, c, d]

print(output)
print(len(output))
income = sorted(output.keys())

one_km_sm = [output[i][0] for i in income]
three_km_sm = [output[i][1] for i in income]
one_km_ff = [output[i][2] for i in income]
three_km_ff = [output[i][3] for i in income]


#####################################################################

# AVG INCOME VS 1KM SUP
# z = np.polyfit(avg_income, one_km_sm, 2)
# p = np.poly1d(z)
# plt.scatter(avg_income, one_km_sm, label="1km supermarkets", c='#639df9', alpha=0.8)
# plt.plot(avg_income, [p(i) for i in avg_income], '-')

z = np.polyfit(income, three_km_sm, 2)
p = np.poly1d(z)
plt.scatter(income, three_km_sm, label="3km supermarkets", c='#639df9', alpha=0.8)
plt.plot(income, [p(i) for i in income], '-')

# AVG INCOME VS 1KM FF
# z = np.polyfit(avg_income, one_km_ff, 2)
# p = np.poly1d(z)
# plt.scatter(avg_income, one_km_ff, label="1km fast food", c='#ce4646', alpha=0.8)
# plt.plot(avg_income, [p(i) for i in avg_income], '-')

# AVG INCOME VS 3KM SUP
# z = np.polyfit(avg_income, three_km_sm, 2)
# p = np.poly1d(z)
# plt.scatter(avg_income, three_km_sm, label="1km fast food", c='#ce4646', alpha=0.8)
# plt.plot(avg_income, [p(i) for i in avg_income], '-')

# AVG INCOME VS 3KM FF
# z = np.polyfit(avg_income, three_km_ff, 2)
# p = np.poly1d(z)
# plt.scatter(avg_income, three_km_ff, label="1km fast food", c='#ce4646', alpha=0.8)
# plt.plot(avg_income, [p(i) for i in avg_income], '-')


# OLD PLOTS (NOT SCATTER)
# plt.plot(avg_income, one_km_sm, label="1km supermarkets", color='blue', marker='o', linestyle='solid', linewidth=1, markersize=5)
# plt.plot(avg_income, one_km_ff, label="1km fast food", color='red', marker='o', linestyle='solid', linewidth=1, markersize=5)
# plt.plot(avg_income, three_km_sm, '-b', label="3km supermarkets")
# plt.plot(avg_income, three_km_ff, label="3km fast food")

# BELOW NEEDED TO PLOT ALL GRAPHS
plt.xlabel('food security', fontsize=12)
plt.ylabel('number of establishments', fontsize=12)
plt.legend()
plt.show()





