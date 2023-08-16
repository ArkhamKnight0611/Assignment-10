import mysql.connector
mydb = mysql.connector.connect(
  host="localhost",
  user="abc",
  password="password"
)
mycursor = mydb.cursor()
mycursor.execute("UPDATE test3.test_table SET College_name = 'KJSOMAIYA' WHERE College_Id = 2")
mycursor.execute("DELETE FROM test3.test_table WHERE College_id = 4")
mydb.commit()
mydb.close()