from flask import Flask, render_template
from project import Project
import requests
import random

app = Flask(__name__)

# ------------------ PROJECTS PARTS COLLECTION FROM JSON -------------#
data_url = "https://api.npoint.io/cc03a8b5a864b248543d"
project_response = requests.get(data_url)
project_data = project_response.json()

project_objects = []
for project in project_data:
    project_object = Project(id = project["project_id"], title=project["title"], technologies=project["technologies"], description_intro=project["description_intro"], description_code=project["description_code"],description_code2=project["description_code2"],image_code=project["image_code"])
    project_objects.append(project_object)


@app.route("/")
def main_page():
    return render_template("homepage.html")

@app.route("/cv")
def cv_page():
    return render_template("cv.html")

@app.route("/portfolio")
def porfolio_main():
    return render_template("porfolio_main_page.html")

@app.route("/portfolio/desktop")
def desktop_apps():
    return render_template("desktop_apps.html")

@app.route("/portfolio/web")
def web_apps():
    return render_template("web_apps.html")

@app.route("/portfolio/ai")
def ai_apps():
    return render_template("machine_learning_tools.html")

@app.route("/code_repo/<int:project_id>")
def code_show(project_id):
    selected_project = None
    for project in project_objects:
        if project.id == project_id:
            selected_project = project
    return render_template("show_project_description.html", project = selected_project)

if __name__ == "__main__":
    app.run(debug=True)