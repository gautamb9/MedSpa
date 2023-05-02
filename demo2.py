import mysql.connector
import json
import requests

# Define the sheet names and corresponding table names
sheet_names = ["Sheet1", "Sheet2", "Sheet3", "Sheet4"]
table_names = ["procedure_risk", "sun_sensitivity", "hq", "retinol"]

# Connect to MySQL
con = mysql.connector.connect(host='localhost', user='root', passwd='', db='test')
cursor = con.cursor()

# Truncate the tables
cursor.execute("TRUNCATE TABLE procedure_risk")
cursor.execute("TRUNCATE TABLE sun_sensitivity")
cursor.execute("TRUNCATE TABLE hq")
cursor.execute("TRUNCATE TABLE retinol")

# Loop through the sheet names and insert data into MySQL
for sheet_name, table_name in zip(sheet_names, table_names):
    # Make the API call
    response = requests.get(f"https://script.google.com/macros/s/AKfycbysUsIeKcTxsYPz7bdR7JMyaZ9vzabM3NstO58mGb-EZTK_0ipTABlaHEUaKrBm1w8/exec?sheetName={sheet_name}")
    
    # Parse the JSON data
    json_obj = json.loads(response.content)
    
    # Define the SQL query
    query = f"INSERT INTO {table_name} ({', '.join(json_obj[0].keys())}) VALUES ({', '.join(['%s']*len(json_obj[0]))})"
    
    # Insert data into MySQL
    for item in json_obj:
        cursor.execute(query, tuple(item.values()))

con.commit()
con.close()
