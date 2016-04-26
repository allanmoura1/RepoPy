import mysql.connector

cnx = mysql.connector.connect(user='root', password='root',host='127.0.0.1',database='world')

cur = cnx.cursor(buffered=True) 
cur.execute("SHOW TABLES")
cur.execute("SELECT * FROM CITY WHERE COUNTRYCODE = 'BRA' AND DISTRICT = 'SERGIPE'")


print(cur.fetchall()) 


cur.close() 
cnx.close()