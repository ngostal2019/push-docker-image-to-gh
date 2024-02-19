from flask import Flask
import time
app = Flask(__name__)

@app.route('/')
def hello_world():
    get_time = time.localtime()
    date_now = time.strftime('%B %d %Y')
    time_now = time.strftime('%I:%M:%S %p', get_time)
    return f'The actual time is: \"{date_now} {time_now}\"'