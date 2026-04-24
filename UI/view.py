from cgitb import reset

import flet as ft


class View(ft.UserControl):
    def __init__(self, page: ft.Page):
        super().__init__()
        # page stuff
        self._page = page
        self._page.title = "Template application using MVC and DAO"
        self._page.horizontal_alignment = 'CENTER'
        self._page.theme_mode = ft.ThemeMode.LIGHT
        # controller (it is not initialized. Must be initialized in the main, after the controller is created)
        self._controller = None
        # -- graphical elements --
        self._title = None

        # Componenti Di selezione
        # row 1
        self.dd_anno = None
        self.dd_brand = None
        self.dd_retailer = None
        # row 2
        self.btn_top_vendite = None
        self.btn_analizza = None

        # Finestra risulati
        self.txt_result = None
        self.txt_container = None
        # -- x --

    def load_interface(self):
        # title
        self._title = ft.Text("Analizza Vendite", color="blue", size=24)
        self._page.controls.append(self._title)

        self.dd_anno = ft.Dropdown(
            label="Anno",
            width= 200,
            options=[ft.dropdown.Option(text="-- nessun filtro --")]
        )
        self._controller.fill_dd_anni()

        self.dd_brand = ft.Dropdown(
            label="Brand",
            width= 200,
            options=[ft.dropdown.Option(text="-- nessun filtro --")]
        )
        self._controller.fill_dd_brand()

        self.dd_retailer = ft.Dropdown(
            label="Retailer",
            width= 360,
            options=[ft.dropdown.Option(key="NONE",text="Nessun Filtro")],
            on_change= self._controller.reset
        )
        self._controller.fill_dd_retailer()


        row1 = ft.Row([self.dd_anno, self.dd_brand, self.dd_retailer])

        self.btn_top_vendite = ft.ElevatedButton(
            text="Top Vendite",
            on_click= self._controller.handle_btn_top_vendite,
        )
        self.btn_analizza = ft.ElevatedButton(
            text="Analizza Vendite",
            on_click= None,
        )

        row2 = ft.Row([self.btn_top_vendite, self.btn_analizza],
                      alignment=ft.MainAxisAlignment.CENTER,)

        self._page.add(row1, row2)

        # List View where the reply is printed
        self.txt_result = ft.ListView(expand=1, spacing=10, padding=20, auto_scroll=True)
        self._page.controls.append(self.txt_result)
        self._page.update()

    @property
    def controller(self):
        return self._controller

    @controller.setter
    def controller(self, controller):
        self._controller = controller

    def set_controller(self, controller):
        self._controller = controller

    def create_alert(self, message):
        dlg = ft.AlertDialog(title=ft.Text(message))
        self._page.dialog = dlg
        dlg.open = True
        self._page.update()

    def update_page(self):
        self._page.update()
