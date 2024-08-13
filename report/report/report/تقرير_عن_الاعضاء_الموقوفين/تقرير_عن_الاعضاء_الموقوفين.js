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
    ],
    onload: function(report) {
        report.page.add_inner_button(__('Clear Filters'), function() {
            frappe.query_report.set_filter_value({
                "tax_id": "",
                "customer": "",
                "customer_name": "",
                "Posting_date": "",
            });
  
            frappe.query_report.refresh();
        });
    }
};
