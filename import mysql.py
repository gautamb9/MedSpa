# Allows python to access SQL DB's
import mysql.connector
# Parse JSON from strings or files
import json
# Helps in rw files 
import os 
#hello


file1 = os.path.abspath(r"C:\Users\gauta\Desktop\MedSpa\Json Files\Sheet1.json")
file2 = os.path.abspath(r"C:\Users\gauta\Desktop\MedSpa\Json Files\Sheet2.json")
file3 = os.path.abspath(r"C:\Users\gauta\Desktop\MedSpa\Json Files\Sheet3.json")
file4 = os.path.abspath(r"C:\Users\gauta\Desktop\MedSpa\Json Files\Sheet4.json")

json_data1=open(file1).read()
json_data2=open(file2).read()
json_data3=open(file3).read()
json_data4=open(file4).read()

#json.loads() method can be used to parse a valid JSON string and convert it into a Python Dictionary.
json_obj1 = json.loads(json_data1)
json_obj2 = json.loads(json_data2)
json_obj3 = json.loads(json_data3)
json_obj4 = json.loads(json_data4)

# connect to MySQL
con = mysql.connector.connect(host = 'localhost',user = 'root',passwd = '',db = 'test')
cursor = con.cursor()

#Run Loop through the data and insert it into MySQL
for item in json_obj1:
    sql = "INSERT INTO procedure_risk(`Modality`, `PIH Risk (0-110)`, `CIT Degree (15-100)`, `LHR (0-100)`, `Frekles (0-100)`, `Melasma`) VALUES (%s, %s, %s, %s, %s, %s)"
    val = (item["Modality"], item["PIH Risk (0-110)"], item["CIT Degree (15-100)"], item["LHR (0-100)"], item["Frekles (0-100)"], item["Melasma"])
    cursor.execute(sql, val)

for item in json_obj2:
    sql = "INSERT INTO sun_sensitivity(`Sun Sensitivity`, `Marks`, `Skin Type`) VALUES (%s, %s, %s)"
    val = (item["Sun Sensitivity"], item["Marks"], item["Skin Type"])
    cursor.execute(sql, val)

for item in json_obj3:
    sql = "INSERT INTO hq(`Hq 4%`, `Marks`) VALUES (%s, %s)"
    val = (item["Hq 4%"], item["Marks"])
    cursor.execute(sql, val)

for item in json_obj4:
    sql = "INSERT INTO retinol(`Retinol`, `Marks`, `Category`) VALUES (%s, %s, %s)"
    val = (item["Retinol"], item["Marks"], item["Category"])
    cursor.execute(sql, val)

con.commit()
con.close()


# for item in json_obj1:
#     sql = "INSERT INTO procedure_risk(`Modality`, `PIH Risk (0-110)`, `CIT Degree (15-100)`, `LHR (0-100)`, `Frekles (0-100)`, `Melasma`) VALUES (%s, %s, %s, %s, %s, %s) ON DUPLICATE KEY UPDATE `PIH Risk (0-110)` = VALUES(`PIH Risk (0-110)`), `CIT Degree (15-100)` = VALUES(`CIT Degree (15-100)`), `LHR (0-100)` = VALUES(`LHR (0-100)`), `Frekles (0-100)` = VALUES(`Frekles (0-100)`), `Melasma` = VALUES(`Melasma`)"
#     val = (item["Modality"], item["PIH Risk (0-110)"], item["CIT Degree (15-100)"], item["LHR (0-100)"], item["Frekles (0-100)"], item["Melasma"])
#     cursor.execute(sql, val)
