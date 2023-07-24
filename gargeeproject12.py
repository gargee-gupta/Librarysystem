#Book Store
print('''   \t////////////////////////////////////////////
         \\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\n
         
      ************* WELCOME TO BooKWoRM.com ************
      
         \\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\n
         ////////////////////////////////////////////
                                                  ''')

#CONNECTING DATABASE
import mysql.connector as conn 
mylib=conn.connect(host="localhost", user="root", passwd="redhat", database="test",charset="utf8")
if mylib.is_connected():
    print('Connection Established To SQL Database')

a=mylib.cursor()
a.execute("drop database test")
a.execute("create database test")
a.execute("use test")
a.execute("drop table if exists library")
a.execute("create table library(book_code int Unique,book_name varchar(50),author varchar(25),publisher varchar(25),price int,stock text, edition varchar(10))")
#INSERTING VALUES 
a.execute("insert into library values(1021,'The Seal of Surya','Amritanshu Pandey','Pirates',175,25,'1st')")
a.execute("insert into library values(2403,'Matilda','Roald Dahl','Penguin',200,30,'3rd')")
a.execute("insert into library values(0082,'Think and grow rich','Napoleon Hill','Penguin',325,10,'5th')")
a.execute("insert into library values(2651,'My Journey','A.P.J. Abdul Kalam','Rupa',190,8,'1st')")
a.execute("insert into library values(3120,'Adventures of Sherlock Holmes','Sir Arthur conan doyle','Maple Press',225,20,'4th')")
a.execute("insert into library values(1026,'The Secret','Rhonda Byrne','Penguin',150,12,'2nd')")
a.execute("insert into library values(1258,'The Alchemist','Paulo Coelho','HarperCollins',200,21,'6th')")
a.execute("insert into library values(2638,'Ace against odds','Sania Mirza','Harpercollins',300,12,'3rd')")
mylib.commit();
#SHOWING RECORDS
print()
print()
print('------The Library Records as of now are ------')
a.execute("select * from library")
data=a.fetchall()
for row in data:
    print(row)
print()
print()
print()
while(True):
        print("HELLO")
        print("WELCOME TO BOOK STORE")
        print("Choose a Task")
        print("1. Adding a new book")
        print("2. Removing an existing book")
        print("3. Display the books available")
        print("4. Updating stock")
        print("5. Exit")
        print()
        cs=int(input("Enter your choice 1,2,etc.: "))
    
        if (cs==1):
            print("ADDING RECORDS")
            print()
            print("Fill the neccessary information to add a new books")
            print()
            print("All information prompted are mandatory to be filled")
            print()
            ucode=int(input('Enter the Book Code'))
            name=str(input("enter book name: "))
            aut=str(input("enter author name: "))
            ph=str(input("enter publishing house: "))
            price=int(input("enter the price: "))
            stock=int(input("enter the new stock:"))
            edi=str(input("enter the edition: "))
            a.execute("insert into library values('"+str(ucode)+"','"+name+" ','"+aut+"','"+str(ph)+"','"+str(price)+"','"+str(stock)+"','"+edi+"')")
            mylib.commit()
            print("*****\\\ New Book Addition procedure Successful ///*****")
            print()
            a.execute("select * from library")
            data=a.fetchall()
            for row in data:
                print(row)
        elif(cs==2):
            print("REMOVING RECORDS")
            print()
            print("Removing Books on the basis of the following:")
            print("1.Book Code")
            print("2.Name")
            print()
            c=int(input("Enter your choice:"))
            print()
            if(c==1):
                print("Fill the Code No. of the book to remove it from the store")
                cde=str(input("enter the name of book to be removed: "))
                a.execute("delete from library where book_code ='"+cde+"'")
                mylib.commit()
                print("*****\\\ Removal Command Successful ///*****")
                print()
                a.execute("select * from library")
                data=a.fetchall()
                for row in data:
                    print(row)

            elif(c==2):
                print("Enter the name of the book to remove it from the store")
                print()
                nme=str(input("enter the name of book to be removed: "))
                a.execute("delete from library where book_name ='"+nme+"'")
                mylib.commit()
                print()
                print("*****\\\ Removal Command Successful ///*****")
                print()
                a.execute("select * from library")
                data=a.fetchall()
                for row in data:
                    print(row)
               
        elif(cs==3):
            print("SELECTING RECORDS")
            print()
            print()
            print("Displaying Details of books on the basis of the following:")
            print()
            print("1.Name")
            print("2.Book Code")
            c=int(input("Enter your choice:"))
            if(c==1):
                name=str(input("Enter the book name: "))
                a.execute("select * from library where book_name='"+name+"'")
                for i in (a):
                    print(i)

         

            elif(c==2):
                bcode=str(input("Enter the book code : "))
                print()
                a.execute("select * from library where book_code='"+bcode+"'")
                for i in (a):
                    print(i)
                    
        elif(cs==4):
            print("UPDATING RECORDS")
            print()
            print("What do you want to update:")
            print("1.Price")
            print("2.Edition")
            print("3.Stock")
            print()
            c=int(input("Enter your choice:"))
            if(c==1):
                print(" Please Fill following details")
                print()
                ncode=int(input("enter book code: "))
                price=int(input("enter the old price: "))
                p1=input("enter the new price:")
                a.execute("update library set price="+p1+"'where book_code='"+ncode+"'")
                print()
                print("PRICE UPDATION SUCCESSFULL")
                mylib.commit()
                a.execute("select * from library")
                data=a.fetchall()
                for row in data:
                    print(row)

            elif(c==2):
                print(" Please Fill following details")
                print()
                namec=str(input("enter book name: "))
                ed=str(input("enter the old edition: "))
                ed1=input("enter the new edition:")
                a.execute("update library set '+edition+'= "'+ed1+'"where book_name= '+namec+'")
                print()
                print("Book Edition Updation Successful")
                mylib.commit()
                a.execute("select * from library")
                data=a.fetchall()
                for row in data:
                    print(row)

            else:
                print(" Please Fill following details")
                print()
                namec=str(input("enter book name: "))
                s=str(input("enter the old stock: "))
                s1=str(input("enter the new stock:"))
                a.execute("update library set stock="+s1+"'where book_name='"+name+"'")
                print()
                print("STOCK UPDATION SUCCESSFUL")
                mylib.commit()
                a.execute("select * from library")
                data=a.fetchall()
                for row in data:
                      print(row)


        else:
            print("THANK YOU!!!!")
            break
