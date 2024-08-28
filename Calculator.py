#Creating a functions to do some Arithmatic operations
def add(num1,num2):
    return num1+num2
def sub(num1,num2):
    return num1-num2
def mul(num1,num2):
    return num1*num2
def div(num1,num2):
    return num1/num2
def diplay_menu():
    print("SELECT THE OPERATION : \n ")
    print("1.Addition\n")
    print("2.Substration\n")
    print("3.Multiplication\n")
    print("4.Division\n")
    
#Asking user to select opeartion
def main():
    while 1:
        diplay_menu()
        choice=int(input("Select operators form like 1,2,3,4 : "))


        
#Getting the first operand from the user and convert it to a float
        number1=float(input("Enter the first operand : "))

#Getting the Second operand from the user and convert it to a float
        number2=float(input("Enter the Second operand : "))


#Check the user's choice and perform the corresponding arithmatic operation
        if choice == 1:
            print(number1,"+",number2,"=",add(number1,number2),"\n")
        elif choice == 2:
            print(number1,"-",number2,"=",sub(number1,number2),"\n")
        elif choice == 3:
            print(number1,"*",number2,"=",mul(number1,number2),"\n")
        elif choice == 4:
            print(number1,"/",number2,"=",div(number1,number2),"\n")
        else:
            print("Invalid Operator")
            
if __name__ == "__main__":
    main()
