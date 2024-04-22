
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



#esercizio 3

def convert_to_title(col_number):

    result: str = ""
    alfabeto = ["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]

    while col_number > 26:

        a = (col_number-1) % 26
        col_number = (col_number // 26)-1
        print(col_number)

        result = alfabeto[a]+result


    result = alfabeto[col_number]+result

    return result 

titolo: int = 1214
coversione: str = convert_to_title(titolo)

print(coversione)
