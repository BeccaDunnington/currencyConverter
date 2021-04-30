from tkinter import *
from tkinter import messagebox
from PIL import ImageTk, Image

root = Tk()
root.title("Currency Converter Calculator")
root.geometry("500x350")
root.configure(bg = "gray18")

#I--------------functions----------------I

#I---------Validation functions----------I

def validate():
# main validation function does all validation checks one after the other
# returning if one error is triggered to stop multiple errorboxes displaying
# at once or the convert function going ahead.
    #retrieve what is entered in the fields
    amount = amountE.get()
    rate = rateE.get()

    #validation
    if presenceValidation(amount, rate) == True:
        if typeValidation(amount) == True:
            if rateValidation(rate) == True:
                if formatValidation(amount) == True:
                    if boundaryValidation(amount) == True:
                        return True

#I------other validation functions-------I
def presenceValidation(x, y):
    if not len(x) or not len(y) > 0:
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


def rateValidation(y):
    try:
        y = float(y)
        if y > 0:
            return True
        else:
            messagebox.showerror("error", errorMessage["exchange"])
            return False
    except:
        messagebox.showerror("error", errorMessage["exchange"])
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
def symbolSelect():
    #retrieve what is entered in the fields
    currencyFrom = drop1.get()
    currencyTo = drop2.get()

# main conversion function -- NOT WORKING YET
def convert():
    if validate() == True:
        #casting strings to floats
        amount = float(amountE.get())
        rate = float(rateE.get())
        #calculate the currency conversion
        conversion = amount*rate
        #format the outputs to 2 decimal places
        amount = "{:.2f}".format(amount)
        conversion = "{:.2f}".format(conversion)
        #display the result
        calc["text"] = "Original amount: " + str(amount) + " \n Here be the calculation! " + str(conversion)





#I----------lists and dictionaries--------------I
symbols = ["£", "€", "¥", "$"]
currency = ["GBP", "EUR", "JPY", "USD"]
flags =["", ""]
errorMessage = {
  "presence":   "Fields cannot be left blank",
  "type":       "Amount to convert must be a number with two decimal places, eg. 10.60.",
  "boundary":   "Amount to convert must be larger than 0.00 and smaller than 1000000.00.",
  "exchange":   "Exchange rate must be a number larger than 0"
}




#I-----------------Gui widgets---------------I

#input fields
amountE = Entry(root, width = 10,
                      bg = "gray25",
                      fg = "snow",
                      font = ("Helvetica Neue", 22))

rateE = Entry(root, width = 10,
                    bg = "gray25",
                    fg = "snow",
                    font = ("Helvetica Neue", 22))

#dropdown menus
drop1 = StringVar()
drop1.set(currency[0])
currencydrop1 = OptionMenu(root, drop1, *currency)
currencydrop1.configure(bg = "gray25",
                        fg = "snow",
                        font = ("Helvetica Neue", 22))

drop2 = StringVar()
drop2.set(currency[1])
currencydrop2 = OptionMenu(root, drop2, *currency)
currencydrop2.configure(bg = "gray25",
                        fg = "snow",
                        font = ("Helvetica Neue", 22))

# Labels
calc = Label(root, bg = "slateblue3",
                    fg = "snow",
                    font = ("Helvetica Neue", 22))
calc.configure(borderwidth = 2, height = 4, width = 30, relief="ridge")


rateLabel = Label(root, text = "Rate",
                        bg = "gray18",
                        fg = "snow",
                        padx = 40,
                        pady = 20,
                        font = ("Helvetica Neue", 22))

toLabel = Label(root, text = "to",
                      bg = "gray18",
                      fg = "snow",
                      padx = 10,
                      pady = 10,
                      font = ("Helvetica Neue", 22))


#Buttons
convertButton = Button(root, text = "Convert",
                             bg = "snow",
                             fg = "gray18",
                             font = ("Helvetica Neue", 22),
                             padx = 20,
                             pady = 10,
                             command = convert)


clearButton = Button(root, text = "Clear",
                           bg = "snow",
                           fg = "gray18",
                           font = ("Helvetica Neue", 22),
                           padx = 20,
                           pady = 10,
                           command = clear)


closeButton = Button(root, text = "Close",
                           bg = "snow",
                           fg = "gray18",
                           font = ("Helvetica Neue", 22),
                           padx = 20,
                           pady = 10,
                           command = root.quit)



#I---------------GUI grid layout----------------I

amountE.grid(row = 0,column = 0)
currencydrop1.grid(row = 0,column = 1)
toLabel.grid(row = 0,column = 2)
currencydrop2.grid(row = 0,column = 3)

rateLabel.grid(row = 1,column = 0)
rateE.grid(row = 1,column = 1)
convertButton.grid(row = 1,column = 2, columnspan = 2)

calc.grid(row = 2,column = 0, columnspan = 4)

clearButton.grid(row = 3,column = 0)
closeButton.grid(row = 3,column = 2)


root.mainloop()
