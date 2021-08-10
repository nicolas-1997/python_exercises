def run():
    lista = []
    print("Enter only numbers and to exit write enough")
    while True:
        entry = input("Enter a numer: ")
        try:
            data = entry.lower()
            if data == "enough":
                print("Your values",lista)
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