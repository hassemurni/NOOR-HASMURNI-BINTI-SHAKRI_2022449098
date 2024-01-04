import tkinter as tk
from tkinter import ttk
import mysql.connector

# Connect to your MySQL database
mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="menu_database"
)

mycursor = mydb.cursor()

def collect_data():
    menu_type = menu_type_var.get()
    menu_list = menu_list_var.get()
    packs = int(packs_entry.get())

    prices = {
        'Grilled Chicken': 25,
        'Prawn Fitter': 28,
        'Fried Crab Claw': 30,
        'Ayam Gepuk': 12,
        'Nasi Ayam': 10,
        'Nasi Briyani': 15,
    }

    total_price = prices[menu_list] * packs

    try:
        sql = 'INSERT INTO MENU (menu_list, menu_packs, total_price) VALUES (%s, %s, %s)'
        val = (menu_list, packs, total_price)
        mycursor.execute(sql, val)
        mydb.commit()
        output_label.config(text=f'Order submitted successfully! Total Price: RM {total_price}')
    except mysql.connector.Error as err:
        output_label.config(text=f'Error submitting order: {err}')

# main window
root = tk.Tk()
root.title("Menu")
root.geometry('600x800')

# Page Title
label = ttk.Label(root, text='Choose Your Meal', font=("Times New Roman", 14, "bold"))
label.pack(ipadx=10, ipady=10)

# Prices List by using textbox
prices_text = tk.Text(root, height=10, width=30)
prices_text.pack(ipadx=10, pady=10)

# Western menu list
prices_text.insert(tk.END, "WESTERN MENU:\n\n")
prices_text.insert(tk.END, "Grilled Chicken \nPrice: RM 25\n\n")
prices_text.insert(tk.END, "Prawn Fitter \nPrice: RM 28\n\n")
prices_text.insert(tk.END, "Fried Crab Claw \nPrice: RM 30\n\n")
prices_text.configure(state='disabled')

# Asian menu list
prices_text = tk.Text(root, height=10, width=30)
prices_text.pack(ipadx=10, pady=10)
prices_text.insert(tk.END, "ASIAN MENU:\n\n")
prices_text.insert(tk.END, "Ayam Gepuk \nPrice: RM 12\n\n")
prices_text.insert(tk.END, "Nasi Ayam \nPrice: RM 10\n\n")
prices_text.insert(tk.END, "Nasi Briyani \nPrice: RM 15\n\n")
prices_text.configure(state='disabled')

# Menu Choosing Frame
menu_info_frame = ttk.LabelFrame(root, text='MENU CHOOSING')
menu_info_frame.pack(padx=10, pady=10)

# Variables to store user selections
menu_type_var = tk.StringVar()
menu_list_var = tk.StringVar()
packs_entry = tk.StringVar()  # Define packs_entry

# Western menu
western_menu_label = ttk.Label(menu_info_frame, text='WESTERN MENU')
western_menu_label.grid(row=0, column=0)
western_menu_combobox = ttk.Combobox(menu_info_frame, values=['Grilled Chicken', 'Prawn Fitter', 'Fried Crab Claw'])
western_menu_combobox.grid(row=0, column=1)
western_menu_spinbox = ttk.Spinbox(menu_info_frame, from_=1, to=10,)
western_menu_spinbox.grid(row=0, column=2)

# Asian menu
asian_menu_label = ttk.Label(menu_info_frame, text='ASIAN MENU')
asian_menu_label.grid(row=1, column=0)
asian_menu_combobox = ttk.Combobox(menu_info_frame, values=['Ayam Gepuk', 'Nasi Ayam', 'Nasi Briyani'])
asian_menu_combobox.grid(row=1, column=1)
asian_menu_spinbox = ttk.Spinbox(menu_info_frame, from_=1, to=10,)
asian_menu_spinbox.grid(row=1, column=2)

save_button = tk.Button(root, text="total price", command=collect_data)
save_button.pack(pady=10)



 # Output Label & result
label = tk.Label(root, text='total price', font=("Times New Romans",12))
label.pack(ipadx=10, ipady=10)
output_label = tk.Label(root, text="")
output_label.pack()



root.mainloop()
