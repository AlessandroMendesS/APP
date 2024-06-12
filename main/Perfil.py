import tkinter
import customtkinter
from PIL import Image, ImageTk


Perfil = customtkinter.CTk()
Perfil.geometry("500x800")
Perfil.title("Perfil")



localidades = ["São Paulo","Rio de Janeiro","Espírito Santo","Minas Gerais","Paraná","Santa Catarina","Rio Grande do Sul","Bahia","Sergipe","Alagoas","Pernambuco","Paraíba","Rio Grande do Norte","Ceará","Piaui","Maranhão","Tocantins","Goiás","Mato Grosso do Sul","Mato Grosso" ]

Caixa = customtkinter.CTkFrame(master=Perfil, width=450, height=900, corner_radius=50, fg_color="white")
Caixa.place(relx=0.5, rely=0.5, anchor=tkinter.CENTER)



imagem_perfil = Image.open("perfil-de-usuario.png").resize((150, 150))
imagem_perfil = ImageTk.PhotoImage(imagem_perfil)


imagem_perfil = customtkinter.CTkLabel(master=Caixa, image=imagem_perfil,text="", width=150, height=150, corner_radius=75, fg_color="transparent")
imagem_perfil.place(relx=0.5, rely=0.1, anchor=tkinter.CENTER)
imagem_perfil.place(x=0, y=50)


Nome = customtkinter.CTkLabel(master=Caixa, text="Nome:", text_color="black", font=("Century Gothic", 16))
Nome.place(relx=0.1, rely=0.4, anchor=tkinter.W)

Email = customtkinter.CTkLabel(master=Caixa, text="Email:", text_color="black", font=("Century Gothic", 16))
Email.place(relx=0.1, rely=0.51, anchor=tkinter.W)

Email_Nome = customtkinter.CTkEntry(master=Caixa, placeholder_text="Digite seu email", text_color="black", width=350, height=35, corner_radius=10)
Email_Nome.place(relx=0.1, rely=0.55, anchor=tkinter.W)

Localidadenome = customtkinter.CTkLabel(master=Caixa, text="Localização:", text_color="black", font=("Century Gothic", 16))
Localidadenome.place(x=50, y=535)

Entrada_Nome = customtkinter.CTkEntry(master=Caixa, placeholder_text="Digite seu nome", width=350, height=35, corner_radius=10)
Entrada_Nome.place(relx=0.1, rely=0.45, anchor=tkinter.W)

Localidade = customtkinter.CTkComboBox(master=Caixa, values=localidades, width=350, height=35, corner_radius=10)
Localidade.place(relx=0.1, rely=0.65, anchor=tkinter.W)
Localidade.set("Selecione uma localidade")

Risco = customtkinter.CTkFrame(master=Perfil, width=15, height=875, fg_color="#EFB810", bg_color="transparent")
Risco.place(x=745,y=70)

img2 = customtkinter.CTkImage(Image.open("home-removebg-preview.png").resize((20, 20)))
Home = customtkinter.CTkButton(master=Caixa, image=img2, text="", width=50, height=20, corner_radius=100, compound="left", text_color="black",
                                    fg_color="transparent",
                                    hover_color="#CDCDCB")
Home.place(x=75, y=825)

img3 = customtkinter.CTkImage(Image.open("opcoes-removebg-preview.png").resize((20, 20)))
Opcoes = customtkinter.CTkButton(master=Caixa, image=img3, text="", width=50, height=20, corner_radius=100, compound="left", text_color="black",
                                    fg_color="transparent",
                                    hover_color="#CDCDCB")
Opcoes.place(x=325, y=825)

img4 = customtkinter.CTkImage(Image.open("Cora.png").resize((20, 20)))
Favoritos = customtkinter.CTkButton(master=Caixa, image=img4, text="", width=50, height=20, corner_radius=100, compound="left", text_color="black",
                                    fg_color="transparent",
                                    hover_color="#CDCDCB")
Favoritos.place(x=200, y=825)


Perfil.mainloop()
