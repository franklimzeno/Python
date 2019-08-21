import sys

def bissexto(ano):
    if ano%4 == 0:
        return print('Ano Bissexto')
    else:
        return print('Ano Comum')

def main():
    ano = int(sys.argv[1])
    bissexto(ano)

if __name__ == "__main__":
    main()