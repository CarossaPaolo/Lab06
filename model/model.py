from database.DAO import DAO

class Model:
    def __init__(self):
        pass

    def get_years(self):
        return DAO.get_years()

    def get_brends(self):
        return DAO.get_brads()

    def get_retailers(self):
        return DAO.get_retailers()

    def get_top_selles(self, year, brend, reselr):
        pass