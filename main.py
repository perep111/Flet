import flet as ft
import time
from flet import IconButton, Page, Row, TextField, icons

def main(page: ft.Page):
    page.title = "Flet counter example"
    page.vertical_alignment = "center"

    txt_number = TextField(value="0", text_align="right", width=100)

    def minus_click(e):
        txt_number.value = str(int(txt_number.value) - 1)
        page.update()

    def plus_click(e):
        txt_number.value = str(int(txt_number.value) + 1)
        page.update()



    page.add(
    ft.Row(controls=[
        ft.TextField(label="Your name"),
        ft.ElevatedButton(text="Say my name!")
    ])
)



    page.add(
        Row(
            [
                IconButton(icons.REMOVE, on_click=minus_click),
                txt_number,
                IconButton(icons.ADD, on_click=plus_click),
            ],
            alignment="center",
        )
    )



    def add_clicked(e):
        page.add(ft.Checkbox(label=new_task.value))
        new_task.value = ""
        new_task.focus()
        new_task.update()


        

    new_task = ft.TextField(hint_text="Whats needs to be done?", width=300)
    page.add(
        ft.Row(
            [
                new_task, ft.ElevatedButton("Add", on_click=add_clicked),
                new_task, ft.ElevatedButton("Add", on_click=add_clicked)
            ]
        )
    )

ft.app(target=main)