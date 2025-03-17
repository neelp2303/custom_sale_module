{
    "name": "BizzAppDev Sale Customization",
    "description": """Custom Sale Module by Neel Patel
    - Enhances Sale, Delivery, and Purchase Orders
    - Implements advanced partner search and tagging features
    - Restricts modifications post-confirmation
    """,
    "summary": "Enhancements for Sales, Deliveries, and Purchases",
    "version": "1.0.0",
    "category": "Sales",
    "sequence": 100,
    "author": "Neel Patel",
    "depends": ["base", "sale", "stock", "purchase", "mrp"],
    "installable": True,
    "application": True,
    "license": "LGPL-3",
    "assets": {
        "web.assets_backend": [
            "static/src/js/copy_widget.js",
            "static/src/xml/copy_widget.xml",
        ]
    },
    "data": [
        "security/ir.model.access.csv",
        "views/res_partner_views.xml",
        "views/sale_order_views.xml",
        "views/stock_picking_views.xml",
        "data/automated_actions.xml",
    ],
}
