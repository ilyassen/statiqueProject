import mysql.connector


def to_str(element):
    return '"' + element + '"'

def creat_db(name):
    mydb = mysql.connector.connect(
        host="localhost",
        user="admin",
        passwd="admin"
    )
    mycursor = mydb.cursor()
    mycursor.execute("CREATE DATABASE " + name)


def creat_table():
    mydb = connect_db()
    mycursor = mydb.cursor()

    mycursor.execute("CREATE TABLE files (filename VARCHAR(255), filepath VARCHAR(255))")

    mydb.close()


def connect_db():
    mydb = mysql.connector.connect(
    host="localhost",
    user="admin",
    passwd="admin",
    database="mydatabase"
    )
    return mydb


def add_line(filename, filepath):
    mydb = connect_db()
    mycursor = mydb.cursor()

    sql = "INSERT INTO files (filename, filepath, CyclomaticComplexity, " \
          "ExcessiveClassLength, ExcessiveMethodLength, ExcessiveParameterList, " \
          "NPathComplexity, CouplingBetweenObjects, EmptyCatchBlock, " \
          "DepthOfInheritance, GotoStatement) " \
          "VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
    val = (filename, filepath, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    mycursor.execute(sql, val)

    mydb.commit()

    print(mycursor.rowcount, "record inserted.")

    mydb.close()

# def files_in_bd():
#     mydb = connect_db()
#     mycursor = mydb.cursor()
#
#     sql = "SELECT filename from files WHERE filepath in '" + oldfilepath + " "
#     print(sql)
#     mycursor.execute(sql)
#
#     mydb.commit()
#
#     print(mycursor.rowcount, "record modified.")
#
#     mydb.close()

def modify_line(newfilepath, oldfilepath):
    mydb = connect_db()
    mycursor = mydb.cursor()

    sql = "UPDATE files SET filepath = '" + newfilepath + "' WHERE filepath = '" + oldfilepath + "' and id <> 0 "
    print(sql)
    mycursor.execute(sql)

    mydb.commit()

    print(mycursor.rowcount, "record modified.")

    mydb.close()


def reset_table():
    mydb = connect_db()
    mycursor = mydb.cursor()

    sql = "Truncate table files "
    mycursor.execute(sql)

    mydb.close()

def get_filenames():
    mydb = connect_db()
    mycursor = mydb.cursor()

    sql = "select filename from files"
    mycursor.execute(sql)

    myresult = mycursor.fetchall()

    array = []
    for x in myresult:
        array.append(x[0])
    return array

def get_filepaths():
    mydb = connect_db()
    mycursor = mydb.cursor()

    sql = "select filepath from files"
    mycursor.execute(sql)

    myresult = mycursor.fetchall()

    array = []
    for x in myresult:
        array.append(x[0])
    return array

def get_filename(filepath):
    mydb = connect_db()
    mycursor = mydb.cursor()

    sql = "select filename from files where filepath =%s "
    adr = (filepath,)
    mycursor.execute(sql, adr)
    myresult = mycursor.fetchone()

    return myresult[0]

    mydb.close()

def get_filepath(filename):
    mydb = connect_db()
    mycursor = mydb.cursor()

    sql = "select filepath from files where filename = " + filename
    mycursor.execute(sql)
    myresult = mycursor.fetchone()

    return myresult

    mydb.close()

def add_dump_files():
    add_line('file1', 'ffiiilllee')
    add_line('file2', 'ffiiilllee')
    add_line('file3', 'ffiiilllee')
    add_line('file4', 'ffiiilllee')
    add_line('file5', 'ffiiilllee')
    add_line('file6', 'ffiiilllee')
    add_line('file7', 'ffiiilllee')


def update_file(file, CyclomaticComplexity, ExcessiveClassLength,
                ExcessiveMethodLength, ExcessiveParameterList, NPathComplexity, CouplingBetweenObjects,
                EmptyCatchBlock, DepthOfInheritance, GotoStatement):
    mydb = connect_db()
    mycursor = mydb.cursor()

    sql = """ UPDATE files
                SET
                CyclomaticComplexity = """ + str(CyclomaticComplexity) + """,
                ExcessiveClassLength = """ + str(ExcessiveClassLength) + """,
                ExcessiveMethodLength =""" + str(ExcessiveMethodLength) + """,
                ExcessiveParameterList = """ + str(ExcessiveParameterList) + """,
                NPathComplexity = """ + str(NPathComplexity) + """,
                CouplingBetweenObjects = """ + str(CouplingBetweenObjects) + """,
                EmptyCatchBlock = """ + str(EmptyCatchBlock) + """,
                DepthOfInheritance = """ + str(DepthOfInheritance) + """,
                GotoStatement = """ + str(GotoStatement) + """
                WHERE filename = """ + to_str(file)
    print(sql)
    mycursor.execute(sql)
    mydb.commit()

# get_filenames()
# get_filepaths()


# update_file("file_ 1", 0, 0, 0, 0, 0, 0, 0, 0, 0)

