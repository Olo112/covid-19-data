from matplotlib import pyplot as plt
from pandas import DataFrame


# --------------------------- GLOBAL LISTS ---------------------------

date = [5, 6, 7, 8, 9, 10, 11, 12]
recovery_per = [95.56, 95.59, 95.65, 95.68, 95.70, 95.70, 95.72, 95.75]
death_per = [4.44, 4.41, 4.38, 4.35, 4.32, 4.30, 4.28, 4.25]


# --------------------------- FIRST SUBPLOT ---------------------------

plt.subplot(2, 1, 1)

plt.plot(date, recovery_per, color='lightgreen', label="recovered", marker='o')
plt.title("Recovery and death rate")
plt.xlabel("In this week")
plt.ylabel("percentage [%]")

plt.legend()
plt.grid()

# --------------------------- SECOND SUBPLOT ---------------------------

plt.subplot(2, 1, 2)

plt.plot(date, death_per, color='gray', label='died', marker='o')
plt.xlabel("In this week")
plt.ylabel("percentage [%]")

plt.legend()
plt.grid()


# --------------------------- DATA IN PANDAS ---------------------------

Data = {
        'all' : [29487100, 933721, 21313861]
}



df = DataFrame(Data, columns=['all'], index=['New Cases', 'Deaths', 'Recovered'])
df.plot.pie(y='all', figsize=(5, 5), autopct='%1.1f%%', startangle=90)


# --------------------------- VISUALIZING DATA ---------------------------

plt.show()
