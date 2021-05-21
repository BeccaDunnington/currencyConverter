from tkinter import *
from tkinter import messagebox
import requests
import json


##########################################
#I--------------functions----------------I

#I---------Validation functions----------I

def validate():
    """main validation function does all validation checks one after the other returning
    if one error is triggered to stop multiple errorboxes displaying at once or the convert
    function going ahead."""

    #retrieve entered info
    amount = amountE.get()
    base = drop1.get()
    target = drop2.get()

    #validation
    if presenceValidation(amount) == True:
        if typeValidation(amount) == True:
            if formatValidation(amount) == True:
                if boundaryValidation(amount) == True:
                    if dropValidation(base, target) == True:
                        return True

#I------other validation functions-------I
def presenceValidation(x):
    """ This function checks that there an input in a user entry box and displays
     an error message if the box is empty. If the error is displayed the function
     returns False other wise the function returns True.
     """
    if not len(x) > 0:
        messagebox.showerror("error", errorMessage["presence"])
        return False
    else:
        return True

def typeValidation(x):
    """ This function takes in one value x and if that value is not a float an
    error message will be displayed. If the error is displayed the function
    returns False other wise the function returns True.
    """
    try:
        x = float(x)
        return True
    except:
        messagebox.showerror("error", errorMessage["type"])
        return False


def formatValidation(x):
    """ This function takes in a float value and checks that it is in correct
    money format with a decimal and 2 digits thereafter. If the error is displayed
    the function returns False other wise the function returns True.
    """
    if "." not in x:
        messagebox.showerror("error", errorMessage["type"])
        return False
    elif len(x.rsplit('.')[-1]) != 2:
        messagebox.showerror("error", errorMessage["type"])
        return False
    else:
        return True

def boundaryValidation(x):
    """ This function takes in a float value and displays an error if the value
    is less than 0 or more than 1,000,000. If the error is displayed the function
    returns False other wise the function returns True.
    """
    x = float(x)
    if x < 0 or x >= 100000000:
        messagebox.showerror("error", errorMessage["boundary"])
        return False
    else:
        return True

def dropValidation(x, y):
    """ This function will display an error and return False if the same selection
    is made in both dropdown menus, otherwise it returns True.
    """
    if x == y:
        messagebox.showerror("error", errorMessage["currency"])
        return False
    else:
        return True


#I---------------API function------------I
def findRate(baseCurrency, targetCurrency):
    """ This function takes in two float values baseCurrency and targetCurrency,
    requests the appropriate exchange rate from the exchange rate API and returns
    that as a float value  """
    #key = eb97e3e5c1cceee13f6ea5e7
    #url = 'https://v6.exchangerate-api.com/v6/eb97e3e5c1cceee13f6ea5e7/pair/EUR/GBP'

    #building the URL
    currencyFormat = baseCurrency + '/' + targetCurrency
    url = 'https://v6.exchangerate-api.com/v6/eb97e3e5c1cceee13f6ea5e7/pair/' + currencyFormat

    # Making a request
    response = requests.get(url)
    data = response.json()

    # JSON object
    rate = (data['conversion_rate'])
    return rate

# I-----------Button command functions-------------I
def clear():
    """ Clears all inputs and outputs from the GUI
    """
    orig["text"] = " "
    calc["text"] = " "
    amountE.delete(0, END)


# main conversion function
def convert():
    """This function will call validate to varify all inputs are as expected,
    collect the inputted amount to convert and call findRate to retrieve the
    conversion rate from the API. It then performs the conversion and displays
    the origional amount and conversion as label outputs to the user.
    """
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
        orig["text"] = "Original amount: " + currencyFrom + str(amount)
        calc["text"] = "Calculation: " + currencyTo + str(conversion)


#################################################
#I----------lists and dictionaries--------------I

currency = {
    "GBP" : "£",
    "EUR" : "€",
    "JPY" : "¥",
    "USD" : "$",
    "AUD" : "$",
    "CAD" : "$",
    "CHF" : "",
    "CNY" : "¥",
    "HKD" : "$",
    "NZD" : "$"
}

#flags =["", ""]

errorMessage = {
    "presence":   "Fields cannot be left blank",
    "type":       "Amount to convert must be a number with two decimal places, eg. 10.60.",
    "boundary":   "Amount to convert must be larger than 0.00 and smaller than 1000000.00.",
    "exchange":   "Exchange rate must be a number larger than 0",
    "currency":   "Currency error. Currency to convert to must be different to the base currency"
}


###############################################
#I----------------GUI Set-up------------------I
root = Tk()
root.title("Currency Converter Calculator")
root.geometry("600x300")
root.configure(bg = "gray18")
frame = Frame(root)
frame.columnconfigure(0, weight=1)
frame.rowconfigure(0, weight=1)
frame.configure(bg = "gray18")
frame.place(relx = 0.5, rely = 0.5, anchor = CENTER)
output = Frame(frame)
output.configure(bg = "slateblue3", borderwidth = 2, padx= 0, pady = 20, relief="ridge")

#I-----------------Gui widgets---------------I

#input fields
amountE = Entry(frame, width = 10,
                      bg = "gray25",
                      fg = "snow",
                      font = ("Helvetica Neue", 22))

#dropdown menus
drop1 = StringVar()
drop1.set(list(currency)[0])
currencydrop1 = OptionMenu(frame, drop1, *currency,) #command = symbolSelect)
currencydrop1.configure(bg = "gray25",
                        fg = "snow",
                        height = 1,
                        font = ("Helvetica Neue", 22))

drop2 = StringVar()
drop2.set(list(currency)[1])
currencydrop2 = OptionMenu(frame, drop2, *currency,) #command = symbolSelect)
currencydrop2.configure(bg = "gray25",
                        fg = "snow",
                        height = 1,
                        font = ("Helvetica Neue", 22))

# Labels
orig = Label(output, bg = "slateblue3",
                    fg = "snow",
                    font = ("Helvetica Neue", 20))


calc = Label(output, bg = "slateblue3",
                    fg = "gray25",
                    font = ("Helvetica Neue", 28))


toLabel = Label(frame, text = "to",
                      bg = "gray18",
                      fg = "snow",
                      font = ("Helvetica Neue", 22))


#Buttons
convertImage = PhotoImage(file = "images/Btn_Convert.png")
convertButton = Button(frame, bg = "gray18",
                              image = convertImage,
                              borderwidth = 0,
                              command = convert)

clearImage = PhotoImage(file = "images/Btn_Clear.png")
clearButton = Button(frame, image = clearImage,
                            bg = "gray18",
                            borderwidth = 0,
                            command = clear)

closeImage = PhotoImage(file = "images/Btn_Close.png")
closeButton = Button(frame, image = closeImage,
                            bg = "gray18",
                            borderwidth = 0,
                            command = root.quit)



#I---------------GUI grid layout----------------I

amountE.grid(row = 0, column = 0)
currencydrop1.grid(row = 0, column = 1, padx = 10)
toLabel.grid(row = 0, column = 2, padx = 10, )
currencydrop2.grid(row = 0, column = 3)

output.grid(row = 1, column = 0, columnspan = 4, sticky = 'nsew', pady = 20)
orig.pack()
calc.pack()


clearButton.grid(row = 3, column = 0, padx = 5)
convertButton.grid(row = 3, column = 1, columnspan = 2)
closeButton.grid(row = 3, column = 3, padx = 5)


root.mainloop()
