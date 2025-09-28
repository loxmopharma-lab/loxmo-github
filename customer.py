customers = []

def add_customer(name, email):
    customer = {
        "name": name,
        "email": email
    }
    customers.append(customer)

def list_customers():
    if not customers:
        print("No customers found.")
    else:
        print("Customer List:")
        for idx, customer in enumerate(customers, 1):
            print(f"{idx}. {customer['name']} ({customer['email']})")
