from tkinter import *
from random import randint

root = Tk()
root.title('Flash Card')
root.geometry("550x410")


#List of words in japanese add more to list
words = [ 
         (("あ") , ("A")),
         (("い") , ("I")),
         (("う") , ("U")),
         (("え") , ("E")),
         (("お") , ("O"))   

]

#get amount of word list

count = len(words)

def next():
    global random_word
    #Create random word selection
    random_word = randint(0, count - 1)
    #update Lable word
    jap_word.config(text = words [random_word][0])

def anwser():
    if my_entry.get().capitalize() == words[random_word][1]:
        answer_label.config(text=f"Correct {words[random_word][0]} is {words[random_word][1]}" )
    else:
        answer_label.config(text=f"Incorrect! {words[random_word][0]} is not {my_entry.get().capitalize()}")

jap_word = Label(root, text = "", font=("Sans-serif ", 20))
jap_word.pack(pady = 50)

answer_label = Label(root, text = "")
answer_label.pack(pady=20)

my_entry = Entry(root, font = ("Sans-serif"))
my_entry.pack(pady=20)

#Create Button 
button_frame = Frame(root)
button_frame.pack(pady=20)

answer_button = Button(button_frame, text="Answer", command=anwser)
answer_button.grid(row = 0, column=0 , padx=20)

next_button = Button(button_frame, text="Next", command = next)
next_button.grid(row = 0, column=1)

hint_button = Button(button_frame, text="Hint")
hint_button.grid(row = 0, column=2 , padx=20)


#Create a hint lable

hint_label = Label(root, text="")
hint_label.pack(pady = 20)


#Run next function when it start up 
next()



root.mainloop()



