// Copyright (c) 2024, ds and contributors
// For license information, please see license.txt
/* eslint-disable */

frappe.query_reports["خطاب المعمل المركزي الذي تم طباعته"] = {
	"filters": [
		{
			"fieldname": 'sales_invoice',
			"label": __('Invoice Name'),
			"fieldtype": 'Link',
			"options": 'Sales Invoice',
			"reqd": 0
		},
		{
			"fieldname": 'customer',
			"label": __('Membership Code'),
			"fieldtype": "Link",
			"options": "Customer",
			"reqd": 0,
		},
		{
            "fieldname": 'custom_name_of_the_cioowner_of_the_company',
            "label": __('CEO Name'),
            "fieldtype": "Data",
            "reqd": 0,
        },
		{
            "fieldname": "custom_customer_status",
            "label": __("Please select Membership Status"),
            "fieldtype": 'Select',
           
            "options": [
                '',
                'Requested',
                'Requested From Website',
                'Active',
                'Inactive',
                'Suspended',
                'استيفاء بيانات'
            ],
            "default": ''
           
        }, 
		{
            "label": __("Company Name"),
            "fieldname": "customer_name",
            "fieldtype": "Data",
            "width": 120,
        },
		{
			"fieldname": 'customer_group',
			"label": __('Membership Category'),
			"fieldtype": "Link",
			"options": "Customer Group",
			"reqd": 0,
		},
		{
            "fieldname": 'from_date',
            "label": 'From Date',
            "fieldtype": "Date",
            "reqd": 0,
        },
        {
            "fieldname": 'to_date',
            "label": 'To Date',
            "fieldtype": "Date",
            "reqd": 0,
        }

	]
};
