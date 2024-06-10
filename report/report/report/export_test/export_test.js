// Copyright (c) 2024, ds and contributors
// For license information, please see license.txt
/* eslint-disable */

frappe.query_reports[`Export Test`] = {
    "filters": [
        {
            "fieldname": "tax_id",
            "label": "Please write Tax ID",
            "fieldtype": "Data",
            "width": "350px"
        }
    ],
    "onload": function(report) {
        // Function to change text color based on the value of 'is_member'
        function applyColorToIsMember() {
            const rows = report.wrapper.querySelectorAll(".dt-scrollable tbody tr");
            
            rows.forEach(row => {
                const isMemberCell = row.querySelector(".is_member");
                
                if (isMemberCell) {
                    const isMemberValue = isMemberCell.textContent.trim();
                    
                    if (isMemberValue === "Yes") {
                        isMemberCell.style.color = "green";
                    } else if (isMemberValue === "No") {
                        isMemberCell.style.color = "red";
                    }
                }
            });
        }
        
        // Apply color to 'is_member' on initial load
        applyColorToIsMember();
        
        // Function to handle validation of tax_id filter
        function validateTaxId(taxId) {
            // Your validation logic here
            // For example, you can check if the tax ID exists or is correct
            // You can make an AJAX request to the server to check the tax ID
            
            // For demonstration purposes, let's assume tax ID must be a 10-digit number
            const taxIdRegex = /^\d{10}$/;
            
            return taxIdRegex.test(taxId);
        }
        
        // Event listener to validate tax_id filter on change
        report.page.wrapper.addEventListener("change", function(event) {
            if (event.target.matches("[data-filter='tax_id']")) {
                const taxIdInput = event.target;
                const taxId = taxIdInput.value.trim();
                
                if (!validateTaxId(taxId)) {
                    frappe.msgprint({
                        title: __("Invalid Tax ID"),
                        message: __("Please enter a valid 10-digit Tax ID."),
                        indicator: "red"
                    });
                    
                    // Clear the invalid value from the input
                    taxIdInput.value = "";
                }
            }
        });
        
        // Optionally, you can reapply the color after any user actions or updates to the report
        report.page.add_inner_button("Refresh Colors", function() {
            applyColorToIsMember();
        });
    }
};

