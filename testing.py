def sum(a, b):
    return a + b

def get_numbers():
    a = float(input("a: "))
    b = float(input("b: "))
    return a, b

def main():
    print(sum(get_numbers))


if __name__ == "main":
    main()
