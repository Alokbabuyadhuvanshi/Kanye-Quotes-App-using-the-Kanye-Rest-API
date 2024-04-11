from tkinter import *
import requests

def get_quotes():
    response = requests.get("https://api.kanye.rest")
    response.raise_for_status()
    data = response.json()
    Quote = data["quote"]
    canvas.itemconfig(quotes_text, text = Quote)



window = Tk()
window.title("Kanya Says....")
window.config(padx=50,pady=50)

canvas = Canvas(width=400,height=400)
background_img = PhotoImage(file ="background.png")
canvas.create_image(200,200,image = background_img)
quotes_text = canvas.create_text(200, 130, text="Kanye Quote Goes HERE" , width = 210 ,font = "Cursive")
canvas.grid(row=0,column=0)
kanye_img = PhotoImage(file="philip-j.png")
kanye_button = Button(image =kanye_img ,highlightthickness=0,command=get_quotes)
kanye_button.grid(row=1,column=0)
window.mainloop()  