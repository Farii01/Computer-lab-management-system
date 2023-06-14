import sys

def add_pc():
    pc_number = input("Enter PC number: ")
    os = input("Enter OS installed: ")
    status = input("Enter status: ")
    pc = [pc_number, os, status]
    if pc_number in lab.keys():
        print("PC with this number already exists!")
        choice = input("Do you want to modify, remove or take no action? (m/r/n): ")
        if choice == "m":
            update_pc(pc_number)
        elif choice == "r":
            remove_pc(pc_number)
        else:
            pass
    else:
        lab[pc_number] = pc
        print("PC added successfully!")


def update_pc(pc_number):
    os = input("Enter new OS installed: ")
    status = input("Enter new status: ")
    lab[pc_number] = [pc_number, os, status]
    print("PC information updated successfully!")


def remove_pc(pc_number):
    del lab[pc_number]
    print("PC removed successfully!")


def display_all_pcs():
    print("PC\t\tOS\t\tStatus")
    for pc in lab.values():
        print(f"{pc[0]}\t\t{pc[1]}\t\t{pc[2]}")


def display_pc(pc_number):
    if pc_number in lab.keys():
        pc = lab[pc_number]
        print(f"PC Number: {pc[0]}")
        print(f"OS Installed: {pc[1]}")
        print(f"Status: {pc[2]}")
    else:
        print("PC not found!")


def search_pc():
    pc_number = input("Enter PC number: ")
    if pc_number in lab.keys():
        display_pc(pc_number)
    else:
        choice = input("PC not found! Do you want to add this PC? (y/n): ")
        if choice == "y":
            add_pc()
        else:
            quit_program()


def store_pcs():
    with open("lab_pcs.txt", "w") as f:
        f.write("PC Number\tOS Installed\tStatus\n")
        for pc in lab.values():
            f.write(f"{pc[0]}\t\t{pc[1]}\t\t{pc[2]}\n")
    print("PC information stored to file successfully!")

    def check_pc(pc_number):
        if pc_number in lab.keys():
            print("PC with this number already exists!")
            choice = input("Do you want to modify, remove or take no action? (m/r/n): ")
            if choice == "m":
                update_pc(pc_number)
            elif choice == "r":
                remove_pc(pc_number)
            else:
                pass
        else:
            lab[pc_number] = pc
            print("PC added successfully!")



def quit_program():
    sys.exit()


def main():
    global lab
    lab = {}
    while True:
        print("\nLab PC Management\n")
        print("1. Add PC")
        print("2. Update PC")
        print("3. Remove PC")
        print("4. Display all PCs")
        print("5. Display a PC")
        print("6. Search PC")
        print("7. Store PCs to file")
        print("8. Quit")

        choice = input("Enter your choice: ")
        if choice == "1":
            add_pc()
        elif choice == "2":
            pc_number = input("Enter PC number to update: ")
            update_pc(pc_number)
        elif choice == "3":
            pc_number = input("Enter PC number to remove: ")
            remove_pc(pc_number)
        elif choice == "4":
            display_all_pcs()
        elif choice == "5":
            pc_number = input("Enter PC number to display: ")
            display_pc(pc_number)
        elif choice == "6":
            search_pc()
        elif choice == "7":
            store_pcs()
        elif choice == "8":
            print("Goodbye!")
            quit_program()
main()
