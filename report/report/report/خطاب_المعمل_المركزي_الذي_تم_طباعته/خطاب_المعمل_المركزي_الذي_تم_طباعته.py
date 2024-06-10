import frappe
from frappe import _


def execute(filters=None):
    columns = [
        {
            "label": _("Invoice Number"),
            "fieldname": "name",
            "fieldtype": "Link",
            "options": "Sales Invoice",
            "width": 100,
        },
        {
            "label": _("Membership Code"),
            "fieldname": "customer",
            "fieldtype": "Link",
            "options": "Customer",
            "width": 120,
        },
        {
            "label": _("Company Name"),
            "fieldname": "customer_name",
            "fieldtype": "Data",
            "width": 120,
        },{ 
            "label":_("CEO Name"),
            "fieldname":"custom_name_of_the_cioowner_of_the_company",
            "fieldtype":"Data",
            "width": 200,

        },
        {
            "label": _("Member Category"),
            "fieldname": "customer_group",
            "fieldtype": "Link",
            "options": "Customer Group",
            "width": 200,
        },
        {
            "label":_("Member Status"),
            "fieldname": "custom_customer_status",
            "fieldtype": "Data",
            "width": 100,
        },
        {
            "label": _("Is Printed"),
            "fieldname": "custom_is_printed",
            "fieldtype": "Check",
            "width": 100,
        },
        {
            "label": _("Posting Date"),
            "fieldname": "posting_date",
            "fieldtype": "Date",
            "width": 100,
        },
        {
            "label": _("Item Code"),
            "fieldname": "items",
            "fieldtype": "Data",
            "width": 100,
        },
    ]
    data = get_sales_invoice_data(filters)

    return columns, data



def get_sales_invoice_data(filters):
    conditions = {
        "docstatus": 1,
    }
    
    if filters.get("sales_invoice"):
        conditions["name"] = filters.get("sales_invoice")
    if filters.get("customer"):
        conditions["customer"] = filters.get("customer")
    if filters.get("customer_group"):
        conditions["customer_group"] = filters.get("customer_group")
    if filters.get("customer_name"):
        conditions["customer_name"] = filters.get("customer_name")
    conditions["custom_service_group"] = "خطاب المعمل المركزي"
    conditions["custom_is_printed"] = 1

    if filters.get("from_date") and filters.get("to_date"):
        conditions["posting_date"] = ["BETWEEN", [filters.get("from_date"), filters.get("to_date")]]
    else:
        if filters.get("from_date"):
            conditions["posting_date"] = [">=", filters.get("from_date")]
        if filters.get("to_date"):
            conditions["posting_date"] = ["<=", filters.get("to_date")]

    customer_filter = {}
    if filters.get("custom_customer_status"):
        customer_filter["custom_customer_status"] = filters.get("custom_customer_status")
    if filters.get("custom_name_of_the_cioowner_of_the_company"):
        customer_filter["custom_name_of_the_cioowner_of_the_company"] = filters.get("custom_name_of_the_cioowner_of_the_company")
    
    if customer_filter:
        customers = frappe.get_all(
            "Customer",
            filters=customer_filter,
            fields=["name"]
        )
        customer_names = [customer["name"] for customer in customers]
        if customer_names:
            conditions["customer"] = ["in", customer_names]
        else:
            # If no customers match the status filter, return an empty list
            return []

    sales_invoices = frappe.get_all(
        "Sales Invoice",
        filters=conditions,
        fields=[
            "name",
            "customer",
            "customer_name",
            "customer_group",
            "custom_is_printed",
            "posting_date",
            "custom_service_group",
        ],
        order_by="custom_is_printed desc",
    )

    for invoice in sales_invoices:
        items = frappe.get_all(
            "Sales Invoice Item",
            filters={"parent": invoice["name"]},
            fields=["item_code"],
        )
        invoice["items"] = ", ".join(item["item_code"] for item in items if item["item_code"] is not None)

        customer_details = frappe.get_all(
            "Customer",
            filters ={"customer_name":invoice["customer_name"]},
            fields=["custom_name_of_the_cioowner_of_the_company","custom_customer_status"]

        )
        if customer_details:   
            customer_info = customer_details[0]
            invoice['custom_customer_status'] = customer_info.get('custom_customer_status')
            invoice['custom_name_of_the_cioowner_of_the_company'] = customer_info.get('custom_name_of_the_cioowner_of_the_company')
          
            print ("invoiceeeeeeeeeeeeeeeee",invoice['custom_customer_status'])
    return sales_invoices






























