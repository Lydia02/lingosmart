import mysql.connector
from mysql.connector import errorcode

try:
    my_db = mysql.connector.connect(
        host="lingosmart.mysql.pythonanywhere-services.com",
        user="lingosmart",
        password="Oms@2002",
        database="lingosmart$user"
    )

    my_cursor = my_db.cursor()

    # Explicitly select the database
    my_cursor.execute("USE lingosmart$user")

    print("Connected to database")

except mysql.connector.Error as err:
    if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
        print("Something is wrong with your user name or password")
    elif err.errno == errorcode.ER_BAD_DB_ERROR:
        print("Database does not exist")
    else:
        print("Error:", err.msg)

finally:
    if my_db.is_connected():
        my_cursor.close()
        my_db.close()
        print("MySQL connection is closed")
