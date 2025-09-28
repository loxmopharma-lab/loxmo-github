# Placeholder for invoice management features
invoices = []

def create_invoice(customer, product_list):
    invoice = {
        "customer": customer,
        "products": product_list
    }
    invoices.append(invoice)

def list_invoices():
    if not invoices:
        print("No invoices found.")
    else:
        print("Invoice List:")
        for idx, invoice in enumerate(invoices, 1):
            customer = invoice["customer"]
            products = invoice["products"]
            print(f"Invoice {idx}: Customer - {customer}, Products - {products}")
