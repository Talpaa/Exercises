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

#3-5. Changing Guest List: You just heard that one of your guests can’t make the dinner, so you need to send out a new set of invitations. 
#You’ll have to think of someone else to invite.
# Start with your program from Exercise 3-4. Add a print() call at the end of your program, stating the name of the guest who can’t make it.
# Modify your list, replacing the name of the guest who can’t make it with the name of the new person you are inviting.
# Print a second set of invitation messages, one for each person who is still in your list.

#3-6. More Guests: You just found a bigger dinner table, so now more space is available. Think of three more guests to invite to dinner.
# Start with your program from Exercise 3-4 or 3-5. Add a print() call to the end of your program, informing people that you found a bigger table.
# Use insert() to add one new guest to the beginning of your list.
# Use insert() to add one new guest to the middle of your list.
# Use append() to add one new guest to the end of your list.
# Print a new set of invitation messages, one for each person in your list.

#3-7. Shrinking Guest List: You just found out that your new dinner table won’t arrive in time for the dinner, and now you have space for only two guests.
# Start with your program from Exercise 3-6. Add a new line that prints a message saying that you can invite only two people for dinner.
# Use pop() to remove guests from your list one at a time until only two names remain in your list. Each time you pop a name from your list, 
#print a message to that person letting them know you’re sorry you can’t invite them to dinner.
# Print a message to each of the two people still on your list, letting them know they’re still invited.
# Use del to remove the last two names from your list, so you have an empty list. Print your list to make sure you actually have an empty list at the end of your program.


def manda_inviti(list_invited: list):

    #ciclo per scrivere l'invito per ogni nome presente nella lista
    for i in list_invited:

        print(f"\nCiao {i}, mi piacerebbe invitarti a cena.")

    

def ritira_inviti(list_invited: list)->list:

    i: int = (len(list_invited))-1

    while(len(list_invited) > 2):

        print(f"\n{list_invited[i]}, sono dispiaciuto di dover annulare la cena organizata")
        list_invited.pop(i)
        i = (len(list_invited))-1

    print("\n")
    for j in list_invited:

        print(f"\n{j}, sei ancora invitato alla cena organizzata")

    del list_invited

    #return list_invited

    


#creazione lista invitati
list_invited: list = ["persona1","persona2","persona3","persona4"]

#chiamo la funzione che ho creato per mandare gli inviti
manda_inviti(list_invited)

print(f"\n\n{list_invited[2]} non potrà partecipare alla cena\n\n")

#sostituisco l'invitato che non può venire con una nuova persona
list_invited[2] = "persona5"

#richiamo la funzione che ho creato per mandare gli inviti
manda_inviti(list_invited)

print("\n\nCiao invitati, vi scrivo per informarvi di aver trovato un tavolo più grande")

#serve a trovare il centro della lista per inserire un nuovo invitato
middle = (len(list_invited))//2
list_invited.insert(middle,"persona7")
list_invited.insert(0,"persona0")
list_invited.append("persona6")

#richiamo la funzione che ho creato per mandare gli inviti
manda_inviti(list_invited)

print("\n\n\n")
list_invited = ritira_inviti(list_invited)

print(f"\n{list_invited}")



#3-8. Seeing the World: Think of at least five places in the world you’d like to visit.
# Store the locations in a list. Make sure the list is not in alphabetical order.
place: list = ["Tenerife","Florida","Giappone","Islanda","Marocco"]

# Print your list in its original order. Don’t worry about printing the list neatly; just print it as a raw Python list.
print(f"{place}")

# Use sorted() to print your list in alphabetical order without modifying the actual list.
print(f"{sorted(place)}")

# Show that your list is still in its original order by printing it.
print(f"{place}")

# Use sorted() to print your list in reverse-alphabetical order without changing the order of the original list.
print(f"{sorted(place, reverse=True)}")

# Show that your list is still in its original order by printing it again.
print(f"{place}")

# Use reverse()  to change the order of your list. Print the list to show that its order has changed.
place.reverse()
print(f"{place}")

# Use reverse() to change the order of your list again. Print the list to show it’s back to its original order.
place.reverse()
print(f"{place}")

# Use sort() to change your list so it’s stored in alphabetical order. Print the list to show that its order has been changed.
place.sort()
print(f"{place}")
# Use sort() to change your list so it’s stored in reverse-alphabetical order. Print the list to show that its order has changed.
place.sort(reverse=True)
print(f"{place}")













