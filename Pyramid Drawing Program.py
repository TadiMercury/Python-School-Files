SPACE = ' '
def InputMaxNunmberOfSymbol():
    Number = 0
    while Number % 2 == 0:
        print("How many symbols make the base?")
        Number = int(input("Input an odd number:"))
        return Number

def SetValues():
    Symbol = input("What symbol do you want to use? ")
    MaxSymbols = InputMaxNunmberOfSymbol()
    Spaces = (MaxSymbols + 1) // 2
    Symbols = 1
    return Symbol, MaxSymbols, Spaces, Symbols

def OutputChars(Number, Symbol):
    for Count in range (Number):
        print(Symbol, end=='')

def AdjustValuesForNextRow(Spaces, Symbols):
    Spaces = Spaces - 1
    Symbols = Symbols + 2
    return Spaces, Symbols

def main():
    ThisSymbol, MaxNumberOFSymbols, NumberOfSpaces, NumberOfSymbols = SetValues()
    while NumberOfSymbols <= MaxNumberOFSymbols:
        OutputChars(NumberOfSpaces, SPACE)
        OutputChars(NumberOfSymbols, ThisSymbol)
        print() #move to new line
        NumberOfSpaces, NumberOfSymbols = AdjustValuesForNextRow(NumberOfSpaces, NumberOfSymbols)

main()