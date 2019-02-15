import sqlite3

connection = sqlite3.connect("PupilsDatabase.db")

cursor = connection.cursor()

data = cursor.execute("SELECT * FROM PupilsDatabase")

Pupils = list(data)

# fields = id, Forename, Surname, Age

# record class

class Record:
    def __init__(self, i, Forename, Surname, Gender, Age,):
        self.id = i
        self.forename = Forename
        self.surname = Surname
        self.gender = Gender
        self.age = Age

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

def remove(i):
    global Pupils

    d = 0

    for r in Pupils:
        if r[0] == i:
            cursor.execute("DELETE FROM PupilsDatabase WHERE id = {ID}".format(ID=i))
            connection.commit()
            d += 1

            print("\n >> Pupil(s) with ID {si} has been removed.".format(si=i))

            print("\n >> Details: ")

            print("\n >> ID: " + str(r[0]))
            print(" >> Forename: " + str(r[1]))
            print(" >> Surname: " + str(r[2]))
            print(" >> Gender: " + str(r[3]))
            print(" >> Age: " + str(r[4]) + "\n")

    if d == 0:
        print("\n >> No pupil(s) with ID {si}".format(si=i))

def edit(i):
    forename = input(" >> Enter Forename: ")
    surname = input(" >> Enter Surname: ")
    gender = input(" >> Enter Gender: ")
    age = int(input(" >> Enter Age: "))

    cursor.execute("UPDATE PupilsDatabase SET Forename = '{f}', Surname = '{s}', Gender = '{g}', Age = {a} WHERE ID = {i}".format(
        f=forename, s=surname, g=gender, a=age, i=i))
    connection.commit()



    for r in list(cursor.execute("SELECT * FROM PupilsDatabase")):
        if str(r[0]) == i:
            print("\n >> Record with ID {id} updated: ".format(id=i))

            print("\n >> ID: " + str(r[0]))
            print(" >> Forename: " + str(r[1]))
            print(" >> Surname: " + str(r[2]))
            print(" >> Gender: " + str(r[3]))
            print(" >> Age: " + str(r[4]) + "\n")

def menu():
    print("\n >> DATABASE OPTIONS <<")
    print(" >> 1: Search for pupils.")
    print(" >> 2: Edit a pupil's record.")
    print(" >> 3: Remove pupil(s).")

    opt = str(input("\n >> "))

    if opt == "1":
        f = input("\n >> Field name: ")
        q = input(" >> Query: ")

        search(f, q)

    if opt == "2":
        i = input("\n >> Enter Pupil ID of pupil record you want to edit: ")
        edit(i)

    if opt == "3":
        si = input("\n >> Enter Pupil ID of record you want to remove: ")

        try:
            remove(int(si))

        except ValueError:
            print(" >> INVALID")

    if opt not in ["1", "2", "3", "4"]:
        print("\n >> INVALID")


while True:
    menu()
