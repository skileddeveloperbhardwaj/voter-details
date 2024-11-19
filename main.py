import flet as ft
import csv

def main(page: ft.Page):
    page.title = "Flet counter example"
    page.theme_mode = ft.ThemeMode.LIGHT
    page.vertical_alignment = ft.MainAxisAlignment.CENTER

    txt_number = ft.TextField(value="Enter Employee ID", text_align=ft.TextAlign.RIGHT, width=100)
    emp_details = ft.TextField(value="Voting Details", text_align=ft.TextAlign.RIGHT, width=200)

    def minus_click(e):
        txt_number.value = str(int(txt_number.value) - 1)
        page.update()

    def plus_click(e):
        txt_number.value = str(int(txt_number.value) + 1)
        page.update()
    
    def fetch_details(e):
        path = 'lc_1000_rows.csv'
        with open(path, mode='r') as file:
            csvFile = csv.reader(file)
            for lines in csvFile:
                if(lines[2] == '3316245'):
                    emp_details.value = str(lines)

    page.add(
        ft.Row(
            [
                # ft.IconButton(ft.icons.REMOVE, on_click=minus_click),
                txt_number,
                emp_details,
                # ft.IconButton(ft.icons.ADD, on_click=plus_click),
                ft.ElevatedButton(text="Fetch Details", on_click=fetch_details),
            ],
            alignment=ft.MainAxisAlignment.CENTER,
        )
    )


ft.app(main, view=ft.AppView.WEB_BROWSER)