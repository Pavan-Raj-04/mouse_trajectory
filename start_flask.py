import subprocess
import webbrowser
import time

# Start the Flask server in a subprocess
flask_process = subprocess.Popen(["python", "app.py"])

# Give Flask some time to start
time.sleep(3)

# Automatically open the browser to the Flask-hosted HTML page
webbrowser.open("http://127.0.0.1:5000")

# Keep the Python script running to keep the Flask server alive
try:
    flask_process.wait()
except KeyboardInterrupt:
    flask_process.terminate()
