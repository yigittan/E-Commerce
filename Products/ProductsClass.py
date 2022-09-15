from datetime import datetime

class Product:
    def __init__(self,title,price,description,category,created_at,discount,size,color):
        self.title = title
        self.price = price
        self.description = description
        self.category = category
        self.created_at = created_at
        self.discount = discount
        self.size = size
        self.color = color