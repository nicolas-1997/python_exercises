def save_data(name, lastname, age: str):
    f = open("nombrecompleto.txt", "a")
    line = str(name) + " " + str(lastname) + " " + str(age) + '\n'
    f.write(line)
    f.close()

    print("Thanks!!")

def run():
    name = input("Enter your name: ")
    lastname = input("Enter your lastname: ")
    age = input("Enter your age: ")

    save_data(name, lastname, age)

if __name__ == "__main__":
    run()