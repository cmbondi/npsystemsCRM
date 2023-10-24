import sqlite3

class CRMDatabase:
    def __init__(self):
        self.con = sqlite3.connect("clients.db")
        self.cur = self.con.cursor()

        self.cur.execute("""
        CREATE TABLE IF NOT EXISTS clients (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            firstname TEXT NOT NULL,
            lastname TEXT NOT NULL,
            busname TEXT,
            phone TEXT,
            email TEXT,
            status TEXT,
            date DATE,
            info TEXT)
        """)

    def get_all_clients(self):
        self.cur.execute("SELECT * FROM clients")
        clients = self.cur.fetchall()
        return clients
    
    def add_client(self, firstname, lastname, busname, phone, email, status, date, info):
            self.cur.execute("""
            INSERT INTO clients (firstname, lastname, busname, phone, email, status, date, info) VALUES (?, ?, ?, ?, ?, ?, ?, ?)
            """, (firstname, lastname, busname, phone, email, status, date, info)
            )
            self.con.commit()

    def get_client_byid(self, client_id):
         self.cur.execute("SELECT * FROM Clients WHERE id = ?", (client_id,))
         client = self.cur.fetchone()
         return client
    
    def edit_client(self, id, firstname, lastname, busname, phone, email, status, date, info):
        self.cur.execute("""
            UPDATE clients SET
            firstname = ?,
            lastname = ?,
            busname = ?, 
            phone = ?,
            email = ?,
            status = ?,
            date = ?,
            info = ?
            WHERE id = ?
            """,
            (firstname, lastname, busname, phone, email, status, date, info, id)
        )
        self.con.commit()
    
    def delete_client(self, id):
         self.cur.execute("DELETE FROM clients WHERE id = ?", (id, ))
         self.con.commit()

    def db_close(self):
         self.con.close()

# if __name__ == "__main__":
#     DB = CRMDatabase()
#     DB.db_close()