def get_operation():
    op = input("operação: ")

    return op

def gather_data():
    n1 = input("primeiro valor: ")
    n2 = input("segundo valor: ")
    op = input("operação: ")

    return n1, n2, op

def main():
    n1, n2, op = gather_data()
    print(eval(n1+op+n2))
    
    return None

if __name__ == "__main__":
    main()
    