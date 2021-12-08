class Reaction:
    def __init__(self, start_color, color_increment, reactants, products, product_shift):
        # Start color: a Color object representing the unedited equilibrium
        self.current_color = start_color
        # Color increment: a Color object representing the change in color WHEN A PRODUCT SHIFT OCCURS
        self.color_increment = color_increment
        # Reactants: a list of strings representing the reactants
        self.reactants = reactants
        # Products: a list of strings representing the products
        self.products = products

    def increment(self):
        self.current_color += self.color_increment

    def decrement(self):
        self.current_color -= self.color_increment
