import cx_Oracle

def get_connection():
    return cx_Oracle.connect("system", "swathi", "localhost:1521/XEPDB1")

while True:
    print("\n--- ICURD Menu ---")
    print("1. Insert")
    print("2. Create Table")
    print("3. Update")
    print("4. Read (Select)")
    print("5. Delete")
    print("6. Exit")

    choice = int(input("Enter your choice: "))

    match choice:
        # INSERT
        case 1:
            conn = get_connection()
            cur = conn.cursor()
            id = int(input("Enter ID: "))
            name = input("Enter Name: ").strip()
            course = input("Enter Course: ").strip()

            # Check duplicate (id, name, course)
            cur.execute("SELECT COUNT(*) FROM stu WHERE id=:1 AND name=:2 AND course=:3",
                        (id, name, course))
            count = cur.fetchone()[0]

            if count == 0:
                cur.execute("INSERT INTO stu (id, name, course) VALUES (:1, :2, :3)",
                            (id, name, course))
                conn.commit()
                print("Record Inserted")
            else:
                print("Duplicate entry for this ID, Name, and Course! Not inserted.")

            cur.close()
            conn.close()

        # CREATE TABLE
        case 2:
            conn = get_connection()
            cur = conn.cursor()
            try:
                # Drop table if exists
                try:
                    cur.execute("DROP TABLE stu PURGE")
                except:
                    pass  # ignore if table does not exist

                # Create table with composite primary key (id, name, course)
                cur.execute("""
                    CREATE TABLE stu (
                        id NUMBER,
                        name VARCHAR2(50),
                        course VARCHAR2(50),
                        CONSTRAINT stu_pk PRIMARY KEY (id, name, course)
                    )
                """)
                print("Table Created")
            except Exception as e:
                print("Error:", e)
            finally:
                cur.close()
                conn.close()

        # UPDATE
        case 3:
            conn = get_connection()
            cur = conn.cursor()
            id = int(input("Enter ID to update: "))
            name = input("Enter Name: ").strip()
            old_course = input("Enter old course: ").strip()
            new_course = input("Enter new course: ").strip()

            # Prevent duplicate (id, name, new_course)
            cur.execute("SELECT COUNT(*) FROM stu WHERE id=:1 AND name=:2 AND course=:3",
                        (id, name, new_course))
            count = cur.fetchone()[0]

            if count > 0:
                print("This combination already exists. Update not allowed.")
            else:
                cur.execute("UPDATE stu SET course=:1 WHERE id=:2 AND name=:3 AND course=:4",
                            (new_course, id, name, old_course))
                conn.commit()
                if cur.rowcount > 0:
                    print("Record Updated")
                else:
                    print("No matching record found.")

            cur.close()
            conn.close()

        # READ
        case 4:
            conn = get_connection()
            cur = conn.cursor()
            cur.execute("SELECT * FROM stu ORDER BY id, name, course")
            rows = cur.fetchall()
            print("\nID   NAME         COURSE")
            print("---------------------------------")
            for r in rows:
                print(f"{r[0]:<5} {r[1]:<12} {r[2]}")
            print(f"\nTotal Records: {len(rows)}")
            cur.close()
            conn.close()

        # DELETE
        case 5:
            conn = get_connection()
            cur = conn.cursor()
            id = int(input("Enter ID to delete: "))
            name = input("Enter Name: ").strip()
            course = input("Enter course to delete: ").strip()
            cur.execute("DELETE FROM stu WHERE id=:1 AND name=:2 AND course=:3",
                        (id, name, course))
            conn.commit()
            if cur.rowcount > 0:
                print("Record Deleted")
            else:
                print("No matching record found.")
            cur.close()
            conn.close()

        # EXIT
        case 6:
            print("Exiting program...")
            break

        # DEFAULT
        case _:
            print("Invalid choice. Try again.")
