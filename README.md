Sales Summary Using SQLite and Python
Objective
The goal of this task is to generate a basic sales summary using SQL inside Python. Specifically, we want to calculate the total quantity sold and the total revenue for each product in a small dataset, then display the results using simple print statements and a basic bar chart.

Tools Used
Python

SQLite (built-in via sqlite3)

pandas (for data manipulation)

matplotlib (for chart visualization)

Dataset
A small SQLite database named sales_data.db was created with one table called sales. This table includes the following columns:

order_id

product

quantity

price

Sample data includes sales records for products like Apples, Bananas, Cherries, and Dates.

Steps Performed
Created the SQLite database and inserted sample sales records.

Used Python to connect to the database using sqlite3.

Executed an SQL query to group the data by product, calculating total quantity and revenue.

Loaded the result into a pandas DataFrame.

Printed the results to the console.

Created a bar chart using matplotlib to show revenue by product.

Output
The output includes a table showing the total quantity sold and total revenue for each product, along with a simple bar chart for visualization.

Summary
This task demonstrates how easy it is to use Python with SQLite to perform simple but effective data analysis. The solution is fast, light, and works perfectly for small datasets or quick insights.
