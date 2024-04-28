# mysql connector program
import mysql.connector
from datetime import timedelta
from datetime import date
import smtplib
from email.message import EmailMessage
import webbrowser
import os


def database(p):
    # creating database
    con = mysql.connector.connect(host="localhost", user="root", password=p)
    cur = con.cursor()
    ch1 = input("ENTER DATABASE NAME OF YOUR CHOICE ")
    q = "CREATE DATABASE " + ch1
    cur.execute(q)
    print("DATABASE CREATED SUCCESSFULLY")
    # this is write  function
    ap_file = open(r"D:\school_project\databases.txt", "a")
    nm = ch1
    ap_file.write(nm + "\n")
    ap_file.close()
    return ch1

def checklist(ab, a, p):
    s = str(a)
    email_list = {}
    # inserting data in table library_management
    con = mysql.connector.connect(host="localhost", user="root", password=p, database=s)
    cur = con.cursor()
    q = "SELECT * FROM " + ab + " WHERE datediff(curdate(),date_of_issue) > 7 AND return_status = 'no'"
    cur.execute(q)
    data = cur.fetchall()
    for j in data:
        ids = j[6]
        b = j[3]
        email_list[b] = ids
        print(j)

    try:
        def send_email(receiver, subject, message):
            server = smtplib.SMTP('smtp.gmail.com', 587)
            server.starttls()
            # Make sure to give app access in your Google account
            # Here the school's email address and password will be placed
            server.login("sankhyapatra0808@gmail.com", "@SankhyaPatra0808@")
            email = EmailMessage()
            # here th same email as the school's one has to be given
            email['From'] = 'sankhyapatra0808@gmail.com'
            email['To'] = receiver
            email['Subject'] = subject
            email.set_content(message)
            server.send_message(email)

        def get_email_info():
            receiver = email_list.values()
            print(receiver)
            subject = "Order to bring back the Library Book"
            print(subject)
            message = "Hello " + str(email_list.keys())[10:len(str(email_list.keys()))-1:] + ", you are CORDIALLY REQUESTED to come to the SCHOOL to give back the LIBRARY BOOK that you have taken SEVEN DAYS ago AS SOON AS POSSIBLE...."
            print(message)
            send_email(receiver, subject, message)

        get_email_info()

    except:
        print("THERE MIGHT BE NO TARGET EMAIL TO SEND RIGHT NOW \n          OR \nMAY BE THE EMAIL COLUMN IS EMPTY")
        ch1 = input("ARE THERE ANY TARGETED EMAILS IN THE DATABASE ").lower()
        if "yes" in ch1:
            print(
                "please do check this before executing if it is off turn this on because without this email cannot be send")
            webbrowser.open(
                "https://myaccount.google.com/lesssecureapps?pli=1&rapt=AEjHL4MGX02yWbsMZOL1S-ZSGFUYRo1Uc1zQnRduYKwnCDzmEz4-uywEMgFqm4oJsJfLzBYmlKzyi5HFZIcO6ImykGRMo838rg")
            ch = input("did you do the previous one")
            if "yes" in ch:
                print(
                    "please even do check this before executing if it is on turn this off because without this email cannot be send")
                webbrowser.open("https://myaccount.google.com/security?origin=3")

            else:
                print(
                    "please do this first because without this email cannot be send")
                webbrowser.open(
                    "https://myaccount.google.com/lesssecureapps?pli=1&rapt=AEjHL4MGX02yWbsMZOL1S-ZSGFUYRo1Uc1zQnRduYKwnCDzmEz4-uywEMgFqm4oJsJfLzBYmlKzyi5HFZIcO6ImykGRMo838rg")

def table_creation(a, p):
    # creating table
    s = str(a)
    con = mysql.connector.connect(host="localhost", user="root", password=p, database=s)
    cur = con.cursor()
    ch2 = input("ENTER TABLE NAME OF YOUR CHOICE ")
    q = "CREATE TABLE " + ch2 + "(book_id int(6),book_name varchar(50),ISBN_no char(15),student_name varchar(40),book_series varchar(30),language varchar(20),email_address varchar(50),date_of_issue date,date_of_return date,return_status varchar(20))"
    cur.execute(q)
    print("TABLE CREATED SUCCESSFULLY")
    # this is write  function
    ap_file = open(r"D:\school_project\tables.txt", "a")
    nm = ch2
    ap_file.write(nm + "\n")
    ap_file.close()
    return ch2

def table_deletion(ab, a, p):
    s = str(a)
    con = mysql.connector.connect(host="localhost", user="root", password=p, database=s)
    cur = con.cursor()
    q = "DROP TABLE " + ab
    cur.execute(q)
    print("TABLE DELETED SUCCESSFULLY")

def database_deletion(a, p):
    s = str(a)
    con = mysql.connector.connect(host="localhost", user="root", password=p, database=s)
    cur = con.cursor()
    q = "DROP DATABASE " + a
    cur.execute(q)
    print("DATABASE DELETED SUCCESSFULLY")

def return_status_check_list(ab, a, p):
    c = 0
    d = 0
    s = str(a)
    con = mysql.connector.connect(host="localhost", user="root", password=p, database=s)
    cur = con.cursor()
    q = "SELECT book_id, book_name, student_name, return_status FROM " + ab
    cur.execute(q)
    data = cur.fetchall()
    lst = ["book_id", "book_name", "student_name", "return_status"]
    print(lst)
    for k in data:
        print(k)

    q2 = "SELECT datediff(curdate(),date_of_issue) FROM " + ab
    cur.execute(q2)
    data1 = cur.fetchall()
    for m in data1:
        if m[0] > 7:
            q1 = "SELECT return_status FROM " + ab
            cur.execute(q1)
            data2 = cur.fetchall()

        else:
            print("BOOK KEEPING DAYS ARE NOT PASSED YET")

    for n in data2:
        if n[0] == "YES":
            c += 1
        else:
            d += 1

    if c == 1:
        print(str(int(c)) + " STUDENT HAS RETURNED HIS/HER BOOK")
    elif c == 0:
        print("")
    else:
        print(str(int(c)) + " STUDENTS HAS RETURNED HIS/HER BOOK")

    if d == 1:
        print(str(int(d)) + " STUDENT HAS NOT RETURNED HIS/HER BOOK")
    elif d == 0:
        print("")
    else:
        print(str(int(d)) + " STUDENTS HAS NOT RETURNED HIS/HER BOOK")

    print("TABLE DISPLAYED SUCCESSFULLY")

def record_deletion(ab, a, p):
    s = str(a)
    con = mysql.connector.connect(host="localhost", user="root", password=p, database=s)
    cur = con.cursor()
    while True:
        id = int(input("ENTER THE ID OF THE BOOK "))
        q = "DELETE FROM " + ab + " WHERE book_id = " + str(id)
        cur.execute(q)
        con.commit()
        print("RECORD DELETED SUCCESSFULLY")
        cho = input("DO YOU WANT TO DELETE MORE JUST PRESS ENTER OR (Q/q) TO QUIT ")
        if cho == "q" or cho == "Q":
            break

def table_display(ab, a, p):
    s = str(a)
    con = mysql.connector.connect(host="localhost", user="root", password=p, database=s)
    cur = con.cursor()
    q = "SELECT * FROM " + ab
    cur.execute(q)
    data = cur.fetchall()
    lst = ["book_id", "book_name", "ISBN_no", "student_name", "book_series", "language", "email_address", "date_of_issue", "date_of_return", "return_status"]
    print(lst)
    for k in data:
        print(k)
    print("TABLE DISPLAYED SUCCESSFULLY")
    ch2 = input("DO YOU WANT TO SEE THE STUDENT'S INFORMATION WHO TOOK THE SAME BOOK ? (yes/no)").lower()
    if ch2 == "yes":
        book = input("ENTER THE NAME OF THE BOOK YOU WANT TO SEARCH ")
        q1 = "SELECT book_id, book_name, student_name, book_series, date_of_issue, date_of_return, return_status FROM " + ab + " WHERE book_name = '" + book + "'"
        cur.execute(q1)
        data1 = cur.fetchall()
        lst = ["book_id", "book_name", "student_name", "book_series",
               "date_of_issue", "date_of_return", "return_status"]
        print(lst)
        for m in data1:
            print(m)

    else:
        print("OK NO PROBLEM USE ME ANYTIME")

def table_display_next(ab, a, p):
    s = str(a)
    con = mysql.connector.connect(host="localhost", user="root", password=p, database=s)
    cur = con.cursor()
    q = "SELECT * FROM " + ab
    cur.execute(q)
    data = cur.fetchall()
    lst = ["book_id", "book_name", "ISBN_no", "student_name", "book_series", "language", "email_address", "date_of_issue", "date_of_return", "return_status"]
    print(lst)
    for k in data:
        print(k)

def table_updation(ab, a, p):
    s = str(a)
    con = mysql.connector.connect(host="localhost", user="root", password=p, database=s)
    cur = con.cursor()
    while True:
        id = int(input("ENTER THE ID OF THE BOOK "))
        q = "UPDATE " + ab + " SET return_status = 'YES' WHERE book_id = " + str(id)
        cur.execute(q)
        con.commit()
        print("TABLE UPDATED SUCCESSFULLY")
        cho = input("DO YOU WANT TO UPDATE MORE JUST PRESS ENTER OR (Q/q) TO QUIT ")
        if cho == "q" or cho == "Q":
            break

def record_update(ab, a, p):
    s = str(a)
    con = mysql.connector.connect(host="localhost", user="root", password=p, database=s)
    cur = con.cursor()
    while True:
        id = int(input("ENTER THE ID OF THE BOOK "))
        stud = input("ENTER THE STUDENT'S NAME ")
        col = input("ENTER THE COLUMN NAME YOU WANT TO CHANGE ")
        if col == "return_status":
            entry = input("PLEASE ENTER THE CHANGED ENTRY ").upper()

        else:
            entry = input("PLEASE ENTER THE CHANGED ENTRY ")

        q = "UPDATE " + ab + " SET " + col + " = '" + entry + "' WHERE book_id = " + str(id) + " AND student_name = '" + stud + "'"
        cur.execute(q)
        con.commit()
        print("TABLE UPDATED SUCCESSFULLY")
        cho = input("DO YOU WANT TO UPDATE MORE JUST PRESS ENTER OR (Q/q) TO QUIT ")
        if cho == "q" or cho == "Q":
            break

def data_entry(ab, a, p):
    # inserting data in table library_management
    s = str(a)
    con = mysql.connector.connect(host="localhost", user="root", password=p, database=s)
    cur = con.cursor()
    while True:
        book_id = int(input("ENTER THE BOOK'S REFERENCE ID "))
        book_name = input("ENTER THE BOOK'S NAME ")
        isbn = input("ENTER THE BOOK'S ISBN ID ")
        student_name = input("ENTER THE STUDENT'S NAME ")
        series = input("ENTER THE BOOK'S SERIES ")
        lang = input("ENTER THE BOOK'S LANGUAGE ")
        email = input("ENTER THE STUDENT'S EMAIL ID ")
        issue_date = date.today()
        return_date = date.today() + timedelta(days=7)
        return_stat = "NO"
        q = "INSERT INTO " + ab + " VALUES({},'{}','{}','{}','{}','{}','{}','{}','{}','{}')".format(book_id, book_name, isbn, student_name, series, lang, email, issue_date, return_date, return_stat)
        cur.execute(q)
        con.commit()
        print("DATA INSERTED SUCCESSFULLY ")
        print("PRESS ANY KEY TO CONTINUE OR PRESS Q/q TO EXIT")
        ch = input("ENTER YOUR CHOICE ")
        if ch == "q" or ch == "Q":
            break

if __name__ == '__main__':
    try:
        path = "d:/school_project"
        os.mkdir(path)

        # this is write new function for databases
        ap_file = open(r"D:\school_project\databases.txt", "a")
        ap_file.write("")
        ap_file.close()

        # this is write new function for tables
        ap_file = open(r"D:\school_project\tables.txt", "a")
        ap_file.write("")
        ap_file.close()

        l = []
        l1 = []
        # this is a read function

        abc = open(r"D:\school_project\databases.txt", "r")
        str1 = " "
        while str1:
            str1 = abc.readlines()
            for i in str1:
                a = i.replace("\n", "")
                l.append(a)
        abc.close()

        c = open(r"D:\school_project\tables.txt", "r")
        str2 = " "
        while str2:
            str2 = c.readlines()
            for j in str2:
                a1 = j.replace("\n", "")
                l1.append(a1)
        c.close()

        p = input("ENTER YOUR MYSQL PASSWORD ")

        print(
            "DO YOU WANT TO INSERT DATA OR DISPLAY TABLE OR CHECK RECORDS OR DELETE TABLE OR DELETE DATABASE OR UPDATE TABLE OR EDIT A RECORD IN A TABLE OR DELETE A RECORD FROM THE TABLE")
        choice = input("ENTER \n(I/i) TO INSERT INTO TABLES \n(S/s) TO DISPLAY TABLE \n(C/c) TO CHECK RECORDS "
                       "\n(D/d) TO DELETE TABLE \n(Db/DB/dB/db) TO DELETE DATABASE \n(U/u) TO UPDATE TABLE "
                       "\n(UT/ut/uT/Ut) TO EDIT A RECORD IN A TABLE \n(DR/dr/dR/Dr) TO DELETE A RECORD FROM THE TABLE \n(R/r) TO CHECK RETURN STATUS \n")
        if choice == "i" or choice == "I":

            ch = input("ENTER YES IF YOU WANT TO CREATE A DATABASE ELSE ENTER NO ").lower()
            if "yes" in ch:
                a = database(p)
                ch = input("ENTER YES IF YOU WANT TO CREATE A TABLE ELSE ENTER NO ").lower()
                if "yes" in ch:
                    ab = table_creation(a, p)
                    ch = input("ENTER YES IF YOU WANT TO ENTER DATA ELSE ENTER NO ").lower()
                    if "yes" in ch:
                        data_entry(ab, a, p)
                    else:
                        print("PLEASE ENTER DATA FIRST")
                else:
                    print("PLEASE ENTER TABLE FIRST")
            else:
                ch = input("ENTER YES IF YOU WANT TO CREATE A TABLE ELSE ENTER NO ").lower()
                if "yes" in ch:
                    print(l)
                    # tb = input("WHICH DATABASE DO YOU WANT TO SELECT ")
                    tb = l[0]
                    # tb = "management"
                    ab = table_creation(tb, p)
                    ch = input("ENTER YES IF YOU WANT TO ENTER DATA ELSE ENTER NO ").lower()
                    if "yes" in ch:
                        data_entry(ab, tb, p)
                    else:
                        print("PLEASE ENTER DATA FIRST")
                else:
                    ch = input("DO YOU WANT TO ENTER DATA ONLY ").lower()
                    if "yes" in ch:
                        print(l)
                        # tb = input("WHICH DATABASE DO YOU WANT TO SELECT ")
                        # tb = "management"
                        tb = l[0]
                        print(l1)
                        # tab = input("WHICH TABLE DO YOU WANT TO SELECT ")
                        # tab = "library"
                        tab = l1[0]
                        data_entry(tab, tb, p)
                    else:
                        print("PLEASE ENTER DATA FIRST")

        elif choice == "c" or choice == "C":
            print(l)
            # tb = input("WHICH DATABASE DO YOU WANT TO SELECT ")
            # tb = "management"
            tb = l[0]
            print(l1)
            # tab = input("WHICH TABLE DO YOU WANT TO SELECT ")
            # tab = "library"
            tab = l1[0]
            checklist(tab, tb, p)

        elif choice == "d" or choice == "D":
            print(l)
            tb = input("WHICH DATABASE DO YOU WANT TO SELECT ")
            # tb = "management"
            # tb = l[0]
            # tab = "library"
            print(l1)
            tab = input("WHICH TABLE DO YOU WANT TO DELETE ")
            table_deletion(tab, tb, p)

        elif choice == "u" or choice == "U":
            print(l)
            # tb = input("WHICH DATABASE DO YOU WANT TO SELECT ")
            # tb = "management"
            tb = l[0]
            # tab = input("WHICH TABLE DO YOU WANT TO SELECT ")
            print(l1)
            tab = l1[0]
            table_updation(tab, tb, p)

        elif choice == "db" or choice == "UB" or choice == "dB" or choice == "Db":
            print(l)
            tb = input("WHICH DATABASE DO YOU WANT TO SELECT ")
            database_deletion(tb)

        elif choice == "s" or choice == "S":
            tb = l[0]
            # tb = "management"
            print(l)
            # tb = input("WHICH DATABASE DO YOU WANT TO SELECT ")
            tab = l1[0]
            # tab = "library"
            print(l1)
            # tab = input("WHICH TABLE DO YOU WANT TO SELECT ")
            table_display(tab, tb, p)

        elif choice == "ut" or choice == "UT" or choice == "uT" or choice == "Ut":
            tb = l[0]
            # tb = "management"
            print(l)
            # tb = input("WHICH DATABASE DO YOU WANT TO SELECT ")
            tab = l1[0]
            # tab = "library"
            print(l1)
            # tab = input("WHICH TABLE DO YOU WANT TO SELECT ")
            table_display_next(tab, tb, p)
            record_update(tab, tb, p)

        elif choice == "dr" or choice == "DR" or choice == "dR" or choice == "Dr":
            tb = l[0]
            # tb = "management"
            print(l)
            # tb = input("WHICH DATABASE DO YOU WANT TO SELECT ")
            tab = l1[0]
            # tab = "library"
            print(l1)
            # tab = input("WHICH TABLE DO YOU WANT TO SELECT ")
            table_display_next(tab, tb, p)
            record_deletion(tab, tb, p)

        elif choice == "r" or choice == "R":
            print(l)
            # tb = input("WHICH DATABASE DO YOU WANT TO SELECT ")
            # tb = "management"
            tb = l[0]
            print(l1)
            # tab = input("WHICH TABLE DO YOU WANT TO SELECT ")
            # tab = "library"
            tab = l1[0]
            return_status_check_list(tab, tb, p)

        else:
            print("PLEASE ENTER VALUES IN THE SLOT")


    except:

        # this is write new function for databases
        ap_file = open(r"D:\school_project\databases.txt", "a")
        ap_file.write("")
        ap_file.close()

        # this is write new function for tables
        ap_file = open(r"D:\school_project\tables.txt", "a")
        ap_file.write("")
        ap_file.close()

        l = []
        l1 = []
        # this is a read function

        abc = open(r"D:\school_project\databases.txt", "r")
        str1 = " "
        while str1:
            str1 = abc.readlines()
            for i in str1:
                a = i.replace("\n", "")
                l.append(a)
        abc.close()

        c = open(r"D:\school_project\tables.txt", "r")
        str2 = " "
        while str2:
            str2 = c.readlines()
            for j in str2:
                a1 = j.replace("\n", "")
                l1.append(a1)
        c.close()

        p = input("ENTER YOUR MYSQL PASSWORD ")

        print("DO YOU WANT TO INSERT DATA OR DISPLAY TABLE OR CHECK RECORDS OR DELETE TABLE OR DELETE DATABASE OR UPDATE TABLE OR EDIT A RECORD IN A TABLE OR DELETE A RECORD FROM THE TABLE")
        choice = input("ENTER \n(I/i) TO INSERT INTO TABLES \n(S/s) TO DISPLAY TABLE \n(C/c) TO CHECK RECORDS "
                       "\n(D/d) TO DELETE TABLE \n(Db/DB/dB/db) TO DELETE DATABASE \n(U/u) TO UPDATE TABLE "
                       "\n(UT/ut/uT/Ut) TO EDIT A RECORD IN A TABLE \n(DR/dr/dR/Dr) TO DELETE A RECORD FROM THE TABLE \n(R/r) TO CHECK RETURN STATUS \n")
        if choice == "i" or choice == "I":


            ch = input("ENTER YES IF YOU WANT TO CREATE A DATABASE ELSE ENTER NO ").lower()
            if "yes" in ch:
                a = database(p)
                ch = input("ENTER YES IF YOU WANT TO CREATE A TABLE ELSE ENTER NO ").lower()
                if "yes" in ch:
                    ab = table_creation(a, p)
                    ch = input("ENTER YES IF YOU WANT TO ENTER DATA ELSE ENTER NO ").lower()
                    if "yes" in ch:
                        data_entry(ab, a, p)
                    else:
                        print("PLEASE ENTER DATA FIRST")
                else:
                    print("PLEASE ENTER TABLE FIRST")
            else:
                ch = input("ENTER YES IF YOU WANT TO CREATE A TABLE ELSE ENTER NO ").lower()
                if "yes" in ch:
                    print(l)
                    #tb = input("WHICH DATABASE DO YOU WANT TO SELECT ")
                    tb = l[0]
                    #tb = "management"
                    ab = table_creation(tb, p)
                    ch = input("ENTER YES IF YOU WANT TO ENTER DATA ELSE ENTER NO ").lower()
                    if "yes" in ch:
                        data_entry(ab, tb, p)
                    else:
                        print("PLEASE ENTER DATA FIRST")
                else:
                    ch = input("DO YOU WANT TO ENTER DATA ONLY ").lower()
                    if "yes" in ch:
                        print(l)
                        # tb = input("WHICH DATABASE DO YOU WANT TO SELECT ")
                        # tb = "management"
                        tb = l[0]
                        print(l1)
                        # tab = input("WHICH TABLE DO YOU WANT TO SELECT ")
                        # tab = "library"
                        tab = l1[0]
                        data_entry(tab, tb, p)
                    else:
                        print("PLEASE ENTER DATA FIRST")

        elif choice == "c" or choice == "C":
            print(l)
            # tb = input("WHICH DATABASE DO YOU WANT TO SELECT ")
            # tb = "management"
            tb = l[0]
            print(l1)
            # tab = input("WHICH TABLE DO YOU WANT TO SELECT ")
            # tab = "library"
            tab = l1[0]
            checklist(tab, tb, p)

        elif choice == "d" or choice == "D":
            print(l)
            tb = input("WHICH DATABASE DO YOU WANT TO SELECT ")
            # tb = "management"
            # tb = l[0]
            # tab = "library"
            print(l1)
            tab = input("WHICH TABLE DO YOU WANT TO DELETE ")
            table_deletion(tab, tb, p)

        elif choice == "u" or choice == "U":
            print(l)
            # tb = input("WHICH DATABASE DO YOU WANT TO SELECT ")
            # tb = "management"
            tb = l[0]
            # tab = input("WHICH TABLE DO YOU WANT TO SELECT ")
            print(l1)
            tab = l1[0]
            table_updation(tab, tb, p)

        elif choice == "db" or choice == "UB" or choice == "dB" or choice == "Db":
            print(l)
            tb = input("WHICH DATABASE DO YOU WANT TO SELECT ")
            database_deletion(tb)

        elif choice == "s" or choice == "S":
            tb = l[0]
            # tb = "management"
            print(l)
            # tb = input("WHICH DATABASE DO YOU WANT TO SELECT ")
            tab = l1[0]
            # tab = "library"
            print(l1)
            # tab = input("WHICH TABLE DO YOU WANT TO SELECT ")
            table_display(tab, tb, p)

        elif choice == "ut" or choice == "UT" or choice == "uT" or choice == "Ut":
            tb = l[0]
            # tb = "management"
            print(l)
            # tb = input("WHICH DATABASE DO YOU WANT TO SELECT ")
            tab = l1[0]
            # tab = "library"
            print(l1)
            # tab = input("WHICH TABLE DO YOU WANT TO SELECT ")
            table_display_next(tab, tb, p)
            record_update(tab, tb, p)

        elif choice == "dr" or choice == "DR" or choice == "dR" or choice == "Dr":
            tb = l[0]
            # tb = "management"
            print(l)
            # tb = input("WHICH DATABASE DO YOU WANT TO SELECT ")
            tab = l1[0]
            # tab = "library"
            print(l1)
            # tab = input("WHICH TABLE DO YOU WANT TO SELECT ")
            table_display_next(tab, tb, p)
            record_deletion(tab, tb, p)

        elif choice == "r" or choice == "R":
            print(l)
            # tb = input("WHICH DATABASE DO YOU WANT TO SELECT ")
            # tb = "management"
            tb = l[0]
            print(l1)
            # tab = input("WHICH TABLE DO YOU WANT TO SELECT ")
            # tab = "library"
            tab = l1[0]
            return_status_check_list(tab, tb, p)

        else:
            print("PLEASE ENTER VALUES IN THE SLOT")
