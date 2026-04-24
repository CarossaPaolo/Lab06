from dataclasses import dataclass


@dataclass
class Retailer:
    id:int
    name:str
    type:str
    country:str

    def __hash__(self):
        return hash(self.id)

    def __repr__(self):
        return f"{self.id} - {self.name} - {self.type} - {self.country}"

    def __str__(self):
        return self.name


