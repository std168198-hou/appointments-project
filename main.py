import tkinter as tk
from tkinter import Menu
import subprocess
from tkinter import PhotoImage

# Δημιουργία του κύριου παραθύρου
main_window = tk.Tk()

# Ορισμός του μεγέθους του παραθύρου σε 800x600
window_width = 800
window_height = 600

# Λήψη του πλάτους και ύψους της οθόνης
screen_width = main_window.winfo_screenwidth()
screen_height = main_window.winfo_screenheight()

# Υπολογισμός της θέσης για να κεντραριστεί το παράθυρο
position_top = int(screen_height/2 - window_height/2)
position_right = int(screen_width/2 - window_width/2)

# Ορισμός της γεωμετρίας του παραθύρου με την υπολογισμένη θέση
main_window.geometry(f"{window_width}x{window_height}+{position_right}+{position_top}")

# Δημιουργία της συνάρτησης για την κλήση του customers.py
def open_customers():
    subprocess.run(["python", "customers.py"])
def open_search():
    subprocess.run(["python", "search.py"])

# Δημιουργία του μενού
menu = Menu(main_window)
main_window.config(menu=menu)

# Προσθήκη επιλογών στο μενού
menu.add_command(command=open_search,label="Αναζήτηση")
menu.add_command(command=open_customers, label="Πελάτες")
menu.add_command(label="Σχετικά")

# Ορισμός του τίτλου του παραθύρου
main_window.title("Ραντεβού")

img = PhotoImage(file="calendar.png")
image_label = tk.Label(main_window, image = img)
image_label.grid_location(800,800)
image_label.pack()


# Εκκίνηση της εφαρμογής
main_window.mainloop()