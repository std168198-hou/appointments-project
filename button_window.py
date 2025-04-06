import tkinter as tk

# Main Window
window = tk.Tk()
window.title("My Buttons Window")

# Buttons
button1 = tk.Button(window, text="Appointment")
button2 = tk.Button(window, text="Search")
button3 = tk.Button(window, text="About")

# Pack layout manager
button1.pack()
button2.pack()
button3.pack()

# Run main loop
window.mainloop()
