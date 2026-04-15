import csv
import psycopg2
from connect import connect

conn = connect()
cur = conn.cursor()





def import_csv():
    with open("contacts.csv", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        for row in reader:
            cur.execute("""
                INSERT INTO phonebook (name, phone)
                VALUES (%s, %s)
                ON CONFLICT (phone) DO NOTHING
            """, (row["name"], row["phone"]))

    conn.commit()
    print("CSV imported.")

with open("functions.sql", encoding="utf-8") as f:
        cur.execute(f.read())

with open("procedures.sql", encoding="utf-8") as f:
        cur.execute(f.read())
conn.commit()

def upsert():
    name = input("Name: ")
    phone = input("Phone: ")

    cur.execute("CALL upsert_contact(%s, %s)", (name, phone))
    conn.commit()
    print("Done.")


def search():
    pattern = input("Search: ")

    cur.execute("SELECT * FROM search_contacts(%s)", (pattern,))
    rows = cur.fetchall()

    if not rows:
        print("No contacts found.")
    else:
        for row in rows:
            print(row)



def bulk_insert():
    names, phones = [], []

    print("Enter: name phone (type 'done')")

    while True:
        line = input("> ").strip()
        if line.lower() == "done":
            break

        parts = line.split()
        if len(parts) != 2:
            print("Wrong format")
            continue

        names.append(parts[0])
        phones.append(parts[1])

    if not names:
        print("No data")
        return

    cur.execute(
        "CALL bulk_insert_contacts(%s::varchar[], %s::varchar[])",
        (names, phones)
    )
    conn.commit()
    print("Bulk insert done.")


def pagination():
    limit = int(input("Limit: "))
    offset = int(input("Offset: "))

    cur.execute("SELECT * FROM get_contacts_paginated(%s, %s)", (limit, offset))
    rows = cur.fetchall()

    for row in rows:
        print(row)



def delete():
    value = input("Enter name or phone: ")

    cur.execute("CALL delete_contact(%s)", (value,))
    conn.commit()
    print("Deleted.")


while True:
    print("\n1. Import CSV")
    print("2. Add/Update")
    print("3. Search")
    print("4. Bulk insert")
    print("5. Pagination")
    print("6. Delete")
    print("0. Exit")

    choice = input("Choose: ")

    if choice == "1":
        import_csv()
    elif choice == "2":
        upsert()
    elif choice == "3":
        search()
    elif choice == "4":
        bulk_insert()
    elif choice == "5":
        pagination()
    elif choice == "6":
        delete()
    elif choice == "0":
        break
    else:
        print("Invalid choice")

