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
        return None

def execute_query(connection, query, values=None):
    try:
        cursor = connection.cursor()
        cursor.execute(query, values) 
        connection.commit() 
    except Error as e:
        print(f"Error executing query: {e}")

def select_all_from_table(connection, table_name): 
    try:
        cursor = connection.cursor()
        cursor.execute(f"SELECT * FROM {table_name}") 
        rows = cursor.fetchall() 
        print(f"\nData from {table_name}:")
        for row in rows:
            print(row)
    except Error as e:
        print(f"Error fetching data from {table_name}: {e}")

def main(): 
    connection = create_connection()
    if connection:
        insert_queries = [
            ("INSERT INTO guru (id_guru, nama_guru, mata_pelajaran, alamat_guru) VALUES (%s, %s, %s, %s)",
             (21, 'Bu Yeni', 'Kesenian', 'Jl. Kesenian')),
            ("INSERT INTO kelas (id_kelas, guru_id_guru, nama_kelas, wali_kelas) VALUES (%s, %s, %s, %s)",
             (41, 21, '1C', 'Bu Yeni')),
            ("INSERT INTO mata_pelajaran (id_pelajaran, guru_id_guru, nama_pelajaran, guru_pengajar) VALUES (%s, %s, %s, %s)",
             (71, 21, 'Kesenian', 'Bu Yeni')),
            ("INSERT INTO siswa (id_siswa, kelas_id_kelas, nama_siswa, alamat_siswa, kelas) VALUES (%s, %s, %s, %s, %s)",
             (101, 41, 'Siti Aminah', 'Jl. Kebangsaan', '1C'))
        ]
        
        for query, values in insert_queries: 
            execute_query(connection, query, values)
        
        for table in ['guru', 'kelas', 'mata_pelajaran', 'siswa']: 
            select_all_from_table(connection, table)
        
        connection.close()

if __name__ == '__main__':
    main()