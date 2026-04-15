import csv
import psycopg2
from connect import connect


conn = connect()
cur = conn.cursor() 



cur.execute("""
    CREATE TABLE IF NOT EXISTS phonebook (
        id SERIAL PRIMARY KEY,
        name VARCHAR(50),
        phone VARCHAR(20) UNIQUE
    )
""")
conn.commit()


def insert_from_csv():
    with open("contacts.csv", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        for row in reader:
            cur.execute("""
                INSERT INTO phonebook (name, phone)
                VALUES (%s, %s)
                ON CONFLICT (phone) DO NOTHING
            """, (row["name"], row["phone"]))
    conn.commit()
    print("Imported from CSV.")


def insert_from_console():
    name = input("Name: ")
    phone = input("Phone: ")
    cur.execute("""
        INSERT INTO phonebook (name, phone)
        VALUES (%s, %s)
        ON CONFLICT (phone) DO NOTHING
    """, (name, phone))
    conn.commit()
    print("Contact added.")


def update_contact():
    phone = input("Enter phone of contact to update: ")
    cur.execute("SELECT * FROM phonebook WHERE phone = %s", (phone,))
    
    if cur.fetchone() is None:
        print("Contact not found.")
        return

    print("1. Update name")
    print("2. Update phone")
    choice = input("Choice: ")

    if choice == "1":
        new_name = input("New name: ")
        cur.execute("UPDATE phonebook SET name = %s WHERE phone = %s", (new_name, phone))
    elif choice == "2":
        new_phone = input("New phone: ")
        cur.execute("UPDATE phonebook SET phone = %s WHERE phone = %s", (new_phone, phone))

    conn.commit()
    print("Updated.")


def search_contacts():
    print("1. Search by name")
    print("2. Search by phone prefix")
    choice = input("Choice: ")

    if choice == "1":
        name = input("Name: ")
        cur.execute("SELECT * FROM phonebook WHERE name ILIKE %s", (f"%{name}%",))
    elif choice == "2":
        prefix = input("Phone prefix: ")
        cur.execute("SELECT * FROM phonebook WHERE phone LIKE %s", (f"{prefix}%",))
    else:
        cur.execute("SELECT * FROM phonebook")

    rows = cur.fetchall()

    if not rows:
        print("No contacts found.")
        return

    for row in rows:
        print(row)


def delete_contact():
    print("1. Delete by phone")
    print("2. Delete by name")
    choice = input("Choice: ")

    if choice == "1":
        phone = input("Phone: ")
        cur.execute("DELETE FROM phonebook WHERE phone = %s", (phone,))
    elif choice == "2":
        name = input("Name: ")
        cur.execute("DELETE FROM phonebook WHERE name ILIKE %s", (name,))
    
    conn.commit()
    print("Deleted.")


while True:
    print("\n1. Import from CSV")
    print("2. Add contact")
    print("3. Update contact")
    print("4. Search contacts")
    print("5. Delete contact")
    print("0. Exit")

    choice = input("Choice: ")

    if choice == "1":
        insert_from_csv()
    elif choice == "2":
        insert_from_console()
    elif choice == "3":
        update_contact()
    elif choice == "4":
        search_contacts()
    elif choice == "5":
        delete_contact()
    elif choice == "0":
        break