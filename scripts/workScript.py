from flask import Flask
from picamera import PiCamera
import subprocess

app = Flask(__name__)

@app.route('/')
def index():
    cmd = "raspivid -t 0 -w 1280 -h 720 -fps 25 -g 75 -fl -o - | ffmpeg -f lavfi -i anullsrc=channel_layout=" \
          "stereo:sample_rate=44100 -i pipe:0 -c:v copy -c:a aac -strict experimental -f flv -f flv rtmp://10.0.0.36/live/1"
    subprocess.call(cmd, shell=True)
    return 'Hello world'

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')