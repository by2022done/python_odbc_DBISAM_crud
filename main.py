import pyodbc
import random

cnxn = pyodbc.connect("DSN=dbisam_vec_test")
odbc = cnxn.cursor()
print ("Opened 'odbc' database successfully");

def converttobinary(filename):
    with open(filename, 'rb') as file:
        binarydata = file.read()
    return binarydata
def convertbinarytofile(binarydata, filename):
    with open(filename, 'wb') as file:
        file.write(binarydata)


# CREATE DATABASE employee
query = """
CREATE TABLE IF NOT EXISTS employee
(
  Last_Name CHAR(20) DESCRIPTION 'Last Name',
  First_Name CHAR(15) DESCRIPTION 'First Name',
  data BLOB,
  
  NOCASE PRIMARY KEY (Last_Name, First_Name) COMPRESS FULL
);
"""
print(query)
odbc.execute(query)
odbc.commit()
# this will Create tables: employee.dat .blb and .idx and dbisam.lck
# as I understand .dat is where you can get data and reference to blb binaries


#insert

query = "INSERT into employee (Last_Name, First_Name, data) VALUES (?,?,?)"
print(query)
convertBMP = converttobinary('sample.bmp') #this can be any bmp file 
odbc.execute(query, 'jkddd'+str(random.getrandbits(12)), 'kuuddd'+str(random.getrandbits(5)), pyodbc.Binary(convertBMP))
odbc.commit()

#select you can also see with other prog http://www.scalabium.com/dbisam/ and only view you can't change or update
query = "SELECT Last_Name, First_Name, data FROM employee"
print(query)
odbc.execute(query)
odbc.commit()
odbc_result = odbc.fetchall()
#print(odbc_result)
for item in odbc_result:
    print("Last_Name: " + str(item[0]))
    print("First_Name: " + str(item[1]))
    convertbinarytofile(item[2], "sample+"+str(random.getrandbits(12)) + ".bmp")
    #print("Binary: " + str(item[2]))
    # to 
    
# update should work same

