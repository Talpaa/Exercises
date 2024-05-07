#esercizo 1
class Person:

    # - name
    # - surname
    # - age

    def __init__(self, name: str, age: int) -> None:
        
        self.name = name

        self.age = age

#esercizio 2
class Student:

    # - name
    # - age
    # - gender
    # - study program
    def __init__(self, name: str, age: int, gender: str, study_program: str) -> None:
        
        self.name = name
        self.age = age
        self.gender = gender
        self.study_program = study_program

    def __str__(self) -> str:
        
        return f"Il nome dello studente è {self.name} ha {self.age} anni il suo gender è {self.gender} e il suo percorso di studi è {self.study_program}"


alice = Person("Alice W.", 45)

bob = Person("Bob M.", 36)

print(bob.age)

if alice.age > bob.age:

    print(alice.name)

else:

    print(bob.name)

persons: list[Person] = [alice, bob,
                         Person("Luca Verdi", 27),
                         Person("Francesco Totti", 52),
                         Person("Mario Rossi", 84)]

youngest: Person = alice

for person in persons:

    if person.age < youngest.age:

        youngest = person


print(youngest.name)



#esercizio 2  
print('\n\n\n')
students: list[Student] = [Student("Mario Rossi", 24, "Male", "Fullstack"),
                           Student("Francesco Verdi", 19, "Male", "Cloud"),
                           Student("Sofia Proietti", 35, "Female", "Cyber Security")
                           ]

for i in students:

    print(i)