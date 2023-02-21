from tkinter import*

root  = Tk()

canvas = Canvas(root , bg = "black", width = 500 , height = 500)

couleur  = Button(root , text = "Choisir une couleur" , font = ("helvetica", "10"))
cercle = Button(root , text = "Cercle" , font = ("helvetica", "10"))
carre = Button(root , text = "Carré" , font = ("helvetica", "10"))
croix = Button(root , text = "Croix" , font = ("helvetica", "10"))

canvas.grid(row = 2 , column = 0)
couleur.grid(row = 0, column = 0)
cercle.grid(row = 1, column = 0, sticky = "w")
carre.grid(row = 2, column = 0, sticky = "w")
croix.grid(row = 3, column = 0, sticky = "w")


root.mainloop()