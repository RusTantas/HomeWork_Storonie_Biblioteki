import numpy as np
import matplotlib.pyplot as plt
import pandas as pd


s = pd.Series(np.arange(5), index=["a", "b", "c", "d", "e"])
print("Выбор одного элемента")
print(s["a"])
print("Выбор нескольких элементов")
print(s[["a", "d"]])
print("Срез")
print(s[1:])
print("Поэлементное сложение")
print(s + s)


students = pd.read_csv("StudentsPerformance.csv")
print(students.head(100))

print()

print(students.groupby(["gender", "test preparation course"])["writing score"].count())

plt.hist(students["math score"], label="Тест по математике")
plt.xlabel("Баллы за тест")
plt.ylabel("Количество студентов")
plt.legend()
plt.show()