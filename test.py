import pandas as pd

students_data = [
        {"name": "Alice", "class": "10th", "grades": [85, 90, 78]},
        {"name": "Bob", "class": "10th", "grades": [70, 88]},
        {"name": "Charlie", "class": "9th", "grades": []},
        {"name": "David", "class": "10th", "grades": [95, 100, 92, 88]},
        {"name": "Eve", "class": "9th", "grades": [80, 85, 88]}
        ]

df=pd.DataFrame(students_data)
df.to_csv("data/data.csv", index=False)
