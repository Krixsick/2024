from tkinter import *
import pandas as pd
import random
BACKGROUND_COLOR = "#B1DDC6"
CARD_FRONT_COLOR = "#FFFFFF"
window = Tk()
window.title("Guess")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)


currentCard = {}
cardsToLearn = {}

try:
    data = pd.read_csv("wordsToLearn.csv")
except FileNotFoundError:
    originalData = pd.read_csv("data/french_words.csv")
    cardsToLearn = originalData.to_dict(orient="records")
else:
    cardsToLearn = data.to_dict(orient="records")
    
def nextCard(): 
    global currentCard
    currentCard = random.choice(cardsToLearn)
    frenchWordReplacement(currentCard["French"])
    window.after(3000, englishWordReplacement)


def frenchWordReplacement(frenchWord):
    canvas.itemconfig(cardImg, image=backGroundImg)
    canvas.itemconfig(word, text=frenchWord, fill="black")
    canvas.itemconfig(language, text="French", fill="black")
    
    
def englishWordReplacement():
    canvas.itemconfig(cardImg, image=cardBackImg)
    canvas.itemconfig(word, text=currentCard["English"], fill="white")
    canvas.itemconfig(language, text="English", fill="white")


def correctClick():
    cardsToLearn.remove(currentCard)
    data = pd.DataFrame(cardsToLearn)
    data.to_csv("data/words_to_learn.csv", index=False)
    nextCard()





#Canvas
canvas = Canvas(window, width=800, height=526, bg=BACKGROUND_COLOR,highlightthickness=0, bd=0)
canvas.grid(row=0, column=0, columnspan=2)

#Background Image
backGroundImg = PhotoImage(file="images/card_front.png")
cardImg = canvas.create_image(410, 263, image=backGroundImg)

language = canvas.create_text(400, 150, text="French", font=("Arial", 40, "italic"), fill="black")
word = canvas.create_text(400, 263, text="trouve", font=("Arial", 60, "bold"), fill="black")

#Card Back Image
cardBackImg = PhotoImage(file="images/card_back.png")

# Load images
xImage = PhotoImage(file="images/wrong.png")
correctImage = PhotoImage(file="images/right.png")

# Create buttons with images
xButton = Button(window, image=xImage, command=nextCard, bg=CARD_FRONT_COLOR, highlightthickness=0, bd=0)
xButton.grid(row=1, column=0)
correctButton = Button(window, image=correctImage, command=correctClick, bg=CARD_FRONT_COLOR, highlightthickness=0, bd=0)
correctButton.grid(row=1, column=1)

nextCard()
window.mainloop()