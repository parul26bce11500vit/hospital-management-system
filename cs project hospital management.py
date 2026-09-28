print("CITY CARE HOSPITAL")
print("HOSPITAL MANAGEMENT SYSTEM")
print()

name = input("Enter patient name: ")
age = int(input("Enter patient age: "))

while True:
    phone = input("Enter 10-digit phone number: ")

    if len(phone) == 10 and phone.isdigit():
        print("Phone number accepted")
        break
    else:
        print("Invalid phone number! Please enter exactly 10 digits.")


doctor_price = 0
test_total = 0
room_total = 0
food_total = 0

while True:

    print()
    print("MAIN MENU")
    print()
    print("1. Doctor Appointment")
    print("2. Medical Tests")
    print("3. Hospital Room")
    print("4. Food Services")
    print("5. Generate Bill")
    print("6. Exit")
    print()

    choice = int(input("Enter your choice: "))

    if choice == 1:

        print()
        print("DOCTOR APPOINTMENT")
        print()
        print("1. General Medicine - Rs. 500")
        print("2. Cardiology - Rs. 1000")
        print("3. Orthopedics - Rs. 700")
        print("4. Dermatology - Rs. 600")
        print()

        doctor = int(input("Enter doctor choice: "))

        if doctor == 1:
            doctor_price = 500
            print("General Medicine selected")

        elif doctor == 2:
            doctor_price = 1000
            print("Cardiology selected")

        elif doctor == 3:
            doctor_price = 700
            print("Orthopedics selected")

        elif doctor == 4:
            doctor_price = 600
            print("Dermatology selected")

        else:
            doctor_price = 0
            print("Invalid doctor choice")

    elif choice == 2:

        print()
        print("MEDICAL TESTS")
        print()
        print("1. Blood Test - Rs. 300")
        print("2. X-Ray - Rs. 500")
        print("3. ECG - Rs. 400")
        print("4. MRI - Rs. 2500")
        print("5. Done")
        print()

        while True:

            test = int(input("Enter test choice: "))

            if test == 1:
                test_total = test_total + 300
                print("Blood Test added")

            elif test == 2:
                test_total = test_total + 500
                print("X-Ray added")

            elif test == 3:
                test_total = test_total + 400
                print("ECG added")

            elif test == 4:
                test_total = test_total + 2500
                print("MRI added")

            elif test == 5:
                print("Medical test selection completed")
                break

            else:
                print("Invalid test choice")

    elif choice == 3:

        print()
        print("HOSPITAL ROOM")
        print()
        print("1. General Ward - Rs. 1000 per day")
        print("2. Semi-Private Room - Rs. 2000 per day")
        print("3. Private Room - Rs. 3500 per day")
        print()

        room = int(input("Enter room choice: "))
        days = int(input("Enter number of days: "))

        if room == 1:
            room_price = 1000
            print("General Ward selected")

        elif room == 2:
            room_price = 2000
            print("Semi-Private Room selected")

        elif room == 3:
            room_price = 3500
            print("Private Room selected")

        else:
            room_price = 0
            print("Invalid room choice")

        room_total = room_price * days

    elif choice == 4:

        print()
        print("FOOD SERVICES")
        print()
        print("1. Breakfast - Rs. 150")
        print("2. Lunch - Rs. 250")
        print("3. Dinner - Rs. 250")
        print("4. Juice - Rs. 100")
        print("5. Done")
        print()

        while True:

            food = int(input("Enter food choice: "))

            if food == 1:
                food_total = food_total + 150
                print("Breakfast added")

            elif food == 2:
                food_total = food_total + 250
                print("Lunch added")

            elif food == 3:
                food_total = food_total + 250
                print("Dinner added")

            elif food == 4:
                food_total = food_total + 100
                print("Juice added")

            elif food == 5:
                print("Food selection completed")
                break

            else:
                print("Invalid food choice")

    elif choice == 5:

        total = doctor_price + test_total + room_total + food_total

        print()
        print("HOSPITAL BILL")
        print()
        print("Patient Name:", name)
        print("Patient Age:", age)
        print("Phone Number:", phone)
        print()
        print("Doctor Charges: Rs.", doctor_price)
        print("Medical Test Charges: Rs.", test_total)
        print("Room Charges: Rs.", room_total)
        print("Food Charges: Rs.", food_total)
        print()
        print("TOTAL PAYMENT: Rs.", total)

    elif choice == 6:

        print()
        print("Thank you for visiting City Care Hospital!")
        print("Have a nice day!")
        break

    else:

        print()
        print("Invalid choice! Please try again.")