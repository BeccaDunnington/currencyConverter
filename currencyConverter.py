from tkinter import *
from tkinter import messagebox
import requests
import json
#from PIL import ImageTk, Image



#I--------------functions----------------I

#I---------------API function------------I


def findRate(baseCurrency, targetCurrency):

    if baseCurrency == targetCurrency:
        messagebox.showerror("error", errorMessage["currency"])

    else:

        #url = 'https://v6.exchangerate-api.com/v6/--APIKEYHERE--/pair/EUR/GBP'

        #building the URL
        currencyFormat = baseCurrency + '/' + targetCurrency
        url = 'https://v6.exchangerate-api.com/v6/--APIKEYHERE--/pair/' + currencyFormat

        # Making a request
        response = requests.get(url)
        data = response.json()

        # JSON object
        rate = (data['conversion_rate'])
        return rate


#I---------Validation functions----------I

def validate():
# main validation function does all validation checks one after the other
# returning if one error is triggered to stop multiple errorboxes displaying
# at once or the convert function going ahead.

    #retrieve what is entered in the fields
    amount = amountE.get()

    #validation
    if presenceValidation(amount) == True:
        if typeValidation(amount) == True:
            if formatValidation(amount) == True:
                if boundaryValidation(amount) == True:
                    return True

#I------other validation functions-------I
def presenceValidation(x):
    if not len(x) > 0:
        messagebox.showerror("error", errorMessage["presence"])
        return False
    else:
        return True

def typeValidation(x):
    try:
        x = float(x)
        return True
    except:
        messagebox.showerror("error", errorMessage["type"])
        ##global valid
        ##valid = "false"
        return False


def formatValidation(x):
    if len(x.rsplit('.')[-1]) != 2:
        messagebox.showerror("error", errorMessage["type"])
        ##global valid
        ##valid = "false"
        return False
    else:
        return True

def boundaryValidation(x):
    x = float(x)
    if x < 0 or x >= 100000000:
        messagebox.showerror("error", errorMessage["boundary"])
        return False
    else:
        return True



# I-----------Button command functions-------------I

def clear():
    calc["text"] = " "
    amountE.delete(0, END)
    rateE.delete(0, END)

#gets correct symbols -- NOT WORKING YET
#def symbolSelect(event):
    #retrieve what is entered in the fields
#    currencyFrom = currency[drop1.get()]
#    currencyTo = currency[drop2.get()]


# main conversion function
def convert():
    if validate() == True:
        #casting strings to floats
        amount = float(amountE.get())
        #rate = float(rateE.get())
        rate = findRate(drop1.get(), drop2.get())
        #calculate the currency conversion
        conversion = amount*rate
        #format the outputs to 2 decimal places
        amount = "{:.2f}".format(amount)
        conversion = "{:.2f}".format(conversion)
        #getting the currency symbols
        currencyFrom = currency[drop1.get()]
        currencyTo = currency[drop2.get()]
        #display the result
        output = "Original amount: " + currencyFrom + str(amount) + " \n Calculation: " + currencyTo + str(conversion)
        calc["text"] = output





#I----------lists and dictionaries--------------I
#symbols = ["£", "€", "¥", "$"]
currency = {
    "GBP" :"£",
    "EUR": "€",
    "JPY": "¥",
    "USD": "$"
}

flags =["", ""]

errorMessage = {
    "presence":   "Fields cannot be left blank",
    "type":       "Amount to convert must be a number with two decimal places, eg. 10.60.",
    "boundary":   "Amount to convert must be larger than 0.00 and smaller than 1000000.00.",
    "exchange":   "Exchange rate must be a number larger than 0",
    "currency":   "Currency error. Currency to convert to must be different to the base currency"
}


#I----------------GUI Set-up------------------I
root = Tk()
root.title("Currency Converter Calculator")
root.geometry("500x300")
root.configure(bg = "gray18")
frame = Frame(root)
frame.configure(bg = "gray18")
frame.place(relx = 0.5, rely = 0.5, anchor = CENTER)
#I-----------------Gui widgets---------------I

#input fields
amountE = Entry(frame, width = 10,
                      bg = "gray25",
                      fg = "snow",
                      font = ("Helvetica Neue", 22))

"""rateE = Entry(frame, width = 10,
                    bg = "gray25",
                    fg = "snow",
                    font = ("Helvetica Neue", 22))
"""
#dropdown menus
drop1 = StringVar()
drop1.set(list(currency)[0])
#drop1.set(currency[0])
currencydrop1 = OptionMenu(frame, drop1, *currency,) #command = symbolSelect)
currencydrop1.configure(bg = "gray25",
                        fg = "snow",
                        height = 1,
                        font = ("Helvetica Neue", 22))

drop2 = StringVar()
drop2.set(list(currency)[1])
#drop2.set(currency[1])
currencydrop2 = OptionMenu(frame, drop2, *currency,) #command = symbolSelect)
currencydrop2.configure(bg = "gray25",
                        fg = "snow",
                        height = 1,
                        font = ("Helvetica Neue", 22))

# Labels
calc = Label(frame, bg = "slateblue3",
                    fg = "snow",
                    font = ("Helvetica Neue", 22))
calc.configure(borderwidth = 2, height = 4, width = 30, relief="ridge")


rateLabel = Label(frame, text = "Rate",
                        bg = "gray18",
                        fg = "snow",
                        padx = 40,
                        pady = 20,
                        font = ("Helvetica Neue", 22))

toLabel = Label(frame, text = "to",
                      bg = "gray18",
                      fg = "snow",
                      padx = 10,
                      pady = 10,
                      font = ("Helvetica Neue", 22))


#Buttons
convertButton = Button(frame, text = "Convert",
                             bg = "snow",
                             fg = "gray18",
                             font = ("Helvetica Neue", 22),
                             padx = 20,
                             pady = 10,
                             command = convert)


clearButton = Button(frame, text = "Clear",
                           bg = "snow",
                           fg = "gray18",
                           font = ("Helvetica Neue", 22),
                           padx = 20,
                           pady = 10,
                           command = clear)


closeButton = Button(frame, text = "Close",
                           bg = "snow",
                           fg = "gray18",
                           font = ("Helvetica Neue", 22),
                           padx = 20,
                           pady = 10,
                           command = root.quit)



#I---------------GUI grid layout----------------I

amountE.grid(row = 0, column = 0)
currencydrop1.grid(row = 0, column = 1)
toLabel.grid(row = 0, column = 2, padx = 30, pady = 30)
currencydrop2.grid(row = 0, column = 3)

#rateLabel.grid(row = 1, column = 0)
#rateE.grid(row = 1, column = 1)


calc.grid(row = 2, column = 0, columnspan = 4, pady = (0, 10))

clearButton.grid(row = 3, column = 0)
convertButton.grid(row = 3, column = 1, columnspan = 2, pady = 25)
closeButton.grid(row = 3, column = 3)


root.mainloop()
