__author__="tomy"
__date__ ="$2013-12-14 15:43:31$"
import mysql.connector
def insertData():
    cnx = mysql.connector.connect(user='root',password='',host='127.0.0.1',database='pythondb')
    cur = cnx.cursor()
    cur.execute('insert into user values (3,"john",33)')
    cnx.commit()
    print 'yes'
    cnx.close()

def showData():
    cnx = mysql.connector.connect(user='root',password='',host='127.0.0.1',database='pythondb')
    cursor = cnx.cursor()
    query = ("SELECT * from user")
    cursor.execute(query)
#    for id, username, age in cursor:
#        print id, username, age
#    cursor.close()
    print cursor.fetchmany(2)
    print cursor.fetchmany(2)
    cnx.close()

showData()