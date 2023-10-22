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
    
    def edit_client(self, client_id, firstname, lastname, busname, phone, email, status, date, info):
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
            (firstname, lastname, busname, phone, email, status, date, info, client_id)
        )
        self.con.commit()
    
    def delete_client(self, client_id):
         self.cur.execute("DELETE FROM clients WHERE id = ?", (client_id, ))
         self.con.commit()

    def db_close(self):
         self.con.close()

# if __name__ == "__main__":
#     DB = CRMDatabase()
#     DB.add_client("Colin", "Bondi", "NP Systems", "3605129704", "colin@npsystems.com", "Active", "10-23-20", "Colin is cool")
#     DB.add_client("Kara", "Smith", "Be Here Meow", "5034944514", "kara@beheremeow.com", "Active", "1-15-23", "Kara is a cool cat")
#     DB.add_client("Lady", "Jasmin", "High Heels Corp", "3605432312", "ladyJ@ladyjasmin.com", "Prospect", "5-15-23", "Lady Jasmin is a Goddess to be worshipped")
#     DB.add_client("Jean", "Viets", "Finity Inc", "5035551212", "jean@finity.com", "Past", "8-17-19", "Jean was a Lady I worshipped back in the day")
#     DB.add_client("Marijke", "Samamara", "Gypsy Passions", "3607263777", "madminlady@passion.com", "Past", "5-13-21", "Oh my this is an incredible thing")
#     result = DB.get_all_clients()
#     print(result)
#     DB.db_close()