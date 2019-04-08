import mysql.connector
cnx=mysql.connector.connect(user='root',password='niko1999',host='localhost',database='pythonfinal')
cursor=cnx.cursor()

user_query = ('select * from isci  INNER JOIN pythonfinal.maas on isci.No=maas.EmpNo')

cursor.execute(user_query)

result = cursor.fetchall()




print("Ən çox maaş alan işçini tapmaq üçün 1:")
print("Ən az maaş alan işçini tapmaq üçün 2:")
print("Butun melumatlari gormek ucun 3:")
print("**************")
a=int(input("Ededi daxil edin: "))

if a==1:
    user_query1=('SELECT *  FROM pythonfinal.isci  INNER JOIN pythonfinal.maas on isci.No=maas.EmpNo ORDER BY Net DESC LIMIT 1')
    cursor.execute(user_query1)
    result = cursor.fetchall()
    for i in result:
        print(i)



elif a==2:
    user_query2=('SELECT *  FROM pythonfinal.isci  INNER JOIN pythonfinal.maas on isci.No=maas.EmpNo ORDER BY Net ASC LIMIT 1')
    cursor.execute(user_query2)
    result = cursor.fetchall()
    for i in result:
        print(i)


elif a==3:
    user_query = ('select * from isci  INNER JOIN pythonfinal.maas on isci.No=maas.EmpNo')
    cursor.execute(user_query)
    result = cursor.fetchall()
    for i in result:
        print(i)
else:
    print("Zehmet olmasa yuxarida melumat lovhesini duzgun oxuyun")
