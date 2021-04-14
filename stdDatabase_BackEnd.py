# Developer : khom
# Date: Tuesday, April 13, 2021
# Backend

import sqlite3
#backend


def studentData():
    con = sqlite3.connect("student.db")
    cur = con.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS "
                "student(id INTEGER PRIMARY KEY, stdID text, Firstname text, Surname text, DoB text, "
                "Age text, Gender text, Mobile text)")
    con.commit()
    con.close()


def addStdRec(StdID, Firstname, Surname, DoB, Age, Gender, Mobile):
    con = sqlite3.connect("student.db")
    cur = con.cursor()
    cur.execute("INSERT INTO student VALUES (NULL, ?, ?, ?, ?, ?, ?, ?, ?)",
                StdID, Firstname, Surname, DoB, Age, Gender, Mobile)
    con.commit()
    con.close()


def viewData():
    con = sqlite3.connect("student.db")
    cur = con.cursor()
    cur.execute("SELECT * FROM student")
    rows = cur.fetchall()
    con.close()
    return rows


def deleteRec(id):
    con = sqlite3.connect("student.db")
    cur = con.cursor()
    cur.execute("DELETE FROM student WHERE id=?", (id,))
    con.commit()
    con.close()


def searchData(StdID = "", Firstname = "", Surname = "", DoB = "", Age = "", Gender = "", Mobile = ""):
    con = sqlite3.connect("student.db")
    cur = con.cursor()
    cur.execute("SELECT * FROM student WHERE "
                "StdID=? OR Firstname=? OR Surname=? OR DoB=? OR Age=? OR Gender=? OR Mobile=?",
                (StdID, Firstname, Surname, DoB, Age, Gender, Mobile))
    rows = cur.fetchall()
    return rows


def dataUpdate(id, StdID = "", Firstname = "", Surname = "", DoB = "", Age = "", Gender = "", Mobile = ""):
    con = sqlite3.connect("student.db")
    cur = con.cursor()
    cur.execute("UPDATE student SET "
                "StdID=?, Firstname=?, Surname=?, DoB=?, Age=?, Gender=?, Mobile=?, WHERE id=?",
                (StdID, Firstname, Surname, DoB, Age, Gender, Mobile,id))
    con.commit()
    con.close()


