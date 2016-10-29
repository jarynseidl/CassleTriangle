import sys
import Tkinter as tk
import ValidatingEntry as ve


class Application(tk.Frame):
    def __init__(self, master = None):
        tk.Frame.__init__(self, master)
        self.grid()
        self.createWidgets()

    def createWidgets(self):
        self.sideALabel = tk.Label(self, text = "Side A length")
        self.sideALabel.grid(row = 1, column = 0)

        self.aLengthEntry = ve.IntegerEntry(self)
        self.aLengthEntry.bind("<FocusOut>", self.focusOut)
        self.aLengthEntry.grid(row = 1, column = 1)

        self.sideBLabel = tk.Label(self, text = "Side B length")
        self.sideBLabel.grid(row = 2, column = 0)

        self.bLengthEntry = ve.IntegerEntry(self)
        self.bLengthEntry.bind("<FocusOut>", self.focusOut)
        self.bLengthEntry.grid(row = 2, column = 1)

        self.sideCLabel = tk.Label(self, text = "Side C length")
        self.sideCLabel.grid(row = 3, column = 0)

        self.cLengthEntry = ve.IntegerEntry(self)
        self.cLengthEntry.bind("<FocusOut>", self.focusOut)
        self.cLengthEntry.grid(row = 3, column = 1)

        self.outputLabel = tk.Label(self, text = "Waiting for input")
        self.outputLabel.grid(row = 4, column = 1, padx = 5, pady = 10)

        self.quitButton = tk.Button(self, text = "Quit", command = self.quit)
        self.quitButton.grid(row = 5, column = 1, pady = 5)

    def classify(self):
        aLength = int(self.aLengthEntry.get())
        bLength = int(self.bLengthEntry.get())
        cLength = int(self.cLengthEntry.get())
        sides = [aLength, bLength, cLength]
        maxLength = max(sides)
        shorterSides = filter((lambda x: x < maxLength), sides)

        while len(shorterSides) < 2:
            shorterSides.append(maxLength)

        # Classify the triangle
        if sum(shorterSides) < maxLength:
            self.outputLabel['text'] = "Invalid triangle.  \nPlease make sure that \nthe two shorter sides add together \nto be larger than the longest side."
        elif self.equilateral(sides):
            self.outputLabel['text'] = "This is a valid Equilateral Triangle."
        elif self.isosceles(sides):
            self.outputLabel['text'] = "This is a valid Isosceles Triangle."
        elif self.right(shorterSides, maxLength):
            self.outputLabel['text'] = "This is a valid Right Triangle."
        else:
            self.outputLabel['text'] = "This is a valid Regular Triangle."

    # If all 3 sides are of equal length
    def equilateral(self, sides):
        return self.equilateral_r(sides[0], sides[1:])

    # Recursive equilateral helper function
    def equilateral_r(self, side, sides):
        if len(sides) == 0:
            return True
        elif side == sides[0]:
            return True and self.equilateral_r(side, sides[1:])
        else:
            return False

    # 2 sides are of equal length
    def isosceles(self, sides):
        return self.isosceles_r(sides[0], sides[1:])

    # Recursive isosceles helper function
    def isosceles_r(self, side, sides):
        if len(sides) == 0:
            return False
        elif side in sides:
            return True
        else:
            return self.isosceles_r(sides[0], sides[1:])

    # a^2 + b^2 = c^2, where C is the hypotenuse
    def right(self, shorterSides, maxLength):
        return reduce((lambda x,y: x+y), map((lambda x: x*x), shorterSides)) == (maxLength * maxLength)

    # Calls classify if all the inputs are provided.
    def focusOut(self, event):
        if self.aLengthEntry.get() != "" and self.bLengthEntry.get() != '' and self.cLengthEntry.get() != "":
            self.classify()
        else:
            self.outputLabel['text'] = "Waiting for input"

app = Application()
app.master.title("Triangle application")
app.mainloop()
