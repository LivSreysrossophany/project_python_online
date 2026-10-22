from repository.product import ProductRepository
from service.product import ProductService
from colorama import Fore, Style, init

init(autoreset=True)
repository = ProductRepository()
service = ProductService(repository)


while True:

    print(Fore.GREEN+"=====================================")
    print(Fore.GREEN+"|Stock information Management System|")
    print(Fore.GREEN+"=====================================")
    print(Fore.GREEN+"| 1/. View All Products             |")
    print(Fore.GREEN+"| 2/. Add New Product               |")
    print(Fore.GREEN+"| 3/. Update Product                |")
    print(Fore.GREEN+"| 4/. Delete Product                |")
    print(Fore.GREEN+"| 5/. Search Product                |")
    print(Fore.GREEN+"| 6/. Manage Categories             |")
    print(Fore.GREEN+"| 7/. Manage Suppliers              |")
    print(Fore.GREEN+"| 8/. Stock Entry                   |")
    print(Fore.GREEN+"| 9/. Stock Adjustment              |")
    print(Fore.GREEN+"| 10/. Purchase Order               |")
    print(Fore.GREEN+"| 11/. Sales Order                  |")
    print(Fore.GREEN+"| 12/. Low Stock Alert              |")
    print(Fore.GREEN+"| 13/. Stock History                |")
    print(Fore.GREEN+"| 14/. Reports                      |")
    print(Fore.GREEN+"| 15/. Exit App                     |")
    print(Fore.GREEN+"=====================================")

    option = input("Enter Option (1-15): ")
    match option:

        case "1":
            print(Fore.CYAN+"========View Product========")
            service.get_products()

        case "2":
            print(Fore.CYAN+"======== Add Product ========")

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

                service.add_product(
                    id,
                    name,
                    price,
                    category,
                    quantity,
                    supplier,
                    description
                )
            except ValueError as e:
                print(Fore.RED + f" Invalid input: {e}")

            except Exception as e:
                print(Fore.RED + f" An error occurred: {e}")
        case "3":
            print(Fore.CYAN+"========Update Product========")
            try:
                id = int(input("Enter Product ID: "))
                name = input("Enter New Name: ")
                price = float(input("Enter New Price: "))
                category = input("Enter New Category: ")
                quantity = int(input("Enter New Quantity: "))
                supplier = input("Enter New Supplier: ")
                description = input("Enter New Description: ")

                service.update_product(
                    id,
                    name,
                    price,
                    category,
                    quantity,
                    supplier,
                    description
                )
            except ValueError:
                print(Fore.RED +"Invalid input! ID and Quanity must be integers, and Price must be a  number")
            except Exception as e:
                print(Fore.RED +"An error occurred: {e}")
        case "4":
            print(Fore.CYAN+"========Delete Product========")
            try:
                id = int(input("Enter Product ID: "))

                service.remove_product(id)
            except ValueError:
                print(Fore.RED +"Invalid inputt! Product ID must be a number.")
            except Exception as e:
                print(Fore.RED +"An error occured: {e}")
        case "5":
            print(Fore.CYAN+"======== Search Product ========")
            try:
                keyword = input("Enter Product ID or Product Name: ")
                if keyword.strip() == "":
                    print(Fore.RED +"Search cannot be emty.")
                else:
                    service.search_product(keyword)
            except Exception as e:
                print(Fore.RED +"An error ocuured: {e}")

        case "6":
            print(Fore.CYAN+"======== Manage Categories ========")
            print("1. View Categories")
            print("2. Add Category")
            try:
                choice = input("Choose option: ")

                if choice == "1":
                    service.get_categories()

                elif choice == "2":
                    category = input("Enter Category Name: ")
                    service.add_category(category)

                else:
                    print(Fore.RED +"Invalid option")
            except Exception as e:
                print(Fore.RED +"An error occured:{e}")

        case "7":
            print(Fore.CYAN+"======== Manage Suppliers ========")
            print("1. View Suppliers")
            print("2. Add Supplier")
            try:
                choice = input("Choose option: ")

                if choice == "1":
                    service.get_suppliers()

                elif choice == "2":
                    supplier = input("Enter Supplier Name: ")
                    service.add_supplier(supplier)

                else:
                    print(Fore.RED +"Invalid option")
            except Exception as e:
                print(Fore.RED +"An error occured:{e}")
        case "8":
            print(Fore.CYAN+"======== Stock Entry ========")
            try:
                id = int(input("Enter Product ID: "))
                quantity = int(input("Enter Stock Quantity: "))
                if quantity<=0:
                    print("Stock quatity must be greater than 0.")
                else:
                    service.stock_entry(id, quantity)
            except ValueError:
                print(Fore.RED +"Invalid input! Product ID and quantity must be numbers.")
            except Exception as e:
                print(Fore.RED +"An error occured:{e}")

        case "9":
            print(Fore.CYAN+"======== Stock Adjustment ========")
            try:
                id = int(input("Enter Product ID: "))
                quantity = int(input("Enter New Quantity: "))
                if quantity<0:
                    print("Quantity cannot be nagative.")
                else:
                    service.stock_adjustment(id, quantity)
            except ValueError:
                print(Fore.RED +"Invalid input! Product ID and quanutity must be numbers.")
            except Exception as e:
                print(Fore.RED +"An error occured:{e}")
        case "10":
            print(Fore.CYAN+"======== Purchase Order ========")
            try:
                id = int(input("Enter Product ID: "))
                quantity = int(input("Enter Purchase Quantity: "))
                if quantity<=0:
                    print(Fore.RED +"Purchase quantity must be greater than 0.")
                else:
                    service.purchase_order(id, quantity)
            except ValueError:
                print(Fore.RED +"Invalid input! Product ID and qauntity must be numbers.")
            except Exception as e:
                print(Fore.RED +"An error occured:{e}")
        case "11":
            print(Fore.CYAN+"======== Sales Order ========")
            try:
                id = int(input("Enter Product ID: "))
                quantity = int(input("Enter Sales Quantity: "))
                if quantity<=0:
                    print("Sales quantity must be greater than 0.")
                else:
                    service.sales_order(id, quantity)
            except ValueError:
                print(Fore.RED +"Invalid input! Product ID and quantity must be numbers.")
            except Exception as e:
                print(Fore.RED +"An error occured:{e}")
        case "12":
            print(Fore.CYAN+"======== Low Stock Alert ========")
            try:
                service.low_stock_alert()
            except Exception as e:
                print(Fore.RED +"An error occured:{e}")
        case "13":
            print(Fore.CYAN+"======== Stock History ========")
            try:
                service.stock_history()
            except Exception as e:
                print(Fore.RED +"An error occured:{e}")
        case "14":
            print("                    ========Reports========                    ")
            try:
                service.get_report()
            except Exception as e:
                print(Fore.RED+"An error occured:{e}")
        case "15":
            print(Fore.CYAN+"Thank you for using this system.")
            break
        case _:
            print(Fore.RED+"INVALID OPTION")