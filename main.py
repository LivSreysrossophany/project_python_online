from repository.product import ProductRepository
from service.product import ProductService
from utils.color import success, error, warning, info, title
from utils.pdf_logger import start_pdf_capture, set_products_source
start_pdf_capture()



repository = ProductRepository()
set_products_source(repository.get_products)
service = ProductService(repository)

while True:
    title("=====================================")
    title("|Stock information Management System|")
    title("=====================================")
    info("| 1/. View All Products             |")
    info("| 2/. Add New Product               |")
    info("| 3/. Update Product                |")
    info("| 4/. Delete Product                |")
    info("| 5/. Search Product                |")
    info("| 6/. Manage Categories             |")
    info("| 7/. Manage Suppliers              |")
    info("| 8/. Stock Entry                   |")
    info("| 9/. Stock Adjustment              |")
    info("| 10/. Purchase Order               |")
    info("| 11/. Sales Order                  |")
    info("| 12/. Low Stock Alert              |")
    info("| 13/. Stock History                |")
    info("| 14/. Reports                      |")
    info("| 15/. Exit App                     |")
    title("=====================================")

    pw =int(input(f"Please, enter your password: "))
    if pw == 168:
        option = input("Enter Option (1-15): ")
        match option:
            case "1":
                    title("========View Product========")
                    service.get_products()
            case "2":
                title("======== Add Product ========")
                try:
                    id = int(input("Enter Product ID: "))
                    name = input("Enter Product Name: ")
                    if name.strip() == "":
                        raise ValueError("Product Name cannot be empty.")
                    if name.isdigit():
                        raise ValueError("Product Name cannot be a number.")
                    price = float(input("Enter Product Price: "))
                    category = input("Enter Product Category: ")
                    if category.strip() == "":
                        raise ValueError("Product Category cannot be empty.")
                    quantity = int(input("Enter Product Quantity: "))
                    supplier = input("Enter Product Supplier: ")
                    description = input("Enter Product Description: ")
                    service.add_product(id, name, price, category, quantity, supplier, description)
                except ValueError as e:
                    error(f"Invalid input: {e}")
                except Exception as e:
                    error(f"An error occurred: {e}")
            case "3":
                title("========Update Product========")
                try:
                    id = int(input("Enter Product ID: "))
                    name = input("Enter New Name: ")
                    price = float(input("Enter New Price: "))
                    category = input("Enter New Category: ")
                    quantity = int(input("Enter New Quantity: "))
                    supplier = input("Enter New Supplier: ")
                    description = input("Enter New Description: ")
                    service.update_product(id, name, price, category, quantity, supplier, description)
                except ValueError:
                    error("Invalid input! ID and Quantity must be integers, and Price must be a number")
                except Exception as e:
                    error(f"An error occurred: {e}")
            case "4":
                title("========Delete Product========")
                try:
                    id = int(input("Enter Product ID: "))
                    service.remove_product(id)
                except ValueError:
                    error("Invalid input! Product ID must be a number.")
                except Exception as e:
                    error(f"An error occurred: {e}")
            case "5":
                title("======== Search Product ========")
                try:
                    keyword = input("Enter Product ID or Product Name: ")
                    if keyword.strip() == "":
                        warning("Search cannot be empty.")
                    else:
                        service.search_product(keyword)
                except Exception as e:
                    error(f"An error occurred: {e}")
            case "6":
                title("======== Manage Categories ========")
                info("1. View Categories")
                info("2. Add Category")
                try:
                    choice = input("Choose option: ")
                    if choice == "1":
                        service.get_categories()
                    elif choice == "2":
                        category = input("Enter Category Name: ")
                        service.add_category(category)
                    else:
                        warning("Invalid option")
                except Exception as e:
                    error(f"An error occurred: {e}")
            case "7":
                title("======== Manage Suppliers ========")
                info("1. View Suppliers")
                info("2. Add Supplier")
                try:
                    choice = input("Choose option: ")
                    if choice == "1":
                        service.get_suppliers()
                    elif choice == "2":
                        supplier = input("Enter Supplier Name: ")
                        service.add_supplier(supplier)
                    else:
                        warning("Invalid option")
                except Exception as e:
                    error(f"An error occurred: {e}")
            case "8":
                title("======== Stock Entry ========")
                try:
                    id = int(input("Enter Product ID: "))
                    quantity = int(input("Enter Stock Quantity: "))
                    if quantity <= 0:
                        warning("Stock quantity must be greater than 0.")
                    else:
                        service.stock_entry(id, quantity)
                except ValueError:
                    error("Invalid input! Product ID and quantity must be numbers.")
                except Exception as e:
                    error(f"An error occurred: {e}")
            case "9":
                title("======== Stock Adjustment ========")
                try:
                    id = int(input("Enter Product ID: "))
                    quantity = int(input("Enter New Quantity: "))
                    if quantity < 0:
                        warning("Quantity cannot be negative.")
                    else:
                        service.stock_adjustment(id, quantity)
                except ValueError:
                    error("Invalid input! Product ID and quantity must be numbers.")
                except Exception as e:
                    error(f"An error occurred: {e}")
            case "10":
                title("======== Purchase Order ========")
                try:
                    id = int(input("Enter Product ID: "))
                    quantity = int(input("Enter Purchase Quantity: "))
                    if quantity <= 0:
                        warning("Purchase quantity must be greater than 0.")
                    else:
                        service.purchase_order(id, quantity)
                except ValueError:
                    error("Invalid input! Product ID and quantity must be numbers.")
                except Exception as e:
                    error(f"An error occurred: {e}")
            case "11":
                title("======== Sales Order ========")
                try:
                    id = int(input("Enter Product ID: "))
                    quantity = int(input("Enter Sales Quantity: "))
                    if quantity <= 0:
                        warning("Sales quantity must be greater than 0.")
                    else:
                        service.sales_order(id, quantity)
                except ValueError:
                    error("Invalid input! Product ID and quantity must be numbers.")
                except Exception as e:
                    error(f"An error occurred: {e}")
            case "12":
                title("======== Low Stock Alert ========")
                try:
                    service.low_stock_alert()
                except Exception as e:
                    error(f"An error occurred: {e}")
            case "13":
                title("======== Stock History ========")
                try:
                    service.stock_history()
                except Exception as e:
                    error(f"An error occurred: {e}")
            case "14":
                title("======== Reports ========")
                try:
                    service.get_report()
                except Exception as e:
                    error(f"An error occurred: {e}")
            case "15":
                success("Thank you for using this system.")
                break
            case _:
                error("INVALID OPTION")
    else:
        print("Try again!")