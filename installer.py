import colorama
import typer
import inquirer
import os
import json
colorama.init( autoreset=True )
path = os.path.dirname(os.path.realpath(__file__))

def install_dependencies(dependencies):
  os.system(f"sudo apt-get install {dependencies}")

def install(app, app_name):
  if app["dependicies"] != "":
    print(f"{colorama.Fore.BLUE}[INFO] {colorama.Fore.GREEN}Installing dependencies...")
    install_dependencies(app["dependicies"])
    print(f"{colorama.Fore.BLUE}[INFO] {colorama.Fore.GREEN}Dependencies installed!\n")
  
  print(f"{colorama.Fore.BLUE}[INFO] {colorama.Fore.GREEN}Installing app...\n")
  # run the app_name.sh file
  path = os.path.dirname(os.path.realpath(__file__))
  os.system(f"bash {path}/apps/{app_name}/{app_name}.sh")
  
  print(f"\n{colorama.Fore.BLUE}[INFO] {colorama.Fore.GREEN}App installed!")
  print(f"{colorama.Fore.BLUE}Notes: {colorama.Fore.RESET}{app['notes']}")

apps = os.listdir("./apps")

# make a function that asks the user for a app to install
app_name = inquirer.list_input("Which app do you want to install?", choices=apps)
with open("./apps/" + app_name + '/' + app_name + ".json", "r") as f:
  app = json.load(f)
  
print(colorama.Fore.BLUE + app_name + colorama.Fore.RESET + ":")
print(f" {colorama.Fore.GREEN}Description:", app["description"])
print(f" {colorama.Fore.GREEN}Homepage:", app["homepage"])
if app["dependicies"] != "":
  print(f" {colorama.Fore.GREEN}Dependicies:", app["dependicies"])

if typer.confirm("Do you want to install this app?"):
  install(app, app_name)
