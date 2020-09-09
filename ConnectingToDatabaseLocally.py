# Author: Itohan Ero
## Conecting to MySQL Database, Executing Queries, Storing Into an Array


#Install connector using terminal/commandline: pip install mysql-connector-python
import mysql.connector

db = mysql.connector.connect(
    host = "insert here",
    user = "insert here",
    password = "insert here",
    database = "insert here"
)


# Make sure that you are connected to the database! Should print a connection line.
print(db)

#Create a pointer object
mycursor = db.cursor()

#Query to store Construction Years
mycursor.execute("SELECT building.constyear FROM building LIMIT 10")
#Stores construction year into an array
years = [year for [year] in mycursor.fetchall()]

#Query to store ATC tag
mycursor.execute("SELECT inspection.ATC_tag FROM inspection LIMIT 10")
#Stores ATC tags into an array
atctag = [atc for [atc] in mycursor.fetchall()]

#Print out items to make sure it was stored into the array completely
for x in years:
    print(x)
    
for y in atctag:
    print(y)
