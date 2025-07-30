def main():
    while True:
        try:
            odgovor = int(input("Da li želis da učis (1), ili da vježbas (2) tablicu množenja?"))
            if odgovor == 1:
                tablica_mnozenja()
            elif odgovor == 2:
                vjezbalica_mnozenja()
            else:
                print("Dakle, izaberi ili 1 ili 2.")
                continue
        except ValueError:
            print("Dakle, izaberi ili 1 ili 2.")
            continue


def vjezbalica_mnozenja():
    import random
    while True:
        try:
            ran_num_1 = random.randint(1, 10)
            ran_num_2 = random.randint(1, 10)
            result = ran_num_1 * ran_num_2
            answer = int(input(f"Koliko je {ran_num_1} * {ran_num_2} = "))
            if answer == result:
                print(f"Bravo!! To je tačan odgovor.")
                continue
            else:
                print(f"Netacno. Odgovor je {result}.")
                continue
        except ValueError:
            print(f"Samo cijeli brojevi se prihvaćaju... a odgovor je bio {result}.")
            continue

def tablica_mnozenja():
    while True:
        try:
            a = list(range(1, 11))
            b = int(input("Unesi broj za koji želiš da izlistaš tablicu. > "))
            for i in a:
                print(f"{i}*{b}=",i * b)
                continue
        except ValueError:
            print("Samo cijele brojeve možeš unositi.")
            continue
