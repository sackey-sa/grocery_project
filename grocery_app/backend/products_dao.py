""" Backend Code for Grocery Personal Project"""
from typing import Any
from sql_connection import get_sql_connection

def get_all_products(connection:Any)-> list[dict[str,str]]:
    """ Prints all the products in the SQL database"""

    cursor = connection.cursor()

    query =( "SELECT products.products_id, products.name, products.uom_id, products.price_per_unit, uom.uom_name "
    "from grocery_store.products inner join uom on products.uom_id = uom.uom_id;")
    cursor.execute(query)

    response = []

    for (products_id,name,uom_id,price_per_unit,uom_name) in cursor:
        response.append(
            {
                'product_id':products_id,
                'name':name,
                'uom_id': uom_id,
                'price_per_unit': price_per_unit,
                'uom_name':uom_name
            }
        )



    return response

def insert_new_product(connection:Any,product:dict[str,str])-> Any:
    """ Inserts a new product row with the inputted data"""
    cursor = connection.cursor()
    query = ("INSERT INTO products"
             "(name,uom_id,price_per_unit)"
             "VALUES (%s,%s,%s)")

    data = (product['product_name'],product["uom_id"],product['price_per_unit'])
    cursor.execute(query,data)
    connection.commit()

    return cursor.lastrowid

def delete_product(connection:Any,products_id:int)->None:
    cursor = connection.cursor()
    query = ("DELETE FROM products where products_id =" + str(products_id))
    cursor.execute(query)
    connection.commit()
    



if __name__ =='__main__':
    connection = get_sql_connection()
    print(delete_product(connection,7))
