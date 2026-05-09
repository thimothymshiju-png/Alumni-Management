import mysql.connector

#1. Establishing the connection to MySQL

def connect_to_db():
    return mysql.connector.connect(
        host="localhost",       # Change if different
        user="root",   # Replace with your MySQL username
        passwd="aittitos7$", # Replace with your MySQL password
        database="alumni_management"
    )

#2. Function to add a new alumni record

def add_alumni(name, graduation_year, degree, email):
    conn = connect_to_db()
    cursor = conn.cursor()
    query = "INSERT INTO alumni1(Alumni_ID,name, graduation_year, degree, email) VALUES (%s,%s, %s, %s, %s)"
    cursor.execute(query, (Alumni_ID,name, graduation_year, degree, email))
    conn.commit()
    print(f"Alumni1 {name} added successfully!")
    conn.close()

#3. Function to update an alumni record

def update_alumni(id, name=None, graduation_year=None, degree=None, email=None):
    conn = connect_to_db()
    cursor = conn.cursor()
    query = "UPDATE Alumni1 SET "
    updates = []
    values = []

    # Only update fields provided
    if name:
        updates.append("name = %s")
        values.append(name)
    if graduation_year:
        updates.append("graduation_year = %s")
        values.append(graduation_year)
    if degree:
        updates.append("degree = %s")
        values.append(degree)
    if email:
        updates.append("email = %s")
        values.append(email)

    query += ", ".join(updates) + " WHERE id = %s"
    values.append(id)
    cursor.execute(query, values)
    conn.commit()
    print(f"Alumni with ID {id} updated successfully!")
    conn.close()

#4. Function to delete an alumni record

def delete_alumni(id):
    conn = connect_to_db()
    cursor = conn.cursor()
    query = "DELETE FROM alumni WHERE id = %s"
    cursor.execute(query, (id,))
    conn.commit()
    print(f"Alumni with ID {id} deleted successfully!")
    conn.close()

#5. Function to view all alumni records

def view_alumni():
    conn = connect_to_db()
    cursor = conn.cursor()
    query = "SELECT * FROM alumni"
    cursor.execute(query)
    records = cursor.fetchall()

    print("Alumni Records:")
    print("ID | Name | Graduation Year | Degree | Email")
    for record in records:
        print(f"{record[0]} | {record[1]} | {record[2]} | {record[3]} | {record[4]}")
    conn.close()
#6 .For searching Alumni
    def search_alumni(connection):
        search_name = input("Enter name to search: ")
        cursor = connection.cursor()
        query = "SELECT * FROM alumni WHERE name LIKE %s"
        cursor.execute(query, ('%' + search_name + '%',))
        alumni = cursor.fetchall()
        if alumni:
            for alum in alumni:
                print(f"ID: {alum[0]}, Name: {alum[1]}, Email: {alum[2]}, Phone: {alum[3]}, Graduation Year: {alum[4]}")
        else:
            print("No alumni found with that name.")


# 7. Add Event
def add_event(connection):
    event_name = input("Enter event name: ")
    event_date = input("Enter event date (YYYY-MM-DD): ")
    event_description = input("Enter event description: ")

    cursor = connection.cursor()
    query = "INSERT INTO events (event_name, event_date, event_description) VALUES (%s, %s, %s)"
    values = (event_name, event_date, event_description)

    cursor.execute(query, values)
    connection.commit()
    print("Event added successfully.")

# 8. Search Event
def search_event(connection):
    event_name = input("Enter event name to search: ")
    cursor = connection.cursor()
    query = "SELECT * FROM events WHERE event_name LIKE %s"
    cursor.execute(query, ('%' + event_name + '%',))
    
    events = cursor.fetchall()
    if events:
        for event in events:
            print(f"Event ID: {event[0]}, Name: {event[1]}, Date: {event[2]}, Description: {event[3]}")
    else:
        print("No event found with that name.")

# 8. Delete Event
def delete_event(connection):
    event_id = int(input("Enter Event ID to delete: "))
    
    cursor = connection.cursor()
    query = "DELETE FROM events WHERE event_id = %s"
    cursor.execute(query, (event_id,))
    connection.commit()
    print("Event deleted successfully.")

# Main menu
def main():
    while True:
        print("\n--- Alumni Management System ---")
        print("1. Register Alumni")
        print("2.  Update Alumni")
        print("3. Delete Alumni")
        print("4. To View Alumni Details")
        print("5. Search Alumni")
        print("6.Add Event")
        print("7.Search Event")
        print("8.Delect a Event ")
        print("9. Exit")

        choice = input("Enter your choice (1-9): ")

        if choice == '1':
            name = input("Enter name: ")
            graduation_year = int(input("Enter graduation year: "))
            degree = input("Enter degree: ")
            email = input("Enter email: ")
            add_alumni(name, graduation_year, degree, email)

        elif choice == '2':
            id = int(input("Enter alumni ID to update: "))
            name = input("Enter new name (leave blank to keep current): ")
            graduation_year = input("Enter new graduation year (leave blank to keep current): ")
            degree = input("Enter new degree (leave blank to keep current): ")
            email = input("Enter new email (leave blank to keep current): ")

            # Only pass values if provided
            update_alumni(
                id,
                name if name else None,
                int(graduation_year) if graduation_year else None,
                degree if degree else None,
                email if email else None
                )

        elif choice == '3':
            id = int(input("Enter alumni ID to delete: "))
            delete_alumni(id)

        elif choice == '4':
            view_alumni()

        elif choice == '9':
            print("Exiting Alumni Management System.")
            break
        elif choice =='5':
            SearchAlumni()
        elif choice =='6':
            add_event(connection)
        elif choice =='7':
            search_event(connection)
        elif choice =='8':
            delete_event(connection)

        else:
            print("Invalid choice. Please enter a number between 1 and 9.")
        

# Run the program
if __name__ == "__main__":
    main()
