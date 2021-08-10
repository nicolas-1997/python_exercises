def find_the_smallest_number(lista):
   less = "init"

   for x in lista:
        if less == "init":
            less = x
        else:
            less = x if x < less  else less
   print(less)
            



def run():
    lista = [1,2,3,555, 222, 30, 200000, 50, 0, 25, -3]

    find_the_smallest_number(lista)

if __name__ == "__main__":
    run()