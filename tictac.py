import tkinter.messagebox
from tkinter import *

play =  Tk()
play.geometry('600x500')
play.title('Tic-Tac-Toe')
play.configure(bg="lightblue")

p1 = StringVar()
p2 = StringVar()
bclick = True
turns =0
buttons=StringVar()

def btnclick(buttons):
    global bclick,turns
    if buttons['text']==' 'and bclick == True:
        buttons['text']='X'
        bclick=False
        possibilities()
        turns+=1
    elif buttons['text']==' 'and bclick == False:
        buttons['text']='O'
        bclick=True
        possibilities()
        turns+=1
    else:
        tkinter.messagebox.showwarning('Tic-Tac-Toe','Buttons already clicked!...')

def possibilities():
    if(b1['text']=='X'and b2['text']=='X'and b3['text']=='X' or b4['text']=='X'and b5['text']=='X'and b6['text']=='X' or b7['text']=='X'and b8['text']=='X'and b9['text']=='X' or b1['text']=='X'and b4['text']=='X'and b7['text']=='X' or b2['text']=='X'and b5['text']=='X'and b8['text']=='X' or b3['text']=='X'and b6['text']=='X'and b9['text']=='X' or b1['text']=='X'and b5['text']=='X'and b9['text']=='X' or b3['text']=='X'and b5['text']=='X'and b7['text']=='X'):
        tkinter.messagebox.showinfo('Tic-Tac-Toe',p1.get()+'Wins!----')

    elif(b1['text']=='O'and b2['text']=='O'and b3['text']=='O' or b4['text']=='O'and b5['text']=='O'and b6['text']=='O' or b7['text']=='O'and b8['text']=='O'and b9['text']=='O' or b1['text']=='O'and b4['text']=='O'and b7['text']=='O' or b2['text']=='O'and b5['text']=='O'and b8['text']=='O' or b3['text']=='O'and b6['text']=='O'and b9['text']=='O' or b1['text']=='O'and b5['text']=='O'and b9['text']=='O' or b3['text']=='O'and b5['text']=='O'and b7['text']=='0'):
        tkinter.messagebox.showinfo('Tic-Tac-Toe',p2.get()+'Wins!----')

    elif turns==8:
        tkinter.messagebox.showinfo('Tic-Tac-Toe','Match Draw')

def reset():
    global turns, bclick
    turns = 0
    bclick = True

    # Clear the text of all buttons
    b1.config(text=' ')
    b2.config(text=' ')
    b3.config(text=' ')
    b4.config(text=' ')
    b5.config(text=' ')
    b6.config(text=' ')
    b7.config(text=' ')
    b8.config(text=' ')
    b9.config(text=' ')
    b10.config(command=reset)






Label(play,text='Tic-Tac-Toe',font=('calibri',30),fg='blue').place(x=200,y=10)
Label(play,text='player 1 Name',font=('calibri',20),bg='lightblue').place(x=70,y=80)

Label(play, text='player 2 Name', font=('calibri', 20), bg='lightblue').place(x=70, y=120)

Entry(play,textvariable=p1,font=('calibri',18)).place(x=280,y=80)
Entry(play, textvariable=p2, font=('calibri', 18)).place(x=280, y=120)

b1=Button(play,text=' ',font=('calibri',20,'bold'),bg='gray',fg='white',width='8',height='2',command=lambda:btnclick(b1))
b1.place(x=100,y=190)

b2=Button(play, text=' ', font=('calibri', 20, 'bold'), bg='gray', fg='white', width='8', height='2', command= lambda:btnclick(b2))
b2.place(x=230, y=190)

b3 =Button(play, text=' ', font=('calibri', 20, 'bold'), bg='gray', fg='white', width='8', height='2',
                    command=lambda: btnclick(b3))
b3.place(x=360, y=190)

b4 =Button(play, text=' ', font=('calibri', 20, 'bold'), bg='gray', fg='white', width='8', height='2',
                    command=lambda: btnclick(b4))
b4.place(x=100, y=290)

b5 = Button(play, text=' ', font=('calibri', 20, 'bold'), bg='gray', fg='white', width='8', height='2',
                    command=lambda: btnclick(b5))
b5.place(x=230, y=290)

b6 = Button(play, text=' ', font=('calibri', 20, 'bold'), bg='gray', fg='white', width='8', height='2',
                    command=lambda: btnclick(b6))
b6.place(x=360, y=290)

b7= Button(play, text=' ', font=('calibri', 20, 'bold'), bg='gray', fg='white', width='8', height='2',
                    command=lambda: btnclick(b7))
b7.place(x=100, y=390)

b8 = Button(play, text=' ', font=('calibri', 20, 'bold'), bg='gray', fg='white', width='8', height='2',
                    command=lambda: btnclick(b8))
b8.place(x=230, y=390)

b9 = Button(play, text=' ', font=('calibri', 20, 'bold'), bg='gray', fg='white', width='8', height='2',
                    command=lambda: btnclick(b9))
b9.place(x=360, y=390)

b10 = Button(play, text='Reset', font=('calibri', 15), bg='green', fg='white', width='10', height='1', command=reset)
b10.place(x=500, y=440)

# Repeat this for other buttons


play.mainloop()







