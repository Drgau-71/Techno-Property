from read import read_land_data, read_customer_data
from operation import rent_land, return_land
import operation
import read

print("\n")
print("\n")
print("\t \t \t \t \t       Techno Property Nepal")
print("\n")
print("\t \t \t \t New Baneshwor, Kathmandu | Contact no. : 9793104925")
print("\n")
print("\t \t _____________________________________________________________________")
print("\t \t Greetings from the system administrator! I wish you a wonderful day ahead of you today!")
print("\t \t _____________________________________________________________________")
print("\n")
print("\t ---------------------------------------------------------------------------------------------------------")
print("\t A couple of options available to you to do the necessary action within the system")
print("\t ---------------------------------------------------------------------------------------------------------")
print("\n")
print("\t Enter 1 to Rent the Land")
print("\t Enter 2 to Return the Land")
print("\t Enter 3 to Exit from system")
print("\n")
print("    --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------")

def main():
    lands = read_land_data()

    while True:
        A = input("Enter a number from above option = ")
        if A == '1':
            file= open("lands.txt","r")
            print(file.read())
            file.close
            
            
            if A == '1':
                chosen_kitta = input("Enter the kitta number of the land to rent: ")
                name = input("Enter customer name: ")
                phone = input("Enter customer phone number: ")
                rent_duration = int(input("Enter rental duration in months: "))
                rent_land(lands, name, phone, rent_duration, chosen_kitta)
                lands = read.read_land_data()  # Refresh land data
            else:
                print("No lands are available for rent at the moment.")

        elif A == '2':
            kitta = input("Enter kitta number: ")
            for i in range(len(lands)):
                if lands[i][0] == kitta:
                    land = lands[i]
                    break
                else:
                    land = None
            if land != None:
                name = input("Enter customer name: ")
                phone = input("Enter customer phone number: ")
                actual_duration = int(input("Enter actual rental duration in months: "))
                return_land(land, name, phone, actual_duration)
                lands = read.read_land_data()
            else:
                print("Land not found.")
        elif A == '3':
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
    
