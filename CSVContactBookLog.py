import csv
import os

FILENAME = "contacts.csv"

if not os.path.exists(FILENAME):
    with open(FILENAME, "w", newline="", encoding="utf-8") as f:
        writer  = csv.writer(f)
        writer.writerow(["Name", "Phone", "Email"])

def add_contact():
    name = input("Name: ").strip()
    phone = input("Phone: ").strip()
    email = input("Email: ").strip()

    #check for duplicates
    with open(FILENAME, "r", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        for row in reader:
            if row["name"].lower() == name.lower():
                print("Contact already exists")
                return

    with open(FILENAME, "a", newline="", encoding="utf-8") as f:
        writers = csv.writer(f)
        writers.writerow([name, phone, email])
        print("Contact added")

def view_contact():
    with open(FILENAME, "r", encoding="utf-8") as f:
        reader = csv.reader(f)
        rows = list(reader)


        if len(rows) < 1:
            print("No contacts found")
            return

        print("\n your Contacts \n")

        for row in rows:
            print(f"{row[0]} | {row[1]} | {row[2]}")
        print()

def search_contact():
    term  = input("Enter the Name to search: ").strip().lower()
    found = False

    with open(FILENAME, "r", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        for row in reader:
            if term in row["name"]:
                print(f"{row['Name']} | {row['Phone']} | {row['Email']}")
                found = True

    if not found:
        print("No mactching contact found")


def update_contact():
    name = input("Enter the name you want to update details of: ")
    updated = False

    with open(FILENAME, 'r', newline="", encoding="UTF-8") as f:
        reader = list(csv.DictReader(f))
        for row in reader:
            if row["Name"].lower() == name.lower():
                print(f" Found: {row['Name']} | {row['Phone']} | {row['Email']}")

                new_name = input("Enter new name: ").strip()
                new_phone =  input("Enter new phone: ").strip()
                new_email = input("Enter new email: ").strip()

                if new_name:
                    row["Name"] = new_name
                if new_phone:
                    row["Phone"] = new_phone
                if new_email:
                    row['Email'] = new_email

                updated = True
                break

        if updated:
            # Rewrite the CSV file with updated contacts
            with open(FILENAME, "w", newline="", encoding="utf-8") as f:
                fieldnames = ["Name", "Phone", "Email"]
                writer = csv.DictWriter(f, fieldnames=fieldnames)
                writer.writeheader()
                writer.writerows(reader)
            print("Contact updated successfully.")
        else:
            print("No matching contact found.")


def remove_contact():
    name = input("Enter the name you want to delete: ").strip()
    removed = False

    with open(FILENAME, 'r', encoding="utf-8") as f:
        reader = csv.DictReader(f)
        rows = list(reader)

    new_rows = []
    for row in reader:
        if row["Name"].lower() == name.lower():
            print(f"Deleted: {row['Name']} | {row['Phone']} | {row['Email']}")
            removed = True
        else:
            new_rows.append(row)

    if removed:
        with open(FILENAME, "w", newline="", encoding="utf-8") as f:
            fieldnames = ["Name", "Phone", "Email"]
            writer = csv.DictWriter(f, fieldnames=fieldnames)
            writer.writeheader()
            writer.writerows(new_rows)
        print("Contact removed successfully.")
    else:
        print("No matching contact found.")







def main():
    while True:
        print("\n Contact Book")
        print("1. Add Contact")
        print("2. View Contact")
        print("3. Search Contact")
        print("4. update contact")
        print("5. remove contact")
        print("6. Exit")

        choice = input("Choose an option: (1-6) ").strip()
        if choice == "1":
            add_contact()
        elif choice == "2":
            view_contact()
        elif choice == "3":
            search_contact()
        elif choice == "4":
            update_contact()
        elif choice == "5":
            remove_contact()
        elif choice == "6":
            print("Thank you for using our software")
        else:
            print("Invalid Choice")


if __name__ == "__main__":
    main()

