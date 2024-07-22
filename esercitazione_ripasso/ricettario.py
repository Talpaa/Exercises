class RecipeManager:

    def __init__(self) -> None:
        
        self.ricettario: dict[str:list[str]] = {}

    def create_recipe(self, name: str, ingredients: list[str])->dict[str:list[str]]|str:

        if name in self.ricettario:

            return f'Errore: Ricetta già presente.'
        
        self.ricettario[name] = ingredients

        dizio: dict[str:list[str]] = {name: ingredients}

        return dizio

    def add_ingredient(self, recipe_name: str, ingredient: str):

        if recipe_name in self.ricettario:

            if ingredient in self.ricettario[recipe_name]:

                pass

            else:

                return f'Errore: Questo ingrediente è gia presente in questa ricetta'

        else:

            return f'Errore: Questa ricetta non esiste'


manager: RecipeManager = RecipeManager()

print(manager.create_recipe("Pizza Margherita", ["Farina", "Acqua", "Lievito", "Pomodoro", "Mozzarella"]))#{'Pizza Margherita': ['Farina', 'Acqua', 'Lievito', 'Pomodoro', 'Mozzarella']}

print(manager.add_ingredient("Pizza Margherita", "Basilico"))#{'Pizza Margherita': ['Farina', 'Acqua', 'Lievito', 'Pomodoro', 'Mozzarella', 'Basilico']}

print(manager.update_ingredient("Pizza Margherita", "Mozzarella", "Mozzarella di Bufala"))#{'Pizza Margherita': ['Farina', 'Acqua', 'Lievito', 'Pomodoro', 'Mozzarella di Bufala', 'Basilico']}

print(manager.remove_ingredient("Pizza Margherita", "Acqua"))#{'Pizza Margherita': ['Farina', 'Lievito', 'Pomodoro', 'Mozzarella di Bufala', 'Basilico']}

print(manager.list_ingredients("Pizza Margherita"))#['Farina', 'Lievito', 'Pomodoro', 'Mozzarella di Bufala', 'Basilico']