# Import the matplotlib.pyplot submodule and name it plt
import matplotlib.pyplot as plt

# Import pandas as pd
import pandas as pd

medals = pd.read_csv('medals_by_country_2016.csv', index_col=0)
fig, ax = plt.subplots()

# Rowing and Gymnastics men's data
ax.bar("Rowing", mens_rowing["Height"].mean())
ax.bar("Gymnastics", mens_gymnastics["Height"].mean())

# ax.hist(mens_rowing["Height"], bins=5) or bins=[150, 160, 170, 180, 190, 200, 210]

# ax.hist(mens_rowing["Height"], bins=5) or bins=[150, 160, 170, 180, 190, 200, 210]
ax.hist(mens_rowing["Height"], label="Rowing", bins=[150, 160, 170, 180, 190, 200, 210], histtype="step")
ax.hist(mens_gymnastics["Height"], label="Gymnastics", bins=[150, 160, 170, 180, 190, 200, 210], histtype="step")
ax.set_xlabel("Height (cm)")
ax.set_ylabel("# of observations")
ax.legend()

#Exercise  1
# Plot a histogram of "Weight" for mens_rowing
ax.hist(mens_rowing["Weight"])

# Compare to histogram of "Weight" for mens_gymnastics
ax.hist(mens_gymnastics["Weight"])

# Set the x-axis label to "Weight (kg)"
ax.set_xlabel("Weight (kg)")

# Set the y-axis label to "# of observations"
ax.set_ylabel("# of observations")

#Exercise 2
# Plot a histogram of "Weight" for mens_rowing
ax.hist(mens_rowing["Weight"], label="Rowing", bins=5, histtype="step")

# Compare to histogram of "Weight" for mens_gymnastics
ax.hist(mens_gymnastics["Weight"], label="Gymnastics", bins=5, histtype="step")

ax.set_xlabel("Weight (kg)")
ax.set_ylabel("# of observations")

# Add the legend and show the Figure
ax.legend()
plt.show()

#Nmber of medals by country
ax.bar(medals.index, medals["Gold"], label="Gold")
ax.bar(medals.index, medals["Silver"], bottom=medals["Gold"], label="Silver")
ax.bar(medals.index, medals["Bronze"], bottom=medals["Gold"] + medals["Silver"], label="Bronze")

# Rotate country name by 90 degree in bar chart
ax.set_xticklabels(medals.index, rotation=90)
ax.set_ylabel("Number of medals")
ax.legend()
plt.show()


#ANSWER

# Add bars for "Gold" with the label "Gold"
ax.bar(medals.index, medals["Gold"], label="Gold")

# Stack bars for "Silver" on top with label "Silver"
ax.bar(medals.index, medals["Silver"], bottom=medals["Gold"], label="Silver")

# Stack bars for "Bronze" on top of that with label "Bronze"
ax.bar(medals.index, medals["Bronze"], bottom=medals["Gold"]+medals["Silver"], label="Bronze")

# Display the legend
ax.legend()

plt.show()


fig, ax = plt.subplots()

# Plot a bar-chart of gold medals as a function of country
ax.bar(medals.index, medals["Gold"])

# Set the x-axis tick labels to the country names
ax.set_xticklabels(medals.index, rotation=90)

# Set the y-axis label
ax.set_ylabel("Number of medals")

plt.show()