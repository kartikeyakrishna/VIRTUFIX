   import subprocess
   import webbrowser
   import os
   import sys
   import time
   
   project_dir = r"D:\Version Control\testing\CURSOR PROJECT\training_mgmt"
   os.chdir(project_dir)
   
   # Start Django server in a new terminal window
   subprocess.Popen(['start', 'cmd', '/k', 'python manage.py runserver'], shell=True)
   
   # Wait a moment to let the server start
   time.sleep(2)
   webbrowser.open("http://127.0.0.1:8000/")