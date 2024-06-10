import frappe
from frappe import _

def execute(filters=None):
    columns = get_columns()
    data = get_customer(filters)
    return columns, data

def get_columns():
    return [
        {"label": _("Member Code"), "fieldname": "member", "fieldtype": "Link", "options": "Customer", "width": 150},
        {"label": _("Customer Name"), "fieldname": "customer_name", "fieldtype": "Link", "options": "Customer", "width": 120},
        {"label": _("Committee Name"), "fieldname": "committee_name", "fieldtype": "Link", "options": "Committee", "width": 150},
        {"label": _("Product Name"), "fieldname": "product_name", "fieldtype": "Data", "width": 150},
        {"label": _("Salutation Type"), "fieldname": "salutation_type", "fieldtype": "Data", "width": 150},
        {"label": _("Customer Status"), "fieldname": "custom_customer_status", "fieldtype": "Data", "width": 150},
        {"label": _("Company Type"), "fieldname": "custom_company_type_", "fieldtype": "Data", "width": 150},
        {"label": _("Customer Activity Type"), "fieldname": "custom_customer_activity_type", "fieldtype": "Data", "width": 150},
        {"label": _("Territory"), "fieldname": "territory", "fieldtype": "Data", "width": 150},
        {"label": _("Joining Date"), "fieldname": "custom_joining_date", "fieldtype": "Date", "width": 150},
        {"label": _("Customer Name English"), "fieldname": "customer_name_english", "fieldtype": "Data", "width": 300},
        {"label": _("CIO/Owner Name"), "fieldname": "custom_name_of_the_cioowner_of_the_company", "fieldtype": "Data", "width": 350},
        {"label": _("CIO/Owner Name English"), "fieldname": "custom_name_of_the_cioowner_of_the_company_in_english", "fieldtype": "Data", "width": 350},
        {"label": _("Commercial Register Number"), "fieldname": "custom_registration_number_in_commercial_register", "fieldtype": "Data", "width": 300},
        {"label": _("Tax ID"), "fieldname": "tax_id", "fieldtype": "Data", "width": 120},
        {"label": _("Primary Contact"), "fieldname": "customer_primary_contact", "fieldtype": "Data", "width": 200},
        {"label": _("Email"), "fieldname": "custom_email", "fieldtype": "Data", "width": 300},
        {"label": _("Responsible Person's Name"), "fieldname": "custom_responsible_persons_name", "fieldtype": "Data", "width": 390},
        {"label": _("Total Amount"), "fieldname": "total_amount", "fieldtype": "Currency", "width": 200}
    ]

def get_customer(filters):
    conditions = []
    params = {}
    committee_name = filters.get("committee_name")
    product_name = filters.get("product_name")
    salutation_type = filters.get("salutation_type")
    custom_customer_status = filters.get("custom_customer_status")
    custom_company_type_ = filters.get("custom_company_type_")
    custom_customer_activity_type = filters.get("custom_customer_activity_type")
    custom_company_code = filters.get("custom_company_code")
    customer_name = filters.get("customer_name")
    territory = filters.get("territory")
    custom_joining_date = filters.get("custom_joining_date")

    if committee_name:
        conditions.append("`tabCommittees you would like to join`.`committees` IN %(committee_name)s")
        params["committee_name"] = tuple(committee_name)

    if product_name:
        conditions.append("`tabCrops that are export`.`product` IN %(product_name)s")
        params["product_name"] = tuple(product_name)

    if salutation_type:
        conditions.append("`tabCommittees you would like to join`.`salutation` LIKE %(salutation_type)s")
        params["salutation_type"] = f"%{salutation_type}%"

    if custom_customer_status:
        conditions.append("`tabCustomer`.`custom_customer_status` = %(custom_customer_status)s")
        params["custom_customer_status"] = custom_customer_status

    if custom_company_type_:
        conditions.append("`tabCustomer`.`custom_company_type_` LIKE %(custom_company_type_)s")
        params["custom_company_type_"] = f"%{custom_company_type_}%"

    if custom_customer_activity_type:
        conditions.append("`tabCustomer`.`custom_customer_activity_type` LIKE %(custom_customer_activity_type)s")
        params["custom_customer_activity_type"] = f"%{custom_customer_activity_type}%"

    if custom_company_code:
        conditions.append("`tabCustomer`.`custom_company_code` LIKE %(custom_company_code)s")
        params["custom_company_code"] = custom_company_code

    if customer_name:
        conditions.append("`tabCustomer`.`name` LIKE %(customer_name)s")
        params["customer_name"] = customer_name

    if territory:
        conditions.append("`tabCustomer`.`territory` IN %(territory)s")
        params["territory"] = tuple(territory)

    if custom_joining_date:
        conditions.append("`tabCustomer`.`custom_joining_date` LIKE %(custom_joining_date)s")
        params["custom_joining_date"] = f"%{custom_joining_date}%"

    # Base SQL query
    sql = """
        SELECT 
            `tabCustomer`.`customer_name` AS `customer_name`,
            GROUP_CONCAT(DISTINCT `tabCommittees you would like to join`.`committees` SEPARATOR ', ') AS `committee_name`,
            `tabCustomer`.`custom_customer_status` AS `custom_customer_status`,
            `tabCustomer`.`custom_company_type_` AS `custom_company_type_`,
            `tabCustomer`.`custom_customer_activity_type` AS `custom_customer_activity_type`,
            `tabCustomer`.`territory` AS `territory`,
            `tabCustomer`.`custom_joining_date` AS `custom_joining_date`,
            `tabCustomer`.`custom_company_code` AS `custom_company_code`,
            `tabCustomer`.`name` AS `member`,
            `tabCustomer`.`custom_customer_name_in_english` AS `customer_name_english`,
            `tabCustomer`.`custom_name_of_the_cioowner_of_the_company` AS `custom_name_of_the_cioowner_of_the_company`,
            `tabCustomer`.`custom_name_of_the_cioowner_of_the_company_in_english` AS `custom_name_of_the_cioowner_of_the_company_in_english`,
            `tabCustomer`.`custom_registration_number_in_commercial_register` AS `custom_registration_number_in_commercial_register`,
            `tabCustomer`.`tax_id` AS `tax_id`,
            `tabCustomer`.`customer_primary_contact` AS `customer_primary_contact`,
            `tabCustomer`.`custom_email` AS `custom_email`,
            `tabCustomer`.`custom_responsible_persons_name` AS `custom_responsible_persons_name`,
            `tabCustomer`.`custom_volume_of__exports` AS `total_amount`,
            GROUP_CONCAT(DISTINCT `tabCrops that are export`.`product` SEPARATOR ', ') AS `product_name`,
            `tabCommittees you would like to join`.`salutation` AS `salutation_type`
        FROM 
            `tabCustomer`
        INNER JOIN `tabCommittees you would like to join`
            ON `tabCommittees you would like to join`.`parent` = `tabCustomer`.`name`
        LEFT JOIN `tabCrops that are export`
            ON `tabCrops that are export`.`parent` = `tabCustomer`.`name`
    """

    # Apply the conditions to the SQL query
    if conditions:
        sql += " WHERE " + " AND ".join(conditions)
    
    sql += " GROUP BY `tabCustomer`.`name`"

    # Execute the query with the filter values
    mydata = frappe.db.sql(sql, params, as_dict=True)

    # Return the data
    return mydata
