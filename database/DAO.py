from database.DB_connect import DBConnect
from model.retailer import Retailer

class DAO:
    def __init__(self):
        raise RuntimeError('Do not create an instance, use the class methods!')

    @staticmethod
    def run_query(query, params=None, as_dictionary=False):
        cnx = DBConnect.get_connection()
        if cnx is None:
            raise RuntimeError('Database connection failed')

        with cnx.cursor(dictionary = as_dictionary) as cursor:
            cursor.execute(query, params or ())
            results = cursor.fetchall()

        cnx.close()
        return results

    @staticmethod
    def get_brads():
        query = """
        select distinct Product_brand from go_products
        """
        result = DAO.run_query(query)
        return [row[0] for row in result]

    @staticmethod
    def get_years():
        query = """ 
        select distinct YEAR(Date) from go_daily_sales
        """
        result = DAO.run_query(query)
        return [row[0] for row in result]

    @staticmethod
    def get_retailers():
        query = """
        select distinct r.Retailer_code, r.Retailer_name, r.country, r.Type from go_retailers as r
        """
        result = DAO.run_query(query, as_dictionary=True)
        retailers = []
        for row in result:
            retailers.append(
               Retailer(
                   id = row["Retailer_code"],
                   name = row["Retailer_name"],
                   country = row["country"],
                   type = row["Type"]
               )
            )
        return retailers

    @staticmethod
    def get_top_selles(year, brend, retailer):
        query = """
        select s.*, s.Unit_sale_price * s.Quantity as ricavo
        from go_daily_sales s
        JOIN go_products gp ON s.Product_number = gp.Product_number 
        WHERE YEAR(s.`Date`) = COALESCE(%s, YEAR(s.Date))
        AND gp.Product_brand = COALESCE(%s, gp.Product_brand)
        AND s.Retailer_code = COALESCE(%s, s.Retailer_code)
        ORDER by ricavo DESC 
        LIMIT 5
        """
        return DAO.run_query(query, (year, brend, retailer), as_dictionary=True)