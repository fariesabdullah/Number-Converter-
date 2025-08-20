import tkinter as tk
from tkinter import ttk
import APU                                                      # import module / converter
from PIL import Image, ImageTk 

class NumberConverterApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Number Converter")
        self.root.geometry("490x495")
        self.root.configure(bg="grey")
        
        # Initialize variables
        self.fromsel = "Hex"
        self.tosel = "Hex"
        self.counter = tk.IntVar(value=0)
        self.y = 0
        self.hexflag = 0
        self.decflag = 0
        self.reset = 0
        self.hexbefore = 0
        self.decbefore = 0
        self.valuepad = 0
        self.decpad = 0
        
        # Create the notebook (tab container)
        self.notebook = ttk.Notebook(root)
        self.notebook.pack(expand=True, fill='both', padx=10, pady=10)
        
        # Create frames for each tab
        self.converter_frame = ttk.Frame(self.notebook)
        self.patch_notes_frame = ttk.Frame(self.notebook)
        
        # Add tabs to notebook
        self.notebook.add(self.converter_frame, text="Number Converter")
        self.notebook.add(self.patch_notes_frame, text="Patch Notes")
        
        # Setup the converter tab
        self.setup_converter_tab()
        
        # Setup the patch notes tab
        self.setup_patch_notes_tab()
    
    def setup_converter_tab(self):
        # Configure the converter frame background
        self.converter_frame.configure(style='Grey.TFrame')
        
        # Create a style for grey background
        style = ttk.Style()
        style.configure('Grey.TFrame', background='grey')
        
        #Selection From Start
        self.selected_var = tk.StringVar()
        items = ["Hex", "Dec", "Bin"]
        selection_label = tk.Label(self.converter_frame, text="From", font=("Arial", 12), bg="grey")
        selection_label.grid(row=0, column=6, columnspan=2, padx=8, pady=10)
        self.combo = ttk.Combobox(self.converter_frame, values=items, textvariable=self.selected_var, state="readonly")
        self.combo.current(0)
        self.combo.grid(row=1, column=6, columnspan=2, pady=5)
        #Selection From End

        #Selection To Start
        self.selected_tovar = tk.StringVar()
        selection_to = tk.Label(self.converter_frame, text="To", font=("Arial", 12), bg="grey")
        selection_to.grid(row=0, column=15, columnspan=2, pady=10)
        self.comboto = ttk.Combobox(self.converter_frame, values=items, textvariable=self.selected_tovar, state="readonly")
        self.comboto.current(0)
        self.comboto.bind("<<ComboboxSelected>>", self.eventselectionTo)
        self.comboto.grid(row=1, column=15, columnspan=2, pady=5)
        #Selection To End

        #Enter Number Start
        tk.Label(self.converter_frame, text="Enter Number:", bg="grey").grid(row=3, column=12, padx=8, pady=8)
        self.entry = tk.Entry(self.converter_frame)
        self.entry.grid(row=4, column=12, columnspan=2, pady=15)

        # Load and setup the convert button with icon
        try:
            img = Image.open("14521.png")
            img = img.resize((30, 30))
            self.patch_icon = ImageTk.PhotoImage(img)
            self.plusbutton = tk.Button(self.converter_frame, text="Convert", command=self.total, 
                                       bg="#99FFFF", image=self.patch_icon, compound="left")
        except:
            # If image file doesn't exist, create button without image
            self.plusbutton = tk.Button(self.converter_frame, text="Convert", command=self.total, bg="#99FFFF")
        
        self.plusbutton.grid(row=7, column=12, columnspan=2, pady=8)
        #Enter Number End

        #Checkbox start
        tk.Label(self.converter_frame, text="Hex signed 2's complement: ", fg="grey", bg="grey").grid(row=10, column=12, padx=8, pady=8)
        self.display2hex = tk.Label(self.converter_frame, text=" ", font=("Arial", 12), bg="grey")
        self.display2hex.grid(row=11, column=12, columnspan=2, pady=10)

        tk.Label(self.converter_frame, text="16 bit Binary: ", fg="grey", bg="grey").grid(row=13, column=12, padx=8, pady=8)
        self.display2dec = tk.Label(self.converter_frame, text=" ", font=("Arial", 12), bg="grey")
        self.display2dec.grid(row=14, column=12, columnspan=2, pady=10)

        self.hexcheck = tk.IntVar()
        tk.Checkbutton(self.converter_frame, text="Show Hex signed\n 2's complement", variable=self.hexcheck, 
                      font=("Arial", 8), command=self.optionchecker, bg="grey").grid(row=7, column=16)
        
        self.deccheck = tk.IntVar()
        tk.Checkbutton(self.converter_frame, text="Show 16 bit Binary", variable=self.deccheck, 
                      font=("Arial", 8), command=self.optionchecker, bg="grey").grid(row=8, column=16)
        #Checkbox end

        #Display result Start
        tk.Label(self.converter_frame, text="Result: ", bg="grey").grid(row=8, column=12, padx=8, pady=8)
        self.display_label = tk.Label(self.converter_frame, text=" ", font=("Arial", 12), bg="grey")
        self.display_label.grid(row=9, column=12, columnspan=2, pady=10)
        #Display result End

        #Credit
        tk.Label(self.converter_frame, text="©Faries_Abdullah", bg="#C0C0C0", font=("Arial", 7)).grid(row=21, column=12, padx=8)
        tk.Label(self.converter_frame, text="V2.0", bg="#C0C0C0", font=("Arial", 7)).grid(row=22, column=12, padx=8)

    def setup_patch_notes_tab(self):
        # Configure the patch notes frame
        self.patch_notes_frame.configure(style='Grey.TFrame')
        
        # Title
        title_label = tk.Label(self.patch_notes_frame, text="Number Converter - Patch Notes", 
                              font=("Arial", 16, "bold"), bg="grey")
        title_label.pack(pady=20)
        
        # Create a scrollable text area for patch notes
        frame = tk.Frame(self.patch_notes_frame, bg="grey")
        frame.pack(expand=True, fill='both', padx=20, pady=10)
        
        # Scrollbar
        scrollbar = tk.Scrollbar(frame)
        scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
        
        # Text widget for patch notes
        self.patch_text = tk.Text(frame, wrap=tk.WORD, yscrollcommand=scrollbar.set, 
                                 font=("Arial", 10), bg="white", fg="black")
        self.patch_text.pack(expand=True, fill='both')
        scrollbar.config(command=self.patch_text.yview)
        
        # Add sample patch notes content
        patch_content = """Version 2.1 - Current
• Added tabbed interface for better organization
• Improved user interface with separate sections
• Added dedicated patch notes page

Version 2.0 - Previous
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

Features:
• Convert between Hexadecimal, Decimal, and Binary number systems
• Optional display of 16-bit binary representation
• Optional display of hex signed 2's complement
• Input validation and error handling
• Clean and intuitive user interface

How to Use:
1. Select the source number system from the "From" dropdown
2. Select the target number system from the "To" dropdown
3. Enter your number in the input field
4. Click "Convert" to see the result
5. Use checkboxes to show additional format representations

Supported Conversions:
• Hex ↔ Dec
• Hex ↔ Bin
• Dec ↔ Bin
• All combinations supported

Known Issues:
• Input validation could be enhanced for edge cases
• Large numbers may not display properly in all formats

Future Updates:
• Support for floating-point numbers
• Additional number systems (Octal)
• Enhanced input validation
• Dark/Light theme options
"""
        
        self.patch_text.insert('1.0', patch_content)
        self.patch_text.config(state='disabled')  # Make it read-only

    def inc(self):
        self.counter.set(self.counter.get() + 1)

    def eventselectionTo(self, event):
        selected_option2 = self.comboto.get()

    def total(self):
        # Clear previous error messages
        tk.Label(self.converter_frame, text="                            ", bg="grey", font=("Arial", 8)).grid(row=3, column=6, columnspan=2, pady=10)
        tk.Label(self.converter_frame, text="              ", bg="grey", font=("Arial", 8)).grid(row=4, column=6, columnspan=2, pady=10)
        tk.Label(self.converter_frame, text="                            ", bg="grey", font=("Arial", 8)).grid(row=3, column=15, columnspan=2, pady=10)
        tk.Label(self.converter_frame, text="              ", bg="grey", font=("Arial", 8)).grid(row=4, column=15, columnspan=2, pady=10)
        
        self.reset = 1
        print("reset: ", self.reset)
        print("hexflag: ", self.hexflag)
        
        try:
            if self.selected_var.get() == "Hex" and self.selected_tovar.get() == "Bin":
                valueaf = APU.hex_to_bin(self.entry.get())
                self.decpad = f"{int(valueaf, 2):016b}" 
                if valueaf != "Error":
                    self.display_label.config(text=f"{valueaf}", fg="black")
                    if self.hexflag == 1:
                        self.display2dec.config(text=self.decpad)
                        self.display2dec.tkraise()
                else:
                    self.display_label.config(text=f"Illegal Input", fg="red")
                    
            elif self.selected_var.get() == "Hex" and self.selected_tovar.get() == "Dec":
                valueaf = APU.hex_to_dec(self.entry.get())
                if valueaf != "Error":
                    self.display_label.config(text=f"{valueaf}", fg="black")
                else:
                    self.display_label.config(text=f"Illegal Input", fg="red")
                    
            elif self.selected_var.get() == "Dec" and self.selected_tovar.get() == "Bin":
                valueaf = APU.dec_to_bin(int(self.entry.get()))
                if valueaf != "Error":
                    self.display_label.config(text=f"{valueaf}", fg="black")
                    self.decpad = f"{int(valueaf, 2):016b}" 
                    if self.hexflag == 1:
                        self.display2dec.config(text=self.decpad)
                        self.display2dec.tkraise()
                else:
                    self.display_label.config(text=f"Illegal Input", fg="red")
                    
            elif self.selected_var.get() == "Dec" and self.selected_tovar.get() == "Hex":
                valueaf = APU.dec_to_hex((int(self.entry.get())))
                self.valuepad = f"0x{int(valueaf, 16):04X}"
                if valueaf != "Error":
                    self.display_label.config(text=f"{valueaf}", fg="black")
                    if self.hexflag == 1:
                        self.display2hex.config(text=self.valuepad)
                        self.display2hex.tkraise()
                else:
                    self.display_label.config(text=f"Illegal Input", fg="red")
                    
            elif self.selected_var.get() == "Bin" and self.selected_tovar.get() == "Hex":
                valueaf = APU.bin_to_hex((int(self.entry.get())))
                self.valuepad = f"0x{int(valueaf, 16):04X}"
                if valueaf != "Error":
                    self.display_label.config(text=f"{valueaf}", fg="black")
                    if self.hexflag == 1:
                        self.display2hex.config(text=self.valuepad)
                        self.display2hex.tkraise()
                else:
                    self.display_label.config(text=f"Illegal Input", fg="red")
                    
            elif self.selected_var.get() == "Bin" and self.selected_tovar.get() == "Dec":
                valueaf = APU.bin_to_dec((self.entry.get()))
                if valueaf != "Error":
                    self.display_label.config(text=f"{valueaf}", fg="black")
                else:
                    self.display_label.config(text=f"Illegal Input", fg="red")
            else:
                # Same units selected
                tk.Label(self.converter_frame, text="Error, units must ", fg="red", font=("Arial", 8), bg="grey").grid(row=3, column=6, columnspan=2, pady=10)
                tk.Label(self.converter_frame, text="be diff ", fg="red", font=("Arial", 8), bg="grey").grid(row=4, column=6, columnspan=2, pady=10)
                tk.Label(self.converter_frame, text="Error, units must ", fg="red", font=("Arial", 8), bg="grey").grid(row=3, column=15, columnspan=2, pady=10)
                tk.Label(self.converter_frame, text="be diff ", fg="red", font=("Arial", 8), bg="grey").grid(row=4, column=15, columnspan=2, pady=10)
        except Exception as e:
            self.display_label.config(text=f"Illegal Input", fg="red")

    def optionchecker(self):
        print(self.reset)
        if self.hexbefore != self.hexflag:
            self.reset = 1
        else:
            self.reset = 0
            
        if self.reset == 1:
            if self.hexcheck.get() == 1 and self.deccheck.get() == 1:  
                self.hexflag = 1
                tk.Label(self.converter_frame, text="Hex signed 2's complement: ", bg="grey").grid(row=10, column=12, padx=8, pady=8)
                tk.Label(self.converter_frame, text="16 bit Binary: ", bg="grey").grid(row=13, column=12, padx=8, pady=8)
                self.hexbefore = self.hexflag
                
            elif self.hexcheck.get() == 0 and self.deccheck.get() == 0:
                self.hexflag = 0
                tk.Label(self.converter_frame, text="Hex signed 2's complement: ", fg="grey", bg="grey").grid(row=10, column=12, padx=8, pady=8)
                self.display2hex = tk.Label(self.converter_frame, text="            ", font=("Arial", 12), bg="grey")
                self.display2hex.grid(row=11, column=12, columnspan=2, pady=10)
                tk.Label(self.converter_frame, text="16 bit Binary: ", fg="grey", bg="grey").grid(row=13, column=12, padx=8, pady=8)
                self.display2dec = tk.Label(self.converter_frame, text="                                         ", font=("Arial", 12), bg="grey")
                self.display2dec.grid(row=14, column=12, columnspan=2, pady=10)
                self.hexbefore = self.hexflag
                
            elif self.hexcheck.get() == 1 and self.deccheck.get() == 0:
                self.hexflag = 1
                tk.Label(self.converter_frame, text="16 bit Binary: ", fg="grey", bg="grey").grid(row=13, column=12, padx=8, pady=8)
                self.display2dec = tk.Label(self.converter_frame, text="                                         ", font=("Arial", 12), bg="grey")
                self.display2dec.grid(row=14, column=12, columnspan=2, pady=10)
                tk.Label(self.converter_frame, text="Hex signed 2's complement: ", bg="grey").grid(row=10, column=12, padx=8, pady=8)
                self.hexbefore = self.hexflag
                
            elif self.hexcheck.get() == 0 and self.deccheck.get() == 1:
                self.hexflag = 1
                tk.Label(self.converter_frame, text="16 bit Binary: ", bg="grey").grid(row=13, column=12, padx=8, pady=8)
                tk.Label(self.converter_frame, text="Hex signed 2's complement: ", fg="grey", bg="grey").grid(row=10, column=12, padx=8, pady=8)
                self.display2hex = tk.Label(self.converter_frame, text="            ", font=("Arial", 12), bg="grey")
                self.display2hex.grid(row=11, column=12, columnspan=2, pady=10)
                self.hexbefore = self.hexflag

        elif self.reset == 0:
            if self.hexcheck.get() == 1 and self.deccheck.get() == 1:
                self.hexflag = 1
                tk.Label(self.converter_frame, text="Hex signed 2's complement: ", bg="grey").grid(row=10, column=12, padx=8, pady=8)
                self.display2hex = tk.Label(self.converter_frame, text="", font=("Arial", 12), bg="grey")
                self.display2hex.grid(row=11, column=12, columnspan=2, pady=10)
                self.display2hex.config(text=self.valuepad)
                tk.Label(self.converter_frame, text="16 bit Binary: ", bg="grey").grid(row=13, column=12, padx=8, pady=8)
                self.display2dec = tk.Label(self.converter_frame, text="", font=("Arial", 12), bg="grey")
                self.display2dec.grid(row=14, column=12, columnspan=2, pady=10)
                self.display2dec.config(text=self.decpad)
                self.hexbefore = self.hexflag
                
            elif self.hexcheck.get() == 0 and self.deccheck.get() == 0:
                self.hexflag = 0
                tk.Label(self.converter_frame, text="Hex signed 2's complement: ", fg="grey", bg="grey").grid(row=10, column=12, padx=8, pady=8)
                self.display2hex = tk.Label(self.converter_frame, text="            ", font=("Arial", 12), bg="grey")
                self.display2hex.grid(row=11, column=12, columnspan=2, pady=10)
                tk.Label(self.converter_frame, text="16 bit Binary: ", fg="grey", bg="grey").grid(row=13, column=12, padx=8, pady=8)
                self.display2dec = tk.Label(self.converter_frame, text="                                         ", font=("Arial", 12), bg="grey")
                self.display2dec.grid(row=14, column=12, columnspan=2, pady=10)
                self.hexbefore = self.hexflag
                
            elif self.hexcheck.get() == 1 and self.deccheck.get() == 0:
                self.hexflag = 1
                tk.Label(self.converter_frame, text="Hex signed 2's complement: ", bg="grey").grid(row=10, column=12, padx=8, pady=8)
                self.display2hex = tk.Label(self.converter_frame, text="", font=("Arial", 12), bg="grey")
                self.display2hex.grid(row=11, column=12, columnspan=2, pady=10)
                self.display2hex.config(text=self.valuepad)
                tk.Label(self.converter_frame, text="16 bit Binary: ", fg="grey", bg="grey").grid(row=13, column=12, padx=8, pady=8)
                self.display2dec = tk.Label(self.converter_frame, text="                                         ", font=("Arial", 12), bg="grey")
                self.display2dec.grid(row=14, column=12, columnspan=2, pady=10)
                self.hexbefore = self.hexflag

            elif self.hexcheck.get() == 0 and self.deccheck.get() == 1:
                self.hexflag = 1
                tk.Label(self.converter_frame, text="Hex signed 2's complement: ", fg="grey", bg="grey").grid(row=10, column=12, padx=8, pady=8)
                self.display2hex = tk.Label(self.converter_frame, text="            ", font=("Arial", 12), bg="grey")
                self.display2hex.grid(row=11, column=12, columnspan=2, pady=10)
                tk.Label(self.converter_frame, text="16 bit Binary: ", bg="grey").grid(row=13, column=12, padx=8, pady=8)
                self.display2dec = tk.Label(self.converter_frame, text="", font=("Arial", 12), bg="grey")
                self.display2dec.grid(row=14, column=12, columnspan=2, pady=10)
                self.display2dec.config(text=self.decpad)
                self.hexbefore = self.hexflag


if __name__ == "__main__":
    root = tk.Tk()
    app = NumberConverterApp(root)
    root.mainloop()