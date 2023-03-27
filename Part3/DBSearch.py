import sys
import sqlite3

def main():
    
    func = int(sys.argv[1])
    
    if func==1:
        street(textProcessing())
    elif func==2:
        scheduler(textProcessing())
    elif func==3:
        salesmen()
    elif func==4:
        client(textProcessing())
    elif func==5:
        admwork()
    elif func==6:
        tech(textProcessing())
    elif func==7:
        commission()
    elif func==8:
        calc()
    else:
        print("Function number out of range, must be a number between 1 and 8")
        
        
#Gives the information of a site on a given street
def street(param):
    con = createConnection("ABC.sqlite")
    cursor=con.cursor()
    
    cursor.execute(
                    """
                      SELECT *
                      FROM Site
                      WHERE address LIKE ?
                    """
                    ,(param,))
    
    
    rows=cursor.fetchall()
    for row in rows:
        print(row)
    
    closeConnection(con)
    
#Gives the information of a display with a given scheduler system
def scheduler(param):
    con = createConnection("ABC.sqlite")
    cursor=con.cursor()
    
    cursor.execute("""
                    SELECT DigitalDisplay.serialNo, DigitalDisplay.modelNo, TechnicalSupport.name 
                    FROM DigitalDisplay 
                    INNER JOIN Specializes ON DigitalDisplay.modelNo = Specializes.modelNo 
                    INNER JOIN TechnicalSupport ON Specializes.empId = TechnicalSupport.empId 
                    WHERE DigitalDisplay.schedulerSystem = ?
                   """)
    
    rows=cursor.fetchall()
    for row in rows:
        print(row[0], row[1])
        if row[1] > 1:
            query2 = "SELECT * FROM Salesman WHERE name = ?"
            c.execute(query2, (row[0],))
            more_rows = c.fetchall()
            for more_row in more_rows:
                print(more_row)
    closeConnection(con)
    
#Gives the names of all salesmen and the number of salesmen with that name
def salesmen():
    con = createConnection("ABC.sqlite")
    cursor=con.cursor()
    
    cursor.execute("""
                    SELECT name, COUNT(*) as cnt 
                    FROM Salesman 
                    GROUP BY name 
                    ORDER BY name ASC
                   """)
    
    rows=cursor.fetchall()
    for row in rows:
        print(row)
    
    closeConnection(con)

#Finds a client with a given phone number
def client(param):
    con = createConnection("ABC.sqlite")
    cursor=con.cursor()
    
    cursor.execute("""
                    SELECT Administers.empId, Administrator.name, SUM(AdmWorkHours.hours) as total_hours 
                    FROM Administers 
                    INNER JOIN AdmWorkHours ON Administers.empId = AdmWorkHours.empId 
                    INNER JOIN Administrator ON Administers.empId = Administrator.empId 
                    GROUP BY Administers.empId 
                    ORDER BY total_hours ASC
                   """)
    
    rows=cursor.fetchall()
    for row in rows:
        print(row[0], row[1], row[2])
        
    closeConnection(con)
    
#Finds the total working hours of each administrator 
def admwork():
    con = createConnection("ABC.sqlite")
    cursor=con.cursor()
    
    cursor.execute("""
                   INSERT SQL HERE
                   """)
    
    rows=cursor.fetchall()
    for row in rows:
        print(row)
        
    closeConnection(con)
    
#Finds technical support that specialize in a specified model
def tech(param):
    con = createConnection("ABC.sqlite")
    cursor=con.cursor()
    
    cursor.execute(
                   """
                   INSERT SQL HERE
                   """
                   )
    
    rows=cursor.fetchall()
    for row in rows:
        print(row)
        
    closeConnection(con)

#Orders salesment in decending order of their average commission rates
def commission():
    con = createConnection("ABC.sqlite")
    cursor=con.cursor()
    
    cursor.execute("""
                   INSERT SQL HERE
                   """)
    
    rows=cursor.fetchall()
    for row in rows:
        print(row)
        
    closeConnection(con)
    
#Calculates the number of administrators, salesmen, and technical supports
def calc():
    con = createConnection("ABC.sqlite")
    cursor=con.cursor()
    
    cursor.execute("""
                   INSERT SQL HERE
                   """)
    
    rows=cursor.fetchall()
    for row in rows:
        print(row)
        
    closeConnection(con)


#Replaces underscores in the argument with spaces
def textProcessing():
    return str(sys.argv[2]).replace("_"," ")

#Creates a connection to the database
def createConnection(file):
    con=None
    try:
        con=sqlite3.connect(file)
        print("Connection successful")
        
    except sqlite3.Error as e:
        print(e)
    
    return con

#Closes the database connection
def closeConnection(con):
    con.close()

#Checks if the user has input arguments for the program
n=len(sys.argv)
if n==1:
    print("Program requires at least 1 argument.") 
else:
    #Calls the main function
    if __name__ == '__main__':
        main() 

   
