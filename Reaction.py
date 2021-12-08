class Reaction:
    def __init__(self, start_color, color_increment, reactants, products):
        # Start color: a list in the form [red, green, blue] representing the color object
        self.current_red = start_color[0]
        self.current_green = start_color[1]
        self.current_blue = start_color[2]
        # Color increment: a list in the form [red, green, blue] representing the change in the color object WHEN A PRODUCT SHIFT OCCURS
        self.color_increment = color_increment
        # Reactants: a list of strings representing the reactants
        self.reactants = reactants
        # Products: a list of strings representing the products
        self.products = products

    def increment(self):
        self.current_red += self.color_increment[0]
        self.current_green += self.color_increment[1]
        self.current_blue += self.color_increment[2]

    def decrement(self):
        self.current_red -= self.color_increment[0]
        self.current_green -= self.color_increment[1]
        self.current_blue -= self.color_increment[2]
