
# HOTEL MANAGEMENT SYSTEM

customers = []

serial_number = 1


def add_customer():
    global serial_number

    print("\n--- Enter Customer Booking Details ---")

    customer = {}

    customer["SL No"] = serial_number
    customer["Booking ID"] = input("Enter Booking ID: ")
    customer["Customer Name"] = input("Enter Customer Name: ")
    customer["Contact Number"] = input("Enter Contact Number: ")
    customer["Email ID"] = input("Enter Email ID: ")
    customer["Address"] = input("Enter Address: ")
    customer["Room Number"] = input("Enter Room Number: ")
    customer["Room Type"] = input("Enter Room Type: ")
    customer["Check-in Date"] = input("Enter Check-in Date: ")
    customer["Check-out Date"] = input("Enter Check-out Date: ")
    customer["Number of Guests"] = input("Enter Number of Guests: ")
    customer["Booking Status"] = input("Enter Booking Status: ")

    customers.append(customer)

    serial_number += 1

    print("\nCustomer Booking Added Successfully!")
    print("Generated SL No:", customer["SL No"])


def display_customers():

    if not customers:
        print("\nNo Customer Records Found!")

    else:
        print("\n--- HOTEL CUSTOMER DETAILS ---")

        for customer in customers:

            for key, value in customer.items():
                print(key, ":", value)

            print("--------------------------------")


def search_customer():

    number = input("Enter Booking ID: ")

    for customer in customers:

        if customer["Booking ID"] == number:

            print("\nCustomer Record Found!")

            for key, value in customer.items():
                print(key, ":", value)

            return

    print("\nCustomer Record Not Found!")


while True:

    print("\n===== HOTEL MANAGEMENT SYSTEM =====")

    print("1. Add Customer Booking")
    print("2. Display All Customers")
    print("3. Search Customer")
    print("4. Exit")

    choice = input("Enter Your Choice: ")

    if choice == "1":
        add_customer()

    elif choice == "2":
        display_customers()

    elif choice == "3":
        search_customer()

    elif choice == "4":
        print("Thank You!")

        break

    else:
        print("Invalid Choice! Try Again.")
