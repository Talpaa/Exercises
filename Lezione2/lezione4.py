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