import pytesseract
pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"

from PIL import ImageGrab, Image
def extract_code_from_clipboard():
    image = ImageGrab.grabclipboard()
    
    config = '--psm 6'  # Adjust the PSM mode based on your code layout
    # You can also add other configuration options, such as language settings, as needed
    if(image==None):
        return None,None
    extracted_text = pytesseract.image_to_string(image, config=config)
    return image,extracted_text

def extract_code_from_image(image_path):
    image = Image.open(image_path)

    config = '--psm 6'  # Adjust the PSM mode based on your code layout
    # You can also add other configuration options, such as language settings, as needed

    extracted_text = pytesseract.image_to_string(image, config=config)
    return image,extracted_text

import customtkinter as ctk
import pyperclip
import tkinter
from tkinter import filedialog
ctk.set_appearance_mode("dark")

root=ctk.CTk()
root.title("Get text")
root.geometry("500x500")

def button_command():
    img,code = extract_code_from_clipboard()
    
    textbox.delete("0.0", "end")
    
    if(code==None):
        textbox.insert("0.0","NO ITEM IN CLIPBOARD")
        textbox.place(relx=0.5, rely=0.5, anchor=tkinter.CENTER)
        return
    
    textbox.insert("0.0",code)
    textbox.place(relx=0.5, rely=0.5, anchor=tkinter.CENTER)
    return

def choose_file():
    try:
        file_path = filedialog.askopenfilename()
    except:
        pass
    try:
        img,code = extract_code_from_image(file_path)
    except:
        img,code=None,None
    textbox.delete("0.0", "end")
    if(code==None):
        textbox.insert("0.0","Wrong file selected")
        textbox.place(relx=0.5, rely=0.5, anchor=tkinter.CENTER)
        return
    
    textbox.insert("0.0",code)
    textbox.place(relx=0.5, rely=0.5, anchor=tkinter.CENTER)
    return

def copy_text():
    text = textbox.get("0.0", "end")
    pyperclip.copy(text)

def on_close():
    global is_window_closed
    is_window_closed = True
    root.destroy()
    
#textbox
textbox = ctk.CTkTextbox(master=root,
                         width=300,
                         height=300,
                         fg_color=("black", "black"))

#button1
btn1 = ctk.CTkButton(master=root,
                     text ="Clipboard",
                     hover_color=("black", "black"),
                     command = button_command)
btn1.place(relx=0.5, rely=0.5,x=-40,y=-200, anchor=tkinter.NE)
#btn1.pack(pady = 10)

#button2
btn2 = ctk.CTkButton(master=root,
                     text ="From directory",
                     hover_color=("black", "black"),
                     command = choose_file)
btn2.place(relx=0.5, rely=0.5,x=40,y=-200, anchor=tkinter.NW)
#btn2.pack(pady = 10)

#button3
btn3 = ctk.CTkButton(master=root,
                     text ="COPY",
                     fg_color=("green", "green"),
                     hover_color=("black", "black"),
                     command = copy_text)
btn3.place(relx=0.5, rely=0.5,x=0,y=200, anchor=tkinter.S)

is_window_closed = False
root.protocol("WM_DELETE_WINDOW", on_close)
if(is_window_closed==True):
    exit()
root.mainloop()