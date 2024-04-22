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