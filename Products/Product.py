class Product:
    def __init__(self, name,
                 price,
                 brand,
                 description,
                 category, created_at, discount, size, color):
        self.name = name
        self.price = price
        self.brand = brand
        self.description = description
        self.category = category
        self.created_at = created_at
        self.discount = discount
        self.size = size
        self.color = color
