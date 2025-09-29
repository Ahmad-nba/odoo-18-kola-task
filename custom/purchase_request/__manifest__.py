{
'name': 'Purchase Request',
'version': '1.0.0',
'summary': 'Simple Purchase Request to create RFQs from employees',
'category': 'Purchases',
'author': 'Ahamada Shamuran',
'depends': ['purchase'],
'data': [
'views/purchase_request_views.xml',
'security/ir.model.access.csv',
],
'installable': True,
'application': False,
'license': 'LGPL-3',
}