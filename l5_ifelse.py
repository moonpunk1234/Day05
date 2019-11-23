from os import system

while True: 
    print("====== Main Menu ========")
    print("1. What is your Name?")
    print("2. What is daughters Name?")
    print("3. Late koro kano?")
    print("4. Exit")
    print("Enter your selection :",end="")
    choice =int( input())


    if choice ==1:
        print('Chand Miah')
    elif choice == 2:
        print('Manahil and Jawaria')
    elif choice ==3:
        print('Rickshawalar Dos')
    elif choice == 4:
        print('Goodbye')
        break    
    else:
        print('Invalid Selection')  

    print("Press Enter to continue ...") 
    input()
    system('cls')

