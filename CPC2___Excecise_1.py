# Basically lets you make your own letter

# Starts a class called "letter"
class letter:

    # Initializes instance variables in constructon and begins the letter formation, @letterFrom and @letterTo for sender and reciever.
    # self._body begins an arrray for the body of the letter.
    def __init__ (self, letterFrom, letterTo) :
        self._sendTo = letterTo
        self._sendFrom = letterFrom
        self._body = []

    # Function that adds lines with @line
    def addLine(self, line) :
        self._body.append(line)

    # Constructs the entire text.
    def getText(self) :
        print("Dear " + self._sendTo + ": \n")

        for line in self._body:
            print(line)

        print("\n")

        print("Sincerely, \n \n" + self._sendFrom + "\n")


myLetter = letter("Alice", "Bob")
myLetter.addLine("I am sorry we must part.")
myLetter.addLine("I wish you all the best.")
myLetter.getText()


