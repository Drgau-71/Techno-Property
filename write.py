import datetime

def write_invoice(name, phoneno, land_data, rent_duration):
    print("\n")
    print("\n")
    print("\t \t \t \t \t       Techno Property Nepal")
    print("\n")
    print("\t \t \t \t New Baneshwor, Kathmandu | Contact no. : 9793104925")
    kitta, location, direction, annas, cost, status = land_data
    filename = f"invoice_{name}_{kitta}_{datetime.datetime.now().strftime('%Y%m%d%H%M%S')}.txt"
    total_cost = int(cost) * rent_duration
    
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

def update_land_status(filename, kitta, new_status):
    lands = []
    file = open(filename, 'r')
    for line in file:
        land_data = line.strip().split(',')
        if land_data[0] == kitta:
            land_data[-1] = new_status
        lands.append(str(land_data[0]) + ',' + str(land_data[1]) + ',' + str(land_data[2]))
    
    file = open(filename, 'w')
    for land in lands:
        file.write(land + '\n')

