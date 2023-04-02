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
        
        
#Gives the information of a site on a given street 1
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
    
    print("Site:")
    for row in rows:
        print(row)
    
    closeConnection(con)

#Gives the information of a display with a given scheduler system 2
def scheduler(param):
    con = createConnection("ABC.sqlite")
    cursor=con.cursor()
    
    cursor.execute("""
                    SELECT DigitalDisplay.serialNo, DigitalDisplay.modelNo, TechnicalSupport.name 
                    FROM DigitalDisplay 
                    INNER JOIN Specializes ON DigitalDisplay.modelNo = Specializes.modelNo 
                    INNER JOIN TechnicalSupport ON Specializes.empId = TechnicalSupport.empId 
                    WHERE DigitalDisplay.schedulerSystem = ?
                   """,(param,))
    
    rows=cursor.fetchall()
    print("Displays:")
    for row in rows:
        print(rows)
        
    closeConnection(con)
    
#Gives the names of all salesmen and the number of salesmen with that name 3
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
    print("Name\t\tCnt")
    print("-"*25)
    for row in rows:
        print(row[0], row[1])
        if row[1] > 1:
            query2 = "SELECT * FROM Salesman WHERE name = ?"
            cursor.execute(query2, (row[0],))
            more_rows = cursor.fetchall()
            for more_row in more_rows:
                print(more_row)
    closeConnection(con)
    
#Finds a client with a given phone number 4
def client(param):
    con = createConnection("ABC.sqlite")
    cursor=con.cursor()
    
    cursor.execute("""
                    SELECT * FROM Client WHERE phone = ?
                   """, (param,))
    
    rows=cursor.fetchall()
    print("Client:")
    for row in rows:
        print(row)
        
    closeConnection(con)
    
#Finds the total working hours of each administrator 5
def admwork():
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
    print("Total working hours of each administrator:")
    for row in rows:
        print(row[0], row[1], row[2])
        
    closeConnection(con)

#Finds technical support that specialize in a specified model 6
def tech(param):
    con = createConnection("ABC.sqlite")
    cursor=con.cursor()
    
    cursor.execute(
                   """
                   SELECT TechnicalSupport.name
                   FROM TechnicalSupport
                   INNER JOIN Specializes ON TechnicalSupport.empID = Specializes.empID
                   WHERE Specializes.modelNo = ?
                   """, (param,)
                   )
    
    rows=cursor.fetchall()
    print("Technical Supports that specialize in the given model:")
    for row in rows:
        print(row[0])
        
    closeConnection(con)

#Orders salesment in decending order of their average commission rates 7
def commission():
    con = createConnection("ABC.sqlite")
    cursor=con.cursor()
    
    cursor.execute("""
                   SELECT Salesman.name, AVG(Purchases.commisionRate) as average_rate
                   FROM Salesman
                   INNER JOIN Purchases ON Salesman.empID = Purchases.empID
                   GROUP BY Salesman.name
                   ORDER BY average_rate desc 
                   """)
    
    rows=cursor.fetchall()
    print("Average commision rates:")
    for row in rows:
        print(row[0], row[1])
        
    closeConnection(con)
    
#Calculates the number of administrators, salesmen, and technical supports 8
def calc():
    con = createConnection("ABC.sqlite")
    cursor=con.cursor()
    
    cursor.execute("""
                   SELECT 'Administrator' as Admin_name, COUNT(Administrator.name)
                   FROM Administrator
                   UNION ALL 
                   SELECT 'Salesman' as Salesman_name, COUNT(Salesman.empID)
                   FROM Salesman
                   UNION ALL 
                   Select 'Technicians' as technicalSupport_name, COUNT(TechnicalSupport.empID)
                   from TechnicalSupport
                   """)
    
    rows=cursor.fetchall()
    amnt=0
    for row in rows:
        print(row[0], row[1])
        amnt+=row[1]
    print("Total Number of administrators, salesmen, and technical supports:")
    print(amnt)
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

   
