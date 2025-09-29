{
'name': 'Custom RFQ Multi-Vendor',
'version': '1.0.0',
'summary': 'Allow assigning RFQs to multiple vendors and collect bids',
'category': 'Purchases',
'author': 'Ahamada Shamuran',
'depends': ['purchase'],
'data': [
'views/purchase_order_views.xml',
'security/ir.model.access.csv',
],
'installable': True,
'application': False,
'license': 'LGPL-3',
}