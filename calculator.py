from tkinter import *




#Create a calculator class
class Calculator:




    def __init__(self, master):

        '''
        DOCSTRING: Define what to do on initialization
        '''
        
        #Assign reference to the main window of the application
        self.master = master

        #Add a name to our application
        master.title("Python Calculator")

        #Create a line where we display the equation
        self.equation=Entry(master, width=36, borderwidth=5)

        #Assign a position for the equation line in the grey application window
        self.equation.grid(row=0, column=0, columnspan=4, padx=10, pady=10)

        #Execute the .creteButton() method
        self.createButton()




    def createButton(self):

        '''
        DOCSTRING: Method that creates the buttons
        INPUT: nothing
        OUTPUT: creates a button
        '''
        
        #We first create each button one by one with the value we want
        #Using addButton() method which is described below
        b0 = self.addButton(0)
        b1 = self.addButton(1)
        b2 = self.addButton(2)
        b3 = self.addButton(3)
        b4 = self.addButton(4)
        b5 = self.addButton(5)
        b6 = self.addButton(6)
        b7 = self.addButton(7)
        b8 = self.addButton(8)
        b9 =  self.addButton(9)
        b_add = self.addButton('+')
        b_sub = self.addButton('-')
        b_mult = self.addButton('*')
        b_div = self.addButton('/')
        b_clear = self.addButton('c')
        b_equal = self.addButton('=')

        #Arrange the buttons into lists which represent calculator rows
        row1=[b7,b8,b9,b_add]
        row2=[b4,b5,b6,b_sub]
        row3=[b1,b2,b3,b_mult]
        row4=[b_clear,b0,b_equal,b_div]

        #Assign each button to a particular location on the GUI
        r=1
        for row in [row1, row2, row3, row4]:
            c=0
            for buttn in row:
                buttn.grid(row=r, column=c, columnspan=1)
                c+=1
            r+=1




    def addButton(self,value):

        '''
        DOCSTRING: Method to process the creation of a button and make it clickable
        INPUT: value of the button (1,2,3,4,5,6,7,8,9,0,+,-,*,/,c,=)
        OUTPUT: returns a designed button object
        '''
        return Button(self.master, text=value, width=9, command = lambda: self.clickButton(str(value)))
    



    def clickButton(self, value):
        
        '''
        DOCSTRING: Method to program the actions that will happen in the calculator after a click of each button
        INPUT: value of the button (1,2,3,4,5,6,7,8,9,0,+,-,*,/,c,=)
        OUTPUT: what action will be performed when a particular button is clicked
        '''
        
        #Get the equation that's entered by the user
        current_equation=str(self.equation.get())
        
        #If user clicked "c", then clear the screen
        if value == 'c':
            self.equation.delete(-1, END)
        
        #If user clicked "=", then compute the answer and display it
        elif value == '=':
            answer = str(eval(current_equation))
            self.equation.delete(-1, END)
            self.equation.insert(0, answer)
        
        #If user clicked any other button, then add it to the equation line
        else:
            self.equation.delete(0, END)
            self.equation.insert(0, current_equation+value)




#Execution
if __name__=='__main__':
    
    #Create the main window of an application
    root = Tk()
    
    #Tell our calculator class to use this window
    my_gui = Calculator(root)
    
    #Executable loop on the application, waits for user input
    root.mainloop()
