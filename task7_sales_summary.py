
import sqlite3
import pandas as pd
import matplotlib.pyplot as plt

# Connect to SQLite database
conn = sqlite3.connect("sales_data.db")

# Query to calculate total quantity and revenue by product
query = """
SELECT 
    product, 
    SUM(quantity) AS total_qty, 
    SUM(quantity * price) AS revenue 
FROM sales 
GROUP BY product;
"""

# Load results into DataFrame
df = pd.read_sql_query(query, conn)
print(df)

# Plot revenue by product
df.plot(kind='bar', x='product', y='revenue', title='Revenue by Product')
plt.ylabel('Revenue')
plt.tight_layout()
plt.savefig("sales_chart.png")
plt.show()

conn.close()
