from flask import Flask
from flask import request
import json
import keyboard

app = Flask(__name__)
ip_addr="localhost"

@app.route("/hate5grip", methods=["POST"])
def cut():
    angle = request.args.get("angle")
    print("Angle:", angle)
    keyboard.press_and_release(angle)
    return json.dumps({})

if __name__ == '__main__':
    app.run(host=ip_addr, port="5000")