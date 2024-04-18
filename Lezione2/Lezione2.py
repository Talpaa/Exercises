#Daniele Taccini


#2-3. Personal Message: Use a variable to represent a person’s name, and print a message to that person. 
#Your message should be simple, such as, “Hello Eric, would you like to learn some Python today?”

#questa variabile contiene il nome
name: str = "Erik"

#questa variabile contiene il messaggio
message: str = f"Hello {name}, ti va di imparare python isieme?"

#stampa il messaggio
print(message)



#2-4. Name Cases: Use a variable to represent a person’s name, and then print that person’s name in lowercase, uppercase, and title case.

#rende nome tutto in maiuscolo
name_upper: str = name.upper()
#rende nome tutto in minuscolo
name_lower: str = name.lower()
#rende la primalettera di nome in maiuscolo
name_title: str = name.title()


print(f"\n{name_upper} ")
print(name_lower)
print(name_title)