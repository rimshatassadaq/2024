# Step 1: Create the list of products (list of dictionaries)
products = [
    {"pid": "p01", "name": "Refrigerator", "image": "refrigerator.jpg", "rating": "4.5"},
    {"pid": "p04", "name": "Washing Machine", "image": "washing_machine.jpg", "rating": "4.2"},
    {"pid": "p05", "name": "Dishwasher", "image": "dishwasher.jpg", "rating": "4.8"},
    {"pid": "p06", "name": "Coffee Maker", "image": "coffee_maker.jpg", "rating": "4.3"},
    {"pid": "p07", "name": "Toaster", "image": "toaster.jpg", "rating": "4.0"},
    {"pid": "p08", "name": "Blender", "image": "blender.jpg", "rating": "4.5"},
    {"pid": "p10", "name": "Air Purifier", "image": "air_purifier.jpg", "rating": "4.6"},
    {"pid": "p11", "name": "Electric Kettle", "image": "electric_kettle.jpg", "rating": "4.1"},
    {"pid": "p12", "name": "New Machine", "image": "new_machine.jpg", "rating": "4.0"}
]

# Step 2: Function to display all products
def show_all_products():
    print("\nAll Products:")
    print("PID\tName\t\t\tImage\t\t\tRating")
    print("-------------------------------------------------------------")
    for product in products:
        print(product["pid"] + "\t" + product["name"] + "\t\t" + product["image"] + "\t\t" + product["rating"])
    print("\n")

# Step 3: Function to add a new product
def add_new_product():
    pid = input("Enter Product ID (pid): ")
    name = input("Enter Product Name: ")
    image = input("Enter Image Filename: ")
    rating = input("Enter Product Rating (1-5): ")
    
    new_product = {"pid": pid, "name": name, "image": image, "rating": rating}
    products.append(new_product)
    
    print("Product added successfully")

# Step 4: Function to delete a product by id
def delete_product():
    pid = input("Enter the Product ID to delete: ")
    for product in products:
        if product["pid"] == pid:
            products.remove(product)
            print("Product with ID deleted successfully")
            return
    print("Product with ID not found")

# Step 5: Function to update product rating without using print(f"")
def update_product_rating():
    pid = input("Enter Product ID to update: ")
    
    for product in products:
        if product["pid"] == pid:
            new_rating = input("Enter new rating for" + product["name"] + ": ")
            product["rating"] = new_rating
            print("Product " + product["name"] + " rating updated to " + new_rating )
            return
    
    print("Product with ID " + pid + " not found")

# Step 6: Main loop to display the menu and handle options
def main():
    while True:
        print("1. Show All Products")
        print("2. Add New Product")
        print("3. Delete a Product")
        print("4. Update Product Rating")
        print("5. Exit")
        
        choice = input("Enter Option to Continue.. ")
        
        if choice == '1':
            show_all_products()
        elif choice == '2':
            add_new_product()
        elif choice == '3':
            delete_product()
        elif choice == '4':
            update_product_rating()
        elif choice == '5':
            print("Exiting program...")
            break
        else:
            print("Invalid option. Please try again")

 # Step 7: Just directly call main() at the end
main()