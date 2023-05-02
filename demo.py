import mysql.connector
import json
import os 

# Define the file paths
file_paths = [
    os.path.abspath(r"C:\Users\gauta\Desktop\MedSpa\Json Files\Sheet1.json"),
    os.path.abspath(r"C:\Users\gauta\Desktop\MedSpa\Json Files\Sheet2.json"),
    os.path.abspath(r"C:\Users\gauta\Desktop\MedSpa\Json Files\Sheet3.json"),
    os.path.abspath(r"C:\Users\gauta\Desktop\MedSpa\Json Files\Sheet4.json")
]

# Parse the JSON files and store them in a list
json_objs = []
for path in file_paths:
    with open(path) as f:
        json_objs.append(json.load(f))

# Connect to MySQL
con = mysql.connector.connect(host='localhost', user='root', passwd='', db='test')
cursor = con.cursor()

# Truncate the tables
cursor.execute("TRUNCATE TABLE procedure_risk")
cursor.execute("TRUNCATE TABLE sun_sensitivity")
cursor.execute("TRUNCATE TABLE hq")
cursor.execute("TRUNCATE TABLE retinol")

# Define a list of tuples for each table
table_data = [
    (json_objs[0], "INSERT INTO procedure_risk(`Modality`, `PIH Risk (0-110)`, `CIT Degree (15-100)`, `LHR (0-100)`, `Frekles (0-100)`, `Melasma`) VALUES (%s, %s, %s, %s, %s, %s)"),
    (json_objs[1], "INSERT INTO sun_sensitivity(`Sun Sensitivity`, `Marks`, `Skin Type`) VALUES (%s, %s, %s)"),
    (json_objs[2], "INSERT INTO hq(`Hq 4%`, `Marks`) VALUES (%s, %s)"),
    (json_objs[3], "INSERT INTO retinol(`Retinol`, `Marks`, `Category`) VALUES (%s, %s, %s)")
]

# Loop through the table data and insert it into MySQL
for data in table_data:
    for item in data[0]:
        cursor.execute(data[1], tuple(item.values()))

con.commit()
con.close()
