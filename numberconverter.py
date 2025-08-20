##Each Section inside the UI code begin with Start and ends with End 

import tkinter as tk
from tkinter import ttk
import APU                                                      # import module / converter
from PIL import Image, ImageTk 
import os , sys
from enum import Enum
import updatechecker
import threading

##universal file finder
def resource_path(relative_path):
    """ Get absolute path to resource, works for dev and for PyInstaller exe """
    if hasattr(sys, '_MEIPASS'):  # running in exe
        return os.path.join(sys._MEIPASS, relative_path)
    return os.path.join(os.path.abspath("."), relative_path)

##enum
class unit(Enum):
    decimal = 1
    hexa = 2
    binary =3

currentunit = 0

fromsel = "Hex"
tosel   = "Hex"
root = tk.Tk()

root.title("Number Converter")
#root.geometry("450x370")
root.geometry("470x550")
root.configure(bg="grey")

##notebook
notebook = ttk.Notebook(root)
notebook.grid(row=0, column=0, sticky="nsew")  
root.grid_rowconfigure(0, weight=2)
root.grid_columnconfigure(0, weight=2)

tab1 = tk.Frame(notebook, bg="grey")
tab2 = tk.Frame(notebook, bg="#CCE5FF")
tab3 = tk.Frame(notebook, bg="#CCCCFF")
tab4 = tk.Frame(notebook, bg="#CCCCFF")

notebook.add(tab1, text="Converter")
notebook.add(tab2, text="Patch Notes")
notebook.add(tab3, text="Help")
notebook.add(tab4, text="Update")
##notebook end

counter = tk.IntVar(value=0)
y = 0
hexflag = 0
decflag = 0
reset = 0

def inc():
    counter.set(counter.get() + 1)
    
#Selection From Start
selected_var = tk.StringVar()
items=["Hex","Dec","Bin"]
selection_label = tk.Label(tab1, text="From", font=("Arial", 12))
selection_label.grid(row=0,column=6,columnspan=2,padx=8,pady=10)
combo = ttk.Combobox(tab1, values=items, textvariable=selected_var, state="readonly")
combo.current(0)
combo.grid(row=1,column=6,columnspan=2,pady=5)
#Selection From End

#Selection To Start
selected_tovar = tk.StringVar()
selection_to = tk.Label(tab1, text="To", font=("Arial", 12))
selection_to.grid(row=0,column=15,columnspan=2,pady=10)
comboto = ttk.Combobox(tab1, values=items,textvariable = selected_tovar, state="readonly")
comboto.current(0)
def eventselectionTo(event):                                           #Event Handler Function
    selected_option2 = comboto.get()                                   #To get value
    #print("you selected : " , selected_option2)
comboto.bind("<<ComboboxSelected>>", eventselectionTo)                 #Event Call
comboto.grid(row=1,column=15,columnspan=2,pady=5)
#Selection To End


#Enter Number Start
tk.Label(tab1, text="Enter Number:").grid(row=3, column=12, padx=8, pady=8)
entry = tk.Entry(tab1)
entry.grid(row=4, column=12, columnspan=2, pady=15)
#valuepad = 0
decpad=0

def total():
    global hexflag
    global hexbefore
    global decflag
    global decbefore
    #print(selected_var.get())
    tk.Label(tab1, text="                            ",bg="grey", font=("Arial", 8)).grid(row=3,column=6,columnspan=2,pady=10)
    tk.Label(tab1, text="              ",bg="grey", font=("Arial", 8)).grid(row=4,column=6,columnspan=2,pady=10)
    tk.Label(tab1, text="                            ",bg="grey", font=("Arial", 8)).grid(row=3,column=15,columnspan=2,pady=10)
    tk.Label(tab1, text="              ",bg="grey", font=("Arial", 8)).grid(row=4,column=15,columnspan=2,pady=10)
    global valuepad
    global reset
    global decpad
    global currentunit
    print("reset: ", reset)
    print("hexflag: ",hexflag)
    display2hex = tk.Label(tab1, text=" ", font=("Arial", 12))
    display2hex.grid(row=11, column=12, columnspan=2, pady=10)
    display2dec = tk.Label(tab1, text=" ", font=("Arial", 12))
    display2dec.grid(row=14, column=12, columnspan=2, pady=10)
    reset = 1
    if selected_var.get()=="Hex" and selected_tovar.get()== "Bin":
        #print("hex to binary")
        currentunit = unit.binary
        display2dec = tk.Label(tab1, text=" ", font=("Arial", 12))
        display2dec.grid(row=14, column=12, columnspan=2, pady=10)
        display2hex
        display2hex.config(text=f"            ")
        display2hex.tkraise()
        valueaf = APU.hex_to_bin(entry.get())
        decpad = f"{int(valueaf, 2):016b}" 
        if valueaf != "Error":
            display_label.config(text=f"{valueaf}",fg="black")
            if decflag == 1:
                display2dec.config(text=decpad)
                display2dec.tkraise()
            
        else:
            display_label.config(text=f"Illegal Input",fg="red")
    elif selected_var.get()=="Hex" and selected_tovar.get()== "Dec":
        #print("hex to dec")
        currentunit = unit.decimal
        display2hex.config(text=f"            ")
        display2hex.tkraise()
        display2dec.config(text=f"                                         ")
        display2dec.tkraise()
        valueaf = APU.hex_to_dec(entry.get())
        if valueaf != "Error":
            #print(valueaf)
            display_label.config(text=f"{valueaf}",fg="black")
        else:
            display_label.config(text=f"Illegal Input",fg="red")
    elif selected_var.get()=="Dec" and selected_tovar.get()== "Bin":
        #print("Dec to Bin")
        currentunit = unit.binary
        display2dec = tk.Label(tab1, text=" ", font=("Arial", 12))
        display2dec.grid(row=14, column=12, columnspan=2, pady=10)  
        display2hex.config(text=f"            ")
        display2hex.tkraise()
        valueaf = APU.dec_to_bin(int(entry.get()))
        if valueaf != "Error":
            #print(valueaf)
            display_label.config(text=f"{valueaf}",fg="black")
            decpad = f"{int(valueaf, 2):016b}" 
            if decflag == 1:
                display2dec.config(text=decpad)
                display2dec.tkraise()
                
        else:
            display_label.config(text=f"Illegal Input",fg="red")
    elif selected_var.get()=="Dec" and selected_tovar.get()== "Hex":
        #print("Dec to Hex")
        currentunit = unit.hexa
        display2dec.config(text=f"                                         ")
        display2dec.tkraise()
        valueaf = APU.dec_to_hex((int(entry.get())))
        valuepad = f"0x{int(valueaf, 16):04X}"
        if valueaf != "Error":
            #print(valueaf)
            display_label.config(text=f"{valueaf}",fg="black")
            if hexflag == 1:
                display2hex.config(text=valuepad)
                display2hex.tkraise()
                
        else:
            display_label.config(text=f"Illegal Input",fg="red")
    elif selected_var.get()=="Bin" and selected_tovar.get()== "Hex":
        #print("Bin to Hex")
        currentunit = unit.hexa
        display2hex = tk.Label(tab1, text=" ", font=("Arial", 12))
        display2hex.grid(row=11, column=12, columnspan=2, pady=10)

        display2dec.config(text=f"                                         ")
        display2dec.tkraise()
        valueaf = APU.bin_to_hex((entry.get()))
        valuepad = f"0x{int(valueaf, 16):04X}"
        if valueaf != "Error":
            #print(valueaf)
            display_label.config(text=f"{valueaf}",fg="black")
            if hexflag == 1:
                display2hex.config(text=valuepad)
                display2hex.tkraise()
                
        else:
            display_label.config(text=f"Illegal Input",fg="red")
    elif selected_var.get()=="Bin" and selected_tovar.get()== "Dec":
        #print("Bin to Dec")
        currentunit = unit.decimal
        display2dec.config(text=f"                                         ")
        display2dec.tkraise()
        display2hex.config(text=f"            ")
        display2hex.tkraise()
        valueaf = APU.bin_to_dec((entry.get()))
        if valueaf != "Error":
            #print(valueaf)
            display_label.config(text=f"{valueaf}",fg="black")
        else:
            display_label.config(text=f"Illegal Input",fg="red")
    else:
        #print("error")
        tk.Label(tab1, text="Error, units must ",fg="red", font=("Arial", 8)).grid(row=3,column=6,columnspan=2,pady=10)
        tk.Label(tab1, text="be diff ",fg="red", font=("Arial", 8)).grid(row=4,column=6,columnspan=2,pady=10)
        tk.Label(tab1, text="Error, units must ",fg="red", font=("Arial", 8)).grid(row=3,column=15,columnspan=2,pady=10)
        tk.Label(tab1, text="be diff ",fg="red", font=("Arial", 8)).grid(row=4,column=15,columnspan=2,pady=10)
    
    
    #print(entry.get())

img_path = resource_path("images/arrow-removebg-preview.png")      # put your PNG file path here
img = Image.open(img_path)
img = img.resize((30, 30))              # resize if needed
patch_icon = ImageTk.PhotoImage(img)   
plusbutton = tk.Button(tab1, text="Convert", command=total,bg="#99FFFF" , image=patch_icon,compound="left")
plusbutton.grid(row=7, column=12, columnspan=2, pady=8)
#Enter Number End

#Checkbox start
tk.Label(tab1, text="4 digit hex: ", fg="grey").grid(row=10, column=12, padx=8, pady=8)
display2hex = tk.Label(tab1, text=" ", font=("Arial", 12))
display2hex.grid(row=11, column=12, columnspan=2, pady=10)

tk.Label(tab1, text="16 bit Binary: ", fg="grey").grid(row=13, column=12, padx=8, pady=8)
display2dec = tk.Label(tab1, text=" ", font=("Arial", 12))
display2dec.grid(row=14, column=12, columnspan=2, pady=10)
hexbefore=0
decbefore=0
def optionchecker():
    global reset
    global hexflag
    global hexbefore
    global decflag
    global decbefore
    global currentunit
    
    if hexbefore != hexflag:
        reset = 1
    else:
        reset = 0
    print("reset: ",reset)
    print("current unit: ", currentunit)
    if reset == 1:
        if hexcheck.get() == 1 and deccheck.get() == 1:  
            hexflag = 1
            decflag =1
            if currentunit == unit.hexa:
                tk.Label(tab1, text="4 digit hex: ").grid(row=10, column=12, padx=8, pady=8)
                tk.Label(tab1, text="16 bit Binary: ").grid(row=13, column=12, padx=8, pady=8)
                display2dec = tk.Label(tab1, text="                                         ", font=("Arial", 12))
            elif currentunit == unit.binary:
                tk.Label(tab1, text="4 digit hex: ").grid(row=10, column=12, padx=8, pady=8)
                display2hex = tk.Label(tab1, text="            ", font=("Arial", 12))
                tk.Label(tab1, text="16 bit Binary: ").grid(row=13, column=12, padx=8, pady=8)
            elif currentunit == unit.decimal:
                tk.Label(tab1, text="4 digit hex: ").grid(row=10, column=12, padx=8, pady=8)
                display2hex = tk.Label(tab1, text="            ", font=("Arial", 12))
                display2hex.grid(row=11, column=12, columnspan=2, pady=10)

                tk.Label(tab1, text="16 bit Binary: ").grid(row=13, column=12, padx=8, pady=8)
                display2dec = tk.Label(tab1, text="                                         ", font=("Arial", 12))
                display2dec.grid(row=14, column=12, columnspan=2, pady=10)
            
            hexbefore = hexflag
            decbefore = decflag
        elif hexcheck.get() == 0 and deccheck.get() ==0:
            hexflag = 0
            decflag = 0
            if currentunit != unit.decimal:
                tk.Label(tab1, text="4 digit hex: ", fg="grey").grid(row=10, column=12, padx=8, pady=8)
                display2hex = tk.Label(tab1, text="            ", font=("Arial", 12))
                display2hex.grid(row=11, column=12, columnspan=2, pady=10)

                tk.Label(tab1, text="16 bit Binary: ",fg="grey").grid(row=13, column=12, padx=8, pady=8)
                display2dec = tk.Label(tab1, text="                                         ", font=("Arial", 12))
                display2dec.grid(row=14, column=12, columnspan=2, pady=10)
                
            elif currentunit == unit.binary:
                tk.Label(tab1, text="16 bit Binary: ").grid(row=13, column=12, padx=8, pady=8)
                display2dec = tk.Label(tab1, text="", font=("Arial", 12))
                display2dec.grid(row=14, column=12, columnspan=2, pady=10)
                display2dec.config(text=decpad)

                tk.Label(tab1, text="16 bit Binary: ").grid(row=13, column=12, padx=8, pady=8)
                display2dec = tk.Label(tab1, text="", font=("Arial", 12))
                display2dec.grid(row=14, column=12, columnspan=2, pady=10)
                display2dec.config(text=decpad)
            hexbefore = hexflag
            decbefore = decflag
        elif hexcheck.get()==1 and deccheck.get()==0:
            hexflag=1
            decflag = 0
            if currentunit != unit.decimal:
                tk.Label(tab1, text="16 bit Binary: ",fg="grey").grid(row=13, column=12, padx=8, pady=8)
                display2dec = tk.Label(tab1, text="                                         ", font=("Arial", 12))
                display2dec.grid(row=14, column=12, columnspan=2, pady=10)

                ttk.Label(tab1, text="4 digit hex: ").grid(row=10, column=12, padx=8, pady=8)
            
            elif currentunit == unit.binary:
                tk.Label(tab1, text="16 bit Binary: ").grid(row=13, column=12, padx=8, pady=8)
                display2dec = tk.Label(tab1, text="", font=("Arial", 12))
                display2dec.grid(row=14, column=12, columnspan=2, pady=10)
                display2dec.config(text=decpad)

                tk.Label(tab1, text="4 digit hex: ").grid(row=13, column=12, padx=8, pady=8)
                display2dec = tk.Label(tab1, text="", font=("Arial", 12))
                display2dec.grid(row=14, column=12, columnspan=2, pady=10)
                display2dec.config(text=decpad)
            hexbefore=hexflag
            decbefore = decflag
        elif hexcheck.get()==0 and deccheck.get() ==1:
            hexflag=0
            decflag = 1
            if currentunit != unit.decimal:
                if currentunit == unit.binary:
                    tk.Label(tab1, text="16 bit Binary: ",fg="grey").grid(row=13, column=12, padx=8, pady=8)

                    tk.Label(tab1, text="4 digit hex: ", fg="grey").grid(row=10, column=12, padx=8, pady=8)
                    display2hex = tk.Label(tab1, text="            ", font=("Arial", 12))
                    display2hex.grid(row=11, column=12, columnspan=2, pady=10)
                    hexbefore=hexflag
                    decbefore = decflag
                elif currentunit == unit.hexa:
                    tk.Label(tab1, text="4 digit hex: ", fg="grey").grid(row=10, column=12, padx=8, pady=8)
                    display2hex = tk.Label(tab1, text="            ", font=("Arial", 12))
                    display2hex.grid(row=11, column=12, columnspan=2, pady=10)

                    tk.Label(tab1, text="16 bit Binary: ",fg="grey").grid(row=13, column=12, padx=8, pady=8)
                    display2dec = tk.Label(tab1, text="                                         ", font=("Arial", 12))
                    display2dec.grid(row=14, column=12, columnspan=2, pady=10)
            elif currentunit == unit.binary:
                tk.Label(tab1, text="16 bit Binary: ").grid(row=13, column=12, padx=8, pady=8)
                display2dec = tk.Label(tab1, text="", font=("Arial", 12))
                display2dec.grid(row=14, column=12, columnspan=2, pady=10)
                display2dec.config(text=decpad)

                tk.Label(tab1, text="16 bit Binary: ").grid(row=13, column=12, padx=8, pady=8)
                display2dec = tk.Label(tab1, text="", font=("Arial", 12))
                display2dec.grid(row=14, column=12, columnspan=2, pady=10)
                display2dec.config(text=decpad)
            hexbefore=hexflag
            decbefore = decflag

    elif reset == 0:
        if hexcheck.get() == 1 and deccheck.get() ==1:
            hexflag = 1
            decflag = 1
            if currentunit == unit.hexa:
                tk.Label(tab1, text="4 digit hex: ").grid(row=10, column=12, padx=8, pady=8)
                display2hex = tk.Label(tab1, text="", font=("Arial", 12))
                display2hex.grid(row=11, column=12, columnspan=2, pady=10)
                display2hex.config(text=valuepad)

                tk.Label(tab1, text="16 bit Binary: ").grid(row=13, column=12, padx=8, pady=8)
                display2dec = tk.Label(tab1, text="                                         ", font=("Arial", 12))
                display2dec.grid(row=14, column=12, columnspan=2, pady=10)
            elif currentunit == unit.binary:
                tk.Label(tab1, text="4 digit hex: ").grid(row=10, column=12, padx=8, pady=8)
                display2hex = tk.Label(tab1, text="            ", font=("Arial", 12))
                display2hex.grid(row=11, column=12, columnspan=2, pady=10)

                tk.Label(tab1, text="16 bit Binary: ").grid(row=13, column=12, padx=8, pady=8)
                display2dec = tk.Label(tab1, text="", font=("Arial", 12))
                display2dec.grid(row=14, column=12, columnspan=2, pady=10)
                display2dec.config(text=decpad)
            elif currentunit == unit.decimal:
                tk.Label(tab1, text="4 digit hex: ", fg="grey").grid(row=10, column=12, padx=8, pady=8)
                display2hex = tk.Label(tab1, text="            ", font=("Arial", 12))
                display2hex.grid(row=11, column=12, columnspan=2, pady=10)

                tk.Label(tab1, text="16 bit Binary: ",fg="grey").grid(row=13, column=12, padx=8, pady=8)
                display2dec = tk.Label(tab1, text="                                         ", font=("Arial", 12))
                display2dec.grid(row=14, column=12, columnspan=2, pady=10)
            
            hexbefore = hexflag
            decbefore = decflag
        elif hexcheck.get() == 0 and deccheck.get() == 0:
            hexflag = 0
            decflag = 0
            if currentunit != unit.decimal:
                tk.Label(tab1, text="4 digit hex: ", fg="grey").grid(row=10, column=12, padx=8, pady=8)
                display2hex = tk.Label(tab1, text="            ", font=("Arial", 12))
                display2hex.grid(row=11, column=12, columnspan=2, pady=10)

                tk.Label(tab1, text="16 bit Binary: ",fg="grey").grid(row=13, column=12, padx=8, pady=8)
                display2dec = tk.Label(tab1, text="                                         ", font=("Arial", 12))
                display2dec.grid(row=14, column=12, columnspan=2, pady=10)
                
            elif currentunit == unit.decimal:
                tk.Label(tab1, text="4 digit hex: ", fg="grey").grid(row=10, column=12, padx=8, pady=8)
                display2hex = tk.Label(tab1, text="            ", font=("Arial", 12))
                display2hex.grid(row=11, column=12, columnspan=2, pady=10)

                tk.Label(tab1, text="16 bit Binary: ",fg="grey").grid(row=13, column=12, padx=8, pady=8)
                display2dec = tk.Label(tab1, text="                                         ", font=("Arial", 12))
                display2dec.grid(row=14, column=12, columnspan=2, pady=10)
            hexbefore=hexflag
            decbefore = decflag
        elif hexcheck.get()==1 and deccheck.get()==0:
            hexflag=1
            decflag = 0
            if currentunit != unit.decimal:
                if currentunit == unit.hexa:
                    tk.Label(tab1, text="4 digit hex: ").grid(row=10, column=12, padx=8, pady=8)
                    display2hex = tk.Label(tab1, text="", font=("Arial", 12))
                    display2hex.grid(row=11, column=12, columnspan=2, pady=10)
                    display2hex.config(text=valuepad)

                    tk.Label(tab1, text="16 bit Binary: ",fg="grey").grid(row=13, column=12, padx=8, pady=8)
                    display2dec = tk.Label(tab1, text="                                         ", font=("Arial", 12))
                    display2dec.grid(row=14, column=12, columnspan=2, pady=10)
                    
                elif currentunit != unit.hexa:
                    tk.Label(tab1, text="4 digit hex: ").grid(row=10, column=12, padx=8, pady=8)
                    display2hex = tk.Label(tab1, text="            ", font=("Arial", 12))
                    display2hex.grid(row=11, column=12, columnspan=2, pady=10)

                    tk.Label(tab1, text="16 bit Binary: ",fg="grey").grid(row=13, column=12, padx=8, pady=8)
                    display2dec = tk.Label(tab1, text="                                         ", font=("Arial", 12))
                    display2dec.grid(row=14, column=12, columnspan=2, pady=10)
                hexbefore=hexflag
                decbefore = decflag
            elif currentunit == unit.decimal:
                tk.Label(tab1, text="4 digit hex: ", fg="grey").grid(row=10, column=12, padx=8, pady=8)
                display2hex = tk.Label(tab1, text="            ", font=("Arial", 12))
                display2hex.grid(row=11, column=12, columnspan=2, pady=10)

                tk.Label(tab1, text="16 bit Binary: ",fg="grey").grid(row=13, column=12, padx=8, pady=8)
                display2dec = tk.Label(tab1, text="                                         ", font=("Arial", 12))
                display2dec.grid(row=14, column=12, columnspan=2, pady=10)
        elif hexcheck.get()==0 and deccheck.get()==1:
            hexflag=0
            decflag = 1
            if currentunit != unit.decimal:
                if currentunit == unit.hexa:
                    tk.Label(tab1, text="4 digit hex: ", fg="grey").grid(row=10, column=12, padx=8, pady=8)
                    display2hex = tk.Label(tab1, text="            ", font=("Arial", 12))
                    display2hex.grid(row=11, column=12, columnspan=2, pady=10)

                    tk.Label(tab1, text="16 bit Binary: ",fg="grey").grid(row=13, column=12, padx=8, pady=8)
                    display2dec = tk.Label(tab1, text="                                         ", font=("Arial", 12))
                    display2dec.grid(row=14, column=12, columnspan=2, pady=10)
                elif currentunit == unit.binary:
                    tk.Label(tab1, text="4 digit hex: ", fg="grey").grid(row=10, column=12, padx=8, pady=8)
                    display2hex = tk.Label(tab1, text="            ", font=("Arial", 12))
                    display2hex.grid(row=11, column=12, columnspan=2, pady=10)

                    tk.Label(tab1, text="16 bit Binary: ").grid(row=13, column=12, padx=8, pady=8)
                    display2dec = tk.Label(tab1, text="", font=("Arial", 12))
                    display2dec.grid(row=14, column=12, columnspan=2, pady=10)
                    display2dec.config(text=decpad)
                
            elif currentunit == unit.decimal:
                tk.Label(tab1, text="4 digit hex: ", fg="grey").grid(row=10, column=12, padx=8, pady=8)
                display2hex = tk.Label(tab1, text="            ", font=("Arial", 12))
                display2hex.grid(row=11, column=12, columnspan=2, pady=10)

                tk.Label(tab1, text="16 bit Binary: ",fg="grey").grid(row=13, column=12, padx=8, pady=8)
                display2dec = tk.Label(tab1, text="                                         ", font=("Arial", 12))
                display2dec.grid(row=14, column=12, columnspan=2, pady=10)
            hexbefore = hexflag
            decbefore = decflag

hexcheck = tk.IntVar()
tk.Checkbutton(tab1, text="Show 4 digit hex", variable=hexcheck, font=("Arial", 8),command=optionchecker).grid(row=7, column=16)
deccheck = tk.IntVar()
tk.Checkbutton(tab1, text="Show 16 bit Binary", variable=deccheck, font=("Arial", 8),command=optionchecker).grid(row=8, column=16)
#Checkbox end

#Display result Start
tk.Label(tab1, text="Result: ").grid(row=8, column=12, padx=8, pady=8)
display_label = tk.Label(tab1, text=" ", font=("Arial", 12))
#display_label.config(text=f"{valueaf}")
display_label.grid(row=9,column=12,columnspan=2,pady=10)
#Display result End



#Credit
tk.Label(tab1, text="©Faries_Abdullah",bg="#C0C0C0", font=("Arial", 7)).grid(row=21, column=12, padx=8 ,pady=10)
tk.Label(tab1, text="V2.3",bg="#C0C0C0", font=("Arial", 7)).grid(row=22, column=12, padx=8)
"""submit = tk.Button(root, text="Total", command=total)
submit.grid(row=8, column=0, columnspan=2, pady=8)"""

##patch content
scrollbar = tk.Scrollbar(tab2)
scrollbar.grid(row=0, column=1, sticky="ns")

# Create Text widget (instead of Label)
patch_text = tk.Text(tab2, wrap="word", yscrollcommand=scrollbar.set, width=64, height=40)
patch_text.grid(row=0, column=0, sticky="nsew")

# Configure scrollbar
scrollbar.config(command=patch_text.yview)
patch_text.insert(tk.END, """
Version 3.0 (Major Update) - 21 Aug 2025
• Add Update feature to check the current version of the app
• User can Download the Latest Version of the App (if any) via Update tab 
                  
Version 2.3 (Mini Update) - 20 Aug 2025
• Fix bug on binary 16-bit result bug when the user tick both\n option for showing 4 digit hex and 16 bit binary                 

Version 2.2 (Mini Update) - 19 Aug 2025
• Fix bug on showing result of hex/dec after the\n corresponding checkbox was untick
                  
Version 2.1 (Mini Update) - 18 Aug 2025
• Added tabbed interface for better organization
• Improved user interface with separate sections
• Added dedicated patch notes page
• Added dedicated help page

Version 2.0 (Major Update)- 15 Aug 2025
• Enhanced number conversion functionality
• Added support for Hex, Decimal, and Binary conversions
• Implemented 16-bit binary display option
• Added hex signed 2's complement display
• Improved error handling for illegal inputs
• Added visual convert button with icon support

Version 1.0 - Initial Release
• Basic number conversion between Hex, Dec, and Bin
• Simple user interface
• Core conversion functionality

Known Issues:
• Input validation could be enhanced for edge cases
• Large numbers may not display properly in all formats
• UI issue when the user dragging the window border in and out

Future Updates:
• Support for floating-point numbers
• Additional number systems (Octal)
• Enhanced input validation
• Dark/Light theme options
• History
""")

patch_text.config(state="disabled", bg= "#CCE5FF")


##patch content end


##Help Content
scrollbar2 = tk.Scrollbar(tab3)
scrollbar2.grid(row=0, column=1, sticky="ns")

# Create Text widget (instead of Label)
patch_text2 = tk.Text(tab3, wrap="word", yscrollcommand=scrollbar2.set, width=64, height=40)
patch_text2.grid(row=0, column=0, sticky="nsew")

# Configure scrollbar
scrollbar2.config(command=patch_text2.yview)
patch_text2.insert(tk.END, """
How to Use:
1. Select the source number system from the "From" dropdown
2. Select the target number system from the "To" dropdown
3. Enter your number in the input field
4. Click "Convert" to see the result
5. Use checkboxes to show additional format representations
                   
Features:
• Convert between Hexadecimal, Decimal, and Binary number systems
• Optional display of 16-bit binary representation
• Optional display of hex signed 2's complement
• Input validation and error handling
• Clean and intuitive user interface

Supported Conversions:
• Hex ↔ Dec
• Hex ↔ Bin
• Dec ↔ Bin
• All combinations supported

Credit to:
• Lee San Hang (QA)
• Chan Shi Chin (QA)
""")

patch_text2.config(state="disabled", bg= "#CCCCFF")
##Help Content End

##Update Content

##For row and column config in tab
for r in range(20):     # allow 10 rows
    tab4.grid_rowconfigure(r, weight=1)
for c in range(20):      # allow 5 columns
    tab4.grid_columnconfigure(c, weight=1)

upd_path = resource_path("images/update.png")      # put your PNG file path here
upd = Image.open(upd_path)
upd = upd.resize((30, 30))              # resize if needed
update_patch_icon = ImageTk.PhotoImage(upd)   

dow_path = resource_path("images/download.png")      # put your PNG file path here
dow = Image.open(dow_path)
dow = dow.resize((30, 30))              # resize if needed
download_patch_icon = ImageTk.PhotoImage(dow)   
data = ""
progressvar = tk.DoubleVar()
def downloadupdate():
    global data
    progressflag = 0
    progress = ttk.Progressbar(tab4, orient="horizontal" , variable= progressvar,maximum=100, length=300, mode="determinate")
    progress.grid(row=6, column=9, padx=8 ,pady=10)
    def rundownload():
        for progress in updatechecker.download_update(data["url"]):
            progressvar.set(progress)
            print("Downloaded % ", progress)
            root.update_idletasks()
        tk.Label(tab4, text="Thanks for downloading the new update",bg="#CC99FF", font=("Arial", 12)).grid(row=8, column=9, padx=8 ,pady=10)
        tk.Label(tab4, text="You can now delete this .exe file\n and use the new downloaded .exe",bg="#CC99FF", font=("Arial", 12)).grid(row=9, column=9, padx=8 ,pady=10)
        tk.Label(tab4, text="Keep on the support!",bg="#CC99FF", font=("Arial", 12)).grid(row=10, column=9, padx=8 ,pady=10)
            

    threading.Thread(target=rundownload, daemon=True).start()
     
         

def updatetask():
    global data
    update, data = updatechecker.check_for_update()
    print("update: ", update)
    if update == True:
        tk.Label(tab4, text="New update available,\n Click 'Download update' to download the update now",bg="#CC99FF", font=("Arial", 12)).grid(row=3, column=9, padx=8 ,pady=10)
        downloadbutton = tk.Button(tab4, text="Download update",bg="#99FFFF" , image=download_patch_icon, command=downloadupdate ,compound="bottom")
        downloadbutton.grid(row=5, column=9, columnspan=2)
        
    elif update == False and data:
        tk.Label(tab4, text="App is Up-to-Date, Thanks for the support!",bg="#CC99FF", font=("Arial", 12)).grid(row=3, column=9, padx=8 ,pady=10)
    
    else:
        tk.Label(tab4, text="Checking Fail, Check your Internet Connection",bg="#CC99FF", font=("Arial", 12)).grid(row=3, column=9, padx=8 ,pady=10)

updatebutton = tk.Button(tab4, text="Check for Update",bg="#99FFFF" , image=update_patch_icon,command= updatetask,compound="bottom")
updatebutton.grid(row=2, column=9, columnspan=2)
##Update Content End
root.mainloop()
