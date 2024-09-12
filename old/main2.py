from tkinter import *
# from tkinter.ttk import *
from tkinter import ttk
import tkinter
import tkinter.scrolledtext as st

root = Tk();

root.title("Tkinter")
root.geometry("500x500")

#########
#########
#############
#Select option
# ttk.Label(root,text='Combobox Example',background='yellow',foreground='black',font=('Times new Roman',15)).grid(row=0,column=1)

# ttk.Label(root,text='Select the Month :',font=('Times New roman',10)).grid(column=0,row=5,padx=10,pady=25)

# #select option
# n = tkinter.StringVar()
# monthchoosen = ttk.Combobox(root,width=27,textvariable=n)

# monthchoosen['values'] = ('January','February','March',
#                           'April','May','June','July','August',
#                           'September','October','November','December')

# monthchoosen.grid(column=1,row=5)
# monthchoosen.current()

#######
##########
##########
# def click():
#     print('Button Clicked')

# frame = Frame(root)
# frame.pack()

#ferme l'application lorsqu'on appuie sur le bouton
# button = Button(frame,text='Turtle Button',command=root.destroy)
# button.pack()

###########
##########
##########
#Page de connexion
# label = Label(root,text='Connexion')
# label.pack()

# user_name = Label(root,text="Username")
# user_name.place(x=40,y=60)

# user_password = Label(root,text='Password')
# user_password.place(x=40,y=100)

# submit_button = Button(root,text='Connecter')
# submit_button.place(x=40,y=130)

# user_name_input_area = Entry(root,width=30)
# user_name_input_area.place(x=110,y=60)

# user_password_input_area = Entry(root,width=30,show='*')
# user_password_input_area.place(x=110,y=100)

########
########
###########
#radio button
# v = StringVar(root,'1')
# values = {
#     "RadioButton 1" : "1",
#     "RadioButton 2" : "2",
#     "RadioButton 3" : "3",
#     "RadioButton 4" : "4",
#     "RadioButton 5" : "5"
# }

# for(text,value) in values.items():
#     Radiobutton(root,text = text,variable = v,value = value).pack(ipady=5)

#########
#########
#############
#checkbox
# w = Label(root,text='Turtle Code',font='50')
# w.pack()

# checkButton1 = IntVar()
# checkButton2 = IntVar()
# checkButton3 = IntVar()

# button1 = Checkbutton(root,text='Tutorial',variable=checkButton1,onvalue=1,offvalue=0,width=10)
# button1.pack()

# button2 = Checkbutton(root,text='Student',variable=checkButton2,onvalue=1,offvalue=0,width=10)
# button2.pack()

# button3 = Checkbutton(root,text='Course',variable=checkButton3,onvalue=1,offvalue=0,width=10)
# button3.pack()

########
########
############
#forme geometrique
# c = Canvas(root, bg='yellow',height=250,width=300)
# line = c.create_line(108,120,320,40,fill='green')

# arc = c.create_arc(180,150,80,210)

# oval = c.create_oval(80,30,140,150,fill='red')

# c.pack()


##############
##############
##############
#formulaire de connexion 2eme version
name_var = tkinter.StringVar()
passw_var = tkinter.StringVar()

def submit():
    name = name_var.get()
    password = passw_var.get()

    print("The name is :" + name)
    print("The password is : " + password)
 
    name_var.set("")
    passw_var.set("")

name_label = tkinter.Label(root,text='Username',font=('calibre',10,'bold'))
name_label.grid(row=0,column=0)

name_entry = tkinter.Entry(root,textvariable=name_var,font=('calibre',10,'normal'))
name_entry.grid(row=0,column=1)

passw_label = tkinter.Label(root,text='Password',font=('calibre',10,'bold'))
passw_label.grid(row=1,column=0)

passw_entry = tkinter.Entry(root,textvariable=passw_var,font=('calibre',10,'normal'),show='*')
passw_entry.grid(row=1,column=1)

sub_btn = tkinter.Button(root,text='Connexion',command=submit)
sub_btn.grid(row=2,column=1)

########
#####################
#####################
#Questionnaire
# def Take_input():
#     input = inputtxt.get('1.0','end-1c')
#     print(input)
#     if(input == '120'):
#         output.insert(END,"Correct\n")
#     else:
#         output.insert(END,"Wrong answer\n")

# l = Label(text='What is 24 * 5 ?')
# l.pack()

# inputtxt = Text(root,height=10,width=25,bg='light yellow')
# inputtxt.pack()

# output = Text(root,height=5,width=25,bg='light cyan')
# output.pack()

# display = Button(root,height=2,width=20,text='Show',command=lambda:Take_input())
# display.pack()

########
########

# w = Label(root,text='Turtle Code',font='50')
# w.pack()

# msg = Message(root,text='Turtle Code Youtube Channel')

# msg.pack()

########33
#############
#############
#Menu
# menuBar = Menu(root)

# file = Menu(menuBar,tearoff=0)
# menuBar.add_cascade(label='File',menu= file)

# root.config(menu=menuBar)
# file.add_command(label='New File')
# file.add_command(label='Open...')
# file.add_command(label='Save...')
# file.add_separator()
# file.add_command(label='Exit',command=root.destroy)

# edit = Menu(menuBar,tearoff=0)
# menuBar.add_cascade(label='Edit',menu=edit)
# edit.add_command(label='Cut')
# edit.add_command(label='Copy')
# edit.add_command(label='Paste')
# edit.add_command(label='Select all')
# edit.add_separator()
# edit.add_command(label='Find')
# edit.add_command(label='Find again')

# help = Menu(menuBar,tearoff=0)
# menuBar.add_cascade(label='Help',menu=help)
# help.add_command(label='tk help')
# help.add_command(label='Demo')
# help.add_separator()
# help.add_command(label='About tk')

#########
########
###########
#counter input
# w = Label(root,text='Turtle Code Counter')
# w.pack()

# sp = Spinbox(root,from_=0,to=20)
# sp.pack()

#############
###########
##############
#progress bar
# progress =ttk.Progressbar(root,orient='horizontal',length=100,mode='determinate')

# def bar():
#     import time
#     progress['value'] = 20
#     root.update_idletasks()
#     time.sleep(1)

#     progress['value'] = 40
#     root.update_idletasks()
#     time.sleep(1)

#     progress['value'] = 50
#     root.update_idletasks()
#     time.sleep(1)

#     progress['value'] = 60
#     root.update_idletasks()
#     time.sleep(1)

#     progress['value'] = 80
#     root.update_idletasks()
#     time.sleep(1)

#     progress['value'] = 100

    
# progress.pack(pady=10)

# Button(root,text='start',command=bar).pack(pady=10)

###############
############3
##########3
#Scroll_Bar
# w = Label(root,text='Turtle Code',font='50')
# w.pack()

# scroll_bar = Scrollbar(root)

# scroll_bar.pack(side=RIGHT,fill=Y)

# myList = Listbox(root,yscrollcommand=scroll_bar.set)

# for line in range(1,26):
#     myList.insert(END,"Geeks" + str(line))

# myList.pack(side=LEFT,fill=BOTH)

# scroll_bar.config(command=myList.yview)


#############
#############
############# text area
# ttk.Label(root,text='Scroll',font="Times New Roman,15",background='green',foreground='white').grid(row=0,column=0)

# text_area = st.ScrolledText(root,width='30',height='8',font="Times New Roman,15")

# text_area.grid(column=0,pady=10,padx=10)

# text_area.configure(state='normal')

#############
#############
############# List box
# listBox = Listbox(root,height=10,width=15,
#                   bg='green',activestyle='dotbox',
#                   font='Helvetica',fg='yellow')

# label = Label(root,text='Food Items')

# listBox.insert(1,"Nachos")
# listBox.insert(2,"Spagheti")
# listBox.insert(3,"Atieke")

# label.pack()
# listBox.pack()

#############3
#################
####################3
#button pack
# w = Label(text='Turtle Code',font='50')
# w.pack()

# frame = Frame(root)
# frame.pack()

# bottomFrame = Frame(root)
# bottomFrame.pack(side=BOTTOM)

# b1_button = Button(frame,text='Turtel',fg='red')
# b1_button.pack(side=LEFT)

# b2_button = Button(frame,text='Turtle2',fg='brown')
# b2_button.pack(side=LEFT)

# b3_button = Button(frame,text='Turtle3',fg='brown')
# b3_button.pack(side=LEFT)

# b4_button = Button(bottomFrame,text='Turtle4',fg='brown')
# b4_button.pack(side=BOTTOM)

# b5_button = Button(bottomFrame,text='Turtle5',fg='brown')
# b5_button.pack(side=BOTTOM)

# b6_button = Button(bottomFrame,text='Turtle6',fg='brown')
# b6_button.pack(side=BOTTOM)

##################3
#####################
############## Scale
# v1 = DoubleVar()

# def show1():
#     sel = 'horizontal Scale value' + str(v1.get())
#     l1.config(text= sel,font=("Courrier",14))

# s1 = Scale(root,variable=v1,from_=1,to=100,orient=HORIZONTAL)

# l3 = Label(root,text="Horizonta Scaler")

# b1 = Button(root,text='Display Horizontal',command=show1,bg='yellow')

# l1 = Label(root)

# s1.pack(anchor=CENTER)
# l3.pack()

# b1.pack(anchor=CENTER)
# l1.pack()

##############3
#############333
############treeview
# ttk.Label(root,text='Treeview').pack()

# treeview = ttk.Treeview(root)

# treeview.pack()

# treeview.insert('',0,'item1',text='Turtle code')
# treeview.insert('',1,'item2',text='Turt code')
# treeview.insert('',2,'item3',text='Tule code')
# treeview.insert('','end','item4',text='Turtle code')

root.mainloop()