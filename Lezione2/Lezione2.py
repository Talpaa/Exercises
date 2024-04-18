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



#2-5. Famous Quote: Find a quote from a famous person you admire. 
#Print the quote and the name of its author. Your output should look something like the following, 
#including the quotation marks: Albert Einstein once said, “A person who never made a mistake never tried anything new.”

#2-6. Famous Quote 2: Repeat Exercise 2-5, but this time, represent the famous person’s name using a variable called famous_person. 
#Then compose your message and represent it with a new variable called message. Print your message. 

#variabile contenente il nome dell'autore
author_name: str = "a"

#variabile contenente la citazione dell'autore
quote: str = "b"


#contiene il messaggio
message1: str = f"{author_name} una volta disse, \"{quote}.\""



#2-8. File Extensions: Python has a removesuffix() method that works exactly like removeprefix(). 
#Assign the value 'python_notes.txt' to a variable called filename. Then use the removesuffix() method to display the filename without the file extension, 
#like some file browsers do.

#variabile con nome del file e la sua estensione
file_name: str = "python_notes.txt"

#variabile con all'interno una funzione che leva l'estensione dal nome
file_name_noext: str = file_name.removesuffix(".txt")

#stampa il nome del file senza l'estensione
print(file_name_noext)



#3-1. Names: Store the names of a few of your friends in a list called names. 
#Print each person’s name by accessing each element in the list, one at a time.


#creazione della lista di nomi
name_list: list = ["Daniele","Andrea","Alessandro","Francesco"]


#stampa i nomi nella lista uno per volta tramite 'for'
for i in name_list:

    print(i)



#3-2. Greetings: Start with the list you used in Exercise 3-1, but instead of just printing each person’s name, print a message to them. 
#The text of each message should be the same, but each message should be personalized with the person’s name.

#stampa per ogni nome della lista "ciao, 'name'"
for i in name_list:

    print(f"\nCiao, {i}")



#3-3. Your Own List: Think of your favorite mode of transportation, such as a motorcycle or a car, and make a list that stores several examples. 
#Use your list to print a series of statements about these items, such as “I would like to own a Honda motorcycle.”

#creazione lista di veicoli
list_vehicles: str = ["auto1","auto2","auto3","auto4"]

#ciclo per scrivere un messaggio per ogni variabile presente
for i in list_vehicles:

    print(f"\nmi piacerebbe avere {i}")



#3-4. Guest List: If you could invite anyone, living or deceased, to dinner, who would you invite? 
#Make a list that includes at least three people you’d like to invite to dinner. 
#Then use your list to print a message to each person, inviting them to dinner.

#creazione lista invitati
list_vehicles: str = ["persona1","persona2","persona3","persona4"]

#ciclo per scrivere l'invito per ogni nome presente nella lista
for i in list_vehicles:

    print(f"\nCiao {i}, mi piacerebbe invitarti a cena.")



#3-5. Changing Guest List: You just heard that one of your guests can’t make the dinner, so you need to send out a new set of invitations. 
#You’ll have to think of someone else to invite.

# Start with your program from Exercise 3-4. Add a print() call at the end of your program, stating the name of the guest who can’t make it.
# Modify your list, replacing the name of the guest who can’t make it with the name of the new person you are inviting.
# Print a second set of invitation messages, one for each person who is still in your list.

