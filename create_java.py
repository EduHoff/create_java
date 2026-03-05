import platform
import os
import re

os_name:str = platform.system()




def clear_screen() -> None:
    if os_name == "Windows":
        os.system('cls')
    else:
        os.system('clear')

'''
if os_name == "Windows":
    print("Running on Windows")
elif os_name == "Linux":
    print("Running on Linux")
elif os_name == "Darwin":
    print("Running on macOS")
else:
    print(f"Running on an unknown OS: {os_name}")
'''




# PROGRAMA PRINCIPAL

clear_screen()
java_project_name_pattern:str = r"^[a-zA-Z_$][a-zA-Z_$0-9]*$"
while(True):
    java_project_name:str = input("Digite o nome do projeto Java: ")
    if re.fullmatch(java_project_name_pattern, java_project_name):
        break
    else:
        clear_screen()
        print("Falha! Nome inválido ou não convencional para um projeto Java.")

clear_screen()
while(True):
    build_tool:str = input("1 | Vanilla \n2 | Gradle \n3 | Maven \n\n|| ")

    match build_tool:
        case '1':
            build_tool = "vanilla"
            break
        case '2':
            build_tool = "gradle"
            break
        case '3':
            build_tool = "maven"
            break
        case _:
                clear_screen()
                print("Opção inválida! Tente novamente.")

clear_screen()
while(True):
    choose:str = input("1 | Sim \n2 | Não \n\n|| ")

    match build_tool:
        case '1':
            spring_boot:bool = True
            break
        case '2':
            spring_boot:bool = False
            break
        case _:
                clear_screen()
                print("Opção inválida! Tente novamente.")
