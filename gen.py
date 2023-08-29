import random
import math # Apparently it's not accessed but I don't care lmao
import time
import tkinter as tk
from tkinter import font

threeblacklist = [333, 444, 555, 666, 777, 888, 999] # Blacklisted numbers in first 3, e.g. (as A) AAA-BBBBBBB

print("\n\n\n\nWelcome to Py95Gen by Dumprr\n--\nWindows 95 Key Generator made in Python. It's fully open source.")
print("Starting in 1 second...")
time.sleep(1)

key = ''

def mod3():
    global m3i
    m3i = ''
    for x in range(3): # Repeat 3 times to make the first 3 numbers
        m3i += str(random.randint(0, 9)) # Random 1-9
    if int(m3i) in threeblacklist: # if the number is in the blacklist
        print("mod3 error! retrying")
        mod3()

def mod7(): # Sort all numbers into individual variables.
    m7i1 = str(random.randint(0, 9)) 
    m7i2 = str(random.randint(0, 9)) 
    m7i3 = str(random.randint(0, 9)) 
    m7i4 = str(random.randint(0, 9)) 
    m7i5 = str(random.randint(0, 9)) 
    m7i6 = str(random.randint(0, 9)) 
    m7i7 = str(random.randint(0, 9)) 
    global m7i
    m7i = (m7i1+m7i2+m7i3+m7i4+m7i5+m7i6+m7i7) # Adds all strings of variables together as one string.
    global intm7i
    intm7i = (int(m7i1)+int(m7i2)+int(m7i3)+int(m7i4)+int(m7i5)+int(m7i6)+int(m7i7)) # Converts all variables to integers to add mathematically.
    if intm7i % 7 != 0: # Basically just saying, if it is not divisible by 7 then do
        print("mod7 error! retrying")
        mod7()
      
def finish():
   mod3()
   mod7()
   keyweight = intm7i / 7 # "Key Weight", saw it used in MobCat's checker, divides it by 7 to get weight.
   print("\n\n-------\n\ndone\n")
   print("Key Weight: " + str(keyweight)) # Prints key weight
   global key
   key = (m3i + "-" + m7i)
   print(key)
   return key

def window():
    window = tk.Tk()
    window.title("Py95Gen")
    window.geometry("540x400")
    window.resizable(False, False)

    titletextsize = 12
    desctextsize = 8
    
  
    textfont = "Verdana"

 
    title = tk.Label(window, text="Py95Gen", font=(textfont, titletextsize))
    title.pack(pady=20)

  
    desc = tk.Label(window, text="Py95Gen creates randomized Windows 95 activation keys.", font=(textfont, desctextsize))
    desc.pack(pady=0)
   
    button = tk.Button(window, text="Get a key", command=lambda: keys_box.insert(tk.END, finish() + "\n"), font=(textfont, desctextsize))
    button.pack(pady=20)
    
    
    keys_box = tk.Text(window, height=14, width=60, font=("Courier", 10))
    keys_box.configure(background='black', fg='lime')
    keys_box.pack()
    
    window.mainloop()

window()