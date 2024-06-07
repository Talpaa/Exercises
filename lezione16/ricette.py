class RecipeManager:

    def __init__(self) -> None:
        
        self.ricettario: dict[str, list[str]] = {}

    def create_recipe(self, name: str, ingredients: list [str]):

        name = name.title()

        if name not in self.ricettario:

            ingredienti: list[str] = []
            ricettario: dict[str, list[str]] = {}

            for ingrediente in ingredients:
                ingredienti.append(ingrediente.casefold())

            self.ricettario[name] = ingredienti
            ricettario[name] = ingredienti
            return ricettario

        else:

            return f'Errore: Ricetta già esistente'
        

    def add_ingredient(self, recipe_name: str, ingredient: str):

        recipe_name = recipe_name.title()
        ingredient = ingredient.casefold()

        if recipe_name in self.ricettario:
            
            for ingredient_in_list in self.ricettario[recipe_name]:

                if ingredient_in_list.casefold() == ingredient:

                    return f'Errore: Ingrediente già presente nella ricetta'

            
            self.ricettario[recipe_name].append(ingredient)

            return f'{recipe_name}: {self.ricettario[recipe_name]}'


        else:

            return f'Errore: Ricetta inesistente'
        
    
    def remove_ingredient(self, recipe_name: str, ingredient: str):

        recipe_name = recipe_name.title()
        ingredient = ingredient.casefold()
        controllo: bool = False

        if recipe_name in self.ricettario:
            
            for ingredient_in_list in self.ricettario[recipe_name]:

                if ingredient_in_list.casefold() == ingredient:

                    controllo = True
                
            if controllo:

                self.ricettario[recipe_name].remove(ingredient)
                return f'{recipe_name}: {self.ricettario[recipe_name]}'

            else:
                
                return f'Errore: Ingrediente non presente nella ricetta'
            
    def update_ingredient(self, recipe_name: str, old_ingredient: str, new_ingredient: str):

        recipe_name = recipe_name.title()
        old_ingredient = old_ingredient.casefold()
        new_ingredient = new_ingredient.casefold()

        controllo: bool = False

        if recipe_name in self.ricettario:
            
            for ingredient_in_list in self.ricettario[recipe_name]:

                if ingredient_in_list.casefold() == old_ingredient:

                    controllo = True
                
            if controllo:

                self.ricettario[recipe_name].remove(old_ingredient)
                self.ricettario[recipe_name].append(new_ingredient)

                return f'nome ricetta:____ ingredienti:_,_,_,_,_'

            else:
                
                return f'Errore: Ingrediente non presente nella ricetta'
            
    def list_recipes(self):

        message: str = 'Ecco tutte le ricette presenti nel ricettario:\n'
        count: int = 0

        for ricetta in self.ricettario:

            count += 1
            message += f'{count}) {ricetta};' 

        
        if len(self.ricettario) > 0:

            return message
        
        else:

            return f'Errore: non sono presenti ricette nel ricettario'
        
    def list_ingredients(self, recipe_name: str): 

        recipe_name = recipe_name.title()

        if recipe_name in self.ricettario:

            message: str = f'Gli ingredienti della ricetta {recipe_name} sono:\n'
            count: int = 0
            
            for ingredient in self.ricettario[recipe_name]:

                message += f'{count}) {ingredient}'

        else:

            return f'Errore: ricetta non presente nel ricettario'

    def search_recipe_by_ingredient(self, ingredient: str):

        message: str = f'Le ricette che usano l\'ingrediente \'{ingredient}\' sono:\n'
        count: int = 0

        for ricetta in self.ricettario:

            if ingredient in self.ricettario[ricetta]:

                message += f'{count}) {ricetta}'

        if message != f'Le ricette che usano l\'ingrediente \'{ingredient}\' sono:\n':

            return message
        
        else:

            return f'Errore: nessuna ricetta presente nel ricettario non usa l\'ingrediente \'{ingredient}\''