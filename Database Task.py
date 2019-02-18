import sqlite3
import os

connection = sqlite3.connect("PupilsDatabase.db")

cursor = connection.cursor()

data = cursor.execute("SELECT * FROM PupilsDatabase")

Pupils = list(data)

# fields = id, Forename, Surname, Age

# record class


class Record:
    def __init__(self, i, forename, surname, gender, age,):
        self.id = i
        self.forename = forename
        self.surname = surname
        self.gender = gender
        self.age = age

# functions


def search(field, t):
    global Pupils

    dc = True

    field_def = {"id": 0,
                 "forename": 1,
                 "surname": 2,
                 "gender": 3,
                 "age": 4}

    pupils = []

    for r in Pupils:

        try:
            if str(r[field_def[field.lower()]]) == str(t) and field_def[field.lower()] in [0, 4]:
                pupils.append(r)

            if r[field_def[field.lower()]].lower() == t.lower() and field_def[field.lower()] not in [0, 4]:
                pupils.append(r)

        except AttributeError:
            continue

        except KeyError:
            print("\n >> INVALID")
            dc = False
            break

    if dc:
        print("\n >> {length} SEARCH RESULTS".format(length=len(pupils)))

        for r in pupils:
            print("\n >> ID: " + str(r[0]))
            print(" >> Forename: " + str(r[1]))
            print(" >> Surname: " + str(r[2]))
            print(" >> Gender: " + str(r[3]))
            print(" >> Age: " + str(r[4]))


def edit(i, forename, surname, gender, age):

    cursor.execute(
        "UPDATE PupilsDatabase SET Forename = '{f}', Surname = '{s}', Gender = '{g}', Age = {a} WHERE ID = {i}"
        .format(f=forename, s=surname, g=gender, a=age, i=i)
    )

    connection.commit()

    for r in list(cursor.execute("SELECT * FROM PupilsDatabase")):
        if str(r[0]) == i:
            print("\n >> Record with ID {id} successfully edited: ".format(id=i))

            print("\n >> ID: " + str(r[0]))
            print(" >> Forename: " + str(r[1]))
            print(" >> Surname: " + str(r[2]))
            print(" >> Gender: " + str(r[3]))
            print(" >> Age: " + str(r[4]) + "\n")


def add(forename, surname, gender, age):

    cursor.execute("INSERT INTO PupilsDatabase (Forename, Surname, Gender, Age) VALUES ('{f}', '{s}', '{g}', '{a}')"
                   .format(f=forename, s=surname, g=gender, a=age))

    connection.commit()

    r = list(cursor.execute("SELECT * FROM PupilsDatabase"))

    print("\n >> New pupil record successfully added.")

    print("\n >> ID: " + str(r[-1][0]))
    print(" >> Forename: " + str(r[-1][1]))
    print(" >> Surname: " + str(r[-1][2]))
    print(" >> Gender: " + str(r[-1][3]))
    print(" >> Age: " + str(r[-1][4]) + "\n")


def remove(i):
    global Pupils

    d = 0

    for r in Pupils:
        if r[0] == i:
            cursor.execute("DELETE FROM PupilsDatabase WHERE id = {ID}".format(ID=i))
            connection.commit()
            d += 1

            print("\n >> Pupil(s) with ID {si} have been successfully removed.".format(si=i))

            print("\n >> Details: ")

            print("\n >> ID: " + str(r[0]))
            print(" >> Forename: " + str(r[1]))
            print(" >> Surname: " + str(r[2]))
            print(" >> Gender: " + str(r[3]))
            print(" >> Age: " + str(r[4]) + "\n")

    if d == 0:
        print("\n >> No pupil(s) with ID {si}".format(si=i))


def menu():
    os.system("cls")
    print("\n >> DATABASE OPTIONS <<")
    print(" >> 1: Search for pupils.")
    print(" >> 2: Edit a pupil's record.")
    print(" >> 3: Add a new pupil record.")
    print(" >> 4: Remove pupil(s).")
    print(" >> 5: Exit.")

    opt = str(input("\n >> "))

    if opt == "1":
        os.system("cls")
        print("\n >> DATABASE SEARCH")
        f = input("\n >> Field name: ")
        q = input(" >> Query: ")

        try:
            search(f, q)
            input()

        except ValueError:
            print("\n >> INVALID")
            input()

    if opt == "2":
        os.system("cls")
        print("\n >> RECORD EDITING")
        i = input("\n >> Enter Pupil ID of pupil record you want to edit: ")
        f = input(" >> Enter Forename: ")
        s = input(" >> Enter Surname: ")
        g = input(" >> Enter Gender: ")
        a = int(input(" >> Enter Age: "))

        try:
            edit(i, f, s, g, a)
            input()

        except ValueError:
            print("\n >> INVALID")
            input()

    if opt == "3":
        os.system("cls")
        print("\n >> ADDING RECORDS")
        f = input("\n >> Enter Forename: ")
        s = input(" >> Enter Surname: ")
        g = input(" >> Enter Gender: ")
        a = input(" >> Enter Age: ")

        try:
            add(f, s, g, a)
            input()

        except ValueError:
            print("\n >> INVALID")
            input()

    if opt == "4":
        os.system("cls")
        print(" \n >> DELETING RECORDS")
        si = input("\n >> Enter Pupil ID of record you want to remove: ")

        try:
            remove(int(si))
            input()

        except ValueError:
            print("\n >> INVALID")
            input()

    if opt == "5":
        os.system("cls")
        print(" >> EXIT PROGRAM")
        confirm = input("\n >> Do you really wish to exit? (Y/N): ")

        if confirm.lower() in ["yes", "y"]:
            input()
            exit()

        else:
            menu()

    if opt not in ["1", "2", "3", "4", "5"]:
        print("\n >> INVALID")
        input()

    menu()


menu()
