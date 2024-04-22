
#esercizio 1

def palindromi(x):

    str_reverse = x[::-1]    

    if x == str_reverse:

        print(f"\n\nIl numero {x} è palindromo")

    else:
        print(f"\n\nIl numero {x} non è palindromo")

    return x == str_reverse



x: int = 7665885667
str_x = str(x)

y: int = 1234567890
str_y = str(y)

palindromi(str_x)

palindromi(str_y)

#esercizio 2

def ultima_parola(s):

    a: int = 0
    b: int = 0

    for i in s[::-1]:

        if i != " ":

            a += 1

        elif(i == " ")and(a != 0):

            return a

    





s1: str = "Hello world     "

ultima = ultima_parola(s1)
print(f"\n\nL'ultima parola della frase è lunga {ultima}")

s2: str = "fly me to the moon"
ultima = ultima_parola(s2)
print(f"\nL'ultima parola della frase è lunga {ultima}")

s3: str = "lufy is still joyboy"
ultima = ultima_parola(s3)
print(f"\nL'ultima parola della frase è lunga {ultima}")

