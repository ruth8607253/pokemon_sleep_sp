from flask import Flask, render_template, request
import os
import sqlite3
import urllib.parse
import urllib
import random

app = Flask(__name__)
app.config['SEND_FILE_MAX_AGE_DEFAULT'] = 0  # 禁用瀏覽器緩存

@app.context_processor
def my_context_processor():
    search_pokemon = None
    if request.method == "POST":
        search_condition = request.form["search_condition"]
        search_pokemon = None
        if search_condition:
            conn = sqlite3.connect("../pokemon_database.db")
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM pokemon WHERE img_num=? OR name=?", (search_condition, search_condition))
            data = cursor.fetchone()
            if data:
                search_pokemon = data
            conn.close()
    return {"search_pokemon": search_pokemon, "urlparse": urllib.parse, "urllib": urllib}

def my_quote_function(string):
    return string.replace(" ", "%20")

@app.route("/", methods=["GET", "POST"])
def index(search_pokemon=None):
    # 如果是 POST 方法，則處理搜尋
    if request.method == "POST":
        search_condition = request.form["search_condition"]
        if search_condition:
            conn = sqlite3.connect("../pokemon_database.db")
            cursor = conn.cursor()
            cursor.execute("SELECT img_num,name,expertise,help_fruit,help_ingredient_1,skill_main FROM pokemon WHERE img_num=? OR name=?", (search_condition, search_condition))
            data = cursor.fetchone()
            if data:
                search_pokemon = data
            conn.close()
        else:
            return redirect("/random")
    return render_template("pokemon.html", search_pokemon=search_pokemon)

@app.route("/r", methods=["POST"])
def r():
    conn = sqlite3.connect("../pokemon_database.db")
    cursor = conn.cursor()

    cursor.execute("SELECT img_num,name,expertise,help_fruit,help_ingredient_1,skill_main FROM pokemon ORDER BY RANDOM() LIMIT 1")
    random_pokemon = cursor.fetchone()
    conn.close()

    return render_template("pokemon.html", search_pokemon=random_pokemon)

@app.template_filter('random_image')
def random_image(arg):
    image_dir = os.path.join(app.static_folder, 'img/display/')
    images = [os.path.join(image_dir, f) for f in os.listdir(image_dir) if f.endswith(('.jpg', '.jpeg', '.png'))]
    random_image = random.choice(images)
    print(random_image)
    return random_image  

if __name__ == "__main__":
    app.run(debug=True)