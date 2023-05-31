class ProductMapper:
    def __init__(self, dataMapper):
        self.id = dataMapper[0]
        self.name = dataMapper[1]
        self.price = dataMapper[2]
        self.quantify = dataMapper[3]

def productMapper(dataMapper):
    return ProductMapper(dataMapper) if dataMapper else None