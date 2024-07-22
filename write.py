import datetime

def write_invoice(name, phone, land_data, rent_duration):
    kitta, location, direction, annas, cost, status = land_data
    filename = f"invoice_{name}_{kitta}_{datetime.datetime.now().strftime('%Y%m%d%H%M%S')}.txt"
    total_cost = int(cost) * rent_duration
    
    with open(filename, "w") as file:
        file.write("\t\t\t\t Techno Property Nepal\n")
        file.write("\t\t\t\t New Baneshwor, Kathmandu, | Contact no. : 9793104925 \n\n")
        file.write(f"Invoice Date: {datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n\n")
        file.write(f"Customer Name: {name}\n")
        file.write(f"Phone Number: {phone}\n\n")
        file.write("Land Details:\n")
        file.write(f"Kitta Number: {kitta}\n")
        file.write(f"Location: {location}\n")
        file.write(f"Direction: {direction}\n")
        file.write(f"Area: {annas} annas\n")
        file.write(f"Monthly Rent: NPR {cost}\n\n")
        file.write(f"Rental Duration: {rent_duration} months\n")
        file.write(f"Total Cost: NPR {total_cost}\n")
        file.write(f"\nRental Start Date: {datetime.date.today()}\n")

    print(f"Invoice generated: {filename}")

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
