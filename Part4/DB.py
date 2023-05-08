import sys
import os
import sqlite3

def main():
    
    con = None
    
    while True:
        name = input("Type the name of the database you would like to access:\n")
        if os.path.exists(name):
            con = createConnection(name)
            break
        else:
            print("Database file not found")
    
    while True:
        print("What would you like to do?:")
        print("1. List all digital displays")
        print("2. Search digital displays given a scheduler system")
        print("3. Insert a new digital display")
        print("4. Delete a digital display")
        print("5. Update a digital display")
        print("6. Exit")
        selection = int(input("\n"))
        
        if selection == 1:
            listDisplays(con)
        elif selection == 2:
            searchDisplays(con)
        elif selection == 3:
            insertDisplay(con)
        elif selection == 4:
            deleteDisplay(con)
        elif selection == 5:
            updateDisplay(con)
        elif selection == 6:
            logout(con)
        else:
            print("Invalid option")
        
            
def listDisplays(con):
    cursor=con.cursor()
    
    cursor.execute(
                    """
                      SELECT *
                      FROM DigitalDisplay
                    """
                    )
    
    rows=cursor.fetchall()
    
    print("Serial Scheduler Model")
    for row in rows:
        print(row)  
    print("\n")
    
    model = input("Type in the model number you would like to know more about\n")
    
    cursor.execute(
                    """
                      SELECT *
                      FROM Model
                      WHERE modelNo = ?
                    """,
                    (model,))
    
    modelRows=cursor.fetchall()
    
    if len(modelRows)==0:
        print("Not found")
    else:
        for row in modelRows:
            print("modelNo: "+row[0])
            print("width: "+str(row[1]))
            print("height: "+str(row[2]))
            print("weight: "+str(row[3]))
            print("depth: "+str(row[4]))
            print("screenSize: "+str(row[5]))
        print("\n")

def searchDisplays(con):
    schedulerSystem = input("Enter a scheduler system (Random/Smart/Virtue): ")
    cursor = con.cursor()

    cursor.execute(
        """
        SELECT *
        FROM DigitalDisplay
        WHERE schedulerSystem = ?
        """,
        (schedulerSystem,)
    )

    rows = cursor.fetchall()

    if len(rows) == 0:
        print("No displays found with this scheduler system.")
    else:
        print("Serial Scheduler Model")
        for row in rows:
            print(row)
        print("\n")

def insertDisplay(con):
    serialNo = input("Enter a serial number: ")
    schedulerSystem = input("Enter a scheduler system (Random/Smart/Virtue): ")
    modelNo = input("Enter a model number: ")
    cursor = con.cursor()

    try:
        cursor.execute(
            """
            INSERT INTO DigitalDisplay (serialNo, schedulerSystem, modelNo)
            VALUES (?, ?, ?)
            """,
            (serialNo, schedulerSystem, modelNo)
        )
        con.commit()
        print("Display successfully inserted.")
    except sqlite3.IntegrityError:
        print("Error: Serial number already exists.")
    print("\n")

def deleteDisplay(con):
    cursor = con.cursor()

    cursor.execute(
        """
          SELECT *
          FROM DigitalDisplay
        """
    )

    rows = cursor.fetchall()

    print("Serial Scheduler Model")
    for row in rows:
        print(row)
    print("\n")
    delete_selection = input("Please select by model Number which digital display you would like to Delete\n")

    cursor.execute(
        """
        DELETE FROM DigitalDisplay
        WHERE modelNo = ?
        """, (delete_selection,)
    )
    
    con.commit()
    
    print("New List of Digital Displays")

    cursor.execute(
        """
          SELECT *
          FROM DigitalDisplay
        """
    )

    rows = cursor.fetchall()

    print("Serial Scheduler Model")
    for row in rows:
        print(row)
    print("\n")
    
    
def updateDisplay(con):
    cursor = con.cursor()

    cursor.execute(
        """
          SELECT *
          FROM DigitalDisplay
        """
    )

    rows = cursor.fetchall()

    print("Serial Scheduler Model")
    for row in rows:
        print(row)
    print("\n")

    selected_display = input("Please select which display you would like to Update by modelNo\n")

    cursor.execute(
        """
        SELECT serialNo, schedulerSystem, modelNo
        FROM DigitalDisplay
        WHERE modelNo = ?
        """, (selected_display,)
    )

    rows = cursor.fetchall()
    print("Serial Scheduler Model")
    for row in rows:
        print(row)
    print("\n")

    print("Select what you would like to update enter 1, 2, or 3\n")
    change_selection = int(input("1 for serial Number, 2 for Scheduler, and 3 for model number\n"))


    if change_selection == 1:
        new_info = input("What would you like to change serialNo to?\n")

        cursor.execute(
            """
            UPDATE DigitalDisplay
            SET serialNo = ?
            WHERE modelNo = ?
            """, (new_info, selected_display, )
        )
        print("New Updated Table\n")

        cursor.execute(
            """
              SELECT *
              FROM DigitalDisplay
            """
        )

        rows = cursor.fetchall()

        print("Serial Scheduler Model")
        for row in rows:
            print(row)
        print("\n")

    elif change_selection == 2:
        new_info = input("What would you like to change schedulerSystem to (Virtual, Random, or Smart)?\n")

        cursor.execute(
            """
            UPDATE DigitalDisplay
            SET schedulerSystem = ?
            WHERE modelNo = ?
            """, (new_info, selected_display,)
        )
        print("New Updated Table\n")

        cursor.execute(
            """
              SELECT *
              FROM DigitalDisplay
            """
        )
        
        con.commit()
        
        rows = cursor.fetchall()

        print("Serial Scheduler Model")
        for row in rows:
            print(row)
        print("\n")

    elif change_selection == 3:
        new_info = input("What would you like to change modelNo to?\n")

        cursor.execute(
            """
            UPDATE DigitalDisplay
            SET modelNo = ?
            WHERE modelNo = ?
            """, (new_info, selected_display,)
        )
        print("New Updated Table\n")

        cursor.execute(
            """
              SELECT *
              FROM DigitalDisplay
            """
        )
        
        con.commit()
        
        rows = cursor.fetchall()

        print("Serial Scheduler Model")
        for row in rows:
            print(row)
        print("\n")

    else:
        print("invalid input\n")
        
    
def logout(con):
    closeConnection(con)
    sys.exit(0)

#Creates a connection to the database
def createConnection(file):
    con=None
    try:
        con=sqlite3.connect(file)
        print("Connection successful\n")
        
    except sqlite3.Error as e:
        print(e)
    
    return con

#Closes the database connection
def closeConnection(con):
    con.close()

#Calls the main function
if __name__ == '__main__':
    main() 
