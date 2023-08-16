import mysql.connector
mydb = mysql.connector.connect(
  host="localhost",
  user="abc",
  password="password"
)
mycursor = mydb.cursor()
query = "ALTER TABLE test3.test_table ADD CGPA_Number INT(10)"
mycursor.execute(query)
mydb.close()
