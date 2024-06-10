// Copyright (c) 2023, ds and contributors
// For license information, please see license.txt
/* eslint-disable */

frappe.query_reports["تقرير عن الاعضاء الموقوفين"] = {
	"filters": [
		{
			"fieldname": 'tax_id',
			"label": __('Tax ID'),
			"fieldtype": "Data",
			"reqd": 0,
		},
		{
			"fieldname": 'customer',
			"label": __('ID'),
			"fieldtype": 'Link',
			"options": 'Customer',
			"reqd": 0
		},
		{
			"fieldname": 'customer_name',
			"label": __('Company Name'),
			"fieldtype": 'Data',
			"reqd": 0
		},
			
		{
			"fieldname": 'Posting_date',
			"label": __('Date'),
			"fieldtype": 'Date',
			"reqd": 0
		},
	]
};
