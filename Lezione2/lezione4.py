"""Let’s try to define a function named subtract ourselves:
- It should take 2 parameters.
- Inside the function, it should subtract the two.
- Then, return the result."""

def sottrazione(a:int,b:int) -> int:

    sott = a - b
    return sott


risultato = sottrazione(434,276)
print(risultato)



"""
Write a function check_value(), which takes a number as an argument.
Using if / else, the function should print whether the number is bigger, smaller,
or equal to the other number.
"""

def check_value(num,check):

    if num > check:
        print(f"{num} è più grande di {check}")

    elif num==check:
        print(f"{num} è uguale a {check}")

    else:
        print(f"{num} è più piccolo di {check}")

#num = input("Inserisci un numero e io ti dirò se è piu grande, uguale o minore del numero : ")
check_value(7,1)




"""
Write a function check_length(), which takes a string as an argument.
Using if / else, check if the length of the string is bigger, smaller, or equal to 10
characters."""

def check_length(stringa):

    len_str = len(stringa)

    if len_str > 10:
        print(f"\"{stringa}\" è più lunga di 10 caratteri")

    elif len_str == 10:
        print(f"\"{stringa}\" è lunga 10 caratteri")

    else:
        print(f"\"{stringa}\" è più corta di 10 caratteri")


stringa = input("inserisci una stringa a piacere e io ti diro se è più lunga, uguale o più corta di 10 caratteri: \n")

check_length(stringa)