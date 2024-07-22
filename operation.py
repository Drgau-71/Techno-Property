import datetime
from write import write_invoice, update_land_status
import write



def rent_land(lands, name, phone, rent_duration, chosen_kitta):
    rented_land = None
    total_cost = 0
    for land in lands:
        kitta, location, direction, annas, cost, status = land
        if status.lower() == 'Available' and kitta == chosen_kitta:
            land_cost = int(cost) * rent_duration
            total_cost += land_cost
            write_invoice(name, phone, land, rent_duration)
            update_land_status('lands.txt', kitta, 'Not Available')
            add_customer_rental('customers.txt', name, phone, kitta)
            rented_land = land
            break
    
    if rented_land:
        print("Land " +chosen_kitta+"rented successfully. Total cost: NPR" +total_cost)
    else:
        print(f"Land with kitta " +chosen_kitta+" is not available for rent.")


def return_land(land_data, name, phone, actual_duration):
    kitta, location, direction, annas, cost, status = land_data
    if status.lower() == 'not available':
        update_land_status('lands.txt', kitta, 'Available')
        
        # Calculate fine if returned late
        expected_duration = get_expected_duration(name, phone, kitta)
        if actual_duration > expected_duration:
            months_late = actual_duration - expected_duration
            fine = int(cost) * months_late * 0.1  # 10% fine per month
            print("Land " + kitta +" has been returned late. Fine: NPR "+ fine)
        else:
            fine = 0
        
        print("Land " + kitta +"has been returned successfully.")
        generate_return_invoice(name, phone, land_data, actual_duration, fine)
    else:
        print("This land is not currently rented.")

def get_expected_duration(name, phone, kitta):
    # This function should read from a file or database to get the expected duration
    # For simplicity, we'll return a fixed value
    return 6  # Assume 6 months rental duration

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
