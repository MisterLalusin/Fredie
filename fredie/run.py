import tkinter as tk
from tkinter import *
from PIL import ImageTk
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.patches import FancyArrowPatch

import matplotlib
matplotlib.use('TkAgg')
import numpy as np
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure

from PIL import Image 

import math 

from astropy import units as u
from astropy.constants import G
from astropy import constants as const

root = tk.Tk()
root.title("Fredie - The Physics Guy")
root.resizable(False, False)
root.configure(bg="#E1DEE6")
root.wm_iconbitmap("E:\\Projects\\Programming\\Python\\fredie\\app.ico")

window_height = 666
window_width = 888

screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()

x_cordinate = int((screen_width/2) - (window_width/2))
y_cordinate = int((screen_height/2) - (window_height/2))

root.geometry("{}x{}+{}+{}".format(window_width, window_height, x_cordinate, y_cordinate - 40))

def popupmsg(msg):
    popup = tk.Tk()
    popup.wm_title("Warning")
    popup.wm_iconbitmap("E:\\Projects\\Programming\\Python\\fredie\\app.ico")
    label = tk.Label(popup, text=msg, font="Instruction 16", bg="#E1DEE6")
    label.pack(side="top", fill="x", pady=10)
    B1 = tk.Button(popup, text="Okay", command = popup.destroy, font="Instruction 13", bg="#1b1b1b", fg="#ffffff", width="16")
    B1.pack()

    popUpWindow_height = 99
    popUpWindow_width = 269

    x_cordinate = int((screen_width/2) - (popUpWindow_width/2))
    y_cordinate = int((screen_height/2) - (popUpWindow_height/2))

    popup.resizable(False, False)
    popup.configure(bg="#E1DEE6")

    popup.geometry("{}x{}+{}+{}".format(popUpWindow_width, popUpWindow_height, x_cordinate, y_cordinate - 40))
    popup.mainloop()

def formulamsg(imageFile):
    formula = tk.Toplevel() 
    formula.wm_title("Formula")
    formula.wm_iconbitmap("E:\\Projects\\Programming\\Python\\fredie\\app.ico")

    canvasMain = Canvas(formula, width = 610, height = 660, highlightbackground = "#1b1b1b", borderwidth = 0, highlightthickness = 0, bg="#E1DEE6")          
    img = PhotoImage(file=imageFile)      
    canvasMain.create_image(10,5, anchor=NW, image=img)   
    canvasMain.pack() 

    B1 = tk.Button(formula, text="Okay", command = formula.destroy, font="Instruction 13", bg="#1b1b1b", fg="#ffffff", width="16")
    B1.pack()

    formulaWindow_height = 199
    formulaWindow_width = 369

    x_cordinate = int((screen_width/2) - (formulaWindow_width/2))
    y_cordinate = int((screen_height/2) - (formulaWindow_height/2))

    formula.resizable(False, False)
    formula.configure(bg="#E1DEE6")

    formula.geometry("{}x{}+{}+{}".format(formulaWindow_width, formulaWindow_height, x_cordinate-400, y_cordinate - 200))
    formula.mainloop() 


def menuDefault():
    velocityLabel.configure(fg='#d1bea8')
    accelerationLabel.configure(fg='#d1bea8')
    freeFallLabel.configure(fg='#d1bea8')
    tangentialSpeedLabel.configure(fg='#d1bea8')
    angularValuesLabel.configure(fg='#d1bea8')
    lawOfInertiaLabel.configure(fg='#d1bea8')
    lawOfAccelerationLabel.configure(fg='#d1bea8')
    centripetalAccelerationLabel.configure(fg='#d1bea8')
    tensionLabel.configure(fg='#d1bea8')
    centripetalForceLabel.configure(fg='#d1bea8')
    torqueLabel.configure(fg='#d1bea8')
    lawOfActionAndReactionLabel.configure(fg='#d1bea8')
    workLabel.configure(fg='#d1bea8')
    forceLabel.configure(fg='#d1bea8')
    kineticEnergyLabel.configure(fg='#d1bea8')
    potentialEnergyLabel.configure(fg='#d1bea8')
    powerLabel.configure(fg='#d1bea8')
    linearMomentumLabel.configure(fg='#d1bea8')
    impulseLabel.configure(fg='#d1bea8')
    collisionLabel.configure(fg='#d1bea8')
    torqueRotationalDynamicsLabel.configure(fg='#d1bea8')
    momentOfInertiaLabel.configure(fg='#d1bea8')
    gravitationalForceLabel.configure(fg='#d1bea8')
    semimajorAxisLabel.configure(fg='#d1bea8')
    shearStressLabel.configure(fg='#d1bea8')
    poissonsRatioLabel.configure(fg='#d1bea8')
    crossSectionalAreaLabel.configure(fg='#d1bea8')
    pressureLabel.configure(fg='#d1bea8')
    potentialEnergyFluidsAndHarmonicsLabel.configure(fg='#d1bea8')
    volumeFlowRateLabel.configure(fg='#d1bea8')
    periodOfOscillationLabel.configure(fg='#d1bea8')
    waveSpeedLabel.configure(fg='#d1bea8')
    wavelengthLabel.configure(fg='#d1bea8')
    requiredHeatLabel.configure(fg='#d1bea8')
    molarHeatCapacityLabel.configure(fg='#d1bea8')
    latentHeatLabel.configure(fg='#d1bea8')
    heatFlowRateLabel.configure(fg='#d1bea8')
    lengthChangeLabel.configure(fg='#d1bea8')
    volumeChangeLabel.configure(fg='#d1bea8')
    thermalStressLabel.configure(fg='#d1bea8')


def resetCalculationsFrame():
    for widget in calculationsframe.winfo_children():
       widget.destroy()


def velocityModule(event):
    menuDefault()
    velocityLabel.configure(fg='#e8e916')
    resetCalculationsFrame()
    velocityModuleDisplay()

def velocityModuleDisplay():
    
    def show_entry_fields():
        try:         
            displacement = float(entry1.get())
            time = float(entry2.get())
            direction = str(entry3.get())
            if len(str(displacement)) != 0 and len(str(time)) != 0 and len(direction) != 0:         
                ans = str((displacement / time)) + " m/s " + direction
                entry4.delete(0,END)
                entry4.insert(0,ans)
        except:   
            popupmsg("Check your inputs")

    label1 = tk.Label(calculationsframe, text="Displacement in meters", font="Instruction 20", bg="#1b1b1b", fg="#d1bea8", width="26", anchor='w')
    entry1 = tk.Entry(calculationsframe, font="Instruction 20", bg="#ffffff", fg="#0ba98b", width="26", highlightbackground = "#1b1b1b", borderwidth = 0, highlightthickness = 2)
    label2 = tk.Label(calculationsframe, text="Time in seconds", font="Instruction 20", bg="#1b1b1b", fg="#d1bea8", width="26", anchor='w')
    entry2 = tk.Entry(calculationsframe, font="Instruction 20", bg="#ffffff", fg="#0ba98b", width="26", highlightbackground = "#1b1b1b", borderwidth = 0, highlightthickness = 2)
    label3 = tk.Label(calculationsframe, text="Direction", font="Instruction 20", bg="#1b1b1b", fg="#d1bea8", width="26", anchor='w')
    entry3 = tk.Entry(calculationsframe, font="Instruction 20", bg="#ffffff", fg="#0ba98b", width="26", highlightbackground = "#1b1b1b", borderwidth = 0, highlightthickness = 2)
    label4 = tk.Label(calculationsframe, text="Answer", font="Instruction 20", bg="#1b1b1b", fg="#d1bea8", width="26", anchor='w')
    entry4 = tk.Entry(calculationsframe, font="Instruction 20", bg="#ffffff", fg="#0ba98b", width="26", highlightbackground = "#1b1b1b", borderwidth = 0, highlightthickness = 2)

    label1.grid(row=0, column=1, pady=(16,0))
    entry1.grid(row=10, column=1, pady=(0,8))
    label2.grid(row=20, column=1, pady=0)
    entry2.grid(row=30, column=1, pady=(0,8))
    label3.grid(row=40, column=1, pady=0)
    entry3.grid(row=50, column=1, pady=(0,8))
    label4.grid(row=60, column=1, pady=0)
    entry4.grid(row=70, column=1, pady=(0,8))

    tk.Button(calculationsframe, text='CALCULATE', font="Instruction 13", bg="#1b1b1b", fg="#ffffff", width="16" ,command=show_entry_fields).grid(
                                                                row=80, 
                                                                column=1, 
                                                                sticky=tk.E, 
                                                                pady=8)

    formulamsg("E:\\Projects\\Programming\\Python\\fredie\\formula\\velocity.png")
                                 

def accelerationModule(event):
    menuDefault()
    accelerationLabel.configure(fg='#e8e916')
    resetCalculationsFrame()
    accelerationModuleDisplay()

def accelerationModuleDisplay():

    def show_entry_fields():
        try:         
            initialVelocity = float(entry1.get())
            finalVelocity = float(entry2.get())
            time = float(entry3.get())
            if len(str(initialVelocity)) != 0 and len(str(finalVelocity)) != 0 and len(str(time)) != 0:         
                ans = str(((finalVelocity - initialVelocity) / 1)) + " m/s^2"
                entry4.delete(0,END)
                entry4.insert(0,ans)
        except:   
            popupmsg("Check your inputs")

    label1 = tk.Label(calculationsframe, text="Initial Velocity in m/s", font="Instruction 20", bg="#1b1b1b", fg="#d1bea8", width="26", anchor='w')
    entry1 = tk.Entry(calculationsframe, font="Instruction 20", bg="#ffffff", fg="#0ba98b", width="26", highlightbackground = "#1b1b1b", borderwidth = 0, highlightthickness = 2)
    label2 = tk.Label(calculationsframe, text="Final Velocity in m/s", font="Instruction 20", bg="#1b1b1b", fg="#d1bea8", width="26", anchor='w')
    entry2 = tk.Entry(calculationsframe, font="Instruction 20", bg="#ffffff", fg="#0ba98b", width="26", highlightbackground = "#1b1b1b", borderwidth = 0, highlightthickness = 2)
    label3 = tk.Label(calculationsframe, text="Time in seconds", font="Instruction 20", bg="#1b1b1b", fg="#d1bea8", width="26", anchor='w')
    entry3 = tk.Entry(calculationsframe, font="Instruction 20", bg="#ffffff", fg="#0ba98b", width="26", highlightbackground = "#1b1b1b", borderwidth = 0, highlightthickness = 2)
    label4 = tk.Label(calculationsframe, text="Answer", font="Instruction 20", bg="#1b1b1b", fg="#d1bea8", width="26", anchor='w')
    entry4 = tk.Entry(calculationsframe, font="Instruction 20", bg="#ffffff", fg="#0ba98b", width="26", highlightbackground = "#1b1b1b", borderwidth = 0, highlightthickness = 2)

    label1.grid(row=0, column=1, pady=(16,0))
    entry1.grid(row=10, column=1, pady=(0,8))
    label2.grid(row=20, column=1, pady=0)
    entry2.grid(row=30, column=1, pady=(0,8))
    label3.grid(row=40, column=1, pady=0)
    entry3.grid(row=50, column=1, pady=(0,8))
    label4.grid(row=60, column=1, pady=0)
    entry4.grid(row=70, column=1, pady=(0,8))

    tk.Button(calculationsframe, text='CALCULATE', font="Instruction 13", bg="#1b1b1b", fg="#ffffff", width="16" ,command=show_entry_fields).grid(
                                                                row=80, 
                                                                column=1, 
                                                                sticky=tk.E, 
                                                                pady=8)

    formulamsg("E:\\Projects\\Programming\\Python\\fredie\\formula\\acceleration.png")

def freeFallModule(event):
    menuDefault()
    freeFallLabel.configure(fg='#e8e916')
    resetCalculationsFrame()
    freeFallModuleDisplay()

def freeFallModuleDisplay():

    def show_entry_fields():
        try:         
            time = float(entry1.get())
            if len(str(time)) != 0:         
                ans = str(((0.5) * (9.8) * math.pow (time, 2))) + " m"
                entry2.delete(0,END)
                entry2.insert(0,ans)
        except:   
            popupmsg("Check your inputs")

    label1 = tk.Label(calculationsframe, text="Time in seconds", font="Instruction 20", bg="#1b1b1b", fg="#d1bea8", width="26", anchor='w')
    entry1 = tk.Entry(calculationsframe, font="Instruction 20", bg="#ffffff", fg="#0ba98b", width="26", highlightbackground = "#1b1b1b", borderwidth = 0, highlightthickness = 2)
    label2 = tk.Label(calculationsframe, text="Answer", font="Instruction 20", bg="#1b1b1b", fg="#d1bea8", width="26", anchor='w')
    entry2 = tk.Entry(calculationsframe, font="Instruction 20", bg="#ffffff", fg="#0ba98b", width="26", highlightbackground = "#1b1b1b", borderwidth = 0, highlightthickness = 2)

    label1.grid(row=0, column=1, pady=(16,0))
    entry1.grid(row=10, column=1, pady=(0,8))
    label2.grid(row=20, column=1, pady=0)
    entry2.grid(row=30, column=1, pady=(0,8))

    tk.Button(calculationsframe, text='CALCULATE', font="Instruction 13", bg="#1b1b1b", fg="#ffffff", width="16" ,command=show_entry_fields).grid(
                                                                row=80, 
                                                                column=1, 
                                                                sticky=tk.E, 
                                                                pady=8)

    formulamsg("E:\\Projects\\Programming\\Python\\fredie\\formula\\free_fall.png")


def tangentialSpeedModule(event):
    menuDefault()
    tangentialSpeedLabel.configure(fg='#e8e916')
    resetCalculationsFrame()
    tangentialSpeedModuleDisplay()

def tangentialSpeedModuleDisplay():

    def show_entry_fields():
        try:         
            radiusInMeters = float(entry1.get())
            angularVelocity = float(entry2.get())
            if len(str(radiusInMeters)) != 0 and len(str(angularVelocity)) != 0:         
                ans = str(((angularVelocity * math.pi) * radiusInMeters)) + " m/s"
                entry3.delete(0,END)
                entry3.insert(0,ans)
        except:   
            popupmsg("Check your inputs")

    label1 = tk.Label(calculationsframe, text="Radius in meters", font="Instruction 20", bg="#1b1b1b", fg="#d1bea8", width="26", anchor='w')
    entry1 = tk.Entry(calculationsframe, font="Instruction 20", bg="#ffffff", fg="#0ba98b", width="26", highlightbackground = "#1b1b1b", borderwidth = 0, highlightthickness = 2)
    label2 = tk.Label(calculationsframe, text="Angular Velocity in rad/s", font="Instruction 20", bg="#1b1b1b", fg="#d1bea8", width="26", anchor='w')
    entry2 = tk.Entry(calculationsframe, font="Instruction 20", bg="#ffffff", fg="#0ba98b", width="26", highlightbackground = "#1b1b1b", borderwidth = 0, highlightthickness = 2)
    label3 = tk.Label(calculationsframe, text="Answer", font="Instruction 20", bg="#1b1b1b", fg="#d1bea8", width="26", anchor='w')
    entry3 = tk.Entry(calculationsframe, font="Instruction 20", bg="#ffffff", fg="#0ba98b", width="26", highlightbackground = "#1b1b1b", borderwidth = 0, highlightthickness = 2)

    label1.grid(row=0, column=1, pady=(16,0))
    entry1.grid(row=10, column=1, pady=(0,8))
    label2.grid(row=20, column=1, pady=0)
    entry2.grid(row=30, column=1, pady=(0,8))
    label3.grid(row=40, column=1, pady=0)
    entry3.grid(row=50, column=1, pady=(0,8))

    tk.Button(calculationsframe, text='CALCULATE', font="Instruction 13", bg="#1b1b1b", fg="#ffffff", width="16" ,command=show_entry_fields).grid(
                                                                row=80, 
                                                                column=1, 
                                                                sticky=tk.E, 
                                                                pady=8)

    formulamsg("E:\\Projects\\Programming\\Python\\fredie\\formula\\tangential_speed.png")

def angularValuesModule(event):
    menuDefault()
    angularValuesLabel.configure(fg='#e8e916')
    resetCalculationsFrame()
    angularValuesModuleDisplay()

def angularValuesModuleDisplay():

    def show_entry_fields():
        try:         
            angleInRadians = float(entry1.get())
            if len(str(angleInRadians)) != 0:         
                ans = str(angleInRadians * (180/math.pi)) + " degrees"
                entry2.delete(0,END)
                entry2.insert(0,ans)
        except:   
            popupmsg("Check your inputs")

    label1 = tk.Label(calculationsframe, text="Angle in Radians", font="Instruction 20", bg="#1b1b1b", fg="#d1bea8", width="26", anchor='w')
    entry1 = tk.Entry(calculationsframe, font="Instruction 20", bg="#ffffff", fg="#0ba98b", width="26", highlightbackground = "#1b1b1b", borderwidth = 0, highlightthickness = 2)
    label2 = tk.Label(calculationsframe, text="Answer", font="Instruction 20", bg="#1b1b1b", fg="#d1bea8", width="26", anchor='w')
    entry2 = tk.Entry(calculationsframe, font="Instruction 20", bg="#ffffff", fg="#0ba98b", width="26", highlightbackground = "#1b1b1b", borderwidth = 0, highlightthickness = 2)

    label1.grid(row=0, column=1, pady=(16,0))
    entry1.grid(row=10, column=1, pady=(0,8))
    label2.grid(row=20, column=1, pady=0)
    entry2.grid(row=30, column=1, pady=(0,8))

    tk.Button(calculationsframe, text='CALCULATE', font="Instruction 13", bg="#1b1b1b", fg="#ffffff", width="16" ,command=show_entry_fields).grid(
                                                                row=80, 
                                                                column=1, 
                                                                sticky=tk.E, 
                                                                pady=8)

    formulamsg("E:\\Projects\\Programming\\Python\\fredie\\formula\\angular_values.png")

def lawOfInertiaModule(event):
    menuDefault()
    lawOfInertiaLabel.configure(fg='#e8e916')
    resetCalculationsFrame()
    lawOfInertiaModuleDisplay()

def lawOfInertiaModuleDisplay():

    def show_entry_fields():
        try:         
            massInKilogram = float(entry1.get())
            radiusInMeters = float(entry2.get())
            if len(str(massInKilogram)) != 0 and len(str(radiusInMeters)) != 0:         
                ans = str((massInKilogram * math.pow (radiusInMeters, 2))) + " kg/m^2"
                entry3.delete(0,END)
                entry3.insert(0,ans)
        except:   
            popupmsg("Check your inputs")

    label1 = tk.Label(calculationsframe, text="Mass in Kilogram", font="Instruction 20", bg="#1b1b1b", fg="#d1bea8", width="26", anchor='w')
    entry1 = tk.Entry(calculationsframe, font="Instruction 20", bg="#ffffff", fg="#0ba98b", width="26", highlightbackground = "#1b1b1b", borderwidth = 0, highlightthickness = 2)
    label2 = tk.Label(calculationsframe, text="Radius in meters", font="Instruction 20", bg="#1b1b1b", fg="#d1bea8", width="26", anchor='w')
    entry2 = tk.Entry(calculationsframe, font="Instruction 20", bg="#ffffff", fg="#0ba98b", width="26", highlightbackground = "#1b1b1b", borderwidth = 0, highlightthickness = 2)
    label3 = tk.Label(calculationsframe, text="Answer", font="Instruction 20", bg="#1b1b1b", fg="#d1bea8", width="26", anchor='w')
    entry3 = tk.Entry(calculationsframe, font="Instruction 20", bg="#ffffff", fg="#0ba98b", width="26", highlightbackground = "#1b1b1b", borderwidth = 0, highlightthickness = 2)

    label1.grid(row=0, column=1, pady=(16,0))
    entry1.grid(row=10, column=1, pady=(0,8))
    label2.grid(row=20, column=1, pady=0)
    entry2.grid(row=30, column=1, pady=(0,8))
    label3.grid(row=40, column=1, pady=0)
    entry3.grid(row=50, column=1, pady=(0,8))

    tk.Button(calculationsframe, text='CALCULATE', font="Instruction 13", bg="#1b1b1b", fg="#ffffff", width="16" ,command=show_entry_fields).grid(
                                                                row=80, 
                                                                column=1, 
                                                                sticky=tk.E, 
                                                                pady=8)

    formulamsg("E:\\Projects\\Programming\\Python\\fredie\\formula\\law_of_inertia.png")

def lawOfAccelerationModule(event):
    menuDefault()
    lawOfAccelerationLabel.configure(fg='#e8e916')
    resetCalculationsFrame()
    lawOfAccelerationModuleDisplay()

def lawOfAccelerationModuleDisplay():

    def show_entry_fields():
        try:         
            massInKilogram = float(entry1.get())
            accelerationInMeterPerSecondSquared = float(entry2.get())
            if len(str(massInKilogram)) != 0 and len(str(accelerationInMeterPerSecondSquared)) != 0:         
                ans = str((massInKilogram * accelerationInMeterPerSecondSquared)) + " N"
                entry3.delete(0,END)
                entry3.insert(0,ans)
        except:   
            popupmsg("Check your inputs")

    label1 = tk.Label(calculationsframe, text="Mass in Kilogram", font="Instruction 20", bg="#1b1b1b", fg="#d1bea8", width="26", anchor='w')
    entry1 = tk.Entry(calculationsframe, font="Instruction 20", bg="#ffffff", fg="#0ba98b", width="26", highlightbackground = "#1b1b1b", borderwidth = 0, highlightthickness = 2)
    label2 = tk.Label(calculationsframe, text="Acceleration in m/s^2", font="Instruction 20", bg="#1b1b1b", fg="#d1bea8", width="26", anchor='w')
    entry2 = tk.Entry(calculationsframe, font="Instruction 20", bg="#ffffff", fg="#0ba98b", width="26", highlightbackground = "#1b1b1b", borderwidth = 0, highlightthickness = 2)
    label3 = tk.Label(calculationsframe, text="Answer", font="Instruction 20", bg="#1b1b1b", fg="#d1bea8", width="26", anchor='w')
    entry3 = tk.Entry(calculationsframe, font="Instruction 20", bg="#ffffff", fg="#0ba98b", width="26", highlightbackground = "#1b1b1b", borderwidth = 0, highlightthickness = 2)

    label1.grid(row=0, column=1, pady=(16,0))
    entry1.grid(row=10, column=1, pady=(0,8))
    label2.grid(row=20, column=1, pady=0)
    entry2.grid(row=30, column=1, pady=(0,8))
    label3.grid(row=40, column=1, pady=0)
    entry3.grid(row=50, column=1, pady=(0,8))

    tk.Button(calculationsframe, text='CALCULATE', font="Instruction 13", bg="#1b1b1b", fg="#ffffff", width="16" ,command=show_entry_fields).grid(
                                                                row=80, 
                                                                column=1, 
                                                                sticky=tk.E, 
                                                                pady=8)

    formulamsg("E:\\Projects\\Programming\\Python\\fredie\\formula\\law_of_acceleration.png")

def centripetalAccelerationModule(event):
    menuDefault()
    centripetalAccelerationLabel.configure(fg='#e8e916')
    resetCalculationsFrame()
    centripetalAccelerationModuleDisplay()

def centripetalAccelerationModuleDisplay():

    def show_entry_fields():
        try:         
            velocityInMeterPerSeconds = float(entry1.get())
            radiusInMeters = float(entry2.get())
            if len(str(velocityInMeterPerSeconds)) != 0 and len(str(radiusInMeters)) != 0:         
                ans = str(math.pow(velocityInMeterPerSeconds, 2)/radiusInMeters) + " m/s^2"
                entry3.delete(0,END)
                entry3.insert(0,ans)
        except:   
            popupmsg("Check your inputs")
    label1 = tk.Label(calculationsframe, text="Velocity in m/s", font="Instruction 20", bg="#1b1b1b", fg="#d1bea8", width="26", anchor='w')
    entry1 = tk.Entry(calculationsframe, font="Instruction 20", bg="#ffffff", fg="#0ba98b", width="26", highlightbackground = "#1b1b1b", borderwidth = 0, highlightthickness = 2)
    label2 = tk.Label(calculationsframe, text="Radius in meters", font="Instruction 20", bg="#1b1b1b", fg="#d1bea8", width="26", anchor='w')
    entry2 = tk.Entry(calculationsframe, font="Instruction 20", bg="#ffffff", fg="#0ba98b", width="26", highlightbackground = "#1b1b1b", borderwidth = 0, highlightthickness = 2)
    label3 = tk.Label(calculationsframe, text="Answer", font="Instruction 20", bg="#1b1b1b", fg="#d1bea8", width="26", anchor='w')
    entry3 = tk.Entry(calculationsframe, font="Instruction 20", bg="#ffffff", fg="#0ba98b", width="26", highlightbackground = "#1b1b1b", borderwidth = 0, highlightthickness = 2)

    label1.grid(row=0, column=1, pady=(16,0))
    entry1.grid(row=10, column=1, pady=(0,8))
    label2.grid(row=20, column=1, pady=0)
    entry2.grid(row=30, column=1, pady=(0,8))
    label3.grid(row=40, column=1, pady=0)
    entry3.grid(row=50, column=1, pady=(0,8))

    tk.Button(calculationsframe, text='CALCULATE', font="Instruction 13", bg="#1b1b1b", fg="#ffffff", width="16" ,command=show_entry_fields).grid(
                                                                row=80, 
                                                                column=1, 
                                                                sticky=tk.E, 
                                                                pady=8)

    formulamsg("E:\\Projects\\Programming\\Python\\fredie\\formula\\centripetal_acceleration.png")


def tensionModule(event):
    menuDefault()
    tensionLabel.configure(fg='#e8e916')
    resetCalculationsFrame()
    tensionModuleDisplay()

def tensionModuleDisplay():
    def show_entry_fields():
        try:         
            forceInNewton = float(entry1.get())
            degrees = float(entry2.get())
            if len(str(forceInNewton)) != 0 and len(str(degrees)) != 0 :         
                ans = str(math.sin(degrees*(math.pi/180)) * forceInNewton) + " N"
                entry3.delete(0,END)
                entry3.insert(0,ans)
        except:   
            popupmsg("Check your inputs")

    label1 = tk.Label(calculationsframe, text="Force in Newton", font="Instruction 20", bg="#1b1b1b", fg="#d1bea8", width="26", anchor='w')
    entry1 = tk.Entry(calculationsframe, font="Instruction 20", bg="#ffffff", fg="#0ba98b", width="26", highlightbackground = "#1b1b1b", borderwidth = 0, highlightthickness = 2)
    label2 = tk.Label(calculationsframe, text="Angle in degrees", font="Instruction 20", bg="#1b1b1b", fg="#d1bea8", width="26", anchor='w')
    entry2 = tk.Entry(calculationsframe, font="Instruction 20", bg="#ffffff", fg="#0ba98b", width="26", highlightbackground = "#1b1b1b", borderwidth = 0, highlightthickness = 2)
    label3 = tk.Label(calculationsframe, text="Answer", font="Instruction 20", bg="#1b1b1b", fg="#d1bea8", width="26", anchor='w')
    entry3 = tk.Entry(calculationsframe, font="Instruction 20", bg="#ffffff", fg="#0ba98b", width="26", highlightbackground = "#1b1b1b", borderwidth = 0, highlightthickness = 2)

    label1.grid(row=0, column=1, pady=(16,0))
    entry1.grid(row=10, column=1, pady=(0,8))
    label2.grid(row=20, column=1, pady=0)
    entry2.grid(row=30, column=1, pady=(0,8))
    label3.grid(row=40, column=1, pady=0)
    entry3.grid(row=50, column=1, pady=(0,8))

    tk.Button(calculationsframe, text='CALCULATE', font="Instruction 13", bg="#1b1b1b", fg="#ffffff", width="16" ,command=show_entry_fields).grid(
                                                                row=80, 
                                                                column=1, 
                                                                sticky=tk.E, 
                                                                pady=8)

    formulamsg("E:\\Projects\\Programming\\Python\\fredie\\formula\\tension.png")


def centripetalForceModule(event):
    menuDefault()
    centripetalForceLabel.configure(fg='#e8e916')
    resetCalculationsFrame()
    centripetalForceModuleDisplay()

def centripetalForceModuleDisplay():

    def show_entry_fields():
        try:         
            massInKilogram = float(entry1.get())
            velocityInMeterPerSeconds = float(entry2.get())
            radiusInMeters = float(entry3.get())
            if len(str(massInKilogram)) != 0 and len(str(velocityInMeterPerSeconds)) != 0 and len(str(radiusInMeters)) != 0:         
                ans = str(math.pow(massInKilogram * velocityInMeterPerSeconds, 2)/radiusInMeters) + " N"
                entry4.delete(0,END)
                entry4.insert(0,ans)
        except:   
            popupmsg("Check your inputs")

    label1 = tk.Label(calculationsframe, text="Mass in Kilogram", font="Instruction 20", bg="#1b1b1b", fg="#d1bea8", width="26", anchor='w')
    entry1 = tk.Entry(calculationsframe, font="Instruction 20", bg="#ffffff", fg="#0ba98b", width="26", highlightbackground = "#1b1b1b", borderwidth = 0, highlightthickness = 2)
    label2 = tk.Label(calculationsframe, text="Velocity in m/s", font="Instruction 20", bg="#1b1b1b", fg="#d1bea8", width="26", anchor='w')
    entry2 = tk.Entry(calculationsframe, font="Instruction 20", bg="#ffffff", fg="#0ba98b", width="26", highlightbackground = "#1b1b1b", borderwidth = 0, highlightthickness = 2)
    label3 = tk.Label(calculationsframe, text="Radius in meters", font="Instruction 20", bg="#1b1b1b", fg="#d1bea8", width="26", anchor='w')
    entry3 = tk.Entry(calculationsframe, font="Instruction 20", bg="#ffffff", fg="#0ba98b", width="26", highlightbackground = "#1b1b1b", borderwidth = 0, highlightthickness = 2)
    label4 = tk.Label(calculationsframe, text="Answer", font="Instruction 20", bg="#1b1b1b", fg="#d1bea8", width="26", anchor='w')
    entry4 = tk.Entry(calculationsframe, font="Instruction 20", bg="#ffffff", fg="#0ba98b", width="26", highlightbackground = "#1b1b1b", borderwidth = 0, highlightthickness = 2)

    label1.grid(row=0, column=1, pady=(16,0))
    entry1.grid(row=10, column=1, pady=(0,8))
    label2.grid(row=20, column=1, pady=0)
    entry2.grid(row=30, column=1, pady=(0,8))
    label3.grid(row=40, column=1, pady=0)
    entry3.grid(row=50, column=1, pady=(0,8))
    label4.grid(row=60, column=1, pady=0)
    entry4.grid(row=70, column=1, pady=(0,8))

    tk.Button(calculationsframe, text='CALCULATE', font="Instruction 13", bg="#1b1b1b", fg="#ffffff", width="16" ,command=show_entry_fields).grid(
                                                                row=80, 
                                                                column=1, 
                                                                sticky=tk.E, 
                                                                pady=8)

    formulamsg("E:\\Projects\\Programming\\Python\\fredie\\formula\\centripetal_force.png")

def torqueModule(event):
    menuDefault()
    torqueLabel.configure(fg='#e8e916')
    resetCalculationsFrame()
    torqueModuleDisplay()

def torqueModuleDisplay():
    def show_entry_fields():
        try:         
            forceInNewton = float(entry1.get())
            radiusInMeters = float(entry2.get())
            degrees = float(entry3.get())
            if len(str(forceInNewton)) != 0 and len(str(radiusInMeters)) != 0  and len(str(degrees)) != 0 :         
                ans = str((forceInNewton * radiusInMeters) * math.sin(degrees*(math.pi/180))) + " N m"
                entry4.delete(0,END)
                entry4.insert(0,ans)
        except:   
            popupmsg("Check your inputs")

    label1 = tk.Label(calculationsframe, text="Force in newton", font="Instruction 20", bg="#1b1b1b", fg="#d1bea8", width="26", anchor='w')
    entry1 = tk.Entry(calculationsframe, font="Instruction 20", bg="#ffffff", fg="#0ba98b", width="26", highlightbackground = "#1b1b1b", borderwidth = 0, highlightthickness = 2)
    label2 = tk.Label(calculationsframe, text="Radius in meters", font="Instruction 20", bg="#1b1b1b", fg="#d1bea8", width="26", anchor='w')
    entry2 = tk.Entry(calculationsframe, font="Instruction 20", bg="#ffffff", fg="#0ba98b", width="26", highlightbackground = "#1b1b1b", borderwidth = 0, highlightthickness = 2)
    label3 = tk.Label(calculationsframe, text="Angle in degrees", font="Instruction 20", bg="#1b1b1b", fg="#d1bea8", width="26", anchor='w')
    entry3 = tk.Entry(calculationsframe, font="Instruction 20", bg="#ffffff", fg="#0ba98b", width="26", highlightbackground = "#1b1b1b", borderwidth = 0, highlightthickness = 2)
    label4 = tk.Label(calculationsframe, text="Answer", font="Instruction 20", bg="#1b1b1b", fg="#d1bea8", width="26", anchor='w')
    entry4 = tk.Entry(calculationsframe, font="Instruction 20", bg="#ffffff", fg="#0ba98b", width="26", highlightbackground = "#1b1b1b", borderwidth = 0, highlightthickness = 2)


    label1.grid(row=0, column=1, pady=(16,0))
    entry1.grid(row=10, column=1, pady=(0,8))
    label2.grid(row=20, column=1, pady=0)
    entry2.grid(row=30, column=1, pady=(0,8))
    label3.grid(row=40, column=1, pady=0)
    entry3.grid(row=50, column=1, pady=(0,8))
    label4.grid(row=60, column=1, pady=0)
    entry4.grid(row=70, column=1, pady=(0,8))

    tk.Button(calculationsframe, text='CALCULATE', font="Instruction 13", bg="#1b1b1b", fg="#ffffff", width="16" ,command=show_entry_fields).grid(
                                                                row=80, 
                                                                column=1, 
                                                                sticky=tk.E, 
                                                                pady=8)

    formulamsg("E:\\Projects\\Programming\\Python\\fredie\\formula\\torque.png")

def lawOfActionAndReactionModule(event):
    menuDefault()
    lawOfActionAndReactionLabel.configure(fg='#e8e916')
    resetCalculationsFrame()
    lawOfActionAndReactionModuleDisplay()

def lawOfActionAndReactionModuleDisplay():

    def show_entry_fields():
        try:         
            forceInNewton = float(entry1.get())
            if len(str(forceInNewton)) != 0:         
                ans = str(0 - forceInNewton) + " N"
                entry2.delete(0,END)
                entry2.insert(0,ans)
        except:   
            popupmsg("Check your inputs")

    label1 = tk.Label(calculationsframe, text="Force in newton", font="Instruction 20", bg="#1b1b1b", fg="#d1bea8", width="26", anchor='w')
    entry1 = tk.Entry(calculationsframe, font="Instruction 20", bg="#ffffff", fg="#0ba98b", width="26", highlightbackground = "#1b1b1b", borderwidth = 0, highlightthickness = 2)
    label2 = tk.Label(calculationsframe, text="Answer", font="Instruction 20", bg="#1b1b1b", fg="#d1bea8", width="26", anchor='w')
    entry2 = tk.Entry(calculationsframe, font="Instruction 20", bg="#ffffff", fg="#0ba98b", width="26", highlightbackground = "#1b1b1b", borderwidth = 0, highlightthickness = 2)

    label1.grid(row=0, column=1, pady=(16,0))
    entry1.grid(row=10, column=1, pady=(0,8))
    label2.grid(row=20, column=1, pady=0)
    entry2.grid(row=30, column=1, pady=(0,8))

    tk.Button(calculationsframe, text='CALCULATE', font="Instruction 13", bg="#1b1b1b", fg="#ffffff", width="16" ,command=show_entry_fields).grid(
                                                                row=80, 
                                                                column=1, 
                                                                sticky=tk.E, 
                                                                pady=8)

    formulamsg("E:\\Projects\\Programming\\Python\\fredie\\formula\\law_of_action_and_reaction.png")



def workModule(event):
    menuDefault()
    workLabel.configure(fg='#e8e916')
    resetCalculationsFrame()
    workModuleDisplay()

def workModuleDisplay():
    def show_entry_fields():
        try:         
            forceInNewton = float(entry1.get())
            displacementInMeters = float(entry2.get())
            if len(str(forceInNewton)) != 0 and len(str(displacementInMeters)) != 0:         
                ans = str(forceInNewton * displacementInMeters) + " J"
                entry3.delete(0,END)
                entry3.insert(0,ans)
        except:   
            popupmsg("Check your inputs")

    label1 = tk.Label(calculationsframe, text="Force in newton", font="Instruction 20", bg="#1b1b1b", fg="#d1bea8", width="26", anchor='w')
    entry1 = tk.Entry(calculationsframe, font="Instruction 20", bg="#ffffff", fg="#0ba98b", width="26", highlightbackground = "#1b1b1b", borderwidth = 0, highlightthickness = 2)
    label2 = tk.Label(calculationsframe, text="Displacement in meters", font="Instruction 20", bg="#1b1b1b", fg="#d1bea8", width="26", anchor='w')
    entry2 = tk.Entry(calculationsframe, font="Instruction 20", bg="#ffffff", fg="#0ba98b", width="26", highlightbackground = "#1b1b1b", borderwidth = 0, highlightthickness = 2)
    label3 = tk.Label(calculationsframe, text="Answer", font="Instruction 20", bg="#1b1b1b", fg="#d1bea8", width="26", anchor='w')
    entry3 = tk.Entry(calculationsframe, font="Instruction 20", bg="#ffffff", fg="#0ba98b", width="26", highlightbackground = "#1b1b1b", borderwidth = 0, highlightthickness = 2)

    label1.grid(row=0, column=1, pady=(16,0))
    entry1.grid(row=10, column=1, pady=(0,8))
    label2.grid(row=20, column=1, pady=0)
    entry2.grid(row=30, column=1, pady=(0,8))
    label3.grid(row=40, column=1, pady=0)
    entry3.grid(row=50, column=1, pady=(0,8))

    tk.Button(calculationsframe, text='CALCULATE', font="Instruction 13", bg="#1b1b1b", fg="#ffffff", width="16" ,command=show_entry_fields).grid(
                                                                row=80, 
                                                                column=1, 
                                                                sticky=tk.E, 
                                                                pady=8)

    formulamsg("E:\\Projects\\Programming\\Python\\fredie\\formula\\work.png")

def forceModule(event):
    menuDefault()
    forceLabel.configure(fg='#e8e916')
    resetCalculationsFrame()
    forceModuleDisplay()

def forceModuleDisplay():

    def show_entry_fields():
        try:         
            workInJoules = float(entry1.get())
            displacementInMeters = float(entry2.get())
            if len(str(workInJoules)) != 0 and len(str(displacementInMeters)) != 0:         
                ans = str(workInJoules / displacementInMeters) + " N"
                entry3.delete(0,END)
                entry3.insert(0,ans)
        except:   
            popupmsg("Check your inputs")

    label1 = tk.Label(calculationsframe, text="Work in joules", font="Instruction 20", bg="#1b1b1b", fg="#d1bea8", width="26", anchor='w')
    entry1 = tk.Entry(calculationsframe, font="Instruction 20", bg="#ffffff", fg="#0ba98b", width="26", highlightbackground = "#1b1b1b", borderwidth = 0, highlightthickness = 2)
    label2 = tk.Label(calculationsframe, text="Displacement in meters", font="Instruction 20", bg="#1b1b1b", fg="#d1bea8", width="26", anchor='w')
    entry2 = tk.Entry(calculationsframe, font="Instruction 20", bg="#ffffff", fg="#0ba98b", width="26", highlightbackground = "#1b1b1b", borderwidth = 0, highlightthickness = 2)
    label3 = tk.Label(calculationsframe, text="Answer", font="Instruction 20", bg="#1b1b1b", fg="#d1bea8", width="26", anchor='w')
    entry3 = tk.Entry(calculationsframe, font="Instruction 20", bg="#ffffff", fg="#0ba98b", width="26", highlightbackground = "#1b1b1b", borderwidth = 0, highlightthickness = 2)

    label1.grid(row=0, column=1, pady=(16,0))
    entry1.grid(row=10, column=1, pady=(0,8))
    label2.grid(row=20, column=1, pady=0)
    entry2.grid(row=30, column=1, pady=(0,8))
    label3.grid(row=40, column=1, pady=0)
    entry3.grid(row=50, column=1, pady=(0,8))

    tk.Button(calculationsframe, text='CALCULATE', font="Instruction 13", bg="#1b1b1b", fg="#ffffff", width="16" ,command=show_entry_fields).grid(
                                                                row=80, 
                                                                column=1, 
                                                                sticky=tk.E, 
                                                                pady=8)

    formulamsg("E:\\Projects\\Programming\\Python\\fredie\\formula\\force.png")

def kineticEnergyModule(event):
    menuDefault()
    kineticEnergyLabel.configure(fg='#e8e916')
    resetCalculationsFrame()
    kineticEnergyModuleDisplay()

def kineticEnergyModuleDisplay():

    def show_entry_fields():
        try:         
            massInKilograms = float(entry1.get())
            velocityInMS = float(entry2.get())
            if len(str(massInKilograms)) != 0 and len(str(velocityInMS)) != 0:         
                ans = str(((0.5) * massInKilograms * math.pow (velocityInMS, 2))) + " J"
                entry3.delete(0,END)
                entry3.insert(0,ans)
        except:   
            popupmsg("Check your inputs")

    label1 = tk.Label(calculationsframe, text="Mass in kilograms", font="Instruction 20", bg="#1b1b1b", fg="#d1bea8", width="26", anchor='w')
    entry1 = tk.Entry(calculationsframe, font="Instruction 20", bg="#ffffff", fg="#0ba98b", width="26", highlightbackground = "#1b1b1b", borderwidth = 0, highlightthickness = 2)
    label2 = tk.Label(calculationsframe, text="Velocity in m/s", font="Instruction 20", bg="#1b1b1b", fg="#d1bea8", width="26", anchor='w')
    entry2 = tk.Entry(calculationsframe, font="Instruction 20", bg="#ffffff", fg="#0ba98b", width="26", highlightbackground = "#1b1b1b", borderwidth = 0, highlightthickness = 2)
    label3 = tk.Label(calculationsframe, text="Answer", font="Instruction 20", bg="#1b1b1b", fg="#d1bea8", width="26", anchor='w')
    entry3 = tk.Entry(calculationsframe, font="Instruction 20", bg="#ffffff", fg="#0ba98b", width="26", highlightbackground = "#1b1b1b", borderwidth = 0, highlightthickness = 2)

    label1.grid(row=0, column=1, pady=(16,0))
    entry1.grid(row=10, column=1, pady=(0,8))
    label2.grid(row=20, column=1, pady=0)
    entry2.grid(row=30, column=1, pady=(0,8))
    label3.grid(row=40, column=1, pady=0)
    entry3.grid(row=50, column=1, pady=(0,8))

    tk.Button(calculationsframe, text='CALCULATE', font="Instruction 13", bg="#1b1b1b", fg="#ffffff", width="16" ,command=show_entry_fields).grid(
                                                                row=80, 
                                                                column=1, 
                                                                sticky=tk.E, 
                                                                pady=8)

    formulamsg("E:\\Projects\\Programming\\Python\\fredie\\formula\\kinetic_energy.png")



def potentialEnergyModule(event):
    menuDefault()
    potentialEnergyLabel.configure(fg='#e8e916')
    resetCalculationsFrame()
    potentialEnergyModuleDisplay()

def potentialEnergyModuleDisplay():

    def show_entry_fields():
        try:         
            massInKilograms = float(entry1.get())
            heightInMeters = float(entry2.get())
            if len(str(massInKilograms)) != 0 and len(str(heightInMeters)) != 0:         
                ans = str((massInKilograms * (9.8) * heightInMeters)) + " J"
                entry3.delete(0,END)
                entry3.insert(0,ans)
        except:   
            popupmsg("Check your inputs")

    label1 = tk.Label(calculationsframe, text="Mass in kilograms", font="Instruction 20", bg="#1b1b1b", fg="#d1bea8", width="26", anchor='w')
    entry1 = tk.Entry(calculationsframe, font="Instruction 20", bg="#ffffff", fg="#0ba98b", width="26", highlightbackground = "#1b1b1b", borderwidth = 0, highlightthickness = 2)
    label2 = tk.Label(calculationsframe, text="Height in meters", font="Instruction 20", bg="#1b1b1b", fg="#d1bea8", width="26", anchor='w')
    entry2 = tk.Entry(calculationsframe, font="Instruction 20", bg="#ffffff", fg="#0ba98b", width="26", highlightbackground = "#1b1b1b", borderwidth = 0, highlightthickness = 2)
    label3 = tk.Label(calculationsframe, text="Answer", font="Instruction 20", bg="#1b1b1b", fg="#d1bea8", width="26", anchor='w')
    entry3 = tk.Entry(calculationsframe, font="Instruction 20", bg="#ffffff", fg="#0ba98b", width="26", highlightbackground = "#1b1b1b", borderwidth = 0, highlightthickness = 2)

    label1.grid(row=0, column=1, pady=(16,0))
    entry1.grid(row=10, column=1, pady=(0,8))
    label2.grid(row=20, column=1, pady=0)
    entry2.grid(row=30, column=1, pady=(0,8))
    label3.grid(row=40, column=1, pady=0)
    entry3.grid(row=50, column=1, pady=(0,8))

    tk.Button(calculationsframe, text='CALCULATE', font="Instruction 13", bg="#1b1b1b", fg="#ffffff", width="16" ,command=show_entry_fields).grid(
                                                                row=80, 
                                                                column=1, 
                                                                sticky=tk.E, 
                                                                pady=8)

    formulamsg("E:\\Projects\\Programming\\Python\\fredie\\formula\\potential_energy.png")


def powerModule(event):
    menuDefault()
    powerLabel.configure(fg='#e8e916')
    resetCalculationsFrame()
    powerModuleDisplay()

def powerModuleDisplay():

    def show_entry_fields():
        try:         
            forceInNewton = float(entry1.get())
            velocityInMS = float(entry2.get())
            if len(str(forceInNewton)) != 0 and len(str(velocityInMS)) != 0:         
                ans = str((forceInNewton * velocityInMS)) + " w"
                entry3.delete(0,END)
                entry3.insert(0,ans)
        except:   
            popupmsg("Check your inputs")

    label1 = tk.Label(calculationsframe, text="Force in newton", font="Instruction 20", bg="#1b1b1b", fg="#d1bea8", width="26", anchor='w')
    entry1 = tk.Entry(calculationsframe, font="Instruction 20", bg="#ffffff", fg="#0ba98b", width="26", highlightbackground = "#1b1b1b", borderwidth = 0, highlightthickness = 2)
    label2 = tk.Label(calculationsframe, text="Velocity in m/s", font="Instruction 20", bg="#1b1b1b", fg="#d1bea8", width="26", anchor='w')
    entry2 = tk.Entry(calculationsframe, font="Instruction 20", bg="#ffffff", fg="#0ba98b", width="26", highlightbackground = "#1b1b1b", borderwidth = 0, highlightthickness = 2)
    label3 = tk.Label(calculationsframe, text="Answer", font="Instruction 20", bg="#1b1b1b", fg="#d1bea8", width="26", anchor='w')
    entry3 = tk.Entry(calculationsframe, font="Instruction 20", bg="#ffffff", fg="#0ba98b", width="26", highlightbackground = "#1b1b1b", borderwidth = 0, highlightthickness = 2)

    label1.grid(row=0, column=1, pady=(16,0))
    entry1.grid(row=10, column=1, pady=(0,8))
    label2.grid(row=20, column=1, pady=0)
    entry2.grid(row=30, column=1, pady=(0,8))
    label3.grid(row=40, column=1, pady=0)
    entry3.grid(row=50, column=1, pady=(0,8))

    tk.Button(calculationsframe, text='CALCULATE', font="Instruction 13", bg="#1b1b1b", fg="#ffffff", width="16" ,command=show_entry_fields).grid(
                                                                row=80, 
                                                                column=1, 
                                                                sticky=tk.E, 
                                                                pady=8)

    formulamsg("E:\\Projects\\Programming\\Python\\fredie\\formula\\power.png")

def linearMomentumModule(event):
    menuDefault()
    linearMomentumLabel.configure(fg='#e8e916')
    resetCalculationsFrame()
    linearMomentumModuleDisplay()

def linearMomentumModuleDisplay():
    def show_entry_fields():
        try:         
            massInKilogram = float(entry1.get())
            velocityInMS = float(entry2.get())
            if len(str(massInKilogram)) != 0 and len(str(velocityInMS)) != 0:         
                ans = str((massInKilogram * velocityInMS)) + " kg m/s"
                entry3.delete(0,END)
                entry3.insert(0,ans)
        except:   
            popupmsg("Check your inputs")

    label1 = tk.Label(calculationsframe, text="Mass in kilogram", font="Instruction 20", bg="#1b1b1b", fg="#d1bea8", width="26", anchor='w')
    entry1 = tk.Entry(calculationsframe, font="Instruction 20", bg="#ffffff", fg="#0ba98b", width="26", highlightbackground = "#1b1b1b", borderwidth = 0, highlightthickness = 2)
    label2 = tk.Label(calculationsframe, text="Velocity in m/s", font="Instruction 20", bg="#1b1b1b", fg="#d1bea8", width="26", anchor='w')
    entry2 = tk.Entry(calculationsframe, font="Instruction 20", bg="#ffffff", fg="#0ba98b", width="26", highlightbackground = "#1b1b1b", borderwidth = 0, highlightthickness = 2)
    label3 = tk.Label(calculationsframe, text="Answer", font="Instruction 20", bg="#1b1b1b", fg="#d1bea8", width="26", anchor='w')
    entry3 = tk.Entry(calculationsframe, font="Instruction 20", bg="#ffffff", fg="#0ba98b", width="26", highlightbackground = "#1b1b1b", borderwidth = 0, highlightthickness = 2)

    label1.grid(row=0, column=1, pady=(16,0))
    entry1.grid(row=10, column=1, pady=(0,8))
    label2.grid(row=20, column=1, pady=0)
    entry2.grid(row=30, column=1, pady=(0,8))
    label3.grid(row=40, column=1, pady=0)
    entry3.grid(row=50, column=1, pady=(0,8))

    tk.Button(calculationsframe, text='CALCULATE', font="Instruction 13", bg="#1b1b1b", fg="#ffffff", width="16" ,command=show_entry_fields).grid(
                                                                row=80, 
                                                                column=1, 
                                                                sticky=tk.E, 
                                                                pady=8)

    formulamsg("E:\\Projects\\Programming\\Python\\fredie\\formula\\linear_momentum.png")

def impulseModule(event):
    menuDefault()
    impulseLabel.configure(fg='#e8e916')
    resetCalculationsFrame()
    impulseModuleDisplay()

def impulseModuleDisplay():
    def show_entry_fields():
        try:         
            forceInNewton = float(entry1.get())
            timeInSeconds = float(entry2.get())
            if len(str(forceInNewton)) != 0 and len(str(timeInSeconds)) != 0:         
                ans = str((forceInNewton * timeInSeconds)) + " N s"
                entry3.delete(0,END)
                entry3.insert(0,ans)
        except:   
            popupmsg("Check your inputs")

    label1 = tk.Label(calculationsframe, text="Force in newton", font="Instruction 20", bg="#1b1b1b", fg="#d1bea8", width="26", anchor='w')
    entry1 = tk.Entry(calculationsframe, font="Instruction 20", bg="#ffffff", fg="#0ba98b", width="26", highlightbackground = "#1b1b1b", borderwidth = 0, highlightthickness = 2)
    label2 = tk.Label(calculationsframe, text="Time in s", font="Instruction 20", bg="#1b1b1b", fg="#d1bea8", width="26", anchor='w')
    entry2 = tk.Entry(calculationsframe, font="Instruction 20", bg="#ffffff", fg="#0ba98b", width="26", highlightbackground = "#1b1b1b", borderwidth = 0, highlightthickness = 2)
    label3 = tk.Label(calculationsframe, text="Answer", font="Instruction 20", bg="#1b1b1b", fg="#d1bea8", width="26", anchor='w')
    entry3 = tk.Entry(calculationsframe, font="Instruction 20", bg="#ffffff", fg="#0ba98b", width="26", highlightbackground = "#1b1b1b", borderwidth = 0, highlightthickness = 2)

    label1.grid(row=0, column=1, pady=(16,0))
    entry1.grid(row=10, column=1, pady=(0,8))
    label2.grid(row=20, column=1, pady=0)
    entry2.grid(row=30, column=1, pady=(0,8))
    label3.grid(row=40, column=1, pady=0)
    entry3.grid(row=50, column=1, pady=(0,8))

    tk.Button(calculationsframe, text='CALCULATE', font="Instruction 13", bg="#1b1b1b", fg="#ffffff", width="16" ,command=show_entry_fields).grid(
                                                                row=80, 
                                                                column=1, 
                                                                sticky=tk.E, 
                                                                pady=8)

    formulamsg("E:\\Projects\\Programming\\Python\\fredie\\formula\\impulse.png")


def collisionModule(event):
    menuDefault()
    collisionLabel.configure(fg='#e8e916')
    resetCalculationsFrame()
    collisionModuleDisplay()

def collisionModuleDisplay():

    def show_entry_fields():
        try:         
            mass1InKilograms = float(entry1.get())
            mass2InKilograms = float(entry2.get())
            initialVelocity1InMS = float(entry3.get())
            initialVelocity2InMS = float(entry4.get())
            finalVelocity2InMS = float(entry5.get())
            if len(str(mass1InKilograms)) != 0 and len(str(mass2InKilograms)) != 0 and len(str(initialVelocity1InMS)) != 0 and len(str(initialVelocity2InMS)) != 0 and len(str(finalVelocity2InMS)) != 0:         
                ans = str((initialVelocity1InMS - ((mass2InKilograms - (mass2InKilograms * initialVelocity1InMS))/mass1InKilograms))/(initialVelocity1InMS - finalVelocity2InMS)) + ""
                entry6.delete(0,END)
                entry6.insert(0,ans)
        except:   
            popupmsg("Check your inputs")

    label1 = tk.Label(calculationsframe, text="Mass₁ in kilograms", font="Instruction 20", bg="#1b1b1b", fg="#d1bea8", width="26", anchor='w')
    entry1 = tk.Entry(calculationsframe, font="Instruction 20", bg="#ffffff", fg="#0ba98b", width="26", highlightbackground = "#1b1b1b", borderwidth = 0, highlightthickness = 2)
    label2 = tk.Label(calculationsframe, text="Mass₂ in kilograms", font="Instruction 20", bg="#1b1b1b", fg="#d1bea8", width="26", anchor='w')
    entry2 = tk.Entry(calculationsframe, font="Instruction 20", bg="#ffffff", fg="#0ba98b", width="26", highlightbackground = "#1b1b1b", borderwidth = 0, highlightthickness = 2)
    label3 = tk.Label(calculationsframe, text="Initial Velocity₁ in m/s", font="Instruction 20", bg="#1b1b1b", fg="#d1bea8", width="26", anchor='w')
    entry3 = tk.Entry(calculationsframe, font="Instruction 20", bg="#ffffff", fg="#0ba98b", width="26", highlightbackground = "#1b1b1b", borderwidth = 0, highlightthickness = 2)
    label4 = tk.Label(calculationsframe, text="Initial Velocity₂ in m/s", font="Instruction 20", bg="#1b1b1b", fg="#d1bea8", width="26", anchor='w')
    entry4 = tk.Entry(calculationsframe, font="Instruction 20", bg="#ffffff", fg="#0ba98b", width="26", highlightbackground = "#1b1b1b", borderwidth = 0, highlightthickness = 2)
    label5 = tk.Label(calculationsframe, text="Final Velocity₂ in m/s", font="Instruction 20", bg="#1b1b1b", fg="#d1bea8", width="26", anchor='w')
    entry5 = tk.Entry(calculationsframe, font="Instruction 20", bg="#ffffff", fg="#0ba98b", width="26", highlightbackground = "#1b1b1b", borderwidth = 0, highlightthickness = 2)
    label6 = tk.Label(calculationsframe, text="Answer", font="Instruction 20", bg="#1b1b1b", fg="#d1bea8", width="26", anchor='w')
    entry6 = tk.Entry(calculationsframe, font="Instruction 20", bg="#ffffff", fg="#0ba98b", width="26", highlightbackground = "#1b1b1b", borderwidth = 0, highlightthickness = 2)

    label1.grid(row=0, column=1, pady=(16,0))
    entry1.grid(row=10, column=1, pady=(0,8))
    label2.grid(row=20, column=1, pady=0)
    entry2.grid(row=30, column=1, pady=(0,8))
    label3.grid(row=40, column=1, pady=0)
    entry3.grid(row=50, column=1, pady=(0,8))
    label4.grid(row=60, column=1, pady=0)
    entry4.grid(row=70, column=1, pady=(0,8))
    label5.grid(row=80, column=1, pady=0)
    entry5.grid(row=90, column=1, pady=(0,8))
    label6.grid(row=100, column=1, pady=0)
    entry6.grid(row=110, column=1, pady=(0,8))

    tk.Button(calculationsframe, text='CALCULATE', font="Instruction 13", bg="#1b1b1b", fg="#ffffff", width="16" ,command=show_entry_fields).grid(
                                                                row=120, 
                                                                column=1, 
                                                                sticky=tk.E, 
                                                                pady=8)

    formulamsg("E:\\Projects\\Programming\\Python\\fredie\\formula\\collision.png")


def torqueRotationalDynamicsModule(event):
    menuDefault()
    torqueRotationalDynamicsLabel.configure(fg='#e8e916')
    resetCalculationsFrame()
    torqueRotationalDynamicsModuleDisplay()

def torqueRotationalDynamicsModuleDisplay():

    def show_entry_fields():
        try:         
            radiusInMeters = float(entry1.get())
            forceInNewton = float(entry2.get())
            degrees = float(entry3.get())
            if len(str(radiusInMeters)) != 0 and len(str(forceInNewton)) != 0 and len(str(degrees)) != 0 :         
                ans = str(radiusInMeters * forceInNewton * math.sin(degrees*(math.pi/180))) + " N m"
                entry4.delete(0,END)
                entry4.insert(0,ans)
        except:   
            popupmsg("Check your inputs")

    label1 = tk.Label(calculationsframe, text="Radius in meters", font="Instruction 20", bg="#1b1b1b", fg="#d1bea8", width="26", anchor='w')
    entry1 = tk.Entry(calculationsframe, font="Instruction 20", bg="#ffffff", fg="#0ba98b", width="26", highlightbackground = "#1b1b1b", borderwidth = 0, highlightthickness = 2)
    label2 = tk.Label(calculationsframe, text="Force in Newton", font="Instruction 20", bg="#1b1b1b", fg="#d1bea8", width="26", anchor='w')
    entry2 = tk.Entry(calculationsframe, font="Instruction 20", bg="#ffffff", fg="#0ba98b", width="26", highlightbackground = "#1b1b1b", borderwidth = 0, highlightthickness = 2)
    label3 = tk.Label(calculationsframe, text="Angle in degrees", font="Instruction 20", bg="#1b1b1b", fg="#d1bea8", width="26", anchor='w')
    entry3 = tk.Entry(calculationsframe, font="Instruction 20", bg="#ffffff", fg="#0ba98b", width="26", highlightbackground = "#1b1b1b", borderwidth = 0, highlightthickness = 2)
    label4 = tk.Label(calculationsframe, text="Answer", font="Instruction 20", bg="#1b1b1b", fg="#d1bea8", width="26", anchor='w')
    entry4 = tk.Entry(calculationsframe, font="Instruction 20", bg="#ffffff", fg="#0ba98b", width="26", highlightbackground = "#1b1b1b", borderwidth = 0, highlightthickness = 2)

    label1.grid(row=0, column=1, pady=(16,0))
    entry1.grid(row=10, column=1, pady=(0,8))
    label2.grid(row=20, column=1, pady=0)
    entry2.grid(row=30, column=1, pady=(0,8))
    label3.grid(row=40, column=1, pady=0)
    entry3.grid(row=50, column=1, pady=(0,8))
    label4.grid(row=60, column=1, pady=0)
    entry4.grid(row=70, column=1, pady=(0,8))

    tk.Button(calculationsframe, text='CALCULATE', font="Instruction 13", bg="#1b1b1b", fg="#ffffff", width="16" ,command=show_entry_fields).grid(
                                                                row=80, 
                                                                column=1, 
                                                                sticky=tk.E, 
                                                                pady=8)

    formulamsg("E:\\Projects\\Programming\\Python\\fredie\\formula\\torque_rotational_dynamics.png")


def momentOfInertiaModule(event):
    menuDefault()
    momentOfInertiaLabel.configure(fg='#e8e916')
    resetCalculationsFrame()
    momentOfInertiaModuleDisplay()

def momentOfInertiaModuleDisplay():

    def show_entry_fields():
        try:         
            massInKilogram = float(entry1.get())
            radiusInMeters = float(entry2.get())
            if len(str(massInKilogram)) != 0 and len(str(radiusInMeters)) != 0:         
                ans = str(massInKilogram * math.pow(radiusInMeters, 2)) + " kg m^2"
                entry3.delete(0,END)
                entry3.insert(0,ans)
        except:   
            popupmsg("Check your inputs")

    label1 = tk.Label(calculationsframe, text="Mass in kilogram", font="Instruction 20", bg="#1b1b1b", fg="#d1bea8", width="26", anchor='w')
    entry1 = tk.Entry(calculationsframe, font="Instruction 20", bg="#ffffff", fg="#0ba98b", width="26", highlightbackground = "#1b1b1b", borderwidth = 0, highlightthickness = 2)
    label2 = tk.Label(calculationsframe, text="Radius in meters", font="Instruction 20", bg="#1b1b1b", fg="#d1bea8", width="26", anchor='w')
    entry2 = tk.Entry(calculationsframe, font="Instruction 20", bg="#ffffff", fg="#0ba98b", width="26", highlightbackground = "#1b1b1b", borderwidth = 0, highlightthickness = 2)
    label3 = tk.Label(calculationsframe, text="Answer", font="Instruction 20", bg="#1b1b1b", fg="#d1bea8", width="26", anchor='w')
    entry3 = tk.Entry(calculationsframe, font="Instruction 20", bg="#ffffff", fg="#0ba98b", width="26", highlightbackground = "#1b1b1b", borderwidth = 0, highlightthickness = 2)

    label1.grid(row=0, column=1, pady=(16,0))
    entry1.grid(row=10, column=1, pady=(0,8))
    label2.grid(row=20, column=1, pady=0)
    entry2.grid(row=30, column=1, pady=(0,8))
    label3.grid(row=40, column=1, pady=0)
    entry3.grid(row=50, column=1, pady=(0,8))

    tk.Button(calculationsframe, text='CALCULATE', font="Instruction 13", bg="#1b1b1b", fg="#ffffff", width="16" ,command=show_entry_fields).grid(
                                                                row=80, 
                                                                column=1, 
                                                                sticky=tk.E, 
                                                                pady=8)

    formulamsg("E:\\Projects\\Programming\\Python\\fredie\\formula\\moment_of_inertia.png")


def gravitationalForceModule(event):
    menuDefault()
    gravitationalForceLabel.configure(fg='#e8e916')
    resetCalculationsFrame()
    gravitationalForceModuleDisplay()

def gravitationalForceModuleDisplay():
    def show_entry_fields():
        try:         
            mass1InKilogram = float(entry1.get())
            mass2InKilogram = float(entry2.get())
            distanceInMeters = float(entry3.get())
            if len(str(mass1InKilogram)) != 0 and len(str(mass2InKilogram)) != 0 and len(str(distanceInMeters)) != 0:         
                ans = str(const.G * ((mass1InKilogram * mass2InKilogram)/(math.pow(distanceInMeters,2)))).replace("m3 / (kg s2)", "") + "N"     
                entry4.delete(0,END)
                entry4.insert(0,ans)
        except:   
            popupmsg("Check your inputs")

    label1 = tk.Label(calculationsframe, text="Mass₁ in kilograms", font="Instruction 20", bg="#1b1b1b", fg="#d1bea8", width="26", anchor='w')
    entry1 = tk.Entry(calculationsframe, font="Instruction 20", bg="#ffffff", fg="#0ba98b", width="26", highlightbackground = "#1b1b1b", borderwidth = 0, highlightthickness = 2)
    label2 = tk.Label(calculationsframe, text="Mass₂ in kilograms", font="Instruction 20", bg="#1b1b1b", fg="#d1bea8", width="26", anchor='w')
    entry2 = tk.Entry(calculationsframe, font="Instruction 20", bg="#ffffff", fg="#0ba98b", width="26", highlightbackground = "#1b1b1b", borderwidth = 0, highlightthickness = 2)
    label3 = tk.Label(calculationsframe, text="Distance in meters", font="Instruction 20", bg="#1b1b1b", fg="#d1bea8", width="26", anchor='w')
    entry3 = tk.Entry(calculationsframe, font="Instruction 20", bg="#ffffff", fg="#0ba98b", width="26", highlightbackground = "#1b1b1b", borderwidth = 0, highlightthickness = 2)
    label4 = tk.Label(calculationsframe, text="Answer", font="Instruction 20", bg="#1b1b1b", fg="#d1bea8", width="26", anchor='w')
    entry4 = tk.Entry(calculationsframe, font="Instruction 20", bg="#ffffff", fg="#0ba98b", width="26", highlightbackground = "#1b1b1b", borderwidth = 0, highlightthickness = 2)

    label1.grid(row=0, column=1, pady=(16,0))
    entry1.grid(row=10, column=1, pady=(0,8))
    label2.grid(row=20, column=1, pady=0)
    entry2.grid(row=30, column=1, pady=(0,8))
    label3.grid(row=40, column=1, pady=0)
    entry3.grid(row=50, column=1, pady=(0,8))
    label4.grid(row=60, column=1, pady=0)
    entry4.grid(row=70, column=1, pady=(0,8))

    tk.Button(calculationsframe, text='CALCULATE', font="Instruction 13", bg="#1b1b1b", fg="#ffffff", width="16" ,command=show_entry_fields).grid(
                                                                row=80, 
                                                                column=1, 
                                                                sticky=tk.E, 
                                                                pady=8)

    formulamsg("E:\\Projects\\Programming\\Python\\fredie\\formula\\gravitational_force.png")

def semimajorAxisModule(event):
    menuDefault()
    semimajorAxisLabel.configure(fg='#e8e916')
    resetCalculationsFrame()
    semimajorAxisModuleDisplay()

def semimajorAxisModuleDisplay():

    def show_entry_fields():
        try:
            def cube(x):
                if 0<=x: return x**(1./3.)
                return -(-x)**(1./3.)         
            orbitalPeriodInYears = float(entry1.get())
            orbitalEccentricity = float(entry2.get())
            if len(str(orbitalPeriodInYears)) != 0 and len(str(orbitalEccentricity)) != 0:         
                ans = str(cube(((math.pow( (31557600 * orbitalPeriodInYears),2))/(4*math.pow(math.pi,2))))) + " m"
                entry3.delete(0,END)
                entry3.insert(0,ans)
        except:   
            popupmsg("Check your inputs")

    label1 = tk.Label(calculationsframe, text="Orbital Period in years", font="Instruction 20", bg="#1b1b1b", fg="#d1bea8", width="26", anchor='w')
    entry1 = tk.Entry(calculationsframe, font="Instruction 20", bg="#ffffff", fg="#0ba98b", width="26", highlightbackground = "#1b1b1b", borderwidth = 0, highlightthickness = 2)
    label2 = tk.Label(calculationsframe, text="Orbital Eccentricity", font="Instruction 20", bg="#1b1b1b", fg="#d1bea8", width="26", anchor='w')
    entry2 = tk.Entry(calculationsframe, font="Instruction 20", bg="#ffffff", fg="#0ba98b", width="26", highlightbackground = "#1b1b1b", borderwidth = 0, highlightthickness = 2)
    label3 = tk.Label(calculationsframe, text="Answer", font="Instruction 20", bg="#1b1b1b", fg="#d1bea8", width="26", anchor='w')
    entry3 = tk.Entry(calculationsframe, font="Instruction 20", bg="#ffffff", fg="#0ba98b", width="26", highlightbackground = "#1b1b1b", borderwidth = 0, highlightthickness = 2)

    label1.grid(row=0, column=1, pady=(16,0))
    entry1.grid(row=10, column=1, pady=(0,8))
    label2.grid(row=20, column=1, pady=0)
    entry2.grid(row=30, column=1, pady=(0,8))
    label3.grid(row=40, column=1, pady=0)
    entry3.grid(row=50, column=1, pady=(0,8))

    tk.Button(calculationsframe, text='CALCULATE', font="Instruction 13", bg="#1b1b1b", fg="#ffffff", width="16" ,command=show_entry_fields).grid(
                                                                row=80, 
                                                                column=1, 
                                                                sticky=tk.E, 
                                                                pady=8)

    formulamsg("E:\\Projects\\Programming\\Python\\fredie\\formula\\semimajor_axis.png")

def shearStressModule(event):
    menuDefault()
    shearStressLabel.configure(fg='#e8e916')
    resetCalculationsFrame()
    shearStressModuleDisplay()

def shearStressModuleDisplay():
    def show_entry_fields():
        try:      
            forceInNewton = float(entry1.get())
            outerDiameterInMeter = float(entry2.get())
            innerDiameterInMeter = float(entry3.get())
            if len(str(forceInNewton)) != 0 and len(str(outerDiameterInMeter)) != 0 and len(str(innerDiameterInMeter)) != 0:         
                ans = str((16 * (forceInNewton * outerDiameterInMeter))/(math.pi * (math.pow(outerDiameterInMeter,4) - math.pow(innerDiameterInMeter,4)))) + " N/m^2"
                entry4.delete(0,END)
                entry4.insert(0,ans)
        except:   
            popupmsg("Check your inputs")

    label1 = tk.Label(calculationsframe, text="Force in N m", font="Instruction 20", bg="#1b1b1b", fg="#d1bea8", width="26", anchor='w')
    entry1 = tk.Entry(calculationsframe, font="Instruction 20", bg="#ffffff", fg="#0ba98b", width="26", highlightbackground = "#1b1b1b", borderwidth = 0, highlightthickness = 2)
    label2 = tk.Label(calculationsframe, text="Outer Diameter in meter", font="Instruction 20", bg="#1b1b1b", fg="#d1bea8", width="26", anchor='w')
    entry2 = tk.Entry(calculationsframe, font="Instruction 20", bg="#ffffff", fg="#0ba98b", width="26", highlightbackground = "#1b1b1b", borderwidth = 0, highlightthickness = 2)
    label3 = tk.Label(calculationsframe, text="Inner Diameter in meter", font="Instruction 20", bg="#1b1b1b", fg="#d1bea8", width="26", anchor='w')
    entry3 = tk.Entry(calculationsframe, font="Instruction 20", bg="#ffffff", fg="#0ba98b", width="26", highlightbackground = "#1b1b1b", borderwidth = 0, highlightthickness = 2)
    label4 = tk.Label(calculationsframe, text="Answer", font="Instruction 20", bg="#1b1b1b", fg="#d1bea8", width="26", anchor='w')
    entry4 = tk.Entry(calculationsframe, font="Instruction 20", bg="#ffffff", fg="#0ba98b", width="26", highlightbackground = "#1b1b1b", borderwidth = 0, highlightthickness = 2)

    label1.grid(row=0, column=1, pady=(16,0))
    entry1.grid(row=10, column=1, pady=(0,8))
    label2.grid(row=20, column=1, pady=0)
    entry2.grid(row=30, column=1, pady=(0,8))
    label3.grid(row=40, column=1, pady=0)
    entry3.grid(row=50, column=1, pady=(0,8))
    label4.grid(row=60, column=1, pady=0)
    entry4.grid(row=70, column=1, pady=(0,8))

    tk.Button(calculationsframe, text='CALCULATE', font="Instruction 13", bg="#1b1b1b", fg="#ffffff", width="16" ,command=show_entry_fields).grid(
                                                                row=80, 
                                                                column=1, 
                                                                sticky=tk.E, 
                                                                pady=8)

    formulamsg("E:\\Projects\\Programming\\Python\\fredie\\formula\\shear_stress.png")

def poissonsRatioModule(event):
    menuDefault()
    poissonsRatioLabel.configure(fg='#e8e916')
    resetCalculationsFrame()
    poissonsRatioModuleDisplay()

def poissonsRatioModuleDisplay():
    def show_entry_fields():
        try:      
            lateralStrain = float(entry1.get())
            axialStrain = float(entry2.get())
            if len(str(lateralStrain)) != 0 and len(str(axialStrain)) != 0:         
                ans = str(lateralStrain/axialStrain) + ""
                entry3.delete(0,END)
                entry3.insert(0,ans)
        except:   
            popupmsg("Check your inputs")

    label1 = tk.Label(calculationsframe, text="Lateral strain", font="Instruction 20", bg="#1b1b1b", fg="#d1bea8", width="26", anchor='w')
    entry1 = tk.Entry(calculationsframe, font="Instruction 20", bg="#ffffff", fg="#0ba98b", width="26", highlightbackground = "#1b1b1b", borderwidth = 0, highlightthickness = 2)
    label2 = tk.Label(calculationsframe, text="Axial strain", font="Instruction 20", bg="#1b1b1b", fg="#d1bea8", width="26", anchor='w')
    entry2 = tk.Entry(calculationsframe, font="Instruction 20", bg="#ffffff", fg="#0ba98b", width="26", highlightbackground = "#1b1b1b", borderwidth = 0, highlightthickness = 2)
    label3 = tk.Label(calculationsframe, text="Answer", font="Instruction 20", bg="#1b1b1b", fg="#d1bea8", width="26", anchor='w')
    entry3 = tk.Entry(calculationsframe, font="Instruction 20", bg="#ffffff", fg="#0ba98b", width="26", highlightbackground = "#1b1b1b", borderwidth = 0, highlightthickness = 2)

    label1.grid(row=0, column=1, pady=(16,0))
    entry1.grid(row=10, column=1, pady=(0,8))
    label2.grid(row=20, column=1, pady=0)
    entry2.grid(row=30, column=1, pady=(0,8))
    label3.grid(row=40, column=1, pady=0)
    entry3.grid(row=50, column=1, pady=(0,8))

    tk.Button(calculationsframe, text='CALCULATE', font="Instruction 13", bg="#1b1b1b", fg="#ffffff", width="16" ,command=show_entry_fields).grid(
                                                                row=80, 
                                                                column=1, 
                                                                sticky=tk.E, 
                                                                pady=8)

    formulamsg("E:\\Projects\\Programming\\Python\\fredie\\formula\\poisson_ratio.png")

def crossSectionalAreaModule(event):
    menuDefault()
    crossSectionalAreaLabel.configure(fg='#e8e916')
    resetCalculationsFrame()
    crossSectionalAreaModuleDisplay()

def crossSectionalAreaModuleDisplay():

    def show_entry_fields():
        try:      
            lengthOriginalInMeters = float(entry1.get())
            youngsModulusInPa = float(entry2.get())
            lengthChangeInMeters = float(entry3.get())
            strainEnergyInJoules = float(entry4.get())
            if len(str(lengthOriginalInMeters)) != 0 and len(str(youngsModulusInPa)) != 0 and len(str(lengthChangeInMeters)) != 0 and len(str(strainEnergyInJoules)) != 0:         
                ans = str((2*(strainEnergyInJoules)*(lengthOriginalInMeters))/(youngsModulusInPa * math.pow(lengthChangeInMeters,2))) + " m^2"
                entry5.delete(0,END)
                entry5.insert(0,ans)
        except:   
            popupmsg("Check your inputs")

    label1 = tk.Label(calculationsframe, text="Length original in meters", font="Instruction 20", bg="#1b1b1b", fg="#d1bea8", width="26", anchor='w')
    entry1 = tk.Entry(calculationsframe, font="Instruction 20", bg="#ffffff", fg="#0ba98b", width="26", highlightbackground = "#1b1b1b", borderwidth = 0, highlightthickness = 2)
    label2 = tk.Label(calculationsframe, text="Young's modulus in Pa", font="Instruction 20", bg="#1b1b1b", fg="#d1bea8", width="26", anchor='w')
    entry2 = tk.Entry(calculationsframe, font="Instruction 20", bg="#ffffff", fg="#0ba98b", width="26", highlightbackground = "#1b1b1b", borderwidth = 0, highlightthickness = 2)
    label3 = tk.Label(calculationsframe, text="Length change in meters", font="Instruction 20", bg="#1b1b1b", fg="#d1bea8", width="26", anchor='w')
    entry3 = tk.Entry(calculationsframe, font="Instruction 20", bg="#ffffff", fg="#0ba98b", width="26", highlightbackground = "#1b1b1b", borderwidth = 0, highlightthickness = 2)
    label4 = tk.Label(calculationsframe, text="Strain energy in joules", font="Instruction 20", bg="#1b1b1b", fg="#d1bea8", width="26", anchor='w')
    entry4 = tk.Entry(calculationsframe, font="Instruction 20", bg="#ffffff", fg="#0ba98b", width="26", highlightbackground = "#1b1b1b", borderwidth = 0, highlightthickness = 2)
    label5 = tk.Label(calculationsframe, text="Answer", font="Instruction 20", bg="#1b1b1b", fg="#d1bea8", width="26", anchor='w')
    entry5 = tk.Entry(calculationsframe, font="Instruction 20", bg="#ffffff", fg="#0ba98b", width="26", highlightbackground = "#1b1b1b", borderwidth = 0, highlightthickness = 2)

    label1.grid(row=0, column=1, pady=(16,0))
    entry1.grid(row=10, column=1, pady=(0,8))
    label2.grid(row=20, column=1, pady=0)
    entry2.grid(row=30, column=1, pady=(0,8))
    label3.grid(row=40, column=1, pady=0)
    entry3.grid(row=50, column=1, pady=(0,8))
    label4.grid(row=60, column=1, pady=0)
    entry4.grid(row=70, column=1, pady=(0,8))
    label5.grid(row=80, column=1, pady=0)
    entry5.grid(row=90, column=1, pady=(0,8))

    tk.Button(calculationsframe, text='CALCULATE', font="Instruction 13", bg="#1b1b1b", fg="#ffffff", width="16" ,command=show_entry_fields).grid(
                                                                row=100, 
                                                                column=1, 
                                                                sticky=tk.E, 
                                                                pady=8)

    formulamsg("E:\\Projects\\Programming\\Python\\fredie\\formula\\cross_sectional_area.png")

def pressureModule(event):
    menuDefault()
    pressureLabel.configure(fg='#e8e916')
    resetCalculationsFrame()
    pressureModuleDisplay()

def pressureModuleDisplay():
    def show_entry_fields():
        try:      
            forceInNewton = float(entry1.get())
            lengthInMeters = float(entry2.get())
            specificGravity = float(entry3.get())
            massInKilograms = float(entry4.get())
            if len(str(forceInNewton)) != 0 and len(str(lengthInMeters)) != 0 and len(str(specificGravity)) != 0 and len(str(massInKilograms)) != 0:         
                ans = str(((forceInNewton * lengthInMeters)*(specificGravity*1000))/(massInKilograms)) + " Pa"
                entry5.delete(0,END)
                entry5.insert(0,ans)
        except:   
            popupmsg("Check your inputs")

    label1 = tk.Label(calculationsframe, text="Force in newton", font="Instruction 20", bg="#1b1b1b", fg="#d1bea8", width="26", anchor='w')
    entry1 = tk.Entry(calculationsframe, font="Instruction 20", bg="#ffffff", fg="#0ba98b", width="26", highlightbackground = "#1b1b1b", borderwidth = 0, highlightthickness = 2)
    label2 = tk.Label(calculationsframe, text="Length in meters", font="Instruction 20", bg="#1b1b1b", fg="#d1bea8", width="26", anchor='w')
    entry2 = tk.Entry(calculationsframe, font="Instruction 20", bg="#ffffff", fg="#0ba98b", width="26", highlightbackground = "#1b1b1b", borderwidth = 0, highlightthickness = 2)
    label3 = tk.Label(calculationsframe, text="Specific gravity", font="Instruction 20", bg="#1b1b1b", fg="#d1bea8", width="26", anchor='w')
    entry3 = tk.Entry(calculationsframe, font="Instruction 20", bg="#ffffff", fg="#0ba98b", width="26", highlightbackground = "#1b1b1b", borderwidth = 0, highlightthickness = 2)
    label4 = tk.Label(calculationsframe, text="Mass in kilograms", font="Instruction 20", bg="#1b1b1b", fg="#d1bea8", width="26", anchor='w')
    entry4 = tk.Entry(calculationsframe, font="Instruction 20", bg="#ffffff", fg="#0ba98b", width="26", highlightbackground = "#1b1b1b", borderwidth = 0, highlightthickness = 2)
    label5 = tk.Label(calculationsframe, text="Answer", font="Instruction 20", bg="#1b1b1b", fg="#d1bea8", width="26", anchor='w')
    entry5 = tk.Entry(calculationsframe, font="Instruction 20", bg="#ffffff", fg="#0ba98b", width="26", highlightbackground = "#1b1b1b", borderwidth = 0, highlightthickness = 2)

    label1.grid(row=0, column=1, pady=(16,0))
    entry1.grid(row=10, column=1, pady=(0,8))
    label2.grid(row=20, column=1, pady=0)
    entry2.grid(row=30, column=1, pady=(0,8))
    label3.grid(row=40, column=1, pady=0)
    entry3.grid(row=50, column=1, pady=(0,8))
    label4.grid(row=60, column=1, pady=0)
    entry4.grid(row=70, column=1, pady=(0,8))
    label5.grid(row=80, column=1, pady=0)
    entry5.grid(row=90, column=1, pady=(0,8))

    tk.Button(calculationsframe, text='CALCULATE', font="Instruction 13", bg="#1b1b1b", fg="#ffffff", width="16" ,command=show_entry_fields).grid(
                                                                row=100, 
                                                                column=1, 
                                                                sticky=tk.E, 
                                                                pady=8)

    formulamsg("E:\\Projects\\Programming\\Python\\fredie\\formula\\pressure.png")

def potentialEnergyFluidsAndHarmonicsModule(event):
    menuDefault()
    potentialEnergyFluidsAndHarmonicsLabel.configure(fg='#e8e916')
    resetCalculationsFrame()
    potentialEnergyFluidsAndHarmonicsModuleDisplay()

def potentialEnergyFluidsAndHarmonicsModuleDisplay():
    def show_entry_fields():
        try:      
            heightInMeters = float(entry1.get())
            if len(str(heightInMeters)) != 0:         
                ans = str((1000) * ((9.81) * (heightInMeters/2)) )+ " J"
                entry2.delete(0,END)
                entry2.insert(0,ans)
        except:   
            popupmsg("Check your inputs")

    label1 = tk.Label(calculationsframe, text="Height in meters", font="Instruction 20", bg="#1b1b1b", fg="#d1bea8", width="26", anchor='w')
    entry1 = tk.Entry(calculationsframe, font="Instruction 20", bg="#ffffff", fg="#0ba98b", width="26", highlightbackground = "#1b1b1b", borderwidth = 0, highlightthickness = 2)
    label2 = tk.Label(calculationsframe, text="Answer", font="Instruction 20", bg="#1b1b1b", fg="#d1bea8", width="26", anchor='w')
    entry2 = tk.Entry(calculationsframe, font="Instruction 20", bg="#ffffff", fg="#0ba98b", width="26", highlightbackground = "#1b1b1b", borderwidth = 0, highlightthickness = 2)

    label1.grid(row=0, column=1, pady=(16,0))
    entry1.grid(row=10, column=1, pady=(0,8))
    label2.grid(row=20, column=1, pady=0)
    entry2.grid(row=30, column=1, pady=(0,8))

    tk.Button(calculationsframe, text='CALCULATE', font="Instruction 13", bg="#1b1b1b", fg="#ffffff", width="16" ,command=show_entry_fields).grid(
                                                                row=80, 
                                                                column=1, 
                                                                sticky=tk.E, 
                                                                pady=8)

    formulamsg("E:\\Projects\\Programming\\Python\\fredie\\formula\\potential_energy_fluids_and_harmonics.png")

def volumeFlowRateModule(event):
    menuDefault()
    volumeFlowRateLabel.configure(fg='#e8e916')
    resetCalculationsFrame()
    volumeFlowRateModuleDisplay()

def volumeFlowRateModuleDisplay():
    def show_entry_fields():
        try:      
            areaInMeters = float(entry1.get())
            velocityInMS = float(entry2.get())
            if len(str(areaInMeters)) != 0 and len(str(velocityInMS)) != 0:         
                ans = str((math.pi * (math.pow(areaInMeters,2)) * (velocityInMS)) )+ " m^3/s"
                entry3.delete(0,END)
                entry3.insert(0,ans)
        except:   
            popupmsg("Check your inputs")

    label1 = tk.Label(calculationsframe, text="Area in meters", font="Instruction 20", bg="#1b1b1b", fg="#d1bea8", width="26", anchor='w')
    entry1 = tk.Entry(calculationsframe, font="Instruction 20", bg="#ffffff", fg="#0ba98b", width="26", highlightbackground = "#1b1b1b", borderwidth = 0, highlightthickness = 2)
    label2 = tk.Label(calculationsframe, text="Velocity in m/s", font="Instruction 20", bg="#1b1b1b", fg="#d1bea8", width="26", anchor='w')
    entry2 = tk.Entry(calculationsframe, font="Instruction 20", bg="#ffffff", fg="#0ba98b", width="26", highlightbackground = "#1b1b1b", borderwidth = 0, highlightthickness = 2)
    label3 = tk.Label(calculationsframe, text="Answer", font="Instruction 20", bg="#1b1b1b", fg="#d1bea8", width="26", anchor='w')
    entry3 = tk.Entry(calculationsframe, font="Instruction 20", bg="#ffffff", fg="#0ba98b", width="26", highlightbackground = "#1b1b1b", borderwidth = 0, highlightthickness = 2)


    label1.grid(row=0, column=1, pady=(16,0))
    entry1.grid(row=10, column=1, pady=(0,8))
    label2.grid(row=20, column=1, pady=0)
    entry2.grid(row=30, column=1, pady=(0,8))
    label3.grid(row=40, column=1, pady=0)
    entry3.grid(row=50, column=1, pady=(0,8))

    tk.Button(calculationsframe, text='CALCULATE', font="Instruction 13", bg="#1b1b1b", fg="#ffffff", width="16" ,command=show_entry_fields).grid(
                                                                row=80, 
                                                                column=1, 
                                                                sticky=tk.E, 
                                                                pady=8)

    formulamsg("E:\\Projects\\Programming\\Python\\fredie\\formula\\volume_flow_rate.png")


def periodOfOscillationModule(event):
    menuDefault()
    periodOfOscillationLabel.configure(fg='#e8e916')
    resetCalculationsFrame()
    periodOfOscillationModuleDisplay()

def periodOfOscillationModuleDisplay():
    def show_entry_fields():
        try:      
            lengthInMeters = float(entry1.get())
            if len(str(lengthInMeters)) != 0:         
                ans = str((2 * math.pi) * (math.sqrt((lengthInMeters/9.8))) )+ " s"
                entry2.delete(0,END)
                entry2.insert(0,ans)
        except:   
            popupmsg("Check your inputs")

    label1 = tk.Label(calculationsframe, text="Length in meters", font="Instruction 20", bg="#1b1b1b", fg="#d1bea8", width="26", anchor='w')
    entry1 = tk.Entry(calculationsframe, font="Instruction 20", bg="#ffffff", fg="#0ba98b", width="26", highlightbackground = "#1b1b1b", borderwidth = 0, highlightthickness = 2)
    label2 = tk.Label(calculationsframe, text="Answer", font="Instruction 20", bg="#1b1b1b", fg="#d1bea8", width="26", anchor='w')
    entry2 = tk.Entry(calculationsframe, font="Instruction 20", bg="#ffffff", fg="#0ba98b", width="26", highlightbackground = "#1b1b1b", borderwidth = 0, highlightthickness = 2)


    label1.grid(row=0, column=1, pady=(16,0))
    entry1.grid(row=10, column=1, pady=(0,8))
    label2.grid(row=20, column=1, pady=0)
    entry2.grid(row=30, column=1, pady=(0,8))

    tk.Button(calculationsframe, text='CALCULATE', font="Instruction 13", bg="#1b1b1b", fg="#ffffff", width="16" ,command=show_entry_fields).grid(
                                                                row=80, 
                                                                column=1, 
                                                                sticky=tk.E, 
                                                                pady=8)

    formulamsg("E:\\Projects\\Programming\\Python\\fredie\\formula\\period_of_oscillation.png")


def waveSpeedModule(event):
    menuDefault()
    waveSpeedLabel.configure(fg='#e8e916')
    resetCalculationsFrame()
    waveSpeedModuleDisplay()

def waveSpeedModuleDisplay():
    def show_entry_fields():
        try:      
            distanceInMeters = float(entry1.get())
            timeInSeconds = float(entry2.get())
            if len(str(distanceInMeters)) != 0 and len(str(timeInSeconds)) != 0:         
                ans = str(distanceInMeters / timeInSeconds)+ " m/s"
                entry3.delete(0,END)
                entry3.insert(0,ans)
        except:   
            popupmsg("Check your inputs")

    label1 = tk.Label(calculationsframe, text="Distance in meters", font="Instruction 20", bg="#1b1b1b", fg="#d1bea8", width="26", anchor='w')
    entry1 = tk.Entry(calculationsframe, font="Instruction 20", bg="#ffffff", fg="#0ba98b", width="26", highlightbackground = "#1b1b1b", borderwidth = 0, highlightthickness = 2)
    label2 = tk.Label(calculationsframe, text="Time in seconds", font="Instruction 20", bg="#1b1b1b", fg="#d1bea8", width="26", anchor='w')
    entry2 = tk.Entry(calculationsframe, font="Instruction 20", bg="#ffffff", fg="#0ba98b", width="26", highlightbackground = "#1b1b1b", borderwidth = 0, highlightthickness = 2)
    label3 = tk.Label(calculationsframe, text="Answer", font="Instruction 20", bg="#1b1b1b", fg="#d1bea8", width="26", anchor='w')
    entry3 = tk.Entry(calculationsframe, font="Instruction 20", bg="#ffffff", fg="#0ba98b", width="26", highlightbackground = "#1b1b1b", borderwidth = 0, highlightthickness = 2)


    label1.grid(row=0, column=1, pady=(16,0))
    entry1.grid(row=10, column=1, pady=(0,8))
    label2.grid(row=20, column=1, pady=0)
    entry2.grid(row=30, column=1, pady=(0,8))
    label3.grid(row=40, column=1, pady=0)
    entry3.grid(row=50, column=1, pady=(0,8))

    tk.Button(calculationsframe, text='CALCULATE', font="Instruction 13", bg="#1b1b1b", fg="#ffffff", width="16" ,command=show_entry_fields).grid(
                                                                row=80, 
                                                                column=1, 
                                                                sticky=tk.E, 
                                                                pady=8)

    formulamsg("E:\\Projects\\Programming\\Python\\fredie\\formula\\wave_speed.png")

def wavelengthModule(event):
    menuDefault()
    wavelengthLabel.configure(fg='#e8e916')
    resetCalculationsFrame()
    wavelengthModuleDisplay()

def wavelengthModuleDisplay():
    def show_entry_fields():
        try:      
            vibrationInMS = float(entry1.get())
            frequencyInHertz = float(entry2.get())
            if len(str(vibrationInMS)) != 0 and len(str(frequencyInHertz)) != 0:         
                ans = str(vibrationInMS / frequencyInHertz)+ " m"
                entry3.delete(0,END)
                entry3.insert(0,ans)
        except:   
            popupmsg("Check your inputs")

    label1 = tk.Label(calculationsframe, text="Vibration in m/s", font="Instruction 20", bg="#1b1b1b", fg="#d1bea8", width="26", anchor='w')
    entry1 = tk.Entry(calculationsframe, font="Instruction 20", bg="#ffffff", fg="#0ba98b", width="26", highlightbackground = "#1b1b1b", borderwidth = 0, highlightthickness = 2)
    label2 = tk.Label(calculationsframe, text="Frequency in hertz", font="Instruction 20", bg="#1b1b1b", fg="#d1bea8", width="26", anchor='w')
    entry2 = tk.Entry(calculationsframe, font="Instruction 20", bg="#ffffff", fg="#0ba98b", width="26", highlightbackground = "#1b1b1b", borderwidth = 0, highlightthickness = 2)
    label3 = tk.Label(calculationsframe, text="Answer", font="Instruction 20", bg="#1b1b1b", fg="#d1bea8", width="26", anchor='w')
    entry3 = tk.Entry(calculationsframe, font="Instruction 20", bg="#ffffff", fg="#0ba98b", width="26", highlightbackground = "#1b1b1b", borderwidth = 0, highlightthickness = 2)


    label1.grid(row=0, column=1, pady=(16,0))
    entry1.grid(row=10, column=1, pady=(0,8))
    label2.grid(row=20, column=1, pady=0)
    entry2.grid(row=30, column=1, pady=(0,8))
    label3.grid(row=40, column=1, pady=0)
    entry3.grid(row=50, column=1, pady=(0,8))

    tk.Button(calculationsframe, text='CALCULATE', font="Instruction 13", bg="#1b1b1b", fg="#ffffff", width="16" ,command=show_entry_fields).grid(
                                                                row=80, 
                                                                column=1, 
                                                                sticky=tk.E, 
                                                                pady=8)

    formulamsg("E:\\Projects\\Programming\\Python\\fredie\\formula\\wavelength.png")

def requiredHeatModule(event):
    menuDefault()
    requiredHeatLabel.configure(fg='#e8e916')
    resetCalculationsFrame()
    requiredHeatModuleDisplay()

def requiredHeatModuleDisplay():

    def show_entry_fields():
        try:      
            massInKilograms = float(entry1.get())
            specificHeatInKcalKgK = float(entry2.get())
            initialTemperatureInC = float(entry3.get())
            finalTemperatureInC = float(entry4.get())
            if len(str(specificHeatInKcalKgK)) != 0 and len(str(specificHeatInKcalKgK)) != 0 and len(str(initialTemperatureInC)) != 0 and len(str(finalTemperatureInC)) != 0:         
                ans = str((massInKilograms * specificHeatInKcalKgK) * ((finalTemperatureInC + 273.15)-(initialTemperatureInC + 273.15)))+ " kcal"
                entry5.delete(0,END)
                entry5.insert(0,ans)
        except:   
            popupmsg("Check your inputs")
    label1 = tk.Label(calculationsframe, text="Mass in kilograms", font="Instruction 20", bg="#1b1b1b", fg="#d1bea8", width="26", anchor='w')
    entry1 = tk.Entry(calculationsframe, font="Instruction 20", bg="#ffffff", fg="#0ba98b", width="26", highlightbackground = "#1b1b1b", borderwidth = 0, highlightthickness = 2)
    label2 = tk.Label(calculationsframe, text="Specific heat in kcal/kg k", font="Instruction 20", bg="#1b1b1b", fg="#d1bea8", width="26", anchor='w')
    entry2 = tk.Entry(calculationsframe, font="Instruction 20", bg="#ffffff", fg="#0ba98b", width="26", highlightbackground = "#1b1b1b", borderwidth = 0, highlightthickness = 2)
    label3 = tk.Label(calculationsframe, text="Initial temperature in C", font="Instruction 20", bg="#1b1b1b", fg="#d1bea8", width="26", anchor='w')
    entry3 = tk.Entry(calculationsframe, font="Instruction 20", bg="#ffffff", fg="#0ba98b", width="26", highlightbackground = "#1b1b1b", borderwidth = 0, highlightthickness = 2)
    label4 = tk.Label(calculationsframe, text="Final temperature in C", font="Instruction 20", bg="#1b1b1b", fg="#d1bea8", width="26", anchor='w')
    entry4 = tk.Entry(calculationsframe, font="Instruction 20", bg="#ffffff", fg="#0ba98b", width="26", highlightbackground = "#1b1b1b", borderwidth = 0, highlightthickness = 2)
    label5 = tk.Label(calculationsframe, text="Answer", font="Instruction 20", bg="#1b1b1b", fg="#d1bea8", width="26", anchor='w')
    entry5 = tk.Entry(calculationsframe, font="Instruction 20", bg="#ffffff", fg="#0ba98b", width="26", highlightbackground = "#1b1b1b", borderwidth = 0, highlightthickness = 2)


    label1.grid(row=0, column=1, pady=(16,0))
    entry1.grid(row=10, column=1, pady=(0,8))
    label2.grid(row=20, column=1, pady=0)
    entry2.grid(row=30, column=1, pady=(0,8))
    label3.grid(row=40, column=1, pady=0)
    entry3.grid(row=50, column=1, pady=(0,8))
    label3.grid(row=60, column=1, pady=0)
    entry3.grid(row=70, column=1, pady=(0,8))
    label4.grid(row=80, column=1, pady=0)
    entry4.grid(row=90, column=1, pady=(0,8))
    label5.grid(row=100, column=1, pady=0)
    entry5.grid(row=110, column=1, pady=(0,8))

    tk.Button(calculationsframe, text='CALCULATE', font="Instruction 13", bg="#1b1b1b", fg="#ffffff", width="16" ,command=show_entry_fields).grid(
                                                                row=120, 
                                                                column=1, 
                                                                sticky=tk.E, 
                                                                pady=8)

    formulamsg("E:\\Projects\\Programming\\Python\\fredie\\formula\\required_heat.png")

def molarHeatCapacityModule(event):
    menuDefault()
    molarHeatCapacityLabel.configure(fg='#e8e916')
    resetCalculationsFrame()
    molarHeatCapacityModuleDisplay()

def molarHeatCapacityModuleDisplay():

    def show_entry_fields():
        try:      
            heatEnergyInKcal = float(entry1.get())
            molarValue = float(entry2.get())
            initialTemperatureInC = float(entry3.get())
            finalTemperatureInC = float(entry4.get())
            if len(str(heatEnergyInKcal)) != 0 and len(str(molarValue)) != 0 and len(str(initialTemperatureInC)) != 0 and len(str(finalTemperatureInC)) != 0:         
                ans = str((heatEnergyInKcal * 4184)/(molarValue * (((finalTemperatureInC + 273.15) - (initialTemperatureInC + 273.15))))) + " kg m^2/k s^2"
                entry5.delete(0,END)
                entry5.insert(0,ans)
        except:   
            popupmsg("Check your inputs")
            
    label1 = tk.Label(calculationsframe, text="Heat energy in kcal", font="Instruction 20", bg="#1b1b1b", fg="#d1bea8", width="26", anchor='w')
    entry1 = tk.Entry(calculationsframe, font="Instruction 20", bg="#ffffff", fg="#0ba98b", width="26", highlightbackground = "#1b1b1b", borderwidth = 0, highlightthickness = 2)
    label2 = tk.Label(calculationsframe, text="Molar value", font="Instruction 20", bg="#1b1b1b", fg="#d1bea8", width="26", anchor='w')
    entry2 = tk.Entry(calculationsframe, font="Instruction 20", bg="#ffffff", fg="#0ba98b", width="26", highlightbackground = "#1b1b1b", borderwidth = 0, highlightthickness = 2)
    label3 = tk.Label(calculationsframe, text="Initial temperature in C", font="Instruction 20", bg="#1b1b1b", fg="#d1bea8", width="26", anchor='w')
    entry3 = tk.Entry(calculationsframe, font="Instruction 20", bg="#ffffff", fg="#0ba98b", width="26", highlightbackground = "#1b1b1b", borderwidth = 0, highlightthickness = 2)
    label4 = tk.Label(calculationsframe, text="Final temperature in C", font="Instruction 20", bg="#1b1b1b", fg="#d1bea8", width="26", anchor='w')
    entry4 = tk.Entry(calculationsframe, font="Instruction 20", bg="#ffffff", fg="#0ba98b", width="26", highlightbackground = "#1b1b1b", borderwidth = 0, highlightthickness = 2)
    label5 = tk.Label(calculationsframe, text="Answer", font="Instruction 20", bg="#1b1b1b", fg="#d1bea8", width="26", anchor='w')
    entry5 = tk.Entry(calculationsframe, font="Instruction 20", bg="#ffffff", fg="#0ba98b", width="26", highlightbackground = "#1b1b1b", borderwidth = 0, highlightthickness = 2)


    label1.grid(row=0, column=1, pady=(16,0))
    entry1.grid(row=10, column=1, pady=(0,8))
    label2.grid(row=20, column=1, pady=0)
    entry2.grid(row=30, column=1, pady=(0,8))
    label3.grid(row=40, column=1, pady=0)
    entry3.grid(row=50, column=1, pady=(0,8))
    label3.grid(row=60, column=1, pady=0)
    entry3.grid(row=70, column=1, pady=(0,8))
    label4.grid(row=80, column=1, pady=0)
    entry4.grid(row=90, column=1, pady=(0,8))
    label5.grid(row=100, column=1, pady=0)
    entry5.grid(row=110, column=1, pady=(0,8))

    tk.Button(calculationsframe, text='CALCULATE', font="Instruction 13", bg="#1b1b1b", fg="#ffffff", width="16" ,command=show_entry_fields).grid(
                                                                row=120, 
                                                                column=1, 
                                                                sticky=tk.E, 
                                                                pady=8)

    formulamsg("E:\\Projects\\Programming\\Python\\fredie\\formula\\molar_heat_capacity.png")

def latentHeatModule(event):
    menuDefault()
    latentHeatLabel.configure(fg='#e8e916')
    resetCalculationsFrame()
    latentHeatModuleDisplay()

def latentHeatModuleDisplay():
    def show_entry_fields():
        try:      
            heatEnergyInKcal = float(entry1.get())
            massInKilogram = float(entry2.get())
            if len(str(heatEnergyInKcal)) != 0 and len(str(massInKilogram)) != 0:         
                ans = str((heatEnergyInKcal * 4184)/massInKilogram) + " J/kg"
                entry3.delete(0,END)
                entry3.insert(0,ans)
        except:   
            popupmsg("Check your inputs")
            
    label1 = tk.Label(calculationsframe, text="Heat energy in kcal", font="Instruction 20", bg="#1b1b1b", fg="#d1bea8", width="26", anchor='w')
    entry1 = tk.Entry(calculationsframe, font="Instruction 20", bg="#ffffff", fg="#0ba98b", width="26", highlightbackground = "#1b1b1b", borderwidth = 0, highlightthickness = 2)
    label2 = tk.Label(calculationsframe, text="Mass in kilogram", font="Instruction 20", bg="#1b1b1b", fg="#d1bea8", width="26", anchor='w')
    entry2 = tk.Entry(calculationsframe, font="Instruction 20", bg="#ffffff", fg="#0ba98b", width="26", highlightbackground = "#1b1b1b", borderwidth = 0, highlightthickness = 2)
    label3 = tk.Label(calculationsframe, text="Answer", font="Instruction 20", bg="#1b1b1b", fg="#d1bea8", width="26", anchor='w')
    entry3 = tk.Entry(calculationsframe, font="Instruction 20", bg="#ffffff", fg="#0ba98b", width="26", highlightbackground = "#1b1b1b", borderwidth = 0, highlightthickness = 2)


    label1.grid(row=0, column=1, pady=(16,0))
    entry1.grid(row=10, column=1, pady=(0,8))
    label2.grid(row=20, column=1, pady=0)
    entry2.grid(row=30, column=1, pady=(0,8))
    label3.grid(row=40, column=1, pady=0)
    entry3.grid(row=50, column=1, pady=(0,8))
    label3.grid(row=60, column=1, pady=0)
    entry3.grid(row=70, column=1, pady=(0,8))

    tk.Button(calculationsframe, text='CALCULATE', font="Instruction 13", bg="#1b1b1b", fg="#ffffff", width="16" ,command=show_entry_fields).grid(
                                                                row=80, 
                                                                column=1, 
                                                                sticky=tk.E, 
                                                                pady=8)

    formulamsg("E:\\Projects\\Programming\\Python\\fredie\\formula\\latent_heat.png")

def heatFlowRateModule(event):
    menuDefault()
    heatFlowRateLabel.configure(fg='#e8e916')
    resetCalculationsFrame()
    heatFlowRateModuleDisplay()

def heatFlowRateModuleDisplay():

    def show_entry_fields():
        try:      
            thermalConductivityInWmK = float(entry1.get())
            surfaceAreaInM2 = float(entry2.get())
            initialTemperatureInC = float(entry3.get())
            finalTemperatureInC = float(entry4.get())
            thicknessOfMaterialInMeter = float(entry5.get())
            if len(str(thermalConductivityInWmK)) != 0 and len(str(surfaceAreaInM2)) != 0 and len(str(initialTemperatureInC)) != 0 and len(str(finalTemperatureInC)) != 0 and len(str(thicknessOfMaterialInMeter)) != 0:         
                ans = str((thermalConductivityInWmK * surfaceAreaInM2 * ( ((finalTemperatureInC + 273.15) - (initialTemperatureInC + 273.15))))/(thicknessOfMaterialInMeter)) + " W"
                entry6.delete(0,END)
                entry6.insert(0,ans)
        except:   
            popupmsg("Check your inputs")
            
    label1 = tk.Label(calculationsframe, text="Thermal cond...ty in W/m K", font="Instruction 20", bg="#1b1b1b", fg="#d1bea8", width="26", anchor='w')
    entry1 = tk.Entry(calculationsframe, font="Instruction 20", bg="#ffffff", fg="#0ba98b", width="26", highlightbackground = "#1b1b1b", borderwidth = 0, highlightthickness = 2)
    label2 = tk.Label(calculationsframe, text="Surface area in m^2", font="Instruction 20", bg="#1b1b1b", fg="#d1bea8", width="26", anchor='w')
    entry2 = tk.Entry(calculationsframe, font="Instruction 20", bg="#ffffff", fg="#0ba98b", width="26", highlightbackground = "#1b1b1b", borderwidth = 0, highlightthickness = 2)
    label3 = tk.Label(calculationsframe, text="Initial temperature in C", font="Instruction 20", bg="#1b1b1b", fg="#d1bea8", width="26", anchor='w')
    entry3 = tk.Entry(calculationsframe, font="Instruction 20", bg="#ffffff", fg="#0ba98b", width="26", highlightbackground = "#1b1b1b", borderwidth = 0, highlightthickness = 2)
    label4 = tk.Label(calculationsframe, text="Final temperature in C", font="Instruction 20", bg="#1b1b1b", fg="#d1bea8", width="26", anchor='w')
    entry4 = tk.Entry(calculationsframe, font="Instruction 20", bg="#ffffff", fg="#0ba98b", width="26", highlightbackground = "#1b1b1b", borderwidth = 0, highlightthickness = 2)
    label5 = tk.Label(calculationsframe, text="Thickness of mat...l in m", font="Instruction 20", bg="#1b1b1b", fg="#d1bea8", width="26", anchor='w')
    entry5 = tk.Entry(calculationsframe, font="Instruction 20", bg="#ffffff", fg="#0ba98b", width="26", highlightbackground = "#1b1b1b", borderwidth = 0, highlightthickness = 2)
    label6 = tk.Label(calculationsframe, text="Answer", font="Instruction 20", bg="#1b1b1b", fg="#d1bea8", width="26", anchor='w')
    entry6 = tk.Entry(calculationsframe, font="Instruction 20", bg="#ffffff", fg="#0ba98b", width="26", highlightbackground = "#1b1b1b", borderwidth = 0, highlightthickness = 2)


    label1.grid(row=0, column=1, pady=(16,0))
    entry1.grid(row=10, column=1, pady=(0,8))
    label2.grid(row=20, column=1, pady=0)
    entry2.grid(row=30, column=1, pady=(0,8))
    label3.grid(row=40, column=1, pady=0)
    entry3.grid(row=50, column=1, pady=(0,8))
    label4.grid(row=60, column=1, pady=0)
    entry4.grid(row=70, column=1, pady=(0,8))
    label5.grid(row=80, column=1, pady=0)
    entry5.grid(row=90, column=1, pady=(0,8))
    label5.grid(row=100, column=1, pady=0)
    entry5.grid(row=110, column=1, pady=(0,8))
    label6.grid(row=120, column=1, pady=0)
    entry6.grid(row=130, column=1, pady=(0,8))

    tk.Button(calculationsframe, text='CALCULATE', font="Instruction 13", bg="#1b1b1b", fg="#ffffff", width="16" ,command=show_entry_fields).grid(
                                                                row=140, 
                                                                column=1, 
                                                                sticky=tk.E, 
                                                                pady=8)

    formulamsg("E:\\Projects\\Programming\\Python\\fredie\\formula\\heat_flow_rate.png")

def lengthChangeModule(event):
    menuDefault()
    lengthChangeLabel.configure(fg='#e8e916')
    resetCalculationsFrame()
    lengthChangeModuleDisplay()

def lengthChangeModuleDisplay():
    def show_entry_fields():
        try:      
            lengthInMeters = float(entry1.get())
            coefficientOfLinearExpansion = float(entry2.get())
            initialTemperatureInC = float(entry3.get())
            finalTemperatureInC = float(entry4.get())
            if len(str(lengthInMeters)) != 0 and len(str(coefficientOfLinearExpansion)) != 0 and len(str(initialTemperatureInC)) != 0 and len(str(finalTemperatureInC)) != 0:         
                ans = str((lengthInMeters * coefficientOfLinearExpansion) *  (((finalTemperatureInC + 273.15) - (initialTemperatureInC + 273.15)))) + " m"
                entry5.delete(0,END)
                entry5.insert(0,ans)
        except:   
            popupmsg("Check your inputs")
            
    label1 = tk.Label(calculationsframe, text="Length in meters", font="Instruction 20", bg="#1b1b1b", fg="#d1bea8", width="26", anchor='w')
    entry1 = tk.Entry(calculationsframe, font="Instruction 20", bg="#ffffff", fg="#0ba98b", width="26", highlightbackground = "#1b1b1b", borderwidth = 0, highlightthickness = 2)
    label2 = tk.Label(calculationsframe, text="Coefficient of linear e...", font="Instruction 20", bg="#1b1b1b", fg="#d1bea8", width="26", anchor='w')
    entry2 = tk.Entry(calculationsframe, font="Instruction 20", bg="#ffffff", fg="#0ba98b", width="26", highlightbackground = "#1b1b1b", borderwidth = 0, highlightthickness = 2)
    label3 = tk.Label(calculationsframe, text="Initial temperature in C", font="Instruction 20", bg="#1b1b1b", fg="#d1bea8", width="26", anchor='w')
    entry3 = tk.Entry(calculationsframe, font="Instruction 20", bg="#ffffff", fg="#0ba98b", width="26", highlightbackground = "#1b1b1b", borderwidth = 0, highlightthickness = 2)
    label4 = tk.Label(calculationsframe, text="Final temperature in C", font="Instruction 20", bg="#1b1b1b", fg="#d1bea8", width="26", anchor='w')
    entry4 = tk.Entry(calculationsframe, font="Instruction 20", bg="#ffffff", fg="#0ba98b", width="26", highlightbackground = "#1b1b1b", borderwidth = 0, highlightthickness = 2)
    label5 = tk.Label(calculationsframe, text="Answer", font="Instruction 20", bg="#1b1b1b", fg="#d1bea8", width="26", anchor='w')
    entry5 = tk.Entry(calculationsframe, font="Instruction 20", bg="#ffffff", fg="#0ba98b", width="26", highlightbackground = "#1b1b1b", borderwidth = 0, highlightthickness = 2)


    label1.grid(row=0, column=1, pady=(16,0))
    entry1.grid(row=10, column=1, pady=(0,8))
    label2.grid(row=20, column=1, pady=0)
    entry2.grid(row=30, column=1, pady=(0,8))
    label3.grid(row=40, column=1, pady=0)
    entry3.grid(row=50, column=1, pady=(0,8))
    label4.grid(row=60, column=1, pady=0)
    entry4.grid(row=70, column=1, pady=(0,8))
    label5.grid(row=80, column=1, pady=0)
    entry5.grid(row=90, column=1, pady=(0,8))

    tk.Button(calculationsframe, text='CALCULATE', font="Instruction 13", bg="#1b1b1b", fg="#ffffff", width="16" ,command=show_entry_fields).grid(
                                                                row=100, 
                                                                column=1, 
                                                                sticky=tk.E, 
                                                                pady=8)

    formulamsg("E:\\Projects\\Programming\\Python\\fredie\\formula\\length_change.png")


def volumeChangeModule(event):
    menuDefault()
    volumeChangeLabel.configure(fg='#e8e916')
    resetCalculationsFrame()
    volumeChangeModuleDisplay()

def volumeChangeModuleDisplay():

    def show_entry_fields():
        try:      
            initialVolumeInCm3 = float(entry1.get())
            coefficientOfExpansion = float(entry2.get())
            initialTemperatureInC = float(entry3.get())
            finalTemperatureInC = float(entry4.get())
            if len(str(initialVolumeInCm3)) != 0 and len(str(coefficientOfExpansion)) != 0 and len(str(initialTemperatureInC)) != 0 and len(str(finalTemperatureInC)) != 0:         
                ans = str((initialVolumeInCm3 * coefficientOfExpansion) * (((finalTemperatureInC + 273.15) - (initialTemperatureInC + 273.15)))) + " m^3"
                entry5.delete(0,END)
                entry5.insert(0,ans)
        except:   
            popupmsg("Check your inputs")
            
    label1 = tk.Label(calculationsframe, text="Initial volume in cm^3", font="Instruction 20", bg="#1b1b1b", fg="#d1bea8", width="26", anchor='w')
    entry1 = tk.Entry(calculationsframe, font="Instruction 20", bg="#ffffff", fg="#0ba98b", width="26", highlightbackground = "#1b1b1b", borderwidth = 0, highlightthickness = 2)
    label2 = tk.Label(calculationsframe, text="Coefficient of expansion", font="Instruction 20", bg="#1b1b1b", fg="#d1bea8", width="26", anchor='w')
    entry2 = tk.Entry(calculationsframe, font="Instruction 20", bg="#ffffff", fg="#0ba98b", width="26", highlightbackground = "#1b1b1b", borderwidth = 0, highlightthickness = 2)
    label3 = tk.Label(calculationsframe, text="Initial temperature in C", font="Instruction 20", bg="#1b1b1b", fg="#d1bea8", width="26", anchor='w')
    entry3 = tk.Entry(calculationsframe, font="Instruction 20", bg="#ffffff", fg="#0ba98b", width="26", highlightbackground = "#1b1b1b", borderwidth = 0, highlightthickness = 2)
    label4 = tk.Label(calculationsframe, text="Final temperature in C", font="Instruction 20", bg="#1b1b1b", fg="#d1bea8", width="26", anchor='w')
    entry4 = tk.Entry(calculationsframe, font="Instruction 20", bg="#ffffff", fg="#0ba98b", width="26", highlightbackground = "#1b1b1b", borderwidth = 0, highlightthickness = 2)
    label5 = tk.Label(calculationsframe, text="Answer", font="Instruction 20", bg="#1b1b1b", fg="#d1bea8", width="26", anchor='w')
    entry5 = tk.Entry(calculationsframe, font="Instruction 20", bg="#ffffff", fg="#0ba98b", width="26", highlightbackground = "#1b1b1b", borderwidth = 0, highlightthickness = 2)


    label1.grid(row=0, column=1, pady=(16,0))
    entry1.grid(row=10, column=1, pady=(0,8))
    label2.grid(row=20, column=1, pady=0)
    entry2.grid(row=30, column=1, pady=(0,8))
    label3.grid(row=40, column=1, pady=0)
    entry3.grid(row=50, column=1, pady=(0,8))
    label4.grid(row=60, column=1, pady=0)
    entry4.grid(row=70, column=1, pady=(0,8))
    label5.grid(row=80, column=1, pady=0)
    entry5.grid(row=90, column=1, pady=(0,8))

    tk.Button(calculationsframe, text='CALCULATE', font="Instruction 13", bg="#1b1b1b", fg="#ffffff", width="16" ,command=show_entry_fields).grid(
                                                                row=100, 
                                                                column=1, 
                                                                sticky=tk.E, 
                                                                pady=8)

    formulamsg("E:\\Projects\\Programming\\Python\\fredie\\formula\\volume_change.png")

def thermalStressModule(event):
    menuDefault()
    thermalStressLabel.configure(fg='#e8e916')
    resetCalculationsFrame()
    thermalStressModuleDisplay()

def thermalStressModuleDisplay():
    def show_entry_fields():
        try:      
            youngModulusInPa = float(entry1.get())
            coefficientOfThermalExpansion = float(entry2.get())
            initialTemperatureInC = float(entry3.get())
            finalTemperatureInC = float(entry4.get())
            if len(str(youngModulusInPa)) != 0 and len(str(coefficientOfThermalExpansion)) != 0 and len(str(initialTemperatureInC)) != 0 and len(str(finalTemperatureInC)) != 0:         
                ans = str((-youngModulusInPa * coefficientOfThermalExpansion) * (((finalTemperatureInC + 273.15) - (initialTemperatureInC + 273.15)))) + " m^3"
                entry5.delete(0,END)
                entry5.insert(0,ans)
        except:   
            popupmsg("Check your inputs")
            
    label1 = tk.Label(calculationsframe, text="Young modulus in Pa", font="Instruction 20", bg="#1b1b1b", fg="#d1bea8", width="26", anchor='w')
    entry1 = tk.Entry(calculationsframe, font="Instruction 20", bg="#ffffff", fg="#0ba98b", width="26", highlightbackground = "#1b1b1b", borderwidth = 0, highlightthickness = 2)
    label2 = tk.Label(calculationsframe, text="Coefficient of thermal e...", font="Instruction 20", bg="#1b1b1b", fg="#d1bea8", width="26", anchor='w')
    entry2 = tk.Entry(calculationsframe, font="Instruction 20", bg="#ffffff", fg="#0ba98b", width="26", highlightbackground = "#1b1b1b", borderwidth = 0, highlightthickness = 2)
    label3 = tk.Label(calculationsframe, text="Initial temperature in C", font="Instruction 20", bg="#1b1b1b", fg="#d1bea8", width="26", anchor='w')
    entry3 = tk.Entry(calculationsframe, font="Instruction 20", bg="#ffffff", fg="#0ba98b", width="26", highlightbackground = "#1b1b1b", borderwidth = 0, highlightthickness = 2)
    label4 = tk.Label(calculationsframe, text="Final temperature in C", font="Instruction 20", bg="#1b1b1b", fg="#d1bea8", width="26", anchor='w')
    entry4 = tk.Entry(calculationsframe, font="Instruction 20", bg="#ffffff", fg="#0ba98b", width="26", highlightbackground = "#1b1b1b", borderwidth = 0, highlightthickness = 2)
    label5 = tk.Label(calculationsframe, text="Answer", font="Instruction 20", bg="#1b1b1b", fg="#d1bea8", width="26", anchor='w')
    entry5 = tk.Entry(calculationsframe, font="Instruction 20", bg="#ffffff", fg="#0ba98b", width="26", highlightbackground = "#1b1b1b", borderwidth = 0, highlightthickness = 2)


    label1.grid(row=0, column=1, pady=(16,0))
    entry1.grid(row=10, column=1, pady=(0,8))
    label2.grid(row=20, column=1, pady=0)
    entry2.grid(row=30, column=1, pady=(0,8))
    label3.grid(row=40, column=1, pady=0)
    entry3.grid(row=50, column=1, pady=(0,8))
    label4.grid(row=60, column=1, pady=0)
    entry4.grid(row=70, column=1, pady=(0,8))
    label5.grid(row=80, column=1, pady=0)
    entry5.grid(row=90, column=1, pady=(0,8))

    tk.Button(calculationsframe, text='CALCULATE', font="Instruction 13", bg="#1b1b1b", fg="#ffffff", width="16" ,command=show_entry_fields).grid(
                                                                row=100, 
                                                                column=1, 
                                                                sticky=tk.E, 
                                                                pady=8)

    formulamsg("E:\\Projects\\Programming\\Python\\fredie\\formula\\thermal_stress.png")





def on_configure(event):
    canvas.configure(scrollregion=canvas.bbox('all'))

canvas = tk.Canvas(root, width=262)
canvas.pack(side=tk.LEFT,  anchor='nw')

scrollbar = tk.Scrollbar(root, command=canvas.yview, bg="grey")
scrollbar.pack(side=tk.LEFT, fill='y')

canvas.configure(yscrollcommand = scrollbar.set, bg="#0ba98b",height=888, borderwidth =0, highlightthickness = 0)

canvas.bind('<Configure>', on_configure)

menuframe = tk.Frame(root, width=385, bg="#0ba98b", borderwidth =0, highlightthickness = 0)
canvas.create_window((0,0), window=menuframe, anchor='nw')

fontMenu = "Instruction 20"
fontMenuTitle = "Instruction 10"

basicKinematicsLabel = tk.Label(menuframe, text="Basic Kinematics", font=fontMenuTitle, bg="#141414", fg="#FF5733", width="16")
basicKinematicsLabel.pack(fill=X, padx=0, pady=0) 

velocityLabel = tk.Label(menuframe, text="Velocity", font=fontMenu, bg="#1b1b1b", fg="#d1bea8", width="16")
velocityLabel.bind("<Button-1>", velocityModule)
velocityLabel.pack(fill=X, padx=0, pady=0) 

accelerationLabel = tk.Label(menuframe, text="Acceleration", font=fontMenu, bg="#141414", fg="#d1bea8", width="16")
accelerationLabel.bind("<Button-1>", accelerationModule)
accelerationLabel.pack(fill=X, padx=0, pady=0) 

freeFallLabel = tk.Label(menuframe, text="Free Fall", font=fontMenu, bg="#1b1b1b", fg="#d1bea8", width="16")
freeFallLabel.bind("<Button-1>", freeFallModule)
freeFallLabel.pack(fill=X, padx=0, pady=0) 

tangentialSpeedLabel = tk.Label(menuframe, text="Tangential S...", font=fontMenu, bg="#141414", fg="#d1bea8", width="16")
tangentialSpeedLabel.bind("<Button-1>", tangentialSpeedModule)
tangentialSpeedLabel.pack(fill=X, padx=0, pady=0) 

angularValuesLabel = tk.Label(menuframe, text="Angular Values", font=fontMenu, bg="#1b1b1b", fg="#d1bea8", width="16")
angularValuesLabel.bind("<Button-1>", angularValuesModule)
angularValuesLabel.pack(fill=X, padx=0, pady=0) 

basicKinematicsLabel = tk.Label(menuframe, text="Newton's Laws of Motion", font=fontMenuTitle, bg="#141414", fg="#C70039", width="16")
basicKinematicsLabel.pack(fill=X, padx=0, pady=0) 

lawOfInertiaLabel = tk.Label(menuframe, text="Law of Inertia", font=fontMenu, bg="#1b1b1b", fg="#d1bea8", width="16")
lawOfInertiaLabel.bind("<Button-1>", lawOfInertiaModule)
lawOfInertiaLabel.pack(fill=X, padx=0, pady=0) 

lawOfAccelerationLabel = tk.Label(menuframe, text="Law of Acce...", font=fontMenu, bg="#141414", fg="#d1bea8", width="16")
lawOfAccelerationLabel.bind("<Button-1>", lawOfAccelerationModule)
lawOfAccelerationLabel.pack(fill=X, padx=0, pady=0) 

centripetalAccelerationLabel = tk.Label(menuframe, text="Centripetal...", font=fontMenu, bg="#1b1b1b", fg="#d1bea8", width="16")
centripetalAccelerationLabel.bind("<Button-1>", centripetalAccelerationModule)
centripetalAccelerationLabel.pack(fill=X, padx=0, pady=0) 

tensionLabel = tk.Label(menuframe, text="Tension", font=fontMenu, bg="#141414", fg="#d1bea8", width="16")
tensionLabel.bind("<Button-1>", tensionModule)
tensionLabel.pack(fill=X, padx=0, pady=0) 

centripetalForceLabel = tk.Label(menuframe, text="Centripetal...", font=fontMenu, bg="#1b1b1b", fg="#d1bea8", width="16")
centripetalForceLabel.bind("<Button-1>", centripetalForceModule)
centripetalForceLabel.pack(fill=X, padx=0, pady=0) 

torqueLabel = tk.Label(menuframe, text="Torque", font=fontMenu, bg="#141414", fg="#d1bea8", width="16")
torqueLabel.bind("<Button-1>", torqueModule)
torqueLabel.pack(fill=X, padx=0, pady=0) 

lawOfActionAndReactionLabel = tk.Label(menuframe, text="Law of Acti...", font=fontMenu, bg="#1b1b1b", fg="#d1bea8", width="16")
lawOfActionAndReactionLabel.bind("<Button-1>", lawOfActionAndReactionModule)
lawOfActionAndReactionLabel.pack(fill=X, padx=0, pady=0) 

translationalDynamicsLabel = tk.Label(menuframe, text="Translational Dynamics", font=fontMenuTitle, bg="#141414", fg="#FFC300", width="16")
translationalDynamicsLabel.pack(fill=X, padx=0, pady=0) 

workLabel = tk.Label(menuframe, text="Work", font=fontMenu, bg="#1b1b1b", fg="#d1bea8", width="16")
workLabel.bind("<Button-1>", workModule)
workLabel.pack(fill=X, padx=0, pady=0) 

forceLabel = tk.Label(menuframe, text="Force", font=fontMenu, bg="#141414", fg="#d1bea8", width="16")
forceLabel.bind("<Button-1>", forceModule)
forceLabel.pack(fill=X, padx=0, pady=0) 

kineticEnergyLabel = tk.Label(menuframe, text="Kinetic Energy", font=fontMenu, bg="#1b1b1b", fg="#d1bea8", width="16")
kineticEnergyLabel.bind("<Button-1>", kineticEnergyModule)
kineticEnergyLabel.pack(fill=X, padx=0, pady=0) 

potentialEnergyLabel = tk.Label(menuframe, text="Potential E...", font=fontMenu, bg="#141414", fg="#d1bea8", width="16")
potentialEnergyLabel.bind("<Button-1>", potentialEnergyModule)
potentialEnergyLabel.pack(fill=X, padx=0, pady=0) 

powerLabel = tk.Label(menuframe, text="Power", font=fontMenu, bg="#1b1b1b", fg="#d1bea8", width="16")
powerLabel.bind("<Button-1>", powerModule)
powerLabel.pack(fill=X, padx=0, pady=0) 

linearMomentumLabel = tk.Label(menuframe, text="Linear Mome...", font=fontMenu, bg="#141414", fg="#d1bea8", width="16")
linearMomentumLabel.bind("<Button-1>", linearMomentumModule)
linearMomentumLabel.pack(fill=X, padx=0, pady=0) 

impulseLabel = tk.Label(menuframe, text="impulse", font=fontMenu, bg="#1b1b1b", fg="#d1bea8", width="16")
impulseLabel.bind("<Button-1>", impulseModule)
impulseLabel.pack(fill=X, padx=0, pady=0) 

collisionLabel = tk.Label(menuframe, text="Collision", font=fontMenu, bg="#141414", fg="#d1bea8", width="16")
collisionLabel.bind("<Button-1>", collisionModule)
collisionLabel.pack(fill=X, padx=0, pady=0) 

rotationalDynamicsLabel = tk.Label(menuframe, text="Rotational Dynamics", font=fontMenuTitle, bg="#1b1b1b", fg="#FF5733", width="16")
rotationalDynamicsLabel.pack(fill=X, padx=0, pady=0) 

torqueRotationalDynamicsLabel = tk.Label(menuframe, text="Torque", font=fontMenu, bg="#141414", fg="#d1bea8", width="16")
torqueRotationalDynamicsLabel.bind("<Button-1>", torqueRotationalDynamicsModule)
torqueRotationalDynamicsLabel.pack(fill=X, padx=0, pady=0) 

momentOfInertiaLabel = tk.Label(menuframe, text="Moment Of I...", font=fontMenu, bg="#1b1b1b", fg="#d1bea8", width="16")
momentOfInertiaLabel.bind("<Button-1>", momentOfInertiaModule)
momentOfInertiaLabel.pack(fill=X, padx=0, pady=0) 

gravityAndElasticityLabel = tk.Label(menuframe, text="Gravity and Elasticity", font=fontMenuTitle, bg="#141414", fg="#C70039", width="16")
gravityAndElasticityLabel.pack(fill=X, padx=0, pady=0) 

gravitationalForceLabel = tk.Label(menuframe, text="Gravitation...", font=fontMenu, bg="#1b1b1b", fg="#d1bea8", width="16")
gravitationalForceLabel.bind("<Button-1>", gravitationalForceModule)
gravitationalForceLabel.pack(fill=X, padx=0, pady=0) 

semimajorAxisLabel = tk.Label(menuframe, text="Semimajor Axis", font=fontMenu, bg="#141414", fg="#d1bea8", width="16")
semimajorAxisLabel.bind("<Button-1>", semimajorAxisModule)
semimajorAxisLabel.pack(fill=X, padx=0, pady=0) 

shearStressLabel = tk.Label(menuframe, text="Shear Stress", font=fontMenu, bg="#1b1b1b", fg="#d1bea8", width="16")
shearStressLabel.bind("<Button-1>", shearStressModule)
shearStressLabel.pack(fill=X, padx=0, pady=0) 

poissonsRatioLabel = tk.Label(menuframe, text="Poisson's R...", font=fontMenu, bg="#141414", fg="#d1bea8", width="16")
poissonsRatioLabel.bind("<Button-1>", poissonsRatioModule)
poissonsRatioLabel.pack(fill=X, padx=0, pady=0) 

crossSectionalAreaLabel = tk.Label(menuframe, text="Cross Secti...", font=fontMenu, bg="#1b1b1b", fg="#d1bea8", width="16")
crossSectionalAreaLabel.bind("<Button-1>", crossSectionalAreaModule)
crossSectionalAreaLabel.pack(fill=X, padx=0, pady=0) 

fluidsAndHarmonicsLabel = tk.Label(menuframe, text="Fluids and Harmonics", font=fontMenuTitle, bg="#141414", fg="#FFC300", width="16")
fluidsAndHarmonicsLabel.pack(fill=X, padx=0, pady=0) 

pressureLabel = tk.Label(menuframe, text="Pressure", font=fontMenu, bg="#1b1b1b", fg="#d1bea8", width="16")
pressureLabel.bind("<Button-1>", pressureModule)
pressureLabel.pack(fill=X, padx=0, pady=0) 

potentialEnergyFluidsAndHarmonicsLabel = tk.Label(menuframe, text="Potential E...", font=fontMenu, bg="#141414", fg="#d1bea8", width="16")
potentialEnergyFluidsAndHarmonicsLabel.bind("<Button-1>", potentialEnergyFluidsAndHarmonicsModule)
potentialEnergyFluidsAndHarmonicsLabel.pack(fill=X, padx=0, pady=0) 

volumeFlowRateLabel = tk.Label(menuframe, text="Volume flow...", font=fontMenu, bg="#1b1b1b", fg="#d1bea8", width="16")
volumeFlowRateLabel.bind("<Button-1>", volumeFlowRateModule)
volumeFlowRateLabel.pack(fill=X, padx=0, pady=0) 

periodOfOscillationLabel = tk.Label(menuframe, text="Period of O...", font=fontMenu, bg="#141414", fg="#d1bea8", width="16")
periodOfOscillationLabel.bind("<Button-1>", periodOfOscillationModule)
periodOfOscillationLabel.pack(fill=X, padx=0, pady=0)

mechanicalWavesAndAcousticsLabel = tk.Label(menuframe, text="Mechanical Waves and Acoustics", font=fontMenuTitle, bg="#1b1b1b", fg="#FF5733", width="16")
mechanicalWavesAndAcousticsLabel.pack(fill=X, padx=0, pady=0) 

waveSpeedLabel = tk.Label(menuframe, text="Wave Speed", font=fontMenu, bg="#141414", fg="#d1bea8", width="16")
waveSpeedLabel.bind("<Button-1>", waveSpeedModule)
waveSpeedLabel.pack(fill=X, padx=0, pady=0)

wavelengthLabel = tk.Label(menuframe, text="Wavelength", font=fontMenu, bg="#1b1b1b", fg="#d1bea8", width="16")
wavelengthLabel.bind("<Button-1>", wavelengthModule)
wavelengthLabel.pack(fill=X, padx=0, pady=0)

kineticGasesAndThermodynamicsLabel = tk.Label(menuframe, text="Kinetic Gases and Thermodynamics", font=fontMenuTitle, bg="#141414", fg="#C70039", width="16")
kineticGasesAndThermodynamicsLabel.pack(fill=X, padx=0, pady=0) 

requiredHeatLabel = tk.Label(menuframe, text="Required Heat", font=fontMenu, bg="#1b1b1b", fg="#d1bea8", width="16")
requiredHeatLabel.bind("<Button-1>", requiredHeatModule)
requiredHeatLabel.pack(fill=X, padx=0, pady=0)

molarHeatCapacityLabel = tk.Label(menuframe, text="Molar Heat C...", font=fontMenu, bg="#141414", fg="#d1bea8", width="16")
molarHeatCapacityLabel.bind("<Button-1>", molarHeatCapacityModule)
molarHeatCapacityLabel.pack(fill=X, padx=0, pady=0)

latentHeatLabel = tk.Label(menuframe, text="Latent Heat", font=fontMenu, bg="#1b1b1b", fg="#d1bea8", width="16")
latentHeatLabel.bind("<Button-1>", latentHeatModule)
latentHeatLabel.pack(fill=X, padx=0, pady=0)

heatFlowRateLabel = tk.Label(menuframe, text="Heat Flow Rate", font=fontMenu, bg="#141414", fg="#d1bea8", width="16")
heatFlowRateLabel.bind("<Button-1>", heatFlowRateModule)
heatFlowRateLabel.pack(fill=X, padx=0, pady=0)

lengthChangeLabel = tk.Label(menuframe, text="Length Change", font=fontMenu, bg="#1b1b1b", fg="#d1bea8", width="16")
lengthChangeLabel.bind("<Button-1>", lengthChangeModule)
lengthChangeLabel.pack(fill=X, padx=0, pady=0)

volumeChangeLabel = tk.Label(menuframe, text="Volume Change", font=fontMenu, bg="#141414", fg="#d1bea8", width="16")
volumeChangeLabel.bind("<Button-1>", volumeChangeModule)
volumeChangeLabel.pack(fill=X, padx=0, pady=0)

thermalStressLabel = tk.Label(menuframe, text="Thermal Stress", font=fontMenu, bg="#1b1b1b", fg="#d1bea8", width="16")
thermalStressLabel.bind("<Button-1>", thermalStressModule)
thermalStressLabel.pack(fill=X, padx=0, pady=0)

calculationsframe = tk.Frame(root, bg="#E1DEE6")
canvas.create_window((0,0), window=calculationsframe, anchor='nw')

calculationsframe.pack()

canvasMain = Canvas(calculationsframe, width = 610, height = 660, highlightbackground = "#1b1b1b", borderwidth = 0, highlightthickness = 0, bg="#E1DEE6")          
img = PhotoImage(file="E:\\Projects\\Programming\\Python\\fredie\\background.png")      
canvasMain.create_image(20,20, anchor=NW, image=img)   
canvasMain.pack()   

root.mainloop()