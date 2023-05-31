carts = []


class CartsRepository:
    def __init__(self):
        pass

    def findById(self, id):
        for cart in carts:
            if id == cart["id"]:
                return cart

        return []

    def create(self, id):
        ids = map(lambda cart: cart['id'], carts)

        if not id in ids:
            carts.append({ "id": id, "products": [] })

    def addProduct(self, id, productId, productQuantify):
        cart = self.findById(id)

        for product in cart["products"]:
            if product["id"] == productId:
                product['quantify'] += productQuantify       
                return

        cart["products"].append({ "id": productId, "quantify": productQuantify })

    def seeCart(self):
        print(carts)

# RESETAR BANCO DE DADOS
# IMPLEMENTAR CARRINHO