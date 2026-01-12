from arduino.app_utils import App
from arduino.app_bricks.web_ui import WebUI

# Initialisation du serveur WebUI
ui = WebUI()

print("WebUI started", flush=True)

# Lancement de l'application App Lab
App.run()
