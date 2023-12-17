import mysql.connector
try:
    conn = mysql.connector.connect(
        host="localhost", user="root", password="9531", auth_plugin='mysql_native_password', database="indigo")
    myCursur = conn.cursor()
    print("Connection Established")
except:
    print("Connection Error")

# myCursur.execute("CREATE DATABASE indigo")
# conn.commit()

# myCursur.execute("""
# create table airport (
#                  airport_id integer primary key,
#                  code varchar(10) not null,
#                  city varchar(50) not null,
#                  name varchar(255) not null
# )
# """)
# conn.commit()

# myCursur.execute("""
# insert into airport values (1, "DEL", "New Delhi", "IGIA"),
# (2, "CCU", "Kolkata", "NSCA"),
# (3, "BOM", "Mumbai", "CSM")
# """)
# conn.commit()


myCursur.execute("""
select * from airport where airport_id > 1
""")
data = myCursur.fetchall()
print(data)


# myCursur.execute("""
# update airport set city = "BOMBAY" where airport_id = 3
# """)
# conn.commit()


myCursur.execute("""
delete from airport where airport_id = 3
""")
conn.commit()