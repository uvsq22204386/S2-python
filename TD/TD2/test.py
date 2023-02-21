from tkinter import*

root  = Tk()

canvas = Canvas(root , bg = "black", width = 500 , height = 500)

couleur  = Button(root , text = "Choisir une couleur" , font = ("helvetica", "10"))

couleur.grid(row = 0, column = 0 , sticky = "n")
canvas.grid(row = 0 , column = 0)

root.mainloop()

