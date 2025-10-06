import pandas as pd
import random
import matplotlib.pyplot as plt

# i made these names up
names = ["A", "B", "C", "D", "E", "F", "G", "H",]
beverageAmount = [0, 0, 0, 1, 0, 2, 0, 1,]
sleepAmount = [8, 8, 8, 8, 1, 7, 7, 5, ]
tiredDuringDay = [True, True, True, True, True, True, True, True, ]
GPA = [4.0, 4.2, 3.8, 3.8, 4.1, 3.4, ]
isFocused = [True, True, True, True, True, True, False, True, ]

data = {
    "Name": [random.choice(names) for _ in range (30)],
    "Beverage Amount": [random.choice(beverageAmount) for _ in range (30)],
    "Sleep Amount": [random.choice(sleepAmount) for _ in range (30)],
    "Tired During Day": [random.choice(tiredDuringDay) for _ in range (30)],
    "GPA": [random.choice(GPA) for _ in range (30)],
    "Is Focused": [random.choice(isFocused) for _ in range (30)],
}

panData = pd.DataFrame(data)

#print(panData)
panData.groupby("Sleep Amount")["GPA"].mean()
panData.groupby("Sleep Amount")["GPA"].mean().plot(kind="bar")
plt.title("Average GPA by Sleep Amount")
plt.xlabel("Sleep")
plt.ylabel("Average GPA")
plt.show()

panData["GPA"].plot(kind="hist", bins=5, edgecolor="black")
plt.title("GPA Distribution")
plt.xlabel("GPA")
plt.ylabel("Number of Students")
plt.show()

plt.scatter(panData)