self,
id,
name,
price,
category,
quantity,
supplier,
description):
for product in self.products:
    if product.get_id == id:
        product.set_name = name
        product.set_price = price
        product.set_category = category
        product.set_quantity = quantity
        product.set_supplier = supplier
        product.set_description = description
    return True

    return False