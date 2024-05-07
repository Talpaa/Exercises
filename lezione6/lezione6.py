class Person:

    # - name
    # - surname
    # - age

    def __init__(self, name: str, surname: str, age: int) -> None:
        
        self.name = name

        self.surname = surname

        self.age = age

lorenzo = Person("Lorenzo","Maggi", 24) #Person.__init__("Lorenzo", "Maggi", 24)
print(f"\n\nNome = {lorenzo.name}; \nCognome = {lorenzo.surname}; \nEtà = {lorenzo.age}")

lorenzo.age = 22
print(f"\nEtà = {lorenzo.age}")


name: str = input("\nInserisci il tuo nome: ")
surname: str = input("Inserisci il tuo cognome: ")
age: int = int(input("Inserisci la tua età: "))

user = Person(name, surname, age)
print(f"\n\nNome = {user.name}; \nCognome = {user.surname}; \nEtà = {user.age}")
print(f"\n\nNome = {lorenzo.name}; \nCognome = {lorenzo.surname}; \nEtà = {lorenzo.age}")


avg_age: float = (lorenzo.age + user.age) / 2
print(f"L'età media è :{avg_age}")


persons: list[Person]= [Person("Lorenzo", "Maggi", 22),
                       Person("Francesco", "Totti", 52),
                       Person("Mario", "Rossi", 84)]


avg_age = 0

for person in persons:

    avg_age += person.age

avg_age /= len(persons)
print(f"L'età media è :{avg_age}")