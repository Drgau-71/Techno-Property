def read_land_data():
    lands = []
    with open("lands.txt", "r") as file:
        next(file)  # Skip the header line
        for line in file:
            parts = line.strip().split(',')
            if len(parts) >= 6:
                kitta, location, direction, annas, cost, status = [part.strip() for part in parts[:6]]
                lands.append([kitta, location, direction, annas, cost, status])
    return lands

def read_customer_data():
    customers = []
    file = open('lands.txt', 'r')
    for line in file:
        parts = line.strip().split(',')
        if len(parts) >= 3:
            name, phone = parts[:2]
            rented_land = ','.join(parts[2:])  # Join any remaining parts as rented_land
            customers.append([name, phone, rented_land])
        else:
            print("Warning: Skipping invalid customer line: {}".format(line.strip()))
    file.close()
    return customers
