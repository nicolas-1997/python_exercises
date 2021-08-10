#Enter first and last name and print them backwards
def flip_words(name, lastname: str):
    print("Your name backwards is: ", name[::-1])
    print("Your lastname backwards is: ", lastname[::-1])

    if name == name[::-1]:
        print("Congratulations your name is a palindrome!!")
    
    if lastname == lastname[::-1]:
        print("Congratulations your lastname is a palindrome!!")



def run():
    name = input("Enter your name: ")
    lastname = input("Enter yout lastname: ")
    
    if len(name) > 1 and len(lastname) > 1:
        flip_words(name, lastname)
    else:
        print("some of the entered words is too short")

if __name__ == "__main__":
    run()