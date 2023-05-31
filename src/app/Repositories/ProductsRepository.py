from Database.main import cursor, connection
from Class.ProductMapper import productMapper

class ProductsRepository():
    def __init__(self):
        pass

    def findByName(self, name):
        cursor.execute(f'''
            SELECT * FROM products
            WHERE name = '{name}'
        ''')

        row = cursor.fetchone()

        return productMapper(row)
    
    def findById(self, id):
        cursor.execute(f'''
            SELECT * FROM products
            WHERE id = '{id}'
        ''')

        row = cursor.fetchone()

        return productMapper(row)

    def findByIds(self, ids):
        cursor.execute(f'''
            SELECT * FROM products
            WHERE id in {tuple(ids)}
        ''')

        rows = cursor.fetchall()

        return map(productMapper, rows)

    def findAll(self):
        cursor.execute("SELECT * FROM products")

        rows = cursor.fetchall()

        return map(productMapper, rows)

    def create(self, name, price, quantify):
        cursor.execute(f'''
            INSERT INTO 
            products (name, price, quantify) 
            VALUES('{name}', '{price}', '{quantify}')
        ''')
        
        connection.commit()

    def update(self, newName, newPrice, newQuantify):
        cursor.execute(f'''
            UPDATE products SET 
                name = '{newName}',
                price = '{newPrice}',
                quantify = '{newQuantify}',
        ''')

        connection.commit()
