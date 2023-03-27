from flask import Flask, render_template
import json
import random

app = Flask(__name__)

with open("proffesion.json", "rt", encoding="utf-8-sig") as f:
        prof_list = json.loads(f.read())
        a = prof_list["professions"][random.randint(len(prof_list) - 1, len(prof_list["professions"]) - 1)]

@app.route('/member')
def index():
    with open("templates/proffesion.json", "rt", encoding="utf-8-sig") as f:
        prof_list = json.loads(f.read())
        a = prof_list["professions"][random.randint(len(prof_list) - 1, len(prof_list["professions"]) - 1)]
        return render_template('index.html', prof=a)

if __name__ == "__main__":
    app.run(debug=True)