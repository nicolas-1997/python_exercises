def is_it_odd_or_even(number: int):
    if number % 2 == 0:
        print(f"The {number} is pair")
    else:
        print(f"The {number} is odd")

def odd_or_even_list(lista):
    list_of_pairs = []
    odd_list = []

    for element in lista:
        if element % 2 == 0:
            list_of_pairs.append(element)
        else:
            odd_list.append(element)

    print("list of pairs",list_of_pairs)
    print("odd list", odd_list)


def run():
    # number = int(input("Enter a integer: "))
    # is_it_odd_or_even(number)
    lista = [1,2,50,25,111,12,16,88,9,161,0,63]
    odd_or_even_list(lista)



if __name__ == "__main__":
    run()