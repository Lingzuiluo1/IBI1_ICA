import matplotlib.pyplot as plt
import numpy as np
#Define population data and make a list([2020,2024],millions)
countries = ['UK', 'China', 'Italy', 'Brazil', 'USA']
population_2020 = [66.7, 1426, 59.4, 208.6, 331.6]
population_2024 = [69.2, 1410, 58.9, 212.0, 340.1]
#calculate and print the percentage change of each country
percentage_change = []
for i in range(len(countries)):
    change = ((population_2024[i] - population_2020[i]) / population_2020[i]) * 100
    percentage_change.append(change)
    print("1.Percentage population change for each country:")
    for country, change in zip(countries, percentage_change):
        print(f"{country}: {change:.2f}%")
#compare the percentage change and print the country with the highest and lowest growth rate
country_change = list(zip(countries, percentage_change))
sorted_change = sorted(country_change, key=lambda x: x[1], reverse=True)
max_country, max_rate = sorted_change[0]
min_country, min_rate = sorted_change[-1]
print(f"Country with highest growth rate: {max_country} ({max_rate:.2f}%)")
print(f"Country with lowest growth rate: {min_country} ({min_rate:.2f}%)")
#create a bar chart
plt.bar(countries, percentage_change, width=0.5)
plt.xlabel("Country")
plt.ylabel("Population Percentage Change (%)")
plt.title("Population Change (2020-2024)")
plt.show()
