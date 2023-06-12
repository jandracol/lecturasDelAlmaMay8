import os

from flask import Flask, render_template
import random
import datetime
import requests

# from post import Post
# import requests
#
# posts = requests.get("https://api.npoint.io/5abcca6f4e39b4955965").json()
# post_objects = []
# for post in posts:
#     post_obj = Post(post["id"], post["title"], post["subtitle"], post["body"])
#     post_objects.append(post_obj)

app = Flask(__name__, template_folder='templates', static_folder='static')
env_config = os.getenv("PROD_APP_SETTINGS", "config.DevelopmentConfig")
app.config.from_object(env_config)

@app.route("/")
def home():
    # return render_template("index.html", all_posts=post_objects)

    current_year = datetime.datetime.now().year
    return render_template("index.html", year = current_year)

@app.route("/cartas")
def get_cartas():
    random_card = random.randint(1, 4)
    cartas_url = "https://api.npoint.io/18ec196cc2d1db5c6398"
    response = requests.get(cartas_url)
    all_cards = response.json()
    desc_card = all_cards[random_card - 1]["desc"]
    htm_desc_card = desc_card.split("<")
    one_card = all_cards[random_card - 1]["meditation"]
    htm_card = one_card.split("<")
    afir_card = all_cards[random_card - 1]["pic_01"]
    htm_afir_card = afir_card.split("<")
    return render_template("cartas.html", cartas=all_cards, ran_c=random_card, htm_card=htm_card, htm_desc_card=htm_desc_card, htm_afir_card=htm_afir_card)


# @app.route("/post/<int:index>")
# def show_post(index):
#     requested_post = None
#     for blog_post in post_objects:
#         if blog_post.id == index:
#             requested_post = blog_post
#     return render_template("post.html", post=requested_post)


if __name__ == "__main__":
    app.run(debug=True)


