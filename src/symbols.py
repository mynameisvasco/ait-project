def read():
    with open("example.txt", "r") as es:
        lines = es.read()

        symbols= set(lines)  #il print di un set genera solo elementi unici, non stampa i doppioni
        print(symbols)
        print(len(symbols))

read()

