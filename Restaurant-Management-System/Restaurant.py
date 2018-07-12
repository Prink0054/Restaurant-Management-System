from tkinter import *
import random
import time
import sqlite3
root =Tk()
root.geometry("1600x800+0+0")
root.title("Restaurent Management System")

text_Input = StringVar()
operator = ""

Tops = Frame(root,width = 1600,height = 50, relief = SUNKEN)
Tops.pack(side = TOP)

f1 = Frame(root,width = 800,height = 700, relief = SUNKEN)
f1.pack(side = LEFT)

f2 = Frame(root,width = 300,height = 700, relief = SUNKEN)
f2.pack(side = RIGHT)

lblInfo = Label(Tops,font =('arial',50,'bold'),text = "Restaurant Management Systems",fg = "Steel Blue",bd = 10,anchor = 'w')
lblInfo.grid(row = 0,column = 0)

# ======================TIME====================================
localtime = time.asctime(time.localtime(time.time()))

# ======================Info==========================================================================
lblInfo = Label(Tops,font =('arial',20,'bold'),text = localtime,fg = "Steel Blue",bd = 10,anchor = 'w')
lblInfo.grid(row = 1,column = 0)

# ====================================CALCULATOR===================================================

def btnClick(numbers):
    global operator
    operator = operator + str(numbers)
    text_Input.set(operator)

def btnClearDsiplay():
    global operator
    operator = ""
    text_Input.set(operator)


def btnEqualsInput():
    global operator
    sumup = str(eval(operator))
    text_Input.set(sumup)
    operator = ""




def qexit():
    root.destroy()


def reset():
    rand.set("")
    Fries.set("")
    Pizzameal.set("")
    Burger.set("")
    Lunchmeal.set("")
    Subtotal.set("")
    Total.set("")
    Service_Charge.set("")
    Drinks.set("")
    Tax.set("")
    cost.set("")
    print("<<<<<<<<<<<<<<<<<<<<<",cost)
    Cheese_burger.set("")
    


def Ref():

    x=random.randint(12980, 50876)
    randomRef = str(x)
    rand.set(randomRef)
    if (Fries.get() == ""):
         cof = "0"
    else:
         cof = float(Fries.get())

    if (Lunchmeal.get() == ""):
        colfries = "0"

    else:
        colfries = float(Lunchmeal.get())

    if (Burger.get() == ""):

        cob = "0"
    else:
        cob = float(Burger.get())
    if (Pizzameal.get() == ""):
        cofi = "0"

    else:
        cofi = float(Pizzameal.get())
    if (Cheese_burger.get() == ""):
        cochee = "0"

    else:
        cochee = float(Cheese_burger.get())
    if (Drinks.get() == ""):
        codr = "0"
        
    else:
        codr = float(Drinks.get())


    costoffries = float(cof*25)
    costoflunchmeal = float(colfries*40)
    costofburger = float(cob*35)
    costofpizzameal = float(cofi*50)
    costofcheeseburger = float(cochee*50)
    costofdrinks = float(codr*35)

    costofmeal =  "Rs " + str('%.2f'% (costoffries +   costoflunchmeal + costofburger + costofpizzameal + costofcheeseburger + costofdrinks))
    PayTax=((costoffries +   costoflunchmeal + costofburger + costofpizzameal +  costofcheeseburger + costofdrinks)*0.33)
    Totalcost=(costoffries +   costoflunchmeal + costofburger + costofpizzameal  + costofcheeseburger + costofdrinks)
    Ser_Charge=((costoffries +  costoflunchmeal + costofburger + costofpizzameal + costofcheeseburger + costofdrinks)/99)
    Service="Rs." + str('%.2f'% Ser_Charge)
    OverAllCost="Rs." + str( PayTax + Totalcost + Ser_Charge)
    PaidTax="Rs." + str('%.2f'% PayTax)

    Service_Charge.set(Service)
    cost.set(costofmeal)
    Tax.set(PaidTax)
    Subtotal.set(costofmeal)
    Total.set(OverAllCost)



txtDisplay = Entry(f2,font =('arial',20,'bold'),textvariable = text_Input ,bd = 30,insertwidth=4,bg = "powder blue",justify = 'right')
txtDisplay.grid(columnspan=4)

btn7 = Button(f2,padx=16,pady = 16,bd = 8,fg = 'black',font = ('arial',20,'bold'),text = "7",bg = "powder blue",command = lambda :btnClick(7)).grid(row = 2,column = 0)

btn8 = Button(f2,padx=16,pady = 16,bd = 8,fg = 'black',font = ('arial',20,'bold'),text = "8",bg = "powder blue",command = lambda :btnClick(8)).grid(row = 2,column = 1)

btn9 = Button(f2,padx=16,pady = 16,bd = 8,fg = 'black',font = ('arial',20,'bold'),text = "9",bg = "powder blue",command = lambda :btnClick(9)).grid(row = 2,column = 2)

Addition = Button(f2,padx=16,pady = 16,bd = 8,fg = 'black',font = ('arial',20,'bold'),text = "+",bg = "powder blue",command = lambda :btnClick('+')).grid(row = 2,column = 3)

# ====================================================================================================

btn4 = Button(f2,padx=16,pady = 16,bd = 8,fg = 'black',font = ('arial',20,'bold'),text = "4",bg = "powder blue",command = lambda :btnClick(4)).grid(row = 3,column = 0)

btn5 = Button(f2,padx=16,pady = 16,bd = 8,fg = 'black',font = ('arial',20,'bold'),text = "5",bg = "powder blue",command = lambda :btnClick(5)).grid(row = 3,column = 1)

btn6 = Button(f2,padx=16,pady = 16,bd = 8,fg = 'black',font = ('arial',20,'bold'),text = "6",bg = "powder blue",command = lambda :btnClick(6)).grid(row = 3,column = 2)

Subtraction = Button(f2,padx=16,pady = 16,bd = 8,fg = 'black',font = ('arial',20,'bold'),text = "-",bg = "powder blue",command =  lambda :btnClick('-')).grid(row = 3,column = 3)

# ====================================================================================================

btn1 = Button(f2,padx=16,pady = 16,bd = 8,fg = 'black',font = ('arial',20,'bold'),text = "1",bg = "powder blue",command = lambda :btnClick(1)).grid(row = 4,column = 0)

btn2 = Button(f2,padx=16,pady = 16,bd = 8,fg = 'black',font = ('arial',20,'bold'),text = "2",bg = "powder blue",command = lambda :btnClick(2)).grid(row = 4,column = 1)

btn3 = Button(f2,padx=16,pady = 16,bd = 8,fg = 'black',font = ('arial',20,'bold'),text = "3",bg = "powder blue",command = lambda :btnClick(3)).grid(row = 4,column = 2)

Multiply = Button(f2,padx=16,pady = 16,bd = 8,fg = 'black',font = ('arial',20,'bold'),text = "*",bg = "powder blue",command =  lambda :btnClick('*')).grid(row = 4,column = 3)

# ====================================================================================================

btn0=Button(f2,padx=16,pady=16,bd=8, fg="black", font=('ariel', 20 ,'bold'),text="0",bg="powder blue", command=lambda: btnClick(0) )
btn0.grid(row=5,column=0)

btnc=Button(f2,padx=16,pady=16,bd=8, fg="black", font=('ariel', 20 ,'bold'),text="c",bg="powder blue",command = lambda :btnClearDsiplay())
btnc.grid(row=5,column  =1)

btnequal=Button(f2,padx=16,pady=16,bd=8, fg="black", font=('ariel', 20 ,'bold'),text="=",bg="powder blue",command = lambda :btnEqualsInput())
btnequal.grid(row=5,column  =2)

Division=Button(f2,padx=16,pady=16,bd=8, fg="black", font=('ariel', 20 ,'bold'),text="/",bg="powder blue", command=lambda: btnClick("/") )
Division.grid(row=5,column=3)
# status = Label(f2,font=('aria', 15, 'bold'),width = 16, text="-By Amar Kumar",bd=2,relief=SUNKEN)
# status.grid(row=7,columnspan=3)

# ====================================================================================================
rand = StringVar()
Fries = StringVar()
Burger = StringVar()
Pizzameal = StringVar()
Subtotal = StringVar()
Total = StringVar()
Service_Charge = StringVar()
Drinks = StringVar()
Tax = StringVar()
Lunchmeal = StringVar()
cost = StringVar()
Cheese_burger = StringVar()
lblReference = Label(f1, font=( 'aria' ,16, 'bold' ),text="Order No.",fg="steel blue",bd=10,anchor='w')
lblReference.grid(row=0, column=0)
txtReference = Entry(f1,font=('ariel' ,16,'bold'), textvariable=rand , bd=6,insertwidth=4,bg="powder blue" ,justify='right')
txtReference.grid(row=0,column=1)

lblfries = Label(f1, font=( 'aria' ,16, 'bold' ),text="Fries Meal",fg="steel blue",bd=10,anchor='w')
lblfries.grid(row=1,column=0)


txtfries = Entry(f1,font=('ariel' ,16,'bold'), textvariable=Fries , bd=6,insertwidth=4,bg="powder blue" ,justify='right')
txtfries.grid(row=1,column=1)


lblLunchmeal = Label(f1, font=( 'aria' ,16, 'bold' ),text="Lunch Meal",fg="steel blue",bd=10,anchor='w')
lblLunchmeal.grid(row=2,column=0)
txtLunchmeal = Entry(f1,font=('ariel' ,16,'bold'), textvariable=Lunchmeal , bd=6,insertwidth=4,bg="powder blue" ,justify='right')
txtLunchmeal.grid(row=2,column=1)



lblburger = Label(f1, font=( 'aria' ,16, 'bold' ),text="Burger Meal",fg="steel blue",bd=10,anchor='w')
lblburger.grid(row=3,column=0)
txtburger = Entry(f1,font=('ariel' ,16,'bold'), textvariable=Burger, bd=6,insertwidth=4,bg="powder blue" ,justify='right')
txtburger.grid(row=3,column=1)

lblPizzameal = Label(f1, font=( 'aria' ,16, 'bold' ),text="Pizza Meal",fg="steel blue",bd=10,anchor='w')
lblPizzameal.grid(row=4,column=0)
txtPizzameal = Entry(f1,font=('ariel' ,16,'bold'), textvariable=Pizzameal , bd=6,insertwidth=4,bg="powder blue" ,justify='right')
txtPizzameal.grid(row=4,column=1)

lblCheese_burger = Label(f1, font=( 'aria' ,16, 'bold' ),text="Cheese burger",fg="steel blue",bd=10,anchor='w')
lblCheese_burger.grid(row=5,column=0)
txtCheese_burger = Entry(f1,font=('ariel' ,16,'bold'), textvariable=Cheese_burger , bd=6,insertwidth=4,bg="powder blue" ,justify='right')
txtCheese_burger.grid(row=5,column=1)

#--------------------------------------------------------------------------------------
lblDrinks = Label(f1, font=( 'aria' ,16, 'bold' ),text="Drinks",fg="steel blue",bd=10,anchor='w')
lblDrinks.grid(row=0,column=2)
txtDrinks = Entry(f1,font=('ariel' ,16,'bold'), textvariable=Drinks , bd=6,insertwidth=4,bg="powder blue" ,justify='right')
txtDrinks.grid(row=0,column=3)

lblcost = Label(f1, font=( 'aria' ,16, 'bold' ),text="cost",fg="steel blue",bd=10,anchor='w')
lblcost.grid(row=1,column=2)
txtcost = Entry(f1,font=('ariel' ,16,'bold'), textvariable=cost , bd=6,insertwidth=4,bg="powder blue" ,justify='right')
txtcost.grid(row=1,column=3)

lblService_Charge = Label(f1, font=( 'aria' ,16, 'bold' ),text="Service Charge",fg="steel blue",bd=10,anchor='w')
lblService_Charge.grid(row=2,column=2)
txtService_Charge = Entry(f1,font=('ariel' ,16,'bold'), textvariable=Service_Charge , bd=6,insertwidth=4,bg="powder blue" ,justify='right')
txtService_Charge.grid(row=2,column=3)

lblTax = Label(f1, font=( 'aria' ,16, 'bold' ),text="Tax",fg="steel blue",bd=10,anchor='w')
lblTax.grid(row=3,column=2)
txtTax = Entry(f1,font=('ariel' ,16,'bold'), textvariable=Tax , bd=6,insertwidth=4,bg="powder blue" ,justify='right')
txtTax.grid(row=3,column=3)

lblSubtotal = Label(f1, font=( 'aria' ,16, 'bold' ),text="Subtotal",fg="steel blue",bd=10,anchor='w')
lblSubtotal.grid(row=4,column=2)
txtSubtotal = Entry(f1,font=('ariel' ,16,'bold'), textvariable=Subtotal , bd=6,insertwidth=4,bg="powder blue" ,justify='right')
txtSubtotal.grid(row=4,column=3)

lblTotal = Label(f1, font=( 'aria' ,16, 'bold' ),text="Total",fg="steel blue",bd=10,anchor='w')
lblTotal.grid(row=5,column=2)
txtTotal = Entry(f1,font=('ariel' ,16,'bold'), textvariable=Total , bd=6,insertwidth=4,bg="powder blue" ,justify='right')
txtTotal.grid(row=5,column=3)


#-----------------------------------------buttons------------------------------------------
lblTotal = Label(f1,text="---------------------",fg="white")
lblTotal.grid(row=6,columnspan=3)

btnTotal=Button(f1,padx=16,pady=8, bd=10 ,fg="black",font=('ariel' ,16,'bold'),width=10, text="TOTAL", bg="powder blue",command = lambda :Ref())
btnTotal.grid(row=7, column=1)

btnreset=Button(f1,padx=16,pady=8, bd=10 ,fg="black",font=('ariel' ,16,'bold'),width=10, text="RESET", bg="powder blue",command = lambda :reset())
btnreset.grid(row=7, column=3)
btnexit=Button(f1,padx=16,pady=8, bd=10 ,fg="black",font=('ariel' ,16,'bold'),width=10, text="EXIT", bg="powder blue",command = lambda :qexit())
btnexit.grid(row=7, column=4)

btnprint=Button(f1,padx=16,pady=8, bd=10 ,fg="black",font=('ariel' ,16,'bold'),width=10, text="PRINT", bg="powder blue",command = lambda :Database())
btnprint.grid(row=7, column=2)

def price():
    roo = Tk()
    roo.geometry("600x220+0+0")
    roo.title("Price List")
    lblinfo = Label(roo, font=('aria', 15, 'bold'), text="ITEM", fg="black", bd=5)
    lblinfo.grid(row=0, column=0)
    lblinfo = Label(roo, font=('aria', 15,'bold'), text="_____________", fg="white", anchor=W)
    lblinfo.grid(row=0, column=2)
    lblinfo = Label(roo, font=('aria', 15, 'bold'), text="PRICE", fg="black", anchor=W)
    lblinfo.grid(row=0, column=3)
    lblinfo = Label(roo, font=('aria', 15, 'bold'), text="Fries Meal", fg="steel blue", anchor=W)
    lblinfo.grid(row=1, column=0)
    lblinfo = Label(roo, font=('aria', 15, 'bold'), text="25", fg="steel blue", anchor=W)
    lblinfo.grid(row=1, column=3)
    lblinfo = Label(roo, font=('aria', 15, 'bold'), text="Lunch Meal", fg="steel blue", anchor=W)
    lblinfo.grid(row=2, column=0)
    lblinfo = Label(roo, font=('aria', 15, 'bold'), text="40", fg="steel blue", anchor=W)
    lblinfo.grid(row=2, column=3)
    lblinfo = Label(roo, font=('aria', 15, 'bold'), text="Burger Meal", fg="steel blue", anchor=W)
    lblinfo.grid(row=3, column=0)
    lblinfo = Label(roo, font=('aria', 15, 'bold'), text="35", fg="steel blue", anchor=W)
    lblinfo.grid(row=3, column=3)
    lblinfo = Label(roo, font=('aria', 15, 'bold'), text="Pizza Meal", fg="steel blue", anchor=W)
    lblinfo.grid(row=4, column=0)
    lblinfo = Label(roo, font=('aria', 15, 'bold'), text="50", fg="steel blue", anchor=W)
    lblinfo.grid(row=4, column=3)
    lblinfo = Label(roo, font=('aria', 15, 'bold'), text="Cheese Burger", fg="steel blue", anchor=W)
    lblinfo.grid(row=5, column=0)
    lblinfo = Label(roo, font=('aria', 15, 'bold'), text="30", fg="steel blue", anchor=W)
    lblinfo.grid(row=5, column=3)
    lblinfo = Label(roo, font=('aria', 15, 'bold'), text="Drinks", fg="steel blue", anchor=W)
    lblinfo.grid(row=6, column=0)
    lblinfo = Label(roo, font=('aria', 15, 'bold'), text="35", fg="steel blue", anchor=W)
    lblinfo.grid(row=6, column=3)

    roo.mainloop()

btnprice=Button(f1,padx=16,pady=8, bd=10 ,fg="black",font=('ariel' ,16,'bold'),width=10, text="PRICE", bg="powder blue",command=price)
btnprice.grid(row=7, column=0)


#=========================================DataBase=================================================

def Database():
    conn = sqlite3.connect('receipt.db')
    print("Opened Database successfully")


    conn.execute("INSERT INTO Data VALUES(?,?,?,?,?,?,?,?,?,?,?,?);",(rand.get(),Fries.get(),Lunchmeal.get(),Burger.get(),Pizzameal.get(),Cheese_burger.get(),Drinks.get(),cost.get(),Service_Charge.get(),Tax.get(),Subtotal.get(),Total.get()))

    print("inserted")
    print()

    cursor = conn.execute("SELECT ORDER_NO,FRIES_MEAL,LUNCH_MEAL, BURGER_MEAL,PIZZA_MEAL,  CHEESE_BURGER, DRINKS,COST, SERVICE_CHARGE,TAX,SUBTOTAL, TOTAL from Data")
    for row in cursor:
        print("ORDER_NO = ", row[0])
        print("FRIES_MEAL = ", row[1])
        print("LUNCH_MEAL = ", row[2])
        print("BURGER_MEAL = ", row[3])
        print("PIZZA_MEAL = " , row[4])
        print("CHEESE_BURGER = ", row[5])
        print("DRINKS = " , row[6])
        print("COST = ", row[7])
        print("SERVICE_CHARGE = ", row[8])
        print("TAX = ", row[9])
        print("SUBTOTAL = ", row[10])
        print("TOTAL = ", row[11], "\n")





root.mainloop()
