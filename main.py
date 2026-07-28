from core.ui import banner, clear, menu_box

from core.startup import boot_sequence

from modules.ai import ai_menu
from modules.system import system_menu
from modules.preferences import preferences_menu
from modules.network import network_menu
from modules.security import security_menu
from modules.files import files_menu
from modules.tools import tools_menu
from modules.diagnostic import diagnostic_menu
from modules.packages import packages_menu
from modules.status import status_menu



def check_navigation(option):

    if option == "00":
        return "home"


    if option.lower() in [
        "s",
        "salir"
    ]:

        return "exit"


    return None



def main():

    boot_sequence()


    while True:


        clear()

        banner()



        menu = """
1. Conciencia
2. Gestor de paquetes
3. Sistema
4. Red
5. Seguridad
6. Archivos
7. Herramientas
8. Diagnóstico
9. Preferencias
10. Estado de ULTRON

00. Inicio
S. Salir
"""


        menu_box(
            menu,
            "ULTRON PANEL"
        )


        option = input(
            "\nSeleccione una opción: "
        )



        nav = check_navigation(
            option
        )



        if nav == "exit":

            clear()

            print("""
ULTRON:

Cerrando sistema...
""")

            break



        if nav == "home":

            continue



        result = None



        if option == "1":

            result = ai_menu()



        elif option == "2":

            result = packages_menu()



        elif option == "3":

            result = system_menu()



        elif option == "4":

            result = network_menu()



        elif option == "5":

            result = security_menu()



        elif option == "6":

            result = files_menu()



        elif option == "7":

            result = tools_menu()



        elif option == "8":

            result = diagnostic_menu()



        elif option == "9":

            result = preferences_menu()



        elif option == "10":

            result = status_menu()



        else:

            print("""
ULTRON:

Opción no válida.
""")


            input(
                "\nENTER para continuar"
            )



        if result == "home":

            continue



if __name__ == "__main__":

    main()
