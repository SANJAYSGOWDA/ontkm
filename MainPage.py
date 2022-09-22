import os
from pydoc import visiblename
import pip
import tkinter as tk
from tkinter import *
from tkinter.font import BOLD
import tkinter.font as f
import numpy as np
import datetime as dt
from datetime import date, datetime
import time

from tkinter.filedialog import askdirectory
from tkinter import messagebox
from PIL import Image, ImageTk
from pypylon import pylon
import cv2
import threading
import math
from AppOpener import run
import sys
import subprocess
from subprocess import PIPE, run
import importlib
import torch
print(torch.cuda.is_available())

from detecto import core

EpochNumber = 0
BatchSizeNumber = 0
numberofVariant = 0
varn = 0
varcomparision = 0

variant_list = []





# function for color choosing
def rgb_hack(rgb):
    return "#%02x%02x%02x" % rgb


def annotates():
    try:
        reqs = subprocess.check_output([sys.executable, '-m', 'pip', 'freeze'])
        installed_packages = [r.decode().split('==')[0] for r in reqs.split()]
        #print(installed_packages)
        package_name = 'labelImg'
        spec = importlib.util.find_spec(package_name)
        if spec is None:
            print(package_name + " is not installed")
            subprocess.check_call([sys.executable, '-m', 'pip', 'install', '<packagename>'])
        else:
            os.system("labelImg")
        # if 'lblImg' in installed_packages:
        #     os.system("labelImg")
        # else:
        #     os.system("start /wait cmd /c {cd /pip install labelImg}")
        #     print(installed_packages)


        #os.system("start /wait cmd /c {cd /../}")
        #run("Google Chrome")
        #os.system("labelImg")
        # res = run('labelImg', shell=True, stdout=PIPE, stderr=PIPE, check=True)
        # print(res.returncode, res.stdout, res.stderr)
        # #os.system("pause")
    except Exception as e:
        #os.system('cmd /c "pip install labelimg"')
        # implement pip as a subprocess:
        print(e)
        # subprocess.check_call([sys.executable, '-m', 'pip', 'install', '<labelImg>'])
        # reqs = subprocess.check_output([sys.executable, '-m', 'pip','freeze'])
        # installed_packages = [r.decode().split('==')[0] for r in reqs.split()]
        # print(installed_packages)
    
        #os.system("pip install labelimg")
        # print("Download the following in command prompt with internet to load the models...")
        # print("pip install labelimg")
        # print(str(e))

# def installes():
#     subprocess.check_call([sys.executable, 'pip', 'install','<labelimg>'])
#     pass

def runn():
    global batch_sz
    global E_sz
    global EpochNumber
    global BatchSizeNumber
    
    E_sz = int(EpochNumber.get())
    batch_sz = int(BatchSizeNumber.get())

def compute():
    global varn
    varn = int(numberofVariant.get())


def addd():
    global varn
    global vrname
    global varcomparision
    
    try:
        print(varn)
        vrname = vartype.get()
        
        if varcomparision < varn:
            variant_list.append(vrname)
            vartype.delete('0', END)
            varcomparision += 1
        else:
            print("Out of Range")

        print(variant_list)
    except Exception as e:
        print(e)



        # for variant in range(0, int(varn)):
        #     if variant<=int(varn):
        #         variant_list.append(vrname)
        #         vartype.delete('0', END)
        #     else:
        #         print("more variants are being entered")
        # print(variant_list)
def filess():
    global my_dir
    global Text_box
    my_dir = askdirectory() # select directory 
    Text_box.insert(END, str(my_dir))
    #window.config(text=my_dir)

def trainn():
    global variant_list
    global batch_sz
    global E_sz
    global EpochNumber
    global BatchSizeNumber
    global Text_inp

    Text_inp = str(Text_box.get())
    
    E_sz = int(EpochNumber.get())
    batch_sz = int(BatchSizeNumber.get())

    Train_dataset=core.Dataset('Dataset/')
    loader=core.DataLoader(Train_dataset, batch_size=batch_sz, shuffle=True)
    model = core.Model(list(variant_list))
    model.fit(loader, epochs=E_sz, lr_step_size=5, learning_rate=0.001, verbose=True)
    model.save("model.pth")











window = tk.Tk()
window.state('zoomed')
window.title("REDBOT INSPECTION")
window.iconbitmap(r"D:\Code\TKM\Icon.ico")
window.geometry("1920x1080")
window['background'] = rgb_hack((200, 220, 200))#'red'     #'whitesmoke'


#Main Image and label frame
lblMainFrame = tk.Frame(window)
lblMainFrame.place(x=0,y=0)


lblRLogo = tk.Label(lblMainFrame)
lblRLogo.grid(row=0, column=0, sticky = "w")
RLogoImage = Image.open(r'D:\Code\TKM\Redbot.png')
RLogoImage.thumbnail((250, 300))
RLogoImage = ImageTk.PhotoImage(RLogoImage)
lblRLogo.configure(image = RLogoImage)
lblRLogo.grid(row=0, column=0)

lblEpochNumber = tk.Label(lblMainFrame, text = "REDBOT INNOVATIONS", fg = "black", bg= rgb_hack((200, 220, 200)))
lblEpochNumber.configure(font =("Times New Roman", 50, BOLD))
lblEpochNumber.grid(row=0, column=2)

# Annotation button frame location
lblAnnotateFrame = tk.Frame(window)
lblAnnotateFrame.place(x=200, y=200)

#Epoch and Batchsize frame

lblEandBFrame = tk.Frame(window)
lblEandBFrame.place(x=100, y=300)


btn_annotate = tk.Button(lblAnnotateFrame, text="ANNOTATE", command=annotates, bg=rgb_hack((255,0,0)), fg="white")
btn_annotate.configure(font=("Times New Roman", 18, BOLD))
btn_annotate.grid(row=0, column=0, sticky="nsew", padx=7, pady=7)


Epoch_var = tk.IntVar()
EpochNumber = tk.Entry(lblEandBFrame, textvariable=Epoch_var ,font=("Times New Roman", 18, BOLD))
EpochNumber.grid(row=0, column=1)

lblEpochNumber = tk.Label(lblEandBFrame, text = "Epoch Number: ", fg = "black")
lblEpochNumber.configure(font=("Times New Roman", 18, BOLD))
lblEpochNumber.grid(row=0, column=0)

Batch_var = tk.IntVar()
BatchSizeNumber = tk.Entry(lblEandBFrame, textvariable=Batch_var ,font=("Times New Roman", 18, BOLD))
BatchSizeNumber.grid(row=1, column=1)

lblBatchNumber = tk.Label(lblEandBFrame, text = "Batch Number: ", fg = "black")
lblBatchNumber.configure(font=("Times New Roman", 18, BOLD))
lblBatchNumber.grid(row=1, column=0)


btn_run = tk.Button(lblEandBFrame, text="UPDATE", command=runn, bg=rgb_hack((123,143,34)), fg="white")
btn_run.configure(font=("Times New Roman", 18, BOLD))
btn_run.grid(row=4, column=0, sticky="nsew", padx=7, pady=7)

# btn_annotate = tk.Button(lblAnnotateFrame, text="install", command=installes, bg=rgb_hack((255,0,0)), fg="white")
# btn_annotate.configure(font=("Times New Roman", 16, BOLD))
# btn_annotate.grid(row=0, column=1, sticky="nsew", padx=7, pady=7)

#Taking the variant list
lblvariant = tk.Frame(window)
lblvariant.place(x=800, y=300)



var_num = tk.IntVar()
numberofVariant = tk.Entry(lblvariant, textvariable=var_num, font=("Times New Roman", 18, BOLD ))
numberofVariant.grid(row=0, column=1)

lblnumberofvariants = tk.Label(lblvariant, text = "Number of variants ", fg = "black")
lblnumberofvariants.configure(font=("Times New Roman", 18, BOLD))
lblnumberofvariants.grid(row=0, column=0)

lblvariants = tk.Label(lblvariant, text = "VARIANTS ", fg = "black")
lblvariants.configure(font=("Times New Roman", 18, BOLD))
lblvariants.grid(row=1, column=0)


#for i in range(1,var_num.get()):

vartype = tk.Entry(lblvariant, text="", font=("Times New Roman", 18, BOLD ))
vartype.grid(row=1, column=1, sticky="w", padx=7, pady=2)
#print(vartype.get())
#variant_list.append(vartype)
    
btn_appendvar = tk.Button(lblvariant, text="ADD", command=addd, bg=rgb_hack((0,12,100)), fg="white")
btn_appendvar.configure(font=("Times New Roman", 18, BOLD))
btn_appendvar.grid(row=3, column=0, sticky="nsew", padx=7, pady=7)

btn_compute = tk.Button(lblvariant, text="COMPUTE", command=compute, bg=rgb_hack((50,0,100)), fg="white")
btn_compute.configure(font=("Times New Roman", 18, BOLD))
btn_compute.grid(row=3, column=2, sticky="nsew", padx=7, pady=7)



#training the model

trainFrame = tk.Frame(window)
trainFrame.place(x=100, y=600)



btn_trainvar = tk.Button(trainFrame, text="TRAIN", command=trainn, bg=rgb_hack((30,57,98)), fg="white")
btn_trainvar.configure(font=("Times New Roman",18,BOLD))
btn_trainvar.grid(row=0, column=0, sticky="nsew", padx=7, pady=7)


#File path for saving the trained models

btn_filepath = tk.Button(trainFrame, text="SELECT PATH", command=filess, bg=rgb_hack((0,24,0)), fg="white")
btn_filepath.configure(font=("Times New Roman",18,BOLD))
btn_filepath.grid(row=4, column=0, sticky="nsew", padx=7, pady=7)

# lbl_dir = tk.Entry(trainFrame, textvariable=var_num, font=("Times New Roman", 18, BOLD ))
# lbl_dir.grid(row=4, column=1)

Text_box = tk.Text(trainFrame, font=("Times New Roman", 18, BOLD ), height=1, width=30)
Text_box.grid(row=4, column=1,sticky="w", padx=7, pady=7)



window.mainloop()