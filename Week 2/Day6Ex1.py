import matplotlib.pyplot as plt

# Line plot
years = [2010, 2011, 2012, 2013]
sales = [100, 120, 140, 160]
plt.plot(years, sales, label = "Sales Trend", color="blue", marker="o")
plt.title("Sales Trend")
plt.xlabel("Years")
plt.ylabel("Sales")
plt.legend()
plt.show()

# Bar chart
categories = ["Electronics", "Clothing", "Grocery"]
revenue = [250, 400, 150]
plt.bar(categories, revenue, color = "green")
plt.title("Revenue by Category")
plt.show()

# Scatter plot
hours_studies = [1, 2, 3, 4, 5]
exam_scores = [50, 55, 65, 70, 85]
plt.scatter(hours_studies, exam_scores, color="red")
plt.title("Exam Scores vs Study Hours")
plt.xlabel("Study Hours")
plt.ylabel("Exam Scores")
plt.show()