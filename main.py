import flet as ft
import csv
import os

def main(page: ft.Page):
    page.title = "Flet counter example"
    page.auto_scroll = True
    page.theme_mode = ft.ThemeMode.LIGHT
    page.vertical_alignment = ft.MainAxisAlignment.CENTER

    txt_number = ft.TextField(value="Enter Employee ID", text_align=ft.TextAlign.RIGHT, width=100)
    emp_details = ft.TextField(value="Voting Details", text_align=ft.TextAlign.RIGHT, width=200, multiline=True,min_lines=5)

    def minus_click(e):
        txt_number.value = str(int(txt_number.value) - 1)
        page.update()

    def plus_click(e):
        txt_number.value = str(int(txt_number.value) + 1)
        page.update()
    
    def fetch_details(e):
        project = os.path.dirname(os.path.abspath(__file__))
        print(project)
        path = os.path.join(project, "records.csv")
        print(path)
        res = 'Not Found'
        with open(path, mode='r') as file:
            csvFile = csv.reader(file)
            for lines in csvFile:
                if lines[2] == '3316245':
                    res = lines

        emp_details.value = res
        page.update()

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
        ),
    )


ft.app(main, view=ft.AppView.WEB_BROWSER)