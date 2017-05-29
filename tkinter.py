from tkinter import *
from tkinter.messagebox import *

from threading import Timer
def timerDone(text):
    text.delete('1.0', END)  # Удалить все
    text.insert(1.0, 'Добавить Текст\n\ в начало первой строки')
window = Tk()
window.title('Сжигание порубочных остатков')
window.geometry('500x200+300+200')
text1 = Text(window, height=5, width=60, font='Arial 14', wrap=WORD)
text1.pack()

mainTimer = Timer(3.0, timerDone(text1))
mainTimer.start()
window.mainloop()

# def hello():
#     print("hello, world")
#
# t = time.Timer(30.0, hello)
#
# t.start() # after 30 seconds, "hello, world" will be printed