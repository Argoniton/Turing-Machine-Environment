
##  Turing Machine Visual - a software developed to simulate Turing machine
##    Copyright (C) 2017 Artemii Yanushevskyi
##
##    This program is free software: you can redistribute it and/or modify
##    it under the terms of the GNU Affero General Public License as
##    published by the Free Software Foundation, either version 3 of the
##    License, or (at your option) any later version.
##
##    This program is distributed in the hope that it will be useful,
##    but WITHOUT ANY WARRANTY; without even the implied warranty of
##    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
##    GNU Affero General Public License for more details.
##
##    You should have received a copy of the GNU Affero General Public License
##    along with this program.  If not, see <http://www.gnu.org/licenses/>.
##
##    You can contact me by email: argoniton@gmail.com
##
##  This is BETA 6 of this application.


'''a file with UI elements
'''

import tkinter as tk
from EventHandler import register, InterfaceClick
width = 640

# colors:
specific = '#00BAB9'
primary = '#404099'

# define main window
top = None 

class Window(tk.Tk):
    """ it passes a Window object to 'top' - it is a main window,
    other classes place their elements over 'top' """
    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args,
                       screenName='The Turing\'s machine',
                       baseName='Machine', className=' Visual Turing (BETA 7)',
                       **kwargs)
        global top
        top = self


class StatusBar(tk.Canvas):
    ''' a bar with 3 indicators. 1 - selected code 2 - code is compiled
    3 - values are selected '''
    height = 25 # status bar height
    def __init__(self, *args, **kwargs):
        register(self, 'StatusBar') # each object gets registered
        tk.Canvas.__init__(self, top, *args, width=640,
                           height=StatusBar.height,
                           bg=specific,
                           highlightthickness=0,bd=0,
                           **kwargs)
        c = self # c for canvas
        self.indicators = [] # array of indicators
        for i in range(3):
            self.indicators.append(c.create_oval(
                30+i*25,5,45+i*25,20, fill='gray', outline=primary, width=0))
        
        def StatusBarClick(event):
            ''' I call this function when I click on StatusBar'''
            InterfaceClick(panel_name='StatusBar',
                           click_coords={'x':event.x,'y':event.y})
            
        c.bind("<Button-1>", StatusBarClick)

    def changeStatus(self, indi, status):
        ''' light up indicator if "ready", shut it down if otherwise" '''
        if status=='not ready':
            self.itemconfig(self.indicators[indi-1], fill='gray',
                            outline=primary, width=0)
        elif status=='ready':
            self.itemconfig(self.indicators[indi-1], fill=primary,
                    outline=primary, width=0)


class SetupBar(tk.Canvas):
    ''' a bar where a code and values get selected. After code has
    to be compiled '''  
    height = 200
    def __init__(self, *args, **kwargs):
        register(self, 'SetupBar') # each object gets registered
        tk.Canvas.__init__(self, top, *args, width=640,
                           height=SetupBar.height,
                           highlightthickness=0,bd=0,
                           **kwargs)

    def displayInstructions(self):
        c = self
        # place a background
        c.img = tk.PhotoImage(file="CodeCompileValues.gif") 
        c.create_image(0,0, anchor='nw', image=self.img)
        def SetupBarClick(event):
            ''' I call this function when I click on SetupBar'''
            InterfaceClick(panel_name='SetupBar',
                           click_coords={'x':event.x,'y':event.y})
        c.bind("<Button-1>", SetupBarClick)


class RunBar(tk.Canvas):
    ''' A bar with run button '''
    height = 150
    def __init__(self, *args, **kwargs):
        register(self, 'RunBar') # each object gets registered
        tk.Canvas.__init__(self, top, *args, width=640,
                           height=RunBar.height,
                           highlightthickness=0,bd=0,
                           **kwargs)

    def displayInstructions(self):
        c = self
        # place a background
        c.img = tk.PhotoImage(file="RunTheMachine.gif")
        c.create_image(0,0, anchor='nw', image=self.img)
        def RunBarClick(event):
            ''' I call this function when I click on RunBar'''
            InterfaceClick(panel_name='RunBar',
                           click_coords={'x':event.x,'y':event.y})
        
        c.bind("<Button-1>", RunBarClick)



class TuringMachineFrame(tk.Frame):
    ''' a frame that exposes what is inside turing machine '''
    def __init__(self):
        register(self, 'TuringMachineFrame') # each object gets registered
        tk.Frame.__init__(self, top)
        from TuringCore import TuringMachine # import a turing machine class
        self.turingmachine = TuringMachine(self) 
        self.turingmachine.pack() # place an element of this class in the frame
        

class Copyright(tk.Tk):
    ''' a window showes of after other windows were closed'''
    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args,className=' Notice', **kwargs)
        tk.Label(self, text='Copyright (C) 2017 Artemii Yanushevskyi').pack()
        print('Copyright (C) 2017 Artemii Yanushevskyi,\n   github.com/argoniton')

mainloop = tk.mainloop

