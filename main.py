import tkinter as tk

root = tk.Tk()

root.title("gile nyoba dulu")

root.geometry("400x300")


label = tk.Label(root, text="HALO GEGNS", font=("Arial", 12))
label.pack(pady=10)

def tombol_ditekan():
    label.config(text="text berubah")
    
button = tk.Button(root, text="Klik aku", command=tombol_ditekan)
button.pack(pady=10)

root.mainloop()