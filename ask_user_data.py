def add_elements(lista):
    result = 0
    for element in lista:
        result += element
    return result

def run():
    lista = []
    print("Enter only numbers and to exit write enough or x")
    while True:
        entry = input("Enter a numer: ")
        try:
            data = entry.lower()
            if data == "enough" or data == "x":
                print("Your values",lista)
                print("the sum of your entered values ​​is: ",add_elements(lista))
                break
            else:
                try:
                    value = int(entry)
                    lista.append(value)
                except:
                    print("Invalid data")
                    break
        except:
            break





if __name__ == "__main__":
    run()