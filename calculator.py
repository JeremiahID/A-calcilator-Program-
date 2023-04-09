# A program for a simple calculator

# A function to multiply two numbers
def Multiply():
    x = int(input("Enter value for Num1: "))
    y = int(input("Enter value for Num2: "))
    Imul = (x * y)
    print("Your Answer is", Imul)

# A function to divide two numbers
def Divide():
    x = int(input("Enter value for Num1: "))
    y = int(input("Enter value for Num2: "))
    Div = (x/y)
    print("Your Answer is", Div)

# A function to add two numbers
def Add():
    x = int(input("Enter value for Num1: "))
    y = int(input("Enter value for Num2: "))
    Add = (x + y)
    print("Your Answer is", Add)

# A function to subtract two numbers
def Subtract():
    x = int(input("Enter value for Num1: "))
    y = int(input("Enter value for Num2: "))
    Sub = (x - y)
    print("Your Answer is", Sub)
# A function for escape
def Esc():
    print ("You exited the calculator")

def main():
    true = 1
    while true:
        print("SLECT AN OPERATION")
        choice = input("Add/Subtract/Divide/Multiply/Esc: ").title()
        if choice == "Add":
            print("You Just Enter The Operation Addition")
            Add()           
        elif choice == "Subtract":
            print("You Just Enter The Operation Subtraction")
            Subtract()
        elif choice == "Divide":
            print("You Just Enter The Operation Division")
            Divide()
        elif choice == "Multiply":
            print("You Just Enter The Operation Multiplication")
            Multiply()
        elif choice == "Esc":
            Esc()
        else:
            print("chioce not found ")
        true = 0 
main()
            
            
        
        
              
