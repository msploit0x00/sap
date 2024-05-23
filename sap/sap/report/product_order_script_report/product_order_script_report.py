# Copyright (c) 2023, ahmed and contributors
# For license information, please see license.txt

import frappe


def execute(filters=None):
	columns, data = [], []
	columns = get_columns(filters)
	data = get_data(filters)
	
	return columns, data


def get_columns(filters=None):
	# print(filters)
	col= [
				{
					'fieldname': 'product_order',
					'label': ('Product Order'),
					'fieldtype': 'Link',
					'options': 'Product Order',
					'width':'200'
				},
				{
				    'fieldname': 'item_serial',
				    'label': ('Item Serial'),
				    'fieldtype': 'Data',
				    # 'options': 'Product Order Details'
					'width':'200'
				},
				{
				    'fieldname': 'pallet_no',
				    'label': ('Pallet No'),
				    'fieldtype': 'Data',
				    # 'options': 'Product Order Details'
					'width':'130'
				},
				{
				    'fieldname': 'quality_status',
				    'label': ('Quality Status'),
				    'fieldtype': 'Data',
				    # 'options': 'Product Order Details'
					'width':'200'
				},
				{
				    'fieldname': 'item_status',
				    'label': ('	Item Status	'),
				    'fieldtype': 'Data',
				    # 'options': 'Product Order Details'
					'width':'150'
				},
				{
				    'fieldname': 'creation_date',
				    'label': ('Creation Date'),
				    'fieldtype': 'Date',
				    # 'options': 'Product Order Details'
					'width':'200'
				},
				{
				    'fieldname': 'sap_serial',
				    'label': ('Sap Serial Number'),
				    'fieldtype': 'Data',
				    # 'options': 'Product Order Details'
					'width':'150'
				},
				{
				    'fieldname': 'qt_inspection_lab',
				    'label': ('Qt Inspection lab'),
				    'fieldtype': 'Data',
				    # 'options': 'Product Order Details'
					'width':'150'
				},
				{
				    'fieldname': 'qt_inspection_yard',
				    'label': ('Qt Inspection yard'),
				    'fieldtype': 'Data',
				    # 'options': 'Product Order Details'
					'width':'150'
				},
				{
				    'fieldname': 'quality_status_lab',
				    'label': ('Quality Status lab'),
				    'fieldtype': 'Data',
				    # 'options': 'Product Order Details'
					'width':'150'
				},
				{
				    'fieldname': 'quality_status_yard',
				    'label': ('Quality Status yard'),
				    'fieldtype': 'Data',
				    # 'options': 'Product Order Details'
					'width':'150'
				},
				
    		]
	return col


def get_data(filters=None):
	#{'company': 'DataSoft', 'report_date': '2022-12-12', 'item': 'item finshed', 'product_order': 'PO00001', 'ageing_based_on': 'Due Date', 'range1': 30, 'range2': 60, 'range3': 90, 'range4': 120}
	results = []
	if filters:
		if filters.product_order:
			product_O_details = frappe.get_doc("Product Order", filters.product_order).as_dict()
			for product_detail in product_O_details.product_details:
				# print(product_detail.sap_serial_no)
				obj = {
						'product_order': filters.product_order,
						'item_serial': product_O_details.item_serial,
						'pallet_no':product_detail.pallet_no,
						'quality_status':product_detail.quality_status,
						'item_status':product_detail.item_status,
						'creation_date':product_detail.creation,
						'sap_serial': product_detail.sap_serial_no,
						'qt_inspection_lab':product_detail.qt_inspection_lab,
						'qt_inspection_yard':product_detail.qt_inspection_yard,
						'quality_status_lab':product_detail.quality_status_lab,
						'quality_status_yard':product_detail.quality_status_yard

					}
				results.append(obj)
				
		else:
			product_orders = frappe.get_all("Product Order",fields=['name', 'creation'])

			for product_order in product_orders: 
				if (product_order.creation).strftime('%Y-%m-%d') >= filters.from_date and (product_order.creation).strftime('%Y-%m-%d') <= filters.to_date:
					PO_productDetails = frappe.get_doc("Product Order", product_order.name).as_dict()
					for product_detail in PO_productDetails.product_details:
						# print(product_detail)
						obj = {
							'product_order': product_order.name,
							'item_serial': PO_productDetails.item_serial,
							'pallet_no':product_detail.pallet_no,
							'quality_status':product_detail.quality_status,
							'item_status':product_detail.item_status,
							'creation_date':product_detail.creation,
							'sap_serial': product_detail.sap_serial_no
						}
						results.append(obj)
	else:
		product_orders = frappe.get_all("Product Order")
		for product_order in product_orders:
			PO_productDetails = frappe.get_doc("Product Order", product_order.name).as_dict()
			for product_detail in PO_productDetails:
				obj = {
					'product_order': product_order.name,
					'item_serial': PO_productDetails.item_serial,
					'pallet_no':product_detail.pallet_no,
					'quality_status':product_detail.quality_status,
					'item_status':product_detail.item_status,
					'creation_date':product_detail.creation,
					'sap_serial': product_detail.sap_serial_no
				}

				results.append(obj)
			#{'name': 'dec22b9f76', 'owner': 'Administrator', 'creation': datetime.datetime(2023, 1, 18, 15, 52, 44, 983276), 'modified': datetime.datetime(2023, 2, 14, 10, 55, 10, 731396), 'modified_by': 'ali@datasoft@eg.com', 'docstatus': 0, 'idx': 10, 'ref': 'MRQCBLHS30-11900-230', 'pallet_no': '0', 'net_weight': None, 'gross_weight': None, 'jambo_roll_no': None, 'quality_status': None, 'item_status': 'Waiting Quality', 'qt_inspection': None, 'scaler': None, 'qr_code': None, 'sap_serial_no': '563/10', 'sap_pallet_no': '563/0', 'qt_inspection_lab': None, 'qt_inspection_yard': None, 'quality_status_lab': None, 'quality_status_yard': None, 'qt_final': None, 'parent': 'PO01104', 'parentfield': 'product_details', 'parenttype': 'Product Order', 'doctype': 'Product Order Details'}
	
	
	return results