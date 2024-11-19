import flet as ft
import pandas as pd

def main(page: ft.Page):
    page.title = "Employee Voting Details"
    page.theme_mode = ft.ThemeMode.LIGHT
    page.vertical_alignment = ft.MainAxisAlignment.CENTER

    txt_number = ft.TextField(value="Employee Number", text_align=ft.TextAlign.RIGHT, width=200)

    def minus_click(e):
        txt_number.value = str(int(txt_number.value) - 1)
        page.update()

    def plus_click(e):
        # mydataset = {
        #    'cars': ["BMW", "Volvo", "Ford"],
        #     'passings': [3, 7, 2]
        # }

        # myvar = pd.DataFrame(mydataset)
        # print(type(str(myvar)))
        # txt_number.value = str(int(txt_number.value) + 1)
        txt_number.value = str("Employee Number")
        page.update()

    page.add(
        ft.Row(
            [
                # ft.IconButton(ft.icons.REMOVE, on_click=minus_click),
                txt_number,
                ft.IconButton(ft.icons.ADD, on_click=plus_click),
                # ft.FilledButton(text="Filled button", on_click=plus_click),
            ],
            alignment=ft.MainAxisAlignment.CENTER,
        )
    )


ft.app(main, view=ft.AppView.WEB_BROWSER)