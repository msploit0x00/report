import frappe
from frappe import _

def execute(filters=None):
    columns = get_columns()
    data = get_customer_data(filters)
    return columns, data

def get_columns():
    return [
        {
            "label": _("Member Code"),
            "fieldname": "name",
            "fieldtype": "Link",
            "options": "Customer",
            "width": 200,
        },
        {
            "label": _("Tax ID"),
            "fieldname": "tax_id",
            "fieldtype": "Data",
            "width": 100,
        },
        {
            "label": _("Company Name"),
            "fieldname": "customer_name",
            "fieldtype": "Data",
            "width": 220,
        },
        {
            "label": _("CEO Name"),
            "fieldname": "custom_name_of_the_cioowner_of_the_company",
            "fieldtype": "Data",
            "width": 100,
        },
        {
            "label": _("Representative Name"),
            "fieldname": "custom_responsible_persons_name",
            "fieldtype": "Data",
            "width": 100,
        },
        {
            "label": _("Member Category"),
            "fieldname": "customer_group",
            "fieldtype": "Link",
            "options": "Customer Group",
            "width": 200,
        },
        {
            "label": _("Count Of Committees"),
            "fieldname": "committees",
            "fieldtype": "Data",
            "width": 100,
        },
        {
            "label": _("Member Status"),
            "fieldname": "custom_customer_status",
            "fieldtype": "Select",
            "options": "\nRequested\nActive\nInActive\nSuspended",
            "width": 100,
        },
        {
            "label": _("Reason For Suspending"),
            "fieldname": "custom_reason_for_susbending",
            "fieldtype": "Data",
            "width": 100,
        },
    ]

def get_customer_data(filters):
    conditions = {"custom_customer_status": "Suspended"}

    if filters.get("customer"):
        conditions["name"] = filters.get("customer")
    if filters.get("tax_id"):
        conditions["tax_id"] = filters.get("tax_id")
    if filters.get("custom_reason_for_susbending"):
        conditions["custom_reason_for_susbending"] = filters.get("custom_reason_for_susbending")

    customers = frappe.get_all(
        "Customer",
        filters=conditions,
        fields=[
            "name",
            "customer_name",
            "customer_group",
            "tax_id",
            "custom_customer_status",
            "custom_name_of_the_cioowner_of_the_company",
            "custom_responsible_persons_name",
            "custom_reason_for_susbending",
        ],
    )

    for customer in customers:
        committees = frappe.get_all(
            "Committees you would like to join",
            filters={"parent": customer["name"]},
            fields=["committees"],
        )
        customer["committees"] = len(committees)  # Store the count of committees

    return customers
