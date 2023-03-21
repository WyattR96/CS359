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
    con = sqlite3.connect("ABC.sqlite")
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
    
#Gives the information of a display with a given scheduler system
def scheduler(param):
    con = sqlite3.connect("ABC.sqlite")
    
    cursor=con.cursor()
    cursor.execute("""
                   INSERT SQL HERE
                   """)
    
    rows=cursor.fetchall()
    for row in rows:
        print(row)
    
#Gives the names of all salesmen and the number of salesmen with that name
def salesmen():
    con = sqlite3.connect("ABC.sqlite")
    
    cursor=con.cursor()
    cursor.execute("""
                   INSERT SQL HERE
                   """)
    
    rows=cursor.fetchall()
    for row in rows:
        print(row)

#Finds a client with a given phone number
def client(param):
    con = sqlite3.connect("ABC.sqlite")
    
    cursor=con.cursor()
    cursor.execute("""
                   INSERT SQL HERE
                   """)
    
    rows=cursor.fetchall()
    for row in rows:
        print(row)
    
#Finds the total working hours of each administrator 
def admwork():
    con = sqlite3.connect("ABC.sqlite")
    
    cursor=con.cursor()
    cursor.execute("""
                   INSERT SQL HERE
                   """)
    
    rows=cursor.fetchall()
    for row in rows:
        print(row)
    
#Finds technical support that specialize in a specified model
def tech(param):
    con = sqlite3.connect("ABC.sqlite")
    
    cursor=con.cursor()
    cursor.execute(
                   """
                   INSERT SQL HERE
                   """
                   )
    
    rows=cursor.fetchall()
    for row in rows:
        print(row)

#Orders salesment in decending order of their average commission rates
def commission():
    con = sqlite3.connect("ABC.sqlite")
    
    cursor=con.cursor()
    cursor.execute("""
                   INSERT SQL HERE
                   """)
    
    rows=cursor.fetchall()
    for row in rows:
        print(row)
    
#Calculates the number of administrators, salesmen, and technical supports
def calc():
    con = sqlite3.connect("ABC.sqlite")
    
    cursor=con.cursor()
    cursor.execute("""
                   INSERT SQL HERE
                   """)
    
    rows=cursor.fetchall()
    for row in rows:
        print(row)

#Replaces underscores in the argument with spaces
def textProcessing():
    return str(sys.argv[2]).replace("_"," ")

#Calls the main function
if __name__ == '__main__':
    main() 
   
