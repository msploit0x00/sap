// Copyright (c) 2023, ahmed and contributors
// For license information, please see license.txt
/* eslint-disable */
var item_name ="";
function get_item_name(itemCode){
	
	frappe.call({
		method: 'alquds.alqudsQueries.get_Item_name',
		args:{
			item_code : itemCode
		},
		callback(r){
			
			item_name = r.message;
			
		}
	})
}
frappe.query_reports["Product Order Script Report"] = {
	"filters": [
		{
			"fieldname": "company",
			"label": __("Company"),
			"fieldtype": "Link",
			"options": "Company",
			"reqd": 1,
			"default": frappe.defaults.get_user_default("Company")
		},
		{
			"fieldname": "from_date",
			"label": __("From Date"),
			"fieldtype": "Date",
			"default": frappe.datetime.get_today()
		},
		{
			"fieldname": "to_date",
			"label": __("To Date"),
			"fieldtype": "Date",
			"default": frappe.datetime.get_today()
		},
		{
			"fieldname": "item",
			"label": __("Items"),
			"fieldtype": "Link",
			"options": "Item",
			on_change: () => {
				var itemCode = frappe.query_report.get_filter_value('item');
				get_item_name(itemCode);
				var itemName = item_name;
				return {
					filters: {
						'item_serial': itemName
					}
				}
			}
		},
		// {
		// 	"fieldname": "product_order_details",
		// 	"label": __("Product Order Details"),
		// 	"fieldtype": "Link",
		// 	"options": "Product Order Details",
		// },
		{
			"fieldname": "product_order",
			"label": __("Product Order"),
			"fieldtype": "Link",
			"options": "Product Order",
			get_query: () => {
				return {
					filters: {
						'item_serial': item_name
					}
				}
			}
		},
		// {
		// 	"fieldname": "supplier",
		// 	"label": __("Supplier"),
		// 	"fieldtype": "Link",
		// 	"options": "Supplier",
		// 	on_change: () => {
			
		// 	}
		// },
		// {
		// 	"fieldname": "party_account",
		// 	"label": __("Payable Account"),
		// 	"fieldtype": "Link",
		// 	"options": "Account",
		// 	get_query: () => {
		// 		var company = frappe.query_report.get_filter_value('company');
		// 		return {
		// 			filters: {
		// 				'company': company,
		// 				'account_type': 'Payable',
		// 				'is_group': 0
		// 			}
		// 		};
		// 	}
		// },
		// {
		// 	"fieldname": "ageing_based_on",
		// 	"label": __("Ageing Based On"),
		// 	"fieldtype": "Select",
		// 	"options": 'Posting Date\nDue Date\nSupplier Invoice Date',
		// 	"default": "Due Date"
		// },
		// {
		// 	"fieldname": "range1",
		// 	"label": __("Ageing Range 1"),
		// 	"fieldtype": "Int",
		// 	"default": "30",
		// 	"reqd": 1
		// },
		// {
		// 	"fieldname": "range2",
		// 	"label": __("Ageing Range 2"),
		// 	"fieldtype": "Int",
		// 	"default": "60",
		// 	"reqd": 1
		// },
		// {
		// 	"fieldname": "range3",
		// 	"label": __("Ageing Range 3"),
		// 	"fieldtype": "Int",
		// 	"default": "90",
		// 	"reqd": 1
		// },
		// {
		// 	"fieldname": "range4",
		// 	"label": __("Ageing Range 4"),
		// 	"fieldtype": "Int",
		// 	"default": "120",
		// 	"reqd": 1
		// },
		// {
		// 	"fieldname": "payment_terms_template",
		// 	"label": __("Payment Terms Template"),
		// 	"fieldtype": "Link",
		// 	"options": "Payment Terms Template"
		// },
		// {
		// 	"fieldname": "supplier_group",
		// 	"label": __("Supplier Group"),
		// 	"fieldtype": "Link",
		// 	"options": "Supplier Group"
		// },
		// {
		// 	"fieldname": "group_by_party",
		// 	"label": __("Group By Supplier"),
		// 	"fieldtype": "Check"
		// },
		// {
		// 	"fieldname": "based_on_payment_terms",
		// 	"label": __("Based On Payment Terms"),
		// 	"fieldtype": "Check",
		// },
		// {
		// 	"fieldname": "show_remarks",
		// 	"label": __("Show Remarks"),
		// 	"fieldtype": "Check",
		// },
		// {
		// 	"fieldname": "tax_id",
		// 	"label": __("Tax Id"),
		// 	"fieldtype": "Data",
		// 	"hidden": 1
		// },
		// {
		// 	"fieldname": "show_future_payments",
		// 	"label": __("Show Future Payments"),
		// 	"fieldtype": "Check",
		// }
	]
};
