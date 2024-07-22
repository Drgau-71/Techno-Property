import datetime

def write_invoice(name, phone, land_data, rent_duration):
    kitta, location, direction, annas, cost, status = land_data
    total_cost = int(cost) * rent_duration
    
    print("\n")
    print("\t\t\t\t Techno Property Nepal")
    print("\t\t\t\t New Baneshwor, Kathmandu, | Contact no. : 9793104925")
    print("\n")
    print(f"Invoice Date: {datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    print("\n")
    print(f"Customer Name: {name}")
    print(f"Phone Number: {phone}")
    print("\n")
    print("Land Details:")
    print(f"Kitta Number: {kitta}")
    print(f"Location: {location}")
    print(f"Direction: {direction}")
    print(f"Area: {annas} annas")
    print(f"Monthly Rent: NPR {cost}")
    print("\n")
    print(f"Rental Duration: {rent_duration} months")
    print(f"Total Cost: NPR {total_cost}")
    print(f"\nRental Start Date: {datetime.date.today()}")
    print("\n")
    print("    --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------")
    print("\n")
    print("\t Enter 1 to Rent the Land")
    print("\t Enter 2 to Return the Land")
    print("\t Enter 3 to Exit from system")
    print("\n")
    print("    --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------")
    print("\n")


def update_land_status(filename, kitta, new_status):
    lands = []
    with open(filename, 'r') as file:
        header = file.readline().strip()  # Read and store the header
        for line in file:
            land_data = line.strip().split(',')
            if land_data[0].strip() == kitta.strip():
                land_data[-1] = new_status
            lands.append(','.join(land_data))
    
    with open(filename, 'w') as file:
        file.write(header + '\n')  # Write the header back
        for land in lands:
            file.write(land + '\n')

def add_customer_rental(filename, name, phone, kitta, rent_duration):
    with open(filename, 'a') as file:
        rental_date = datetime.date.today()
        file.write(f"{name},{phone},{kitta},{rental_date},{rent_duration}\n")
