import mysql.connector

def create_connection(): 
    try:
        return mysql.connector.connect(
            host='localhost',
            port=3306,
            user='root',
            database='sd1sukolilo'
        )
    except mysql.connector.Error as e:
        print(f"Error connecting to MySQL: {e}")
        return None

def execute_delete_query(connection, table, condition): 
    try:
        cursor = connection.cursor()
        delete_query = f"DELETE FROM {table} WHERE {condition} LIMIT 1"
        cursor.execute(delete_query)
        connection.commit()
        print(f"Deleted 1 row from {table}")
    except mysql.connector.Error as e:
        print(f"Error deleting from {table}: {e}")

def main(): 
    try:
        connection = create_connection()
        if connection:
            execute_delete_query(connection, "siswa", "id_siswa=100")

            execute_delete_query(connection, "kelas", "id_kelas=40")

            execute_delete_query(connection, "mata_pelajaran", "id_pelajaran=70")

            execute_delete_query(connection, "guru", "id_guru=20")

    except mysql.connector.Error as e:
        print(f"Error: {e}")

    finally:
        if connection and connection.is_connected(): 
            connection.close()
            print("MySQL connection closed")

if __name__ == '__main__': 
    main()