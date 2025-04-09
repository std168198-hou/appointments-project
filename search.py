import tkinter as tk
from tkinter import Menu

# Δημιουργία του κύριου παραθύρου
main_window = tk.Tk()

# Ορισμός του μεγέθους του παραθύρου σε 800x600
window_width = 400
window_height = 300

# Λήψη του πλάτους και ύψους της οθόνης
screen_width = main_window.winfo_screenwidth()
screen_height = main_window.winfo_screenheight()

# Υπολογισμός της θέσης για να κεντραριστεί το παράθυρο
position_top = int(screen_height/2 - window_height/2)
position_right = int(screen_width/2 - window_width/2)

# Ορισμός της γεωμετρίας του παραθύρου με την υπολογισμένη θέση
main_window.geometry(f"{window_width}x{window_height}+{position_right}+{position_top}")

# Δημιουργία του μενού
menu = Menu(main_window)
main_window.config(menu=menu)

# Ορισμός του τίτλου του παραθύρου
main_window.title("Αναζήτηση")

# Εκκίνηση της εφαρμογής
main_window.mainloop()