import pyodbc

def get_db_conn():
    try:
        db_connection = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};'
                                        'SERVER=DESKTOP-5KATTA1\SQLEXPRESS;'
                                        'DATABASE=codechallenge_petpals;'
                                        'Trusted_Connection=yes;')
        print("Database connection successful!")
        cursor = db_connection.cursor()
        cursor.execute("select * from Pets")
        rows = cursor.fetchall()
        for row in rows:
            print(row)
    except Exception as e:
        print(f"Failed to connect to the database: {e}")
        exit() 


