import flet as ft

def main(page: ft.page):
    page.title ="Petőfi Sándor verse"
    page.bgcolor=ft.colors.AMBER_100
    page.font_family='Arima Madurai, cursive;'
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.add(
        ft.Text(value="Rószabokor a domboldalon", text_align=ft.TextAlign.CENTER, size=19, width=500)
    )
    page.add(
        ft.Text(value="---2024.02.12---",  text_align=ft.TextAlign.CENTER, italic=True, size=9, width=500)
    )
    page.add(        
        ft.Text(
     value="""Rózsabokor a domboldalon,
Borúlj a vállamra, angyalom,
Súgjad a fülembe, hogy szeretsz,
Hejh, milyen jól esik nekem ez!""", color="red", text_align=ft.TextAlign.CENTER,italic=True, size=30, width=500)
    )
    page.add(
        ft.Text(value="Vers folytatása >>>", size=20, text_align=ft.TextAlign.RIGHT, width=500)
    )
    
    page.update()

if __name__ =='__main__':
    ft.app(target=main)
