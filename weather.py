# Import the matplotlib.pyplot submodule and name it plt
import matplotlib.pyplot as plt

# Create a Figure and an Axes with plt.subplots 3 rows and 2 columns with same units on y axis
fig, ax = plt.subplots(2, 1, sharey=True)

# Plot MLY-PRCP-NORMAL from seattle_weather against the MONTH
ax[0].plot(seattle_weather["MONTH"], seattle_weather["MLY-PRCP-NORMAL"], marker = "d", color = 'b')
ax[0].plot(seattle_weather["MONTH"], seattle_weather["MLY-PRCP-25PCTL"], marker = "d", linestyle = ':', color = 'b')
ax[0].plot(seattle_weather["MONTH"], seattle_weather["MLY-PRCP-75PCTL"], marker = "d", linestyle = ':', color = 'b')

# Plot MLY-PRCP-NORMAL from austin_weather against MONTH
ax[1].plot(austin_weather["MONTH"], austin_weather["MLY-PRCP-NORMAL"], marker = "X", color = 'r')
ax[1].plot(austin_weather["MONTH"], austin_weather["MLY-PRCP-25PCTL"], marker = "X", linestyle = ':', color = 'r')
ax[1].plot(austin_weather["MONTH"], austin_weather["MLY-PRCP-75PCTL"], marker = "X", linestyle = ':', color = 'r')\

ax.set_xlabel("Time (month)")
ax[0].set_ylabel("Average percipitation (inches) in Seattle")
ax[1].set_ylabel("Average percipitation (inches) in Austin")
ax.set_title("Weather Comparison Seattle and Austin")
# Call the show function
plt.show()