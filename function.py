"""
Name: Ahamid Adam, Kenneth Gomez, Ngor Ruot
Date: Dec 13, 2025

Program Description:
Car Inventory Application.
- Uses a Car class
- Stores cars in a LIST
- Loads from data.txt on start
- Saves to data.txt on demand
"""

DATA_FILE = "data.txt"


# ---------- Car Class ----------
class Car:
    def __init__(self, cid, name, make, body, year, value):
        self.cid = cid
        self.name = name
        self.make = make
        self.body = body
        self.year = year
        self.value = value

    def display(self):
        return f"{self.cid}\t{self.name}\t{self.make}\t{self.body}\t{self.year}\t{self.value:.1f}"


cars = []  # LIST of Car objects


# ---------- Menu ----------
def show_menu():
    print("\nWhat would you like to do today?\n")
    print("-Add a car? enter 1")
    print("-Search for car? enter 2")
    print("-Edit car info? enter 3")
    print("-Remove a car? enter 4")
    print("-Print the car list? enter 5")
    print("-Save the data to a file? enter 6")
    print("-Exit? enter 0.")
    return input().strip()


# ---------- Persistence ----------
def load_data():
    global cars
    cars = []
    try:
        with open(DATA_FILE, "r", encoding="utf-8") as f:
            for line in f:
                cid, name, make, body, year, value = line.strip().split(",")
                cars.append(Car(int(cid), name, make, body, int(year), float(value)))
    except FileNotFoundError:
        pass


def save_data():
    with open(DATA_FILE, "w", encoding="utf-8") as f:
        for c in cars:
            f.write(f"{c.cid},{c.name},{c.make},{c.body},{c.year},{c.value}\n")
    print("Data saved to local file successfully!")


# ---------- Helpers ----------
def find_by_id(cid):
    for c in cars:
        if c.cid == cid:
            return c
    return None


def find_by_name(name):
    for c in cars:
        if c.name.lower() == name.lower():
            return c
    return None


# ---------- Core Actions ----------
def run_add():
    while True:
        print("\nEnter id of the car, followed by the car's information.")

        cid = int(input("Id:\n"))
        name = input("name:\n")
        make = input("make:\n")
        body = input("Body:\n")
        year = int(input("year:\n"))
        value = float(input("value:\n"))

        if find_by_id(cid):
            print("Incorrect Id. Id already exist in the system.")
        elif find_by_name(name):
            print("The car is already in the inventory. No action is required..")
        else:
            car = Car(cid, name, make, body, year, value)
            cars.append(car)
            print("car is added to the inventory.")
            print(car.display())

        again = input("\nDo you want to add more cars? y(yes)/n(no)\n").lower()
        if again not in ["y", "yes"]:
            break


def run_search():
    while True:
        print("\nTo search using the Id enter 1. To search using the name of the car enter 2. Enter -1 to return to the previous menu")
        choice = input().strip()

        if choice == "-1":
            break

        if choice == "1":
            cid = int(input("Please Enter the id of the car:\n"))
            car = find_by_id(cid)
            print("Car found ", car.display() if car else "Car not found")

        elif choice == "2":
            name = input("Please Enter the name of the car:\n")
            car = find_by_name(name)
            print("Car found ", car.display() if car else "Car not found")


def run_edit():
    while True:
        cid = input("\nEnter the id of the car. Enter -1 to return to the previous menu\n")
        if cid == "-1":
            break

        car = find_by_id(int(cid))
        if not car:
            print("Car not found")
            continue

        car.name = input("Name:\n")
        car.make = input("make:\n")
        car.body = input("Body:\n")
        car.year = int(input("year:\n"))
        car.value = float(input("value:\n"))

        print("Car's new info is ", car.display())


def run_remove():
    while True:
        cid = int(input("\nEnter id of the car that you want to remove from the inventory.\nid:\n"))
        car = find_by_id(cid)

        if car:
            cars.remove(car)
            print("car removed")
        else:
            print("Car not found")

        again = input("Do you want to remove more cars? y(yes)/n(no) ").lower()
        if again not in ["y", "yes"]:
            break


def run_print():
    for car in cars:
        print(car.display())
