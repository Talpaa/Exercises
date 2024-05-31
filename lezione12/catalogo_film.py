class MovieCatalog:
    
    def __init__(self) -> None:
        
        self.catalogo: dict[str, list[str]] = {}

    def add_movie(self, director_name: str, movies: str):

        flag: bool = True

        for regista in self.catalogo:

            if regista.lower() == director_name.lower():

                self.catalogo[regista].append(movies.title())
                print(f'Il film {movies.title()} è stato aggiunto alla lista di film del regista {director_name.title()}.\n')
                flag = False

        if flag:
            print(f'Il film {movies.title()} non è stato aggiunto perchè il regista {director_name.title()} non è presente nel catalogo.\n')


    def remove_movie(self, director_name: str, movies: str):
        
        if director_name.title() in self.catalogo:

            self.catalogo[director_name.title()].remove(movies.title())
            print(f'Il film {movies.title()} è stato rimosso dalla lista di film del regista {director_name.title()}.\n')

        else:
            print(f'Il film {movies.title()} non è stato rimosso perchè il regista {director_name.title()} non è presente nel catalogo.\n')

    def list_directors(self):

        i: int = 0

        print(f'Ecco a te la lista di tutti i registi presenti nel catalogo:\n')

        for regista in self.catalogo:

            i += 1
            print(f'{i}) {regista.title()};\n')

    def get_movies_by_director(self, director_name: str):

        flag: bool = True

        for regista in self.catalogo:

            if regista.lower() == director_name.lower():
                i: int = 0
                print(f'Ecco la lista di film del regista {director_name.title()} disponibili nel catalogo:\n')

                for film in self.catalogo[regista]:

                    print(f'{i}) {film.title()};\n')

                flag = False

        if flag:
            print(f'Il regista {director_name.title()} non è presente nel catalogo.\n')




#catalogo: dict[str, list[str]] = {'nome_regista, ['nome_film_1', 'nome_film_2']}
