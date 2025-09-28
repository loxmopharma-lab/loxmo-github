import customers

def main():
    while True:
        print("\nWelcome to Billing Software!")
        print("1. Add customer")
        print("2. List customers")
        print("3. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            name = input("Enter customer name: ")
            email = input("Enter customer email: ")
            customers.add_customer(name, email)
            print("Customer added.")
        elif choice == "2":
            customers.list_customers()
        elif choice == "3":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Try again.")

if __name__ == "__main__":
    main()
