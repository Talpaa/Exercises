import random

def estrazione():

    return random.randrange(0, 15)

numeri: list = [0,1,2,3,4,5,6,7,8,9, 'a', 'b', 'c', 'd','e','f']

golden_ticket: list = []

golden_ticket.append(numeri[estrazione()])
golden_ticket.append(numeri[estrazione()])
golden_ticket.append(numeri[estrazione()])
golden_ticket.append(numeri[estrazione()])

print(f'\n\nTutti i biglietti uguali a questo {golden_ticket} sono vincitori')