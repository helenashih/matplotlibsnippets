# Import the matplotlib.pyplot submodule and name it plt
import matplotlib.pyplot as plt

# Import pandas as pd
import pandas as pd

# Read the data from file using read_csv
climate_change = pd.read_csv('climate_change.csv', parse_dates = True, index_col = "date")

# Create a Figure and an Axes with plt.subplots 3 rows and 2 columns with same units on y axis
fig, ax = plt.subplots()

def plot_timeseries(axes, x, y, color, xlabel, ylabel) :
    axes.plot(x, y, color=color)
    axes.set_xlabel(xlabel)
    axes.set_ylabel(ylabel, color=color)
    axes.tick_params('y', colors=color)


# plot_timeseries(ax, climate_change.index, climate_change['co2'], 'blue', 'Time', 'CO2 (ppm)') and
# plot_timeseries(ax2, climate_change.index, climate_change['relative_temp'], 'red', 'Time', 'Relative temperature (Celsius)') and
fig, ax = plt.subplots()

        # Plot the CO2 levels time-series in blue
        plot_timeseries(ax, climate_change.index, climate_change['co2'], "blue","Time (years)", "CO2 levels")

        # Create a twin Axes object that shares the x-axis
        ax2 = ax.twinx()

        # Plot the relative temperature data in red
        plot_timeseries(ax2, climate_change.index, climate_change['relative_temp'], "red",
        "Time (years)", "Relative temperature (Celsius)")

        plt.show()

ax.plot(climate_change.index, climate_change[' co2'], color = 'blue')

seventies = climate_change["1970-01-01" : "1979-12-31"]
ax.plot(seventies.index, seventies['co2'])
ax.set_xlabel('Time')
ax.set_ylabel('CO2 (ppm)', color = 'blue')
ax.tick_params('y', colors = 'blue')
# using twin axes to show data with different scales
ax2 = ax.twinx()
ax2.plot(climate_change.index, climate_change['relative_temp'], color = 'red')
ax2.setylabel('Relative temperature (Celsius)', color = 'red')
ax2.tick_params('y', colors = 'red')


        # Add the time-series for "relative_temp" to the plot
        # ax.plot(climate_change.index, climate_change['relative_temp'])

        # Set the x-axis label
        # ax.set_xlabel('Time')

        # Set the y-axis label
        # ax.set_ylabel('Relative temperature (Celsius)')

        # Show the figure
        # plt.show()


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