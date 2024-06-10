// Copyright (c) 2024, Frappe Technologies Pvt. Ltd. and contributors
// For license information, please see license.txt
/* eslint-disable */

frappe.query_reports["خاص بالاعضاء والتسويق وايضا مديرين النظام6"] = {
    "filters": [
        {
            "fieldname": "customer_name",
            "label": __("Customer"),
            "fieldtype": "Link",
            "options": "Customer",
            "width": "200px"
        },
        {
            "fieldname": "committee_name",
            "label": __("Please write committee name"),
            "fieldtype": "MultiSelectList",
            "options": "Committee",
            "width": "200px",
            get_data: function(txt) {
                if (!frappe.query_report.filters) return;
                let committee_name = "Committee";
                return frappe.db.get_link_options(committee_name, txt);
            },
            on_change: function(txt) {
                frappe.query_report.refresh();
            }
        },
        {
            "fieldname": "product_name",
            "label": __("Please select product"),
            "fieldtype": "MultiSelectList",
            "options": "",
            "width": "200px",
            get_data: function(txt) {
                if (!frappe.query_report.filters) return;
                let product = "Product";
                return frappe.db.get_link_options(product, txt);
            },
            on_change: function(txt) {
                frappe.query_report.refresh();
            }
        },
        // {
        //     "fieldname": "salutation_type",
        //     "label": __("Please select salutation type"),
        //     "fieldtype": "Link",
        //     "options": "Salutation",
        //     "width": "200px"
        // },
        {
            "fieldname": "custom_customer_status",
            "label": __("Please select Membership Status"),
            "fieldtype": "Select",
            "options": [
                "",
                "Requested",
                "Requested From Website",
                "Active",
                "Inactive",
                "Suspended",
                "استيفاء بيانات"
            ],
            "default": ""
        },
        {
            "fieldname": "custom_company_type_",
            "label": __("Please Select Company Type"),
            "fieldtype": "Link",
            "options": "Company Type",
            "width": "350px"
        },
        {
            "fieldname": "activity_type",
            "label": __("Please Select customer activity type"),
            "fieldtype": "Link",
            "options": "Customer Activity Type",
            "width": "350px"
        },
        {
            "fieldname": "territory",
            "label": __("Please Select Territory"),
            "fieldtype": "MultiSelectList",
            "options": "Territory",
            "width": "350px",
            get_data: function(txt) {
                if (!frappe.query_report.filters) return;
                let Territory = "Territory";
                return frappe.db.get_link_options(Territory, txt);
            },
            on_change: function(txt) {
                frappe.query_report.refresh();
            }
        },
        {
            "fieldname": "custom_joining_date",
            "label": __("Please Select custom joining date"),
            "fieldtype": "Date",
            "width": "350px"
        },
        {
            "fieldname": "custom_company_code",
            "label": __("Please Enter company code"),
            "fieldtype": "Data",
            "width": "200px"
        }
    ],
    onload: function(report) {
        // Create the clear filters button
        let clearFiltersButton = report.page.add_inner_button(__('Clear Filters'), function() {
            report.filters.forEach(function(filter) {
                // Reset the value of the filter
                if (filter.fieldtype === 'MultiSelectList' || filter.fieldtype === 'Select') {
                    filter.set_value([]);
                } else if (filter.fieldtype === 'Link' || filter.fieldtype === 'Date' || filter.fieldtype === 'Data') {
                    filter.set_value('');
                }
            });
            // Refresh the report to apply the cleared filters
            report.refresh();
        });

        // Apply custom styles to the clear filters button
        $(clearFiltersButton).css({
            'background-color': '#4CAF50',
            'color': 'white',
            'border': 'none',
            // 'padding': '10px 20px',
            'text-align': 'center',
            'text-decoration': 'none',
            'display': 'inline-block',
            'font-size': '16px',
            'margin': '4px 2px',
            'cursor': 'pointer',
            'border-radius': '4px'
        });
		
    }
};
