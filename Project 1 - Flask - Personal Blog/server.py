from flask import Flask, render_template
from post import Post
import requests

app = Flask(__name__)

# ------------------ BLOG PARTS COLLECTION FROM JSON -------------#
data_url = "https://api.npoint.io/1c1a71947bab2c050e0a"
blog_response = requests.get(data_url)
blog_data = blog_response.json()

# ------------------ creation of the individual POST objects ------# 
article_objects = []
for article_data in blog_data:
    article_object = Post(id = article_data["id"], title = article_data["title"], subtitle = article_data["subtitle"], body = article_data["body"], image_text = article_data["image_text"], post_date = article_data["post_date"])
    article_objects.append(article_object)



@app.route("/")
def main_page():
    return render_template("main_page.html", all_posts = blog_data)

@app.route("/read/<int:num>")
def read_page(num):
    selected_post = None
    for article in article_objects:
        if article.id == num:
            selected_post = article
    return render_template("read_page.html", post = selected_post)



if __name__ == "__main__":
    app.run(debug=True)