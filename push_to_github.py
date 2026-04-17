import subprocess
import time

while True:
   try:
       subprocess.run(["git", "add", "data/garden_current.json"])
       subprocess.run(["git", "commit", "-m", "Autoupdate sensor data"])
       subprocess.run(["git", "push"])
       print("Pushed to Github")

   except Exception as e:
       print("Error:", e)

   time.sleep(30)
