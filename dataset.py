import pandas as pd
import random

# i made these names up
names = ["A", "B", "C", "D", "E", "F", "G", "H",]
beverageAmount = [0, 0, 0, 1, 0, 2, 0, 1,]
sleepAmount = [8, 8, 8, 8, 1, 7, 7, 5, ]
tiredDuringDay = [True, True, True, True, True, True, True, True, ]
GPA = [4.0, "N/A", 4.2, "N/A", 3.8, 3.8, 4.1, 3.4, ]
isFocused = [True, True, True, True, True, True, False, True, ]

data = {
    "Name": names,
    "Beverage Amount": beverageAmount,
    "Sleep Amount": sleepAmount,
    "Tired During Day": tiredDuringDay,
    "GPA": GPA,
    "Is Focused": isFocused,
}

panData = pd.DataFrame(data)

print(panData)