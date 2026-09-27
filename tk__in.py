from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from validation import *

person_list = []


def age_validator(param):
    pass


def save_click():
    try:
        person = {
            "name":name.get(),
            "family":family.get(),
            "age":age_validator(age.get()),
            "city":city.get(),
            "phone":phone_validator(phone.get())
        }
        person_list.append(person)


        messagebox.showinfo("save","person saved")
        name.set(" ")
        family.set(" ")
        age.set("0")
        city.set("Tabriz")
    except Exception as e:
        messagebox.showerror("save Error" , f"Error {e}")


window = Tk()

window.title("Profile")
window.geometry("600x400")

# Name
Label(window, text = "Name").place(x =20, y =20)
name = StringVar()
Entry(window,textvariable=name).place(x =90 , y =20)

# Family
Label(window , text = "Family").place(x =20 , y =60)
family = StringVar()
Entry(window, textvariable=family).place(x=90 , y =60)

# Age
Label(window, text = "Age").place (x =20 , y =100)
age = IntVar()
Entry(window, textvariable=age).place(x=90 , y=100)

# City
Label(window, text = "City").place(x=20, y= 140)
city = StringVar(value="Shiraz")
ttk.Combobox(window , values=["Shiraz","Tabriz","Tehran","Isfahan"],textvariable=city,
state="readonly").place(x=90, y=140, width=125)
        
 #phone
Label(window, text = "Phone").place(x=20 , y=180)
phone = StringVar()
Entry(window, textvariable=phone).place(x=90 , y=180)
        
        
Button(window, text="save",
command=save_click).place(x=300, y=300 , width=80)
window.mainloop()
        
        

