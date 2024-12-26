import mysql.connector
from mysql.connector import Error

def create_connection():
    try:
        connection = mysql.connector.connect(
            host='localhost',
            port=3306,
            user='root',
            database='sd1sukolilo'
        )
        if connection.is_connected():
            print("Connected to MySQL database")
            return connection
    except Error as e:
        print(f"Error while connecting to MySQL: {e}")

def execute_query(connection, query, values=None): 
    try:
        cursor = connection.cursor()
        cursor.execute(query, values)
        if query.strip().lower().startswith('select'):
            rows = cursor.fetchall()
            for row in rows:
                print(row)
        else:
            connection.commit()
            print("Query executed successfully")
    except Error as e:
        print(f"Error executing query: {e}")

def main(): 
    connection = create_connection()
    if connection:
        queries = [
            ("SELECT * FROM guru", None),
            ("SELECT * FROM kelas", None),
            ("SELECT * FROM mata_pelajaran", None),
            ("SELECT * FROM siswa", None),
            ("UPDATE guru SET nama_guru='Bu Yeni Updated' WHERE id_guru=21", None),
            ("UPDATE kelas SET nama_kelas='1C Updated' WHERE id_kelas=41", None),
            ("UPDATE mata_pelajaran SET nama_pelajaran='Kesenian Updated' WHERE id_pelajaran=71", None),
            ("UPDATE siswa SET nama_siswa='Siti Aminah Updated' WHERE id_siswa=101", None)
        ]
        for query, values in queries:
            execute_query(connection, query, values)
        connection.close()

if __name__ == '__main__': 
    main()