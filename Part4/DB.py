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
    print("\nSearch\n")

def insertDisplay(con):
    print("\ninsert\n")

def deleteDisplay(con):
    print("\nDelete\n")
    
def updateDisplay(con):
    print("\nUpdate\n")
    
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