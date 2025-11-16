# -------------------------------------------------------------
# Name: Raj Tilak Singh
# Date: 20-Nov-2025
# Project Title: Contact Book Management System
# Course: MCA (AI & ML) - Programming for Problem Solving Using Python
# Faculty: Ms. Neha Kaushik
# -------------------------------------------------------------


import csv
import json
from datetime import datetime

def log_error(op, msg):
    with open("error_log.txt", "a") as log:
        log.write(f"[{datetime.now()}] {op}: {msg}\n")

print("Welcome to Contact Book Manager")

csv_file = "contacts.csv"

def add_contact():
    try:
        name = input("Enter Name: ").strip()
        phone = input("Enter Phone Number: ").strip()
        email = input("Enter Email Address: ").strip()
        contact = {"name": name, "phone": phone, "email": email}
        with open(csv_file, "a", newline="") as f:
            w = csv.DictWriter(f, ["name", "phone", "email"])
            if f.tell() == 0: w.writeheader()
            w.writerow(contact)
        print(f"Contact '{name}' added successfully!\n")
    except Exception as e:
        log_error("Add", str(e))
        print("Error adding contact!. Check error_log.txt\n") 

def view_contacts():
    try:
        with open(csv_file, "r") as f:
            contacts = list(csv.DictReader(f))
        if not contacts:
            print("No contacts found!\n")
            return
        print("\nSaved Contacts:")
        print("-" * 50)
        print(f"{'Name':<20}\t{'Phone':<15}\t{'Email'}")
        print("-" * 50)
        for c in contacts:
            print(f"{c['name']:<20} {c['phone']:<15} {c['email']}")
        print("-" * 50 + "\n")
        
    except FileNotFoundError as e:
        log_error("View", "FileNotFoundError: contacts.csv missing")
        print("No Contact file found! Add contact first\n")

    except Exception as e:
        log_error("View", str(e))
        print("Error viewing Contact!. Check error_log.txt\n")

def search_contact():
    try:
        name = input("Enter name to search: ").strip().lower()
        with open(csv_file, "r") as f:
            for c in csv.DictReader(f):
                if c["name"].lower() == name:
                    print(f"\nFound Contact:\nName: {c['name']}\nPhone: {c['phone']}\nEmail: {c['email']}\n")
                    return
        print("Contact Not found!\n")
    except Exception as e:
        log_error("Search", str(e))
        print("Error searching Contact!. Check error_log.txt\n")

def update_contact():
    try:
        name = input("Enter the name of the contact to update: ").strip().lower()
        with open(csv_file, "r") as f:
            contacts = list(csv.DictReader(f))
        for c in contacts:
            if c["name"].lower() == name:
                print(f"Current: {c}")
                c["phone"] = input("New phone: ") or c["phone"]
                c["email"] = input("New email: ") or c["email"]
                with open(csv_file, "w", newline="") as f:
                    w = csv.DictWriter(f, ["name", "phone", "email"])
                    w.writeheader()
                    w.writerows(contacts)
                print(f"Contact '{name}' updated successfully!\n")
                return
        print("Contact Not found\n")
    except Exception as e:
        log_error("Update", str(e))
        print("Error updating contact. Check error_log.txt\n")

def delete_contact():
    try:
        name = input("Enter the name of the contact to delete: ").strip().lower()
        with open(csv_file, "r") as f:
            contacts = list(csv.DictReader(f))
        new_c = [c for c in contacts if c["name"].lower() != name]
        if len(new_c) == len(contacts):
            print("Contact Not found!\n")
            return
        with open(csv_file, "w", newline="") as f:
            w = csv.DictWriter(f, ["name", "phone", "email"])
            w.writeheader()
            w.writerows(new_c)
        print(f"Contact '{name}' deleted successfully!\n")
    except Exception as e:
        log_error("Delete Contact", str(e))
        print("Error deleting contact!. Check error_log.txt\n")

def export_to_json():
    try:
        with open(csv_file, "r") as f:
            contacts = list(csv.DictReader(f))
        if not contacts:
            print("No contacts to export!\n")
            return
        with open("contacts.json", "w") as f:
            json.dump(contacts, f, indent=4)
        print("Contacts exported to contacts.json successfully!\n")
    except Exception as e:
        log_error("Export", str(e))
        print("Error exporting to JSON!. Check error_log.txt\n")

def load_from_json():
    try:
        with open("contacts.json", "r") as f:
            contacts = json.load(f)
        print("\nContact Loaded from JSON:")
        print("-" * 50)
        print(f"{'Name':<20}\t{'Phone':<15}\t{'Email'}")
        print("-" * 50)
        for c in contacts:
            print(f"{c['name']:<20} {c['phone']:<15} {c['email']}")
        print("-" * 50 + "\n")
    except FileNotFoundError:
        print("contacts.json not found.Please Export first\n")
    except Exception as e:
        log_error("Load", str(e))
        print("Error loading from JSON!. Check error_log.txt\n")

def main():
    menu = {
        "1": add_contact,
        "2": view_contacts,
        "3": search_contact,
        "4": update_contact,
        "5": delete_contact,
        "6": export_to_json,
        "7": load_from_json,
    }
    while True:
        print("1. Add Contact\n2. View Contacts\n3. Search Contact\n4. Update Contact\n5. Delete Contact\n6. Export to JSON\n7. Load to JSON\n8. Exit")
        choice = input("Choice (1-8): ")
        if choice == "8":
            print("Goodbye!")
            break
        elif choice in menu:
            menu[choice]()
        else:
            print("Invalid\n")

if __name__ == "__main__":
    main()
