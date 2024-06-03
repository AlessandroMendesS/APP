import customtkinter
from tkinter import ttk
import tkinter
from PIL import  Image, ImageTk

window = customtkinter.CTk()
window.geometry("600x400")

imgori = Image.open("Cora.png").resize((600,400))
img = ImageTk.PhotoImage(imgori)

# label = tkinter.Label(window, text ="", image=img)
# label.pack()

botao = tkinter.Button(window, image=img)
botao.place()



window.mainloop()