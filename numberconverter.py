##Each Section inside the UI code begin with Start and ends with End 

import tkinter as tk
from tkinter import ttk
import APU                                                      # import module / converter
from PIL import Image, ImageTk 
import os , sys
from enum import Enum
import updatechecker
import threading

#style = ttk.Style()
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
root.geometry("550x550")
root.configure(bg="grey")

##notebook
notebook = ttk.Notebook(root)
notebook.grid(row=0, column=0, sticky="nsew")  
root.grid_rowconfigure(0, weight=2)
root.grid_columnconfigure(0, weight=2)

tab1 = tk.Frame(notebook, bg="#0080FF")
tab2 = tk.Frame(notebook, bg="#CCE5FF")
tab3 = tk.Frame(notebook, bg="#CCCCFF")
tab4 = tk.Frame(notebook, bg="#CCCCFF")

notebook.add(tab1, text="Converter")
notebook.add(tab2, text="Patch Notes")
notebook.add(tab3, text="Help")
notebook.add(tab4, text="Update")
##notebook end


##Separator Start
left_frame = tk.Frame(tab1 ,bg="#0080FF")
left_frame.pack(side=tk.LEFT, fill=tk.BOTH, expand=True, )


# right frame
right_frame = tk.Frame(tab1 ,bg="#0080FF")
right_frame.pack(side=tk.RIGHT, fill=tk.BOTH, expand=True)


# right frame
centerf = tk.Frame(tab1 ,bg="#0080FF")
centerf.pack(side=tk.TOP, fill=tk.BOTH, expand=True)

##Separator End
counter = tk.IntVar(value=0)
y = 0
hexflag = 0
decflag = 0
reset = 0

def inc():
    counter.set(counter.get() + 1)

updatestartflag , dummydata = updatechecker.check_for_update()

#Selection From Start
selected_var = tk.StringVar()
items=["Hex","Dec","Bin"]
selection_label = ttk.Label(left_frame, text="From", font=("Arial", 12), background="#99ccff")
selection_label.pack(padx=5, pady=20)
combo = ttk.Combobox(left_frame, values=items, textvariable=selected_var, state="readonly")
combo.current(0)
combo.pack(pady=5, padx=5)
#combo.grid(row=1,column=6,columnspan=2,pady=5)
#Selection From End

#Selection To Start
selected_tovar = tk.StringVar()
selection_to = ttk.Label(right_frame, text="To", font=("Arial", 12), background="#99ccff")
selection_to.pack(padx=5, pady=20)
#selection_to.place(x=390,y=20)
comboto = ttk.Combobox(right_frame, values=items,textvariable = selected_tovar, state="readonly")
comboto.current(0)
comboto.pack(pady=5, padx=5)
def eventselectionTo(event):                                           #Event Handler Function
    selected_option2 = comboto.get()                                   #To get value
    #print("you selected : " , selected_option2)
comboto.bind("<<ComboboxSelected>>", eventselectionTo)                 #Event Call

#comboto.grid(row=1,column=15,columnspan=2,pady=5)
#Selection To End


#Enter Number Start
enternumberlabel=ttk.Label(centerf, text="Enter Number:",font=("Arial",12), background="#99ccff")
enternumberlabel.pack(pady=20)
entry = ttk.Entry(centerf, width=30)
entry.pack(pady=5)
#entry.grid(row=4, column=12, columnspan=2, pady=15)
#valuepad = 0
decpad=0

def total():
    global hexflag   
    global decflag
    global valuepad
    global reset
    global decpad
    global currentunit
 
    print("reset: ", reset)
    print("hexflag: ",hexflag)

    reset = 1
    if selected_var.get()=="Hex" and selected_tovar.get()== "Bin":
        #print("hex to binary")
        currentunit = unit.binary
       
        valueaf = APU.hex_to_bin(entry.get())
        decpad = f"{int(valueaf, 2):016b}" 
        if valueaf != "Error":
            display_label.config(text=f"{decpad}",justify="center",compound="center")
            
        else:
            display_label.config(text=f"Illegal Input")
    elif selected_var.get()=="Hex" and selected_tovar.get()== "Dec":
        #print("hex to dec")
        currentunit = unit.decimal
       
        valueaf = APU.hex_to_dec(entry.get())
        if valueaf != "Error":
            #print(valueaf)
            display_label.config(text=f"{valueaf}",justify="center",compound="center")
        else:
            display_label.config(text=f"Illegal Input")
    elif selected_var.get()=="Dec" and selected_tovar.get()== "Bin":
        #print("Dec to Bin")
        currentunit = unit.binary
       
        valueaf = APU.dec_to_bin(int(entry.get()))
        if valueaf != "Error":
            #print(valueaf)
            decpad = f"{int(valueaf, 2):016b}" 
            display_label.config(text=f"{decpad}",justify="center",compound="center")
        
                
        else:
            display_label.config(text=f"Illegal Input")
    elif selected_var.get()=="Dec" and selected_tovar.get()== "Hex":
        #print("Dec to Hex")
        currentunit = unit.hexa
       
        valueaf = APU.dec_to_hex((int(entry.get())))
        if valueaf != "Error":
            #print(valueaf)
            valuepad = f"0x{int(valueaf, 16):04X}"
            display_label.config(text=f"{valuepad}",justify="center",compound="center")
            
                
                
        else:
            display_label.config(text=f"Illegal Input",justify="center")
    elif selected_var.get()=="Bin" and selected_tovar.get()== "Hex":
        #print("Bin to Hex")
        currentunit = unit.hexa
        
       
        valueaf = APU.bin_to_hex((entry.get()))
        valuepad = f"0x{int(valueaf, 16):04X}"
        if valueaf != "Error":
            #print(valueaf)
            display_label.config(text=f"{valuepad}",justify="center",compound="center")

                
        else:
            display_label.config(text=f"Illegal Input")
    elif selected_var.get()=="Bin" and selected_tovar.get()== "Dec":
        #print("Bin to Dec")
        currentunit = unit.decimal

        valueaf = APU.bin_to_dec((entry.get()))
        if valueaf != "Error":
            #print(valueaf)
            display_label.config(text=f"{valueaf}",justify="center")
        else:
            display_label.config(text=f"Illegal Input",justify="center",compound="center")
    else:
        #print("error")
        display_label.config(text=f"Error, Units must be diff",justify="center",compound="center")
    
    
    #print(entry.get())

img_path = resource_path("images/arrow-removebg-preview.png")      # put your PNG file path here
img = Image.open(img_path)
img = img.resize((30, 30))              # resize if needed
patch_icon = ImageTk.PhotoImage(img)   
plusbutton = ttk.Button(centerf, text="Convert", command=total,width=20, image=patch_icon,compound="left")
plusbutton.pack(pady=30)
#Enter Number End

#Display result Start
displaylabelpack = ttk.Label(centerf, text="Result: ", background="#99ccff")
displaylabelpack.pack( pady=10)
display_label = ttk.Label(centerf, text=" ", font=("Arial", 12), width=20, justify="center",compound="center")
#display_label.config(text=f"{valueaf}")
display_label.pack(pady=10)
#Display result End



#Credit
credit1 = ttk.Label(centerf, text="©Faries_Abdullah",background="#C0C0C0", font=("Arial", 7))
credit1.pack(pady=5)
credit2 = ttk.Label(centerf, text="V2.3",background="#C0C0C0", font=("Arial", 7))
credit2.pack(pady=5)

if(updatestartflag == True):
    credit3 = ttk.Label(centerf, text="New Update Available\nGo to Update tab to download\n the new update now",background="#C0C0C0", font=("Arial", 9),justify="center")
    credit3.pack(pady=5)


##patch content
scrollbar = ttk.Scrollbar(tab2)
scrollbar.pack(side="right", fill="both")

# Create Text widget (instead of Label)
patch_text = tk.Text(tab2, wrap="word", yscrollcommand=scrollbar.set, width=550, height=550)
#patch_text.grid(row=0, column=0, sticky="nsew")
patch_text.pack()

# Configure scrollbar
scrollbar.config(command=patch_text.yview)
patch_text.insert(tk.END, """
Version 4.0 (Major Update) - 24 Aug 2025
• UI revamp
• Additional Option is now removed
                  
Version 3.0 (Major Update) - 20 Aug 2025
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

Version 2.0 (Core Update)- 15 Aug 2025
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
scrollbar2.pack(side="right",fill="both")

# Create Text widget (instead of Label)
patch_text2 = tk.Text(tab3, wrap="word", yscrollcommand=scrollbar2.set, width=550, height=550)
patch_text2.pack()

# Configure scrollbar
scrollbar2.config(command=patch_text2.yview)
patch_text2.insert(tk.END, """
How to Use:
1. Select the source number system from the "From" dropdown
2. Select the target number system from the "To" dropdown
3. Enter your number in the input field
4. Click "Convert" to see the result
                   
Features:
• Convert between Hexadecimal, Decimal, and Binary number systems
• Optional display of 16-bit binary representation
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
ttk.Style().configure("TButton", padding=6, relief="flat",
   background="#ccc")
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
checkpressflag = 0
def downloadupdate():
    global data
    progress = ttk.Progressbar(tab4, orient="horizontal" , variable= progressvar,maximum=100, length=300, mode="determinate")
    progress.pack(pady=5)
    def rundownload():
        for progress in updatechecker.download_update(data["url"]):
            progressvar.set(progress)
            print("Downloaded % ", progress)
            root.update_idletasks()
        thankslabel1 = ttk.Label(tab4, text="Thanks for downloading the new update", background="#E5CCFF",font=("Arial", 10))#.grid(row=8, column=9, padx=8 ,pady=10)
        thankslabel1.pack(pady=5)
        thankslabel2 = ttk.Label(tab4, text="You can now delete this .exe file and use the new downloaded .exe",background="#E5CCFF", font=("Arial", 10))#.grid(row=9, column=9, padx=8 ,pady=10)
        thankslabel2.pack(pady=5)
        thankslabel3 =ttk.Label(tab4, text="Thanks for the support!",background="#E5CCFF", font=("Arial", 10))#.grid(row=10, column=9, padx=8 ,pady=10)
        thankslabel3.pack(pady=5)    

    threading.Thread(target=rundownload, daemon=True).start()
     
         

def updatetask():
    global data
    global checkpressflag
    update, data = updatechecker.check_for_update()
    print("update: ", update)
    if update == True:
        l1=ttk.Label(tab4, text="New update available, Click 'Download update' to download the update now",background="#E5CCFF", font=("Arial", 10))#.grid(row=3, column=9, padx=8 ,pady=10)
        l1.pack()
        downloadbutton = ttk.Button(tab4, text="Download update", image=download_patch_icon, command=downloadupdate ,compound="left",width=20)
        downloadbutton.pack(pady=5)
        checkpressflag = 1
        
    elif update == False and data:
        uptodatelabel = ttk.Label(tab4, text="App is Up-to-Date, Thanks for the support!",background="#E5CCFF", font=("Arial", 12))#.grid(row=3, column=9, padx=8 ,pady=10)
        uptodatelabel.pack(pady=5)
        checkpressflag = 1
    else:
        noconnectionlabel=ttk.Label(tab4, text="Checking Fail, Check your Internet Connection",background="#E5CCFF", font=("Arial", 12))#.grid(row=3, column=9, padx=8 ,pady=10)
        noconnectionlabel.pack(pady=5)
        checkpressflag = 1

updatebutton = ttk.Button(tab4, text="Check for Update" , image=update_patch_icon,command= updatetask,compound="left",width=20)
updatebutton.pack(side="top", padx=0, pady=9)

#updatebutton.grid(row=2, column=9, columnspan=2)
##Update Content End
root.mainloop()
