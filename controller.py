import mysql.connector
from person import Person
class DatabaseManager:
    def __init__(self, host, user, password, database):
        self.host = host
        self.user = user
        self.password = password
        self.database = database
        
        self.conn = None
        self.cursor = None
        self.connect()
    
    def connect(self):
        try:
            self.conn = mysql.connector.connect(
                host=self.host,
                user=self.user,
                password=self.password,
                database=self.database
            )
            self.cursor = self.conn.cursor()
            print("Connected to the database")
        except:
            print("Error connecting to the database")
    
    def add_person(self, name, phone):
        sql = "INSERT INTO persons (name, phone) VALUES (%s, %s)"
        self.cursor.execute(sql, (name, phone))
        self.conn.commit()
        print("Person added successfully")
    
    def list_persons(self):
        sql = "SELECT * FROM persons"
        self.cursor.execute(sql)
        rows = self.cursor.fetchall()
        for row in rows:
            person = Person(row[0], row[1], row[2])
            person.display()
    
    def list_by_id(self, id):
        sql = "SELECT * FROM persons WHERE id = %s"
        self.cursor.execute(sql, (id,))
        rows = self.cursor.fetchall()
        for row in rows:
            person = Person(row[0], row[1], row[2])
            person.display()
    
    def delete_person(self, id):
        sql = "DELETE FROM persons WHERE id = %s"
        self.cursor.execute(sql, (id,))
        self.conn.commit()
        print("Person deleted successfully")
    
    def update_person(self, id, name, phone):
        sql = "UPDATE persons SET name = %s, phone = %s WHERE id = %s"
        self.cursor.execute(sql, (name, phone, id))
        self.conn.commit()
        print("Person updated successfully")
    
    def search_person(self, name):
        sql = f"SELECT * FROM persons WHERE name LIKE '{name}%';" 
        self.cursor.execute(sql)
        rows = self.cursor.fetchall()
        for row in rows:
            person = Person(row[0], row[1], row[2])
            person.display()
        
        if len(rows) == 0:
            print("No person found")