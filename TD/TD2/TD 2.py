import tkinter as tk

CANVAS_WIDTH, CANVAS_HEIGHT = 600, 400


root = tk.Tk()

canvas = tk.Canvas(root, width = CANVAS_WIDTH + 200, height = CANVAS_HEIGHT + 200)

# Début de votre code
x0 = 100
x1 = CANVAS_WIDTH - 100
y = CANVAS_HEIGHT / 2
canvas.create_line(y, x0, y, x1)
canvas.create_oval(y +  50, x0 - 50, y - 50, x0 + 50)
canvas.create_oval(y + 50, x1 - 50, y - 50, x1 + 50)
canvas.create_oval(y + 50, (x0 + x1) / 2 - 50, y - 50, (x0 + x1) / 2 + 50)
    
# Fin de votre code
canvas.grid()
root.mainloop()