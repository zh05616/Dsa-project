#####################################DSA Final Project################################
#######################Syed Muhammad Abdullah Al Muttaqui,Zain Ul Haq, Ali Zain Sardar######################
################################sa06146,zh05616,as06998#######################################

from tkinter import *
from tkinter import ttk
import random
import time

###############################################colours###########################################

RED = '#F22810'
DARK_GRAY = '#65696B'
LIGHT_GRAY = '#C4C5BF'
PURPLE = '#BF01FB'
BLUE = '#0CA8F6'
YELLOW = '#F7E806'
DARK_BLUE = '#4204CC'
WHITE = '#FFFFFF'
BLACK = '#000000'
LIGHT_GREEN = '#05F50E'
PINK = '#F50BED'
ALICE_BLUE = '#F0F8FF'
DARK_GRAY = '#A9A9A9'
DARK_MAGENTA = '#8B008B'
DARK_ORANGE = '#FF8C00'



#########################################merge_sort######################################################

def merge(data, start, mid, end, bars, timeTick):
    arr_temp = []
    ending = mid + 1
    starting = start
    

    for i in range(start, end+1):
        if starting > mid:
            arr_temp.append(data[ending])
            ending+=1
        elif ending > end:
            arr_temp.append(data[starting])
            starting+=1
        elif data[starting] < data[ending]:
            arr_temp.append(data[starting])
            starting+=1
        else:
            arr_temp.append(data[ending])
            ending+=1

    for starting in range(len(arr_temp)):
        data[start] = arr_temp[starting]
        start += 1

def merge_sort(data, start, end, bars, timeTick):
    if start < end:
        mid = int((start + end) / 2)
        merge_sort(data, start, mid, bars, timeTick)
        merge_sort(data, mid+1, end, bars, timeTick)

        merge(data, start, mid, end, bars, timeTick)

        bars(data, [PURPLE if x >= start and x < mid else YELLOW if x == mid 
                        else DARK_MAGENTA if x > mid and x <=end else BLUE for x in range(len(data))])
        time.sleep(timeTick)

    bars(data, [BLUE for x in range(len(data))])


#######################################quick_sort########################################

def partition(data, start, end, bars, timeTick):
    i = start + 1
    pivot = data[start]

    for j in range(start+1, end+1):
        if data[j] < pivot:
            data[i], data[j] = data[j], data[i]
            i+=1
    data[start], data[i-1] = data[i-1], data[start]
    return i-1

def quick_sort(data, start, end, bars, timeTick):
    if start < end:
        pivot_position = partition(data, start, end, bars, timeTick)
        quick_sort(data, start, pivot_position-1, bars, timeTick)
        quick_sort(data, pivot_position+1, end, bars, timeTick)

        bars(data, [PURPLE if x >= start and x < pivot_position else YELLOW if x == pivot_position
                        else DARK_ORANGE if x > pivot_position and x <=end else BLUE for x in range(len(data))])
        time.sleep(timeTick)
        
    bars(data, [BLUE for x in range(len(data))])




###################################selection _sort#############################################

def selection_sort(data, bars, timeTick):
    for i in range(len(data)-1):
        minimum = i
        for k in range(i+1, len(data)):
            if data[k] < data[minimum]:
                minimum = k

        data[minimum], data[i] = data[i], data[minimum]
        bars(data, [YELLOW if x == minimum or x == i else BLUE for x in range(len(data))] )
        time.sleep(timeTick)
        
    bars(data, [BLUE for x in range(len(data))])

###############################################insertion_sort###########################################

def insertion_sort(data, bars, timeTick):
    for i in range(len(data)):
        temp = data[i]
        k = i
        while k > 0 and temp < data[k-1]:
            data[k] = data[k-1]
            k -= 1
        data[k] = temp
        bars(data, [ALICE_BLUE if x == k or x == i else DARK_GRAY for x in range(len(data))])
        time.sleep(timeTick)
        
    bars(data, [BLUE for x in range(len(data))])

#################################################bubble_sort##########################################

def bubble_sort(data, bars, timeTick):
    lenght = len(data)
    for i in range(lenght-1):
        for j in range(lenght-i-1):
            if data[j] > data[j+1]:
                data[j], data[j+1] = data[j+1], data[j]
                bars(data, [YELLOW if x == j or x == j+1 else BLUE for x in range(len(data))] )
                time.sleep(timeTick)
                
    bars(data, [BLUE for x in range(len(data))])


#############################################Main screen###########################################
screen = Tk()
screen.title("DSA Sorting Algorithms Visualizer")
screen.maxsize(1000, 800)
screen.config(bg = 'black')
# welcome = ttk.Label(text="Hello")
# welcome.pack()

info = []
select_spd = StringVar()
name_algo = StringVar()
speed_list = ['Fast', 'Medium', 'Slow']
algo_list = ['Merge Sort','Selection Sort', 'Quick Sort', 'Bubble Sort','Insertion Sort' ]

def sort():
    global info
    timeTick = set_speed()
    
    if algo_menu.get() == 'Insertion Sort':
        insertion_sort(info, bars, timeTick)
    elif algo_menu.get() == 'Selection Sort':
        selection_sort(info, bars, timeTick)
    elif algo_menu.get() == 'Quick Sort':
        quick_sort(info, 0, len(info)-1, bars, timeTick)
    elif algo_menu.get() == 'Bubble Sort':
        bubble_sort(info, bars, timeTick)
    elif algo_menu.get() == 'Merge Sort':
        merge_sort(info, 0, len(info)-1, bars, timeTick)


def set_speed():
    if speed_menu.get()=='Fast':
        return 0.001
    elif speed_menu.get() == 'Medium':
        return 0.01
    else:
        return 0.1

###########################draw numerical arrays as well as bars#####################################

def bars(info, colorArray):
    canvas.delete("all")
    gap_between = 5
    height_canva = 400
    left_space = 5
    Width_canva = 800
    width = Width_canva / (len(info) + 1)
    normalizedData = [i / max(info) for i in info]

    for i, height in enumerate(normalizedData):
        axis_yone = height_canva
        axis_xone = (i + 1) * width + left_space
        axis_yzero = height_canva - height * 390
        axis_xzero = i * width + left_space + gap_between
        canvas.create_rectangle(axis_xzero, axis_yzero, axis_xone, axis_yone, fill=colorArray[i])

    screen.update_idletasks()

########################################random arrays generator###############################

def random_array_generator():
    global info
    info = []
    for i in range(0, 100):
        random_value = random.randint(1, 150)
        info.append(random_value)
    bars(info, [BLACK for x in range(len(info))])

########################################User Interface##############################################
Screen_UserInterface = Frame(screen, width= 900, height=300, bg='black')
Screen_UserInterface.grid(row=0, column=0, padx=10, pady=5)

Second_label = Label(Screen_UserInterface, text="Sorting Speed: ", bg='grey')
Second_label.grid(row=1, column=0, padx=10, pady=10, sticky=W)
speed_menu = ttk.Combobox(Screen_UserInterface, textvariable=select_spd, values=speed_list)
speed_menu.grid(row=1, column=1, padx=10, pady=10)
speed_menu.current(0)

First_label = Label(Screen_UserInterface, text="Please Select An Algorithm: ", bg='grey')
First_label.grid(row=0, column=0, padx=10, pady=5, sticky=W)
algo_menu = ttk.Combobox(Screen_UserInterface, textvariable=name_algo, values=algo_list)
algo_menu.grid(row=0, column=1, padx=5, pady=5)
algo_menu.current(0)

canvas = Canvas(screen, width=800, height=400, bg='grey')
canvas.grid(row=1, column=0, padx=10, pady=10)

second_button = Button(Screen_UserInterface, text="Generate Array", command=random_array_generator, bg=LIGHT_GRAY)
second_button.grid(row=2, column=0, padx=0, pady=5)

first_button= Button(Screen_UserInterface, text="Sort", command=sort, bg=LIGHT_GRAY)
first_button.grid(row=2, column=1, padx=5, pady=5)




screen.mainloop()
