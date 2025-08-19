import tkinter
from tkinter import *


# Important Variables
items = []
prices = []
quantities = []
purchased_items = []
purchased_prices = []

# Clearing Entry After Clicking Into It
def clear_entry_on_click(event):
    event.widget.delete(0, tkinter.END)

# Shop Owner Window
shop_owner_window = tkinter.Tk()
shop_owner_window.title("Shop Management System - Tkinter GUI - Iqra Chaudhary")
shop_owner_window.state("zoomed")
shop_owner_window.config(bg="#d9e1ed")

# Title Label
shop_owner_label = Label(shop_owner_window, text="Shop Owner", fg="black", bg="#d9e1ed", font=("Arial", 50, "bold underline")).place(x=570, y=10)

# Add Item Area
add_item_area = Label(shop_owner_window, height=40, width=80, bg="#e2eeff").place(x=150, y=150)
add_items_label = Label(add_item_area, text="Add Items", font=("Arial", 30, "bold"), fg="black", bg="#e2eeff").place(x=330, y=170)

# Entries for Item Information
item_name_entry = Entry(shop_owner_window, width=25, font=("Arial", 20))
item_price_entry = Entry(shop_owner_window, width=25, font=("Arial", 20))
item_quantity_entry = Entry(shop_owner_window, width=25, font=("Arial", 20))

# Default Text In The Entries
item_name_entry.insert(0, "Item Name")
item_price_entry.insert(0, "Item Price")
item_quantity_entry.insert(0, "Item Quantity")

# Placing Entries
item_name_entry.place(x=230, y=250)
item_price_entry.place(x=230, y=330)
item_quantity_entry.place(x=230, y=410)

# Clearing Text After Clicking Into Them
item_name_entry.bind("<Button-1>", clear_entry_on_click)
item_price_entry.bind("<Button-1>", clear_entry_on_click)
item_quantity_entry.bind("<Button-1>", clear_entry_on_click)

# Add Button Function
def add_button_function():
    item_name = item_name_entry.get()
    item_price = item_price_entry.get()
    item_quantity = item_quantity_entry.get()
    
    # Append the item information to the lists
    items.append(item_name)
    prices.append(item_price)
    quantities.append(item_quantity)

    # Clear the entry fields
    item_name_entry.delete(0, tkinter.END)
    item_price_entry.delete(0, tkinter.END)
    item_quantity_entry.delete(0, tkinter.END)

# Display Button Function (Show Items)
def display_button_function1():
    y_value1 = 250
    for every_item in items:
        y_value1 += 40
        Label(display_items_label, text=f"{every_item}", font=("Arial", 20), fg="black", bg="#e2eeff").place(x=850, y=y_value1)
    y_value2 = 250
    for every_price in prices:
        y_value2 += 40
        Label(display_items_label, text=f"{every_price}", font=("Arial", 20), fg="black", bg="#e2eeff").place(x=1055, y=y_value2)
    y_value3 = 250
    for every_quantity in quantities:
        y_value3 += 40
        Label(display_items_label, text=f"{every_quantity}", font=("Arial", 20), fg="black", bg="#e2eeff").place(x=1225, y=y_value3)

# Shop As A Customer Function
def shop_as_a_customer():
    shop_owner_window.destroy()
    customer_window = tkinter.Tk()
    customer_window.title("Customer Window - Tkinter GUI - Iqra Chaudhary")
    customer_window.state("zoomed") 
    customer_window.config(bg="#d9e1ed")

    Label(customer_window, text="Shopping Mall", fg="black", bg="#d9e1ed", font=("Arial", 50, "bold underline")).place(x=550, y=10)
    Label(customer_window, height=40, width=200, bg="#e2eeff").place(x=35, y=150)
    Label(customer_window, text="Items Available", font=("Arial", 30, "bold underline"), fg="black", bg="#e2eeff").place(x=130, y=170)

    # Display Column Labels
    Label(customer_window, text="Items", font=("Arial", 20, "bold"), fg="black", bg="#e2eeff").place(x=80, y=250)
    Label(customer_window, text="Price", font=("Arial", 20, "bold"), fg="black", bg="#e2eeff").place(x=215, y=250)
    Label(customer_window, text="Quantity", font=("Arial", 20, "bold"), fg="black", bg="#e2eeff").place(x=345, y=250)
    Label(customer_window, text="InStock/OutStock", font=("Arial", 20, "bold"), fg="black", bg="#e2eeff").place(x=520, y=250)

    # Cart Area to show selected items
    cart_label = Label(customer_window, text="Cart:", font=("Arial", 20, "bold"), bg="#d9e1ed")
    cart_label.place(x=800, y=200)

    cart_area = Text(customer_window, height=15, width=40, font=("Arial", 16))
    cart_area.place(x=800, y=250)

    def display_available_quantities():
        # Displaying items available for purchase
        y_value1 = 240
        btn_refs = []
        global status_lbl
        for i, (item, price, quantity) in enumerate(zip(items, prices, quantities)):
            y_value1 += 40
            try:
                q = int(str(quantity).strip())
            except Exception:
                q = 0

            print(f"[DEBUG] item={item!r} price={price!r} raw_qty={quantity!r} parsed_qty={q}")

            btn = tkinter.Button(
                customer_window,
                text=f"{item}",
                font=("Arial", 20),
                fg="black",
                bg="#e2eeff",
                border=0,
                command=lambda idx=i: handle_purchase(idx)
            )
            btn.place(x=72, y=y_value1)

            tkinter.Label(customer_window, text=f"{price}", font=("Arial", 20), fg="black", bg="#e2eeff").place(x=215, y=y_value1)
            tkinter.Label(customer_window, text=f"{q}    ", font=("Arial", 20), fg="black", bg="#e2eeff").place(x=345, y=y_value1)

            status_text = "InStock   " if q > 0 else "OutStock"
            status_lbl = tkinter.Label(customer_window, text=status_text, font=("Arial", 20), fg=("black" if q > 0 else "red"), bg="#e2eeff")
            status_lbl.place(x=525, y=y_value1)

            if q <= 0:
                btn.configure(state=tkinter.DISABLED)
                btn.configure(fg="#888888")

            btn_refs.append(btn)
        if q <= 0:
            btn.config(state="disabled")
            status_lbl.config(fg="red")
    display_available_quantities()
    # Function to handle purchase action
    def handle_purchase(index):
        popup = Toplevel(customer_window)
        popup.title("Purchase Item")
        popup.geometry("400x300")
        popup.config(bg="#f0f0f0")

        Label(popup, text=f"Buying: {items[index]}", font=("Arial", 20, "bold"), bg="#f0f0f0").pack(pady=10)
        Label(popup, text=f"Price per Unit: {prices[index]}", font=("Arial", 16), bg="#f0f0f0").pack()
        Label(popup, text=f"Available Quantity: {quantities[index]}", font=("Arial", 16), bg="#f0f0f0").pack()

        quantity_input = Entry(popup, font=("Arial", 16))
        quantity_input.pack(pady=10)
        quantity_input.insert(0, "Enter Quantity")
        quantity_input.bind("<Button-1>", clear_entry_on_click)

        result_label = Label(popup, text="", font=("Arial", 16), fg="green", bg="#f0f0f0")
        result_label.pack()

        def confirm_purchase():
            total_price = 0
            try:
                qty = int(quantity_input.get())
                available_qty = int(quantities[index])
                price = float(prices[index])
                if qty > available_qty:
                    result_label.config(text="Not enough stock!", fg="red")
                    return
                total_cost = qty * price
                purchased_prices.append(total_cost)
                total_price += total_cost
                quantities[index] = str(available_qty - qty)  

            
                status_text = "InStock" if available_qty - qty > 0 else "OutStock"
                status_lbl.config(text=status_text, fg="black" if available_qty - qty > 0 else "red")
                
                purchased_items.append((items[index], qty, total_cost))  # Log
                cart_area.insert(END, f"{items[index]} x {qty} = ${total_cost:.2f}\n")
                result_label.config(text=f"Added to cart!", fg="green")
                display_available_quantities()  
                popup.after(500, popup.destroy)  
            except ValueError:
                result_label.config(text="Enter valid number", fg="red")
        
        Button(popup, text="Confirm", command=confirm_purchase, font=("Arial", 14)).pack(pady=10)
    def total_bill():
        total_bill = 0
        for every_price in purchased_prices:
            total_bill += int(every_price)
        cart_area.insert(END, "----------------------------------------------------------\n")
        cart_area.insert(END, f"TOTAL BILL: ${total_bill}\n")

    submit_button = Button(customer_window, text="Submit", font=("Arial", 30), fg="black", bg="#e2eeff" ,border=0, command=total_bill).place(x=975, y=620)
    customer_window.mainloop()

# Add Button
add_button = Button(shop_owner_window, text="Add Item", font=("Arial", 19), fg="black", bg="#d9e1ed", width=25, command=add_button_function).place(x=230, y=500)

# Display Button
dsiplay_button = Button(shop_owner_window, text="Display Items", font=("Arial", 19), fg="black", bg="#d9e1ed", width=25, command=display_button_function1).place(x=230, y=570)

# Display Item Area
display_items_area = Label(shop_owner_window, height=40, width=80, bg="#e2eeff").place(x=800, y=150)

# Display Area Title
display_items_label = Label(add_item_area, text="Total Items", font=("Arial", 30, "bold"), fg="black", bg="#e2eeff").place(x=980, y=170)

# Column Labels
item_label = Label(display_items_area, text="Items", font=("Arial", 20, "bold"), fg="black", bg="#e2eeff").place(x=850, y=250)
price_label = Label(display_items_area, text="Price", font=("Arial", 20, "bold"), fg="black", bg="#e2eeff").place(x=1055, y=250)
quantity_label = Label(display_items_area, text="Quantity", font=("Arial", 20, "bold"), fg="black", bg="#e2eeff").place(x=1225, y=250)

# Shop As A Customer Button
shop_as_a_customer_button = Button(shop_owner_window, text="Shop as a Customer", font=("Arial", 17, "underline"), fg="black", bg="#d9e1ed", borderwidth=0, activebackground="#d9e1ed", activeforeground="black", cursor="hand2", command=shop_as_a_customer).place(x=1300, y=756)

# Running the MainLoop for Shop Owner Window
shop_owner_window.mainloop()
