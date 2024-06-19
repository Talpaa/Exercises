from movie_genre import Azione, Commedia, Drama

class Noleggio:

    def __init__(self, film_list: list[Azione | Commedia | Drama]) -> None:
        
        self.film_list: list[Azione, Commedia, Drama] = film_list #lista film disponibili all'acquisto
        self.rented_film: dict[int: list[Azione, Commedia, Drama]] = {}

    def isAvaible(self, film: Azione | Commedia | Drama):

        if film in self.film_list:

            print(f"Il film scelto è disponibile: {film.getTitle()}!")
            return True
        
        else:

            print(f"Il film scelto non è disponibile: {film.getTitle()}!")
            return False
        
    def rentAMovie(self, film: Azione | Commedia | Drama, id_client: int):

        if self.isAvaible(film):

            self.film_list.remove(film)

            if id_client in self.rented_film:

                self.rented_film[id_client].append(film)

            else:

                self.rented_film[id_client] = film

            print(f'Il cliente {id_client} ha noleggiato {film.getTitle()}!')

        else:

            print(f'Il cliente {id_client} non ha potuto noleggiare {film.getTitle()}!')

    def giveBack(self,film: Azione | Commedia | Drama, id_client: int, giorni_affitto: int):

        if id_client in self.rented_film:

            if film in self.rented_film[id_client]:

                self.rented_film[id_client].remove(film)
                self.film_list.append(film)

                print(f"Cliente: {id_client}! La penale da pagare per il film {film.getTitle()} e' di {film.calcolaPenaleRitardo()} euro!")