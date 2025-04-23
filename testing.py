def sum(a, b):
    return a + b

def get_numbers():
    a = float(input("a: "))
    b = float(input("b: "))
    return a, b

def main():
    a, b = get_numbers()
    print(sum(a, b))

print("adding text to test commit")


if __name__ == "__main__":
    main()
