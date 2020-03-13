from tkinter import *
import tkinter
import tkinter.font as font
from tkinter.messagebox import *


# *** GUI ***
win = tkinter.Tk()
win.title('Data Structure')
win.geometry("500x500")
win.resizable(0, 0)


# Stack Class
class Stack:
    def __init__(self, max_st):
        self.items = []
        self.max = max_st

    def push(self, item):
        if len(self.items) == self.max:
            return -1
        else:
            self.items.append(item)

    def pop(self):
        if self.items == []:
            return -1
        else:
            self.items.pop()

    def empty(self):
        if self.items == []:
            return 1
        else:
            return 0

    def top(self):
        if self.items == []:
            return -1
        else:
            return int(len(self.items) - 1)


# Stack GUI
nameFont = font.Font(family='맑은 고딕', size=40)

stack_nameLabel = Label(win, text="Stack", font=nameFont)
stack_nameLabel.place(x=50, y=30)

size_label = Label(win, text="Stack size (1~10)")
size_label.place(x=50, y=120)

size_entry = Entry(win)
size_entry.place(x=52, y=140, width=50, height=20)

# Create initialized stack
st = Stack(0)


# Create stack box
def st_box(max_stack):
    m = 1
    t_margin = (max_stack - 1) * m
    box_h = (360 - t_margin) / max_stack
    start_x = 20
    start_y = 20
    end_x = 180
    end_y = 20 + box_h

    for i in range(0, max_stack):
        cvs.create_rectangle((start_x, start_y+(box_h+m)*i, end_x, end_y+(box_h+m)*i), fill="white")


# Get size of stack
def get_max():
    try:
        max_stack = int(size_entry.get())
        if 1 <= max_stack <= 10:
            Label(win, text="Stack size : " + str(max_stack)).place(x=50, y=160)
            global st, top_label, empty_label
            st = Stack(max_stack)
            st_box(max_stack)
            top_label = Label(win, text="Top " + str(st.top())).place(x=50, y=400)
            empty_label = Label(win, text="Empty " + str(st.empty())).place(x=50, y=420)
        else:
            showinfo("Error", "Enter integer 1~10 !!")
    except ValueError:
        showinfo("Error", "Enter integer 1~10 !!")


size_button = Button(win, text="Enter", command=get_max)
size_button.place(x=110, y=140, width=50, height=20)

stack_entry1 = Entry(win)
stack_entry1.place(x=110, y=200, width=50, height=30)

top_label = Label(win, text="Top "+str(st.top())).place(x=50, y=400)
empty_label = Label(win, text="Empty "+str(st.empty())).place(x=50, y=420)

# Execute push function
txt_list = []


def push_txt(obj, item):
    m = 1
    t_margin = (obj.max - 1) * m
    box_h = (360 - t_margin) / obj.max
    start_x = 20
    start_y = 20
    end_x = 180
    i = (obj.max - 1) - obj.top()  # insert bottom up

    tmp = cvs.create_text(start_x+(end_x-start_x)/2, (start_y+(box_h+m)*i)+(box_h/2), text=item, font=("", 20))
    txt_list.append(tmp)


def st_push():
    global st, top_label, empty_label
    if st.max > 0:
        if st.top() == st.max - 1:
            showinfo("Full", "Stack is full state!")
        else:
            st.push(stack_entry1.get())
            push_txt(st, stack_entry1.get())
            top_label = Label(win, text="Top " + str(st.top())).place(x=50, y=400)
            empty_label = Label(win, text="Empty " + str(st.empty())).place(x=50, y=420)
    else:
        showinfo("Error", "Set stack size!")


stack_button1 = Button(win, text="Push", command=st_push)
stack_button1.place(x=50, y=200, width=50, height=30)


# Execute pop function
def pop_txt():
    cvs.delete(txt_list[len(txt_list)-1])
    txt_list.pop()


def st_pop():
    global st, top_label, empty_label
    if st.max > 0:
        if st.empty() == TRUE:
            showinfo("Empty", "Stack is empty!")
        else:
            st.pop()
            pop_txt()
            top_label = Label(win, text="Top " + str(st.top())).place(x=50, y=400)
            empty_label = Label(win, text="Empty " + str(st.empty())).place(x=50, y=420)
    else:
        showinfo("Error", "Set stack size!")


stack_button2 = Button(win, text="Pop", command=st_pop)
stack_button2.place(x=50, y=250, width=50, height=30)


cvs = Canvas(win, bg="black", width=200, height="400")
cvs.create_rectangle((10, 10, 190, 390), fill="white")
cvs.place(x=250, y=50)

win.mainloop()
