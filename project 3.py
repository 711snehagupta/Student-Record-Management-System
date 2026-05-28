import json

FILENAME = "inventory.json"

def load_data():
    try:
        with open(FILENAME, "r") as file:
            return json.load(file)
    except:
        return []

def save_data(products):
    with open(FILENAME, "w") as file:
        json.dump(products, file, indent=4)

def add_product(products):
    product_id = input("Enter Product ID: ")
    name = input("Enter Product Name: ")
    quantity = int(input("Enter Quantity: "))
    price = float(input("Enter Price: "))

    product = {
        "id": product_id,
        "name": name,
        "quantity": quantity,
        "price": price
    }

    products.append(product)
    save_data(products)

    print("Product Added Successfully!")

def view_products(products):

    if len(products) == 0:
        print("No Products Found")
        return

    print("\n===== Product List =====")

    for product in products:
        print("\nProduct ID:", product["id"])
        print("Name:", product["name"])
        print("Quantity:", product["quantity"])
        print("Price:", product["price"])

def search_product(products):

    search = input("Enter Product Name to Search: ")

    found = False

    for product in products:

        if search.lower() == product["name"].lower():

            print("\nProduct Found")
            print("Product ID:", product["id"])
            print("Name:", product["name"])
            print("Quantity:", product["quantity"])
            print("Price:", product["price"])

            found = True

    if not found:
        print("Product Not Found")

def update_product(products):

    product_id = input("Enter Product ID to Update: ")

    for product in products:

        if product["id"] == product_id:

            product["name"] = input("Enter New Name: ")
            product["quantity"] = int(input("Enter New Quantity: "))
            product["price"] = float(input("Enter New Price: "))

            save_data(products)

            print("Product Updated Successfully!")
            return

    print("Product Not Found")

def delete_product(products):

    product_id = input("Enter Product ID to Delete: ")

    for product in products:

        if product["id"] == product_id:

            products.remove(product)

            save_data(products)

            print("Product Deleted Successfully!")
            return

    print("Product Not Found")

def main():

    products = load_data()

    while True:

        print("\n===== Inventory Management System =====")
        print("1. Add Product")
        print("2. View Products")
        print("3. Search Product")
        print("4. Update Product")
        print("5. Delete Product")
        print("6. Exit")

        choice = input("Enter Your Choice: ")

        if choice == "1":
            add_product(products)

        elif choice == "2":
            view_products(products)

        elif choice == "3":
            search_product(products)

        elif choice == "4":
            update_product(products)

        elif choice == "5":
            delete_product(products)

        elif choice == "6":
            print("Exiting Program...")
            break

        else:
            print("Invalid Choice")

main()
