import matplotlib.pyplot as plt

# Pie chart with price tiers of a HIGH INCOME neighborhood (90266)
labels = ['\$', '\$\$', '\$\$\$']
sizes = [1, 8, 4]
explode = (0, 0, 0)
fig1, ax1 = plt.subplots()
ax1.pie(sizes, explode=explode, labels=labels, autopct='%1.1f%%',
        shadow=False, startangle=90)
ax1.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.
ax1.set_title('Supermarket price distribution in highest-income neighborhoods')
plt.show()

# Pie chart with price tiers of a LOW INCOME neighborhood (90021)
labels = ['\$', '\$\$', '\$\$\$']
sizes = [19, 41, 10]
explode = (0, 0, 0)

fig1, ax1 = plt.subplots()
ax1.pie(sizes, explode=explode, labels=labels, autopct='%1.1f%%',
        shadow=True, startangle=90)
ax1.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.
ax1.set_title('Supermarket price distribution in lowest-income neighborhoods')
plt.show()

