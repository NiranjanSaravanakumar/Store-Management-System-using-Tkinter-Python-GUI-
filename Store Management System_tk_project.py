import tkinter as tk
from tkinter import messagebox
from tkinter import ttk

# Initialize the main window
root = tk.Tk()
root.title("Store Management System")
root.geometry("1000x1000")  # Set the window size

# Main Frame
main_frame = tk.Frame(root, bg="skyblue", width=900, height=900)
main_frame.pack(padx=20, pady=20)
# Data storage
products = {}
payment_method = tk.StringVar(value="Cash")  # Default payment method
apply_discount = tk.BooleanVar(value=False)  # Discount option
main_frame.pack_propagate(False)  # Prevent the frame from resizing to its contents

# Function to add a product
def add_product():
    product_id = product_id_entry.get()
    product_name = product_name_entry.get()
    product_qty = product_qty_entry.get()
    customer_name = customer_name_entry.get()
    customer_contact = customer_contact_entry.get()
    if product_id and product_name and product_qty.isdigit():
        products[product_id] = {
            'name': product_name,
            'quantity': int(product_qty),
            'payment': payment_method.get(),
            'discount': apply_discount.get(),
            'customer_name': customer_name,
            'customer_contact': customer_contact
        }
        update_product_list()
        product_id_entry.delete(0, tk.END)
        product_name_entry.delete(0, tk.END)
        product_qty_entry.delete(0, tk.END)
        customer_name_entry.delete(0, tk.END)
        customer_contact_entry.delete(0, tk.END)
        display_total_amount()  # Display total amount after adding product
    else:
        messagebox.showwarning("Input Error", "Please enter valid product ID, name, and quantity.")

def exit_window():
    root.destroy()

# Function to update a product quantity
def update_product():
    product_id = product_id_entry.get()
    product_qty = product_qty_entry.get()
    if product_id in products and product_qty.isdigit():
        products[product_id]['quantity'] = int(product_qty)
        update_product_list()
        product_id_entry.delete(0, tk.END)
        product_qty_entry.delete(0, tk.END)
    else:
        messagebox.showwarning("Input Error", "Product not found or invalid quantity.")

# Function to remove a product
def remove_product():
    product_id = product_id_entry.get()
    if product_id in products:
        del products[product_id]
        update_product_list()
        product_id_entry.delete(0, tk.END)
    else:
        messagebox.showwarning("Input Error", "Product not found.")

# Function to update the product list display and total amount
def update_product_list():
    product_list.delete(0, tk.END)
    total_amount = 0
    for product_id, product in products.items():
        discount_status = "Yes" if product['discount'] else "No"
        product_list.insert(tk.END, f"ID: {product_id}, Name: {product['name']}, Quantity: {product['quantity']}, Payment: {product['payment']}, Discount: {discount_status}, Customer: {product['customer_name']}, Contact: {product['customer_contact']}")
        # Calculate total amount
 
# Function to update the product name entry with the selected product from the dropdown
def update_product_name(event):
    selected_product = department_combobox.get()
    product_name_entry.delete(0, tk.END)
    product_name_entry.insert(0, selected_product)

# Function to display the total amount in the list box
def display_total_amount():
    total_amount = total_amt_entry.get()
    if total_amount.isdigit():
        product_list.insert(tk.END, f"Total Amount: {total_amount}")
    else:
        messagebox.showwarning("Input Error", "Please enter a valid total amount.")

# Main Label
main_label = tk.Label(main_frame, text="PS Electronic Gadgets ", font=('Arial', 16), bg="violet")
main_label.grid(row=0, column=0, columnspan=3, pady=10)

# Widgets

# 1. Label for product ID
product_id_label = tk.Label(main_frame, text="Product ID:", bg="red")
product_id_label.grid(row=4, column=0, padx=10, pady=5, sticky="e")

# 2. Entry for product ID
product_id_entry = tk.Entry(main_frame)
product_id_entry.grid(row=4, column=1, padx=10, pady=5)

# 3. Label for product name
product_name_label = tk.Label(main_frame, text="Product Name:", bg="red")
product_name_label.grid(row=2, column=0, padx=10, pady=5, sticky="e")

# 4. Entry for product name
product_name_entry = tk.Entry(main_frame)
product_name_entry.grid(row=2, column=1, padx=10, pady=5)

# 5. Label for product quantity
product_qty_label = tk.Label(main_frame, text="Product Quantity:", bg="red")
product_qty_label.grid(row=3, column=0, padx=10, pady=5, sticky="e")

# 6. Entry for product quantity
product_qty_entry = tk.Entry(main_frame)
product_qty_entry.grid(row=3, column=1, padx=10, pady=5)

# 7. Dropdown for department store items
department_items = ["Headphones", "USB", "Mobiles", "Laptop", "Earbuds", "Fitness trackers", "VR headset", "Gaming accessories"]
department_label = tk.Label(main_frame, text="Products:", bg="red")
department_label.grid(row=1, column=0, padx=10, pady=5, sticky="e")

department_combobox = ttk.Combobox(main_frame, values=department_items)
department_combobox.grid(row=1, column=1, padx=20, pady=5)
department_combobox.set("Select Product")
department_combobox.bind("<<ComboboxSelected>>", update_product_name)  # Bind the function to the dropdown selection event

# 8. Label for customer name
customer_name_label = tk.Label(main_frame, text="Customer Name:", bg="red")
customer_name_label.grid(row=5, column=0, padx=10, pady=5, sticky="e")

# 9. Entry for customer name
customer_name_entry = tk.Entry(main_frame)
customer_name_entry.grid(row=5, column=1, padx=10, pady=5)

# 10. Label for customer contact
customer_contact_label = tk.Label(main_frame, text="Customer Contact:", bg="red")
customer_contact_label.grid(row=6, column=0, padx=10, pady=5, sticky="e")

# 11. Entry for customer contact
customer_contact_entry = tk.Entry(main_frame)
customer_contact_entry.grid(row=6, column=1, padx=10, pady=5)

# 12. Button to add a product
add_product_button = tk.Button(main_frame, text="Add Product", command=add_product, bg="violet")
add_product_button.grid(row=7, column=0, padx=50, pady=10)

# 13. Button to update product quantity
update_product_button = tk.Button(main_frame, text="Update Quantity", command=update_product, bg="violet")
update_product_button.grid(row=7, column=1, padx=50, pady=10)

# 14. Button to remove a product
remove_product_button = tk.Button(main_frame, text="Remove Product", command=remove_product, bg="violet")
remove_product_button.grid(row=7, column=2, padx=50, pady=10)

# 15. Listbox to display product list
product_list = tk.Listbox(main_frame, width=100)
product_list.grid(row=8, column=0, columnspan=8, padx=20, pady=20)

# 16. Radio button for GPay
gpay_radio = tk.Radiobutton(main_frame, text="Online payment", variable=payment_method, value="GPay", bg="lightgreen")
gpay_radio.grid(row=10, column=0, padx=10, pady=10)

# 17. Radio button for Cash
cash_radio = tk.Radiobutton(main_frame, text="Cash", variable=payment_method, value="Cash", bg="lightgreen")
cash_radio.grid(row=10, column=1, padx=10, pady=10)

# 18. Checkbutton to apply discount
discount_checkbutton = tk.Checkbutton(main_frame, text="Apply Discount", variable=apply_discount, bg="lightgreen")
discount_checkbutton.grid(row=10, column=2, padx=10, pady=10)

# 19. Button to exit the application
exit_button = tk.Button(main_frame, text="Exit", command=exit_window)
exit_button.grid(row=11, column=1, padx=10, pady=10)

# 20. Label for total amount
total_amt_label = tk.Label(main_frame, text="Total amt:", bg="lightgreen")
total_amt_label.grid(row=9, column=0, padx=10, pady=5, sticky="e")

# 21. Entry for total amount
total_amt_entry = tk.Entry(main_frame)
total_amt_entry.grid(row=9, column=1, padx=10, pady=5)

# Main loop
root.mainloop()