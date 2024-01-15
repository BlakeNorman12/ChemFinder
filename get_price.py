import mysql.connector
import suppliers
from suppliers import Chemical_Suppliers

def search_chemical(db_config, Chemical_Suppliers):
    # Connect to the database
    conn = mysql.connector.connect(**db_config)
    cursor = conn.cursor()

    # Ask the user for the chemical they want to search for
    chemical_name = input("Enter the chemical name you want to search for: ")

    # Flag to check if chemical is found
    found = False

    # Iterate over each table and search for the chemical
    for table_name in Chemical_Suppliers:
        query = f"SELECT * FROM {table_name} WHERE Chemical_Name = %s"
        cursor.execute(query, (chemical_name,))

        result = cursor.fetchall()
        if result:
            found = True
            print(f"Found in {table_name}: {result}")

    if not found:
        print("Chemical not found in any table.")

    # Close the cursor and the connection
    cursor.close()
    conn.close()

# Database configuration
db_config = {
    'user': 'root',
    'password': 'root',
    'host': '127.0.0.1',
    'database': 'websites'
}


# Call the function
search_chemical(db_config, Chemical_Suppliers)