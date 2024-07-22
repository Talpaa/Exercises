class RecipeManager:

    def __init__(self) -> None:
        
        self.ricettario: dict[str:list[str]] = {}

    def create_recipe(self, ricetta: str, ingredienti: list[str])->dict[str:list[str]]|str:

        if ricetta in self.ricettario:

            return f'Errore: Ricetta già presente.'
        
        self.ricettario[ricetta] = ingredienti

        dizio: dict[str:list[str]] = {ricetta: ingredienti}

        return dizio



manager: RecipeManager = RecipeManager()

print(manager.create_recipe("Pizza Margherita", ["Farina", "Acqua", "Lievito", "Pomodoro", "Mozzarella"]))#{'Pizza Margherita': ['Farina', 'Acqua', 'Lievito', 'Pomodoro', 'Mozzarella']}

print(manager.add_ingredient("Pizza Margherita", "Basilico"))#{'Pizza Margherita': ['Farina', 'Acqua', 'Lievito', 'Pomodoro', 'Mozzarella', 'Basilico']}

print(manager.update_ingredient("Pizza Margherita", "Mozzarella", "Mozzarella di Bufala"))#{'Pizza Margherita': ['Farina', 'Acqua', 'Lievito', 'Pomodoro', 'Mozzarella di Bufala', 'Basilico']}

print(manager.remove_ingredient("Pizza Margherita", "Acqua"))#{'Pizza Margherita': ['Farina', 'Lievito', 'Pomodoro', 'Mozzarella di Bufala', 'Basilico']}

print(manager.list_ingredients("Pizza Margherita"))#['Farina', 'Lievito', 'Pomodoro', 'Mozzarella di Bufala', 'Basilico']