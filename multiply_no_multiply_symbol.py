def multiply_no_multiply_symbol(a,b : int):
    x = 0
    for _ in range(b):
       x += a

    return x

def run(): 
    try:
        a = int(input("Enter the first number to multiply: "))
        b = int(input("Enter the second number to multiply: "))
    except:
        print("You can only use number")
        exit()
    print(f"{a} x {b} = ",multiply_no_multiply_symbol(a,b))


if __name__ == "__main__":
    run()