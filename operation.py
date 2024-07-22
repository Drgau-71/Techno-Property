import datetime
from write import add_customer_rental, write_invoice, update_land_status


def rent_land(lands, name, phone, rent_duration, chosen_kitta):
    rented_land = None
    total_cost = 0
    for land in lands:
        kitta, location, direction, annas, cost, status = land
        if status.strip().lower() == 'available' and kitta.strip() == chosen_kitta.strip():
            land_cost = int(cost) * rent_duration
            total_cost += land_cost
            write_invoice(name, phone, land, rent_duration)
            update_land_status('lands.txt', kitta, 'Not Available')
            add_customer_rental('customers.txt', name, phone, kitta, rent_duration)
            rented_land = land
            break
    
    if rented_land:
        print(f"Land {chosen_kitta} rented successfully. Total cost: NPR {total_cost}")
        print("Customer information has been recorded.")
    else:
        print(f"Land with kitta {chosen_kitta} is not available for rent.")


import datetime
from write import update_land_status

def return_land(lands, kitta, name, phone, actual_duration):
    returned_land = None
    for land in lands:
        if land[0].strip() == kitta.strip():  # Assuming kitta is the second element
            returned_land = land
            break
    
    if returned_land is None:
        print(f"Land with kitta {kitta} not found.")
        return

    if returned_land[5].strip().lower() == 'available':
        print(f"Land with kitta {kitta} is not currently rented.")
        return

    # Calculate fine if returned late
    expected_duration = get_expected_duration(name, phone, kitta)
    fine = 0
    if actual_duration > expected_duration:
        months_late = actual_duration - expected_duration
        fine = int(returned_land[4]) * months_late * 0.1  # 10% fine per month

    # Update land status
    update_land_status('lands.txt', kitta, 'Available')

    # Calculate total cost
    total_cost = int(returned_land[4]) * actual_duration + fine

    # Print return invoice
    print("\n")
    print("\t\t\t\t Techno Property Nepal")
    print("\t\t\t\t New Baneshwor, Kathmandu, | Contact no. : 9793104925")
    print("\n")
    print(f"Return Invoice Date: {datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    print("\n")
    print(f"Customer Name: {name}")
    print(f"Phone Number: {phone}")
    print("\n")
    print("Land Details:")
    print(f"Kitta Number: {returned_land[0]}")
    print(f"Location: {returned_land[1]}")
    print(f"Direction: {returned_land[2]}")
    print(f"Area: {returned_land[3]} annas")
    print(f"Monthly Rent: NPR {returned_land[4]}")
    print("\n")
    print(f"Actual Rental Duration: {actual_duration} months")
    print(f"Rental Cost: NPR {int(returned_land[4]) * actual_duration}")
    print(f"Late Return Fine: NPR {fine}")
    print(f"Total Cost: NPR {total_cost}")
    print(f"\nReturn Date: {datetime.date.today()}")
    print("\n")
    print("    --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------")

    print(f"Land {kitta} has been returned successfully.")
    print("Thank you for using Techno Property Nepal's rental service.")
    print("Have a nice day! :)")
    print("\n")

def get_expected_duration(name, phone, kitta):
    with open('customers.txt', 'r') as file:
        for line in file:
            customer_name, customer_phone, customer_kitta, rental_date, duration = line.strip().split(',')
            if customer_name == name and customer_phone == phone and customer_kitta == kitta:
                return int(duration)
    return 6  # Default to 6 months if not found

def generate_return_invoice(name, phone, land_data, actual_duration, fine):
    kitta, location, direction, annas, cost, status = land_data
    filename = "return_invoice_" + name + "_" + str(kitta) + "_" + datetime.datetime.now().strftime('%Y%m%d%H%M%S') + ".txt"
    total_cost = int(cost) * actual_duration + fine

    file= open(filename, "w")
    file.write("\t\t\t\t Techno Property Nepal\n")
    file.write("\t\t\t\t New Baneshwor, Kathmandu, | Contact no. : 9793104925 \n\n")
    file.write(f"Return Invoice Date: {datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n\n")
    file.write("Customer Name: "+ name+ "\n")
    file.write("Phone Number: \n\n"+str(phone))
    file.write("Land Details:\n")
    file.write("Kitta Number: "+ kitta +"\n")
    file.write("Location: "+ location+"\n")
    file.write("Direction: "+ direction +"\n")
    file.write("Area:  " + annas +" annas\n")
    file.write("Monthly Rent: NPR " + cost + "\n\n")
    file.write("Actual Rental Duration: "+ actual_duration +" months\n")
    file.write("Rental Cost: NPR " +int(cost) * actual_duration+ "\n")
    file.write("Late Return Fine: NPR " + fine + "\n")
    file.write("Total Cost: NPR " + total_cost + "\n")
    file.write("\nReturn Date: " + datetime.date.today() + "\n")

    print("Return invoice generated: "+ filename)
