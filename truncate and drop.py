import mysql.connector
mydb = mysql.connector.connect(
  host="localhost",
  user="abc",
  password="password"
)
mycursor = mydb.cursor()
mycursor.execute("TRUNCATE TABLE test3.test_table") 
mycursor.execute("DROP TABLE test3.test_table")

