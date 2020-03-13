from tkinter import *
import tkinter
import tkinter.font as font
from tkinter.messagebox import *


# *** GUI ***
win = tkinter.Tk()
win.title('Data Structure')
win.geometry("500x500")
win.resizable(0, 0)


class Queue:
    def __init__(self, q_max):
        self.items = []
        self.max = int(q_max)
        self.front = -1
        self.rear = -1

    def next_idx(self, idx):
        return (idx + 1) % self.max

    def is_empty(self):
        if self.front == -1:
            return True
        else:
            return False

    def is_full(self):
        if self.next_idx(self.rear) == self.front:
            return True
        else:
            return False

    def enqueue(self, item):
        if self.is_full() is True:
            return -1
        else:
            self.items.append(item)
            if len(self.items) == 1:
                self.front = self.next_idx(self.front)
                self.rear = self.next_idx(self.rear)
            else:
                self.rear = self.next_idx(self.rear)

    def deque(self):
        if self.is_empty() is True:
            return -1
        else:
            self.items.pop(0)
            if self.items == []:
                self.front = -1
                self.rear = -1
            else:
                self.front = self.next_idx(self.front)


# Queue GUI
nameFont = font.Font(family='맑은 고딕', size=40)

q_nameLabel = Label(win, text="Circular Queue", font=nameFont).place(x=50, y=30)
size_label = Label(win, text="Queue size (1~10)").place(x=50, y=120)
size_entry = Entry(win)
size_entry.place(x=52, y=140, width=50, height=20)

# Create initialized queue
q = Queue(0)


# Create queue box
def q_box(max_q):
    m = 1
    t_margin = (max_q - 1) * m
    box_w = (470 - t_margin) / max_q
    start_x = 10
    start_y = 10
    end_x = 10 + box_w
    end_y = 140

    for i in range(0, max_q):
        cvs.create_rectangle((start_x+(box_w+m)*i, start_y, end_x+(box_w+m)*i, end_y), fill="white")


front_label = Label(win, text="Front "+str(q.front)).place(x=50, y=190)
rear_label = Label(win, text="Rear "+str(q.rear)).place(x=50, y=210)
front_txt = Label(win, text="F", font=('', 10))
front_txt.place(x=5, y=265)
rear_txt = Label(win, text="R", font=('', 10))
rear_txt.place(x=5, y=280)


# Get size of queue
def get_max():
    try:
        max_q = int(size_entry.get())
        if 1 <= max_q <= 10:
            Label(win, text="Queue size : " + str(max_q)).place(x=50, y=160)
            global q, front_label, rear_label, front_txt, rear_txt, txt_list
            q = Queue(max_q)
            q_box(max_q)
            front_label = Label(win, text="Front " + str(q.front)).place(x=50, y=190)
            rear_label = Label(win, text="Rear " + str(q.rear)).place(x=50, y=210)
            front_txt.place(x=5, y=265)
            rear_txt.place(x=5, y=280)
            txt_list = []
        else:
            showinfo("Error", "Enter integer 1~10 !!")
    except:
        showinfo("Error", "Enter integer 1~10 !!")


size_button = Button(win, text="Enter", command=get_max)
size_button.place(x=110, y=140, width=50, height=20)

# Enqueue
q_entry1 = Entry(win)
q_entry1.place(x=360, y=130, width=50, height=30)

# Execute push function
txt_list = []


def enqueue_txt(obj, item):
    global front_txt, rear_txt
    m = 1
    t_margin = (obj.max - 1) * m
    box_w = (470 - t_margin) / obj.max
    start_x = 10
    start_y = 10
    end_y = 140
    i = obj.rear

    tmp = cvs.create_text(start_x+(box_w+m)*i+(box_w/2), (start_y+(end_y-start_y)/2), text=item, font=("", 20))
    txt_list.append(tmp)
    if obj.front == 0 and obj.rear == 0:
        front_txt.place(x=start_x+(box_w+m)*i+(box_w/2), y=265)
        rear_txt.place(x=start_x+(box_w+m)*i+(box_w/2), y=280)
    else:
        front_txt.place(y=280)
        rear_txt.place(x=start_x + (box_w + m) * i + (box_w / 2), y=280)


def q_enqueue():
    global q, front_label, rear_label, front_txt
    if q.max > 0:
        if q.is_full() is True:
            showinfo("Full", "Queue is full state!")
        else:
            q.enqueue(q_entry1.get())
            enqueue_txt(q, q_entry1.get())
            front_label = Label(win, text="Front " + str(q.front)).place(x=50, y=190)
            rear_label = Label(win, text="Rear " + str(q.rear)).place(x=50, y=210)
    else:
        showinfo("Error", "Set queue size!")


q_button1 = Button(win, text="Enqueue", command=q_enqueue)
q_button1.place(x=300, y=130, width=50, height=30)


# Execute deque function
def deque_txt(obj):
    global front_txt, rear_txt
    m = 1
    t_margin = (obj.max - 1) * m
    box_w = (470 - t_margin) / obj.max
    start_x = 10
    i = obj.front

    cvs.delete(txt_list[0])
    txt_list.pop(0)

    if obj.front == obj.rear:
        front_txt.place(x=start_x + (box_w + m) * i + (box_w / 2), y=265)
        rear_txt.place(x=start_x + (box_w + m) * i + (box_w / 2), y=280)
    else:
        front_txt.place(x=start_x + (box_w + m) * i + (box_w / 2), y=280)


def q_deque():
    global q, front_label, rear_label, front_txt, rear_txt
    if q.max > 0:
        if q.is_empty() is True:
            showinfo("Empty", "Queue is empty!")
        else:
            q.deque()
            deque_txt(q)
            front_label = Label(win, text="Front " + str(q.front)).place(x=50, y=190)
            rear_label = Label(win, text="Rear " + str(q.rear)).place(x=50, y=210)
            if q.is_empty() is True:
                front_txt.place(x=5, y=265)
                rear_txt.place(x=5, y=280)
    else:
        showinfo("Error", "Set queue size!")


q_button2 = Button(win, text="Deque", command=q_deque)
q_button2.place(x=300, y=170, width=50, height=30)

# Create Canvas
cvs = Canvas(win, bg="black", width=490, height="150")
cvs.create_rectangle((10, 10, 480, 140), fill="white")
cvs.place(x=5, y=300)

win.mainloop()
