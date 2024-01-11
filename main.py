from flask import Flask, render_template, Response
from cam import EngageWise

app = Flask(__name__)
ew = EngageWise()

@app.route("/")
def index():
    return render_template("index.html", blink=ew.blink_count, yawn=ew.yawn_count, state=ew.state, d=int(ew.d))

def gen(engage_wise):
    while True:
        frame = engage_wise.get_frame()
        yield (b'--frame\r\n'b'Content-Type: image/jpeg\r\n\r\n'+ frame + b'\r\n\r\n')

@app.route("/video_feed")
def video_feed():
    return Response(gen(ew), mimetype='multipart/x-mixed-replace; boundary=frame')

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000, debug=True)