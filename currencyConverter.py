from currency_converter import CurrencyConverter
import tkinter as tk
currConvert = CurrencyConverter()

window = tk.Tk()
window.geometry("500x400")

def clicked():
    amount = int(amountEntryBox.get())
    curr1 = firstCurrencyEntryBox.get()
    curr2 = requiredCurrencyEntryBox.get()
    data = currConvert.convert(amount,curr1,curr2)
    btnLabel = tk.Label(window, text=data, font="Times 14 bold").place(x = 230, y = 280)

windowLabel = tk.Label(window,text="Currency Converter", font="Times 20 bold").place(x = 130, y = 50)
amountLabel = tk.Label(window,text="Enter amount here : ", font="Times 14 bold").place(x = 70, y = 100)
amountEntryBox = tk.Entry(window)

firstCurrencyLabel = tk.Label(window,text="Enter currency : ", font="Times 14 bold").place(x = 100, y = 150)
firstCurrencyEntryBox = tk.Entry(window)

requiredCurrencyLabel = tk.Label(window, text="Enter required currency : ", font="Times 14 bold").place(x = 28, y = 200)
requiredCurrencyEntryBox = tk.Entry(window)

btn = tk.Button(window, text="click", command= clicked).place(x = 230, y = 250)

amountEntryBox.place(x = 250, y = 105)
firstCurrencyEntryBox.place(x = 250, y = 155)
requiredCurrencyEntryBox.place(x = 250, y = 205)

window.mainloop()


# a = CurrencyConverter()
# print(a.convert(1,'SGD','INR'))