import tkinter
import customtkinter
from PIL import ImageTk, Image




# def opcoes():
#     main.destroy()
#     Perfil = customtkinter.CTk()
#     Perfil.geometry("500x800")
#     Perfil.title("Perfil")


#     Caixa = customtkinter.CTkFrame(master=Perfil, width=450, height=900, corner_radius=50, fg_color="white")
#     Caixa.place(relx=0.5, rely=0.5, anchor=tkinter.CENTER)

#     img2 = customtkinter.CTkImage(Image.open("home-removebg-preview.png").resize((20, 20)))

#     Home = customtkinter.CTkButton(master=Caixa, image=img2, text="", width=50, height=20, corner_radius=100, compound="left", text_color="black",
#                                     fg_color="transparent",
#                                     hover_color="#CDCDCB")
#     Home.place(x=75, y=825)

#     img3 = customtkinter.CTkImage(Image.open("opcoes-removebg-preview.png").resize((20, 20)))

#     Opcoes = customtkinter.CTkButton(master=Caixa, image=img3, text="", width=50, height=20, corner_radius=100, compound="left", text_color="black",
#                                     fg_color="transparent",
#                                     hover_color="#CDCDCB",
#                                     command=opcoes)
#     Opcoes.place(x=325, y=825)

#     img4 = customtkinter.CTkImage(Image.open("Cora.png").resize((20, 20)))

#     Favoritos = customtkinter.CTkButton(master=Caixa, image=img4, text="", width=50, height=20, corner_radius=100, compound="left", text_color="black",
#                                     fg_color="transparent",
#                                     hover_color="#CDCDCB")
#     Favoritos.place(x=200, y=825)


#     Perfil.mainloop()






customtkinter.set_appearance_mode('ligth')


main = customtkinter.CTk()
main.geometry("500x800")
main.title("Página Principal")




Caixa = customtkinter.CTkFrame(master=main, width=450, height=900, corner_radius=50, fg_color="white")
Caixa.place(relx=0.5, rely=0.5, anchor=tkinter.CENTER)

Plano2 = customtkinter.CTkLabel(master=Caixa, text="World Refugees", font=("Century Gothic", 20))
Plano2.place(x=150, y=45)

search = customtkinter.CTkEntry(master=Caixa, placeholder_text='Search', text_color='#b5b5b5', font=('', 18),width=400, height=50, corner_radius=40)
search.place(x=25,y=100)

categorias = customtkinter.CTkLabel(master=Caixa, text= 'Categorias', font=('Century Gothic', 20))
categorias.place(x=30,y=165)

botao1 = customtkinter.CTkButton(master=Caixa, text='Europa', corner_radius=50, fg_color='#EFB810', width=115, height=30, text_color='black', hover_color='#a87b05')
botao1.place(x=30,y=210)


botao2 = customtkinter.CTkButton(master=Caixa, text='África', corner_radius=50, fg_color='#EFB810', width=115, height=30, text_color='black', hover_color='#a87b05')
botao2.place(x=165,y=210)


botao3 = customtkinter.CTkButton(master=Caixa, text='Ásia', corner_radius=50, fg_color='#EFB810', width=115, height=30, text_color='black', hover_color='#a87b05')
botao3.place(x=300,y=210)


Caixa2 = customtkinter.CTkFrame(master=Caixa, width=300, height=450, fg_color="#A5B4C2", corner_radius=15)
Caixa2.place(relx=0.5, rely=0.5, anchor=tkinter.CENTER)
Caixa2.place(x=0, y=90)


img2 = customtkinter.CTkImage(Image.open("home-removebg-preview.png").resize((20, 20)))

Home = customtkinter.CTkButton(master=Caixa, image=img2, text="", width=50, height=20, corner_radius=100, compound="left", text_color="black",
                                fg_color="transparent",
                                hover_color="#CDCDCB")
Home.place(x=75, y=825)

img3 = customtkinter.CTkImage(Image.open("opcoes-removebg-preview.png").resize((20, 20)))

Opcoes = customtkinter.CTkButton(master=Caixa, image=img3, text="", width=50, height=20, corner_radius=100, compound="left", text_color="black",
                                fg_color="transparent",
                                hover_color="#CDCDCB"
                            )
Opcoes.place(x=325, y=825)

img4 = customtkinter.CTkImage(Image.open("Cora.png").resize((20, 20)))

Favoritos = customtkinter.CTkButton(master=Caixa, image=img4, text="", width=50, height=20, corner_radius=100, compound="left", text_color="black",
                                fg_color="transparent",
                                hover_color="#CDCDCB")
Favoritos.place(x=200, y=825)



main.mainloop()