import flet as ft
from model.model import Model

class Controller:
    def __init__(self, view, model):
        # the view, with the graphical elements of the UI
        self._view = view
        # the model, which implements the logic of the program and holds the data
        self._model = Model()

    def fill_dd_anni(self):
        for i in self._model.get_years():
            self._view.dd_anno.options.append(
                ft.dropdown.Option(
                    key=i
                )
            )

    def fill_dd_brand(self):
        for i in self._model.get_brends():
            self._view.dd_brand.options.append(
                ft.dropdown.Option(
                    key=i
                )
            )
    def fill_dd_retailer(self):
        for i in self._model.get_retailers():
            self._view.dd_retailer.options.append(
                ft.dropdown.Option(
                    key=i.id,
                    text=i.__str__(),
                    data=i,
                )
            )

    def handle_btn_top_vendite(self, e):
        retailer = self._view.dd_retailer.value
        anno = self._view.dd_anno.value
        brend = self._view.dd_brand.value
        print(retailer, type(retailer))
        print(anno, type(anno))
        print(brend, type(brend))
        # records = self._model.get_top_selles(anno, brend, retailer)

    def reset(self, e):
        if self._view.dd_retailer.value == "NONE":
            self._view.dd_retailer.value = None
            self._view.dd_retailer.update()

