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

def fetch_all_data(connection): 
    tables = ['guru', 'kelas', 'mata_pelajaran', 'siswa']
    try:
        cursor = connection.cursor() 
        for table in tables:
            cursor.execute(f"SELECT * FROM {table}")
            rows = cursor.fetchall()
            print(f"\nData from {table}:")
            for row in rows:
                print(row)
    except Error as e:
        print(f"Error fetching data: {e}")

def main():
    connection = create_connection()
    if connection:
        fetch_all_data(connection)
        connection.close()

if __name__ == '__main__':
    main()