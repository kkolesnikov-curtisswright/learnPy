product_catalog = {
    "SKU123" : {
        "name": "Widget A",
        "price": 19.99,
        "quantity": 50
    },
    "SKU456": {
        "name": "Gadget B",
        "price": 34.95,
        "quantity": 25
    },
    "SKU789": {
        "name": "Gizmo C",
        "price": 9.99,
        "quantity": 100
    }
}
sku = "SKU123"
print("The price of " + product_catalog[sku]["name"] + " is $" + str(product_catalog[sku]["price"]))