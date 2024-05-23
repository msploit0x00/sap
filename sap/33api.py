import frappe

@frappe.whitelist(allow_guest=True)
def get_all_customer():
    customers = frappe.db.sql("""SELECT * FROM `tabCustomer`;""",as_dict=True)

    return customers