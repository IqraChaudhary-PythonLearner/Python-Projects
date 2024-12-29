# Importing Modules
import requests
from tkinter import *
from tkinter import ttk
from ttkwidgets.autocomplete import AutocompleteCombobox
# First Class
class RealTimeCurrencyConverter():
    def __init__(self, url):
        # Getting Currencies from API
        self.data = requests.get(url).json()
        self.currencies = self.data['rates']
    def convert(self, from_currency, to_currency, amount):
        # Getting the Rate of Currencies
        amount = amount / self.currencies[from_currency]
        amount = round(amount * self.currencies[to_currency], 2)
        return amount
    
# Second Class
class MainApplication(Tk):
    def __init__(self, converter):
        Tk.__init__(self)
        # Creating the Real Application
        self.currency_converter = converter
        self.title("Currency Converter - Iqra Chaudhary")
        self.geometry("1000x650")
        self.bg_img = PhotoImage(file="D:\\Currency Converter\\simple_bg_img.png")
        # Placing the image
        img_canvas = Canvas(self, width=1000, height=650)
        img_canvas.pack(expand=True)
        img_canvas.create_image(0,0, image=self.bg_img, anchor="nw")
        # Storing Selections and Amount
        self.currency_from = StringVar()
        self.currency_to = StringVar()
        self.amount_to_convert = IntVar()
        # Main Label
        self.currency_converter_label = Label(self, text="Currency Converter", bg="#48465c", fg="#79c4bd",font=("Courier New", 55, "bold italic underline")).place(x=100, y=2)
        # From Currency, To Currency, and Amount Variables 
        self.from_label = Label(self, text="What currency do you want to convert from?", font=("Courier New", 20, "italic bold"), bg="#48465c", fg="#72c1ea").place(x=150, y=115)
        self.to_label = Label(self, text="What currency do you want to convert to?", font=("Courier New", 20, "italic bold"), bg="#48465c", fg="#72c1ea").place(x=150, y=210)
        self.amount_label = Label(self, text="How much money do you want to convert?", font=("Courier New", 20, "italic bold"), bg="#48465c", fg="#72c1ea").place(x=150, y=315)
        # Dropdowns
        self.from_currency_dropdown = AutocompleteCombobox(self, textvariable=self.currency_from,completevalues=list(self.currency_converter.currencies.keys()), font = ("Courier", 12, "bold"), width=24, height=5).place(x=330, y=165)
        self.to_currency_dropdown = AutocompleteCombobox(self, textvariable=self.currency_to,completevalues=list(self.currency_converter.currencies.keys()), font = ("Courier", 12, "bold"), width=24, height=5).place(x=330, y=260)
        # Amount Entry Box
        self.amount_entry = Entry(self, fg="#f26659", font=("Courier New", 17, "italic bold"), textvariable=self.amount_to_convert).place(x=330, y=365)
        # Submit Button
        self.submit_button = Button(self, text="Submit", font=("Courier New", 40, "italic bold"), bg="#48465c", fg="#f7cd54", borderwidth=0, activebackground="#48465c", activeforeground="#f7cd54", cursor="hand2", command=self.perform).place(x=350, y=400)
    def perform(self):
        # Retrieving the Amounts from the Dropdown Menu's and Entry
        amount = float(self.amount_to_convert.get())
        from_curr = self.currency_from.get()
        to_curr = self.currency_to.get()
        # Converting the Amounts
        converted_amount = self.currency_converter.convert(from_curr,to_curr,amount)
        Label(self, text=f"{str(converted_amount)} {self.currency_to.get()}", font=("Courier", 26, "bold italic"), bg="#48465c", fg="#72c1ea").place(x=375, y=478)

url = 'https://api.exchangerate-api.com/v4/latest/USD'
converter = RealTimeCurrencyConverter(url)
MainApplication(converter)
mainloop()
"""def on_select(event):
    selected_option = combobox.get()
    print("Current Option", selected_option)"""