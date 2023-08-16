import mysql.connector
mydb = mysql.connector.connect(
  host="localhost",
  user="abc",
  password="password"
)
mycursor = mydb.cursor()
mycursor.execute("Create table if not exists test3.test_table(College_Id int(2),College_name varchar(30),Branch varchar(10))")
mycursor.execute("insert into test3.test_table values(1,'TCET','COMP','9.42')")
mycursor.execute("insert into test3.test_table values(2,'TCET','ENTC','9.81')")
mycursor.execute("insert into test3.test_table values(3,'SFIT','MECH','8.12')")
mycursor.execute("insert into test3.test_table values(4,'DJSANGHVI','CHEM','7.42')")
mydb.commit()
mydb.close()