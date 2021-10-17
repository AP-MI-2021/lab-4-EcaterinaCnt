def read_list():
    lst = []
    lst_str = input('Dati numere separate prin spatiu: ')
    lst_str_split = lst_str.split(' ')
    for num_str in lst_str_split:
        lst.append((int(num_str)))
    return lst


def show_menu():
    print("1. Citire lista: ")


def main():
    lst = []
    while True:
        show_menu()
        optiune=input("Alege optiunea: ")
        if optiune == "1" :
            lst= read_list()
            print('Numerele din lista: ', lst)
        elif optiune == "x":
            break
        else:
            print("Optiune invalida.")

if __name__ == '__main__':
    main( )