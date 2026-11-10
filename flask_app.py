from flask import Flask, render_template, request, jsonify, redirect, url_for, abort
from datetime import datetime

app = Flask(__name__)

@app.route("/")
def accueil():
    return render_template("index.html", page="Accueil")

@app.route("/bonjour")
def bonjour():
    return render_template("index.html", page="Bonjour", message="Bonjour et bienvenue sur mon site !")

@app.route("/a-propos")
def apropos():
    return render_template("index.html", page="À propos")

@app.route("/saluer")
def saluer():
    nom = request.args.get("nom", "visiteur").strip()[:60]
    return render_template("index.html", page="Salutation", message=f"Bonjour {nom} !")

@app.route("/contact", methods=["GET", "POST"])
def contact():
    message = None
    if request.method == "POST":
        nom = request.form.get("nom", "visiteur").strip()[:60]
        texte = request.form.get("message", "").strip()[:500]
        message = f"Merci {nom} ! Votre message a été reçu pour cette démonstration : {texte}"
    return render_template("index.html", page="Formulaire", message=message)

@app.route("/interdit")
def interdit():
    abort(403)

@app.route("/introuvable")
def introuvable():
    abort(404)

@app.route("/redirection")
def redirection():
    return redirect(url_for("accueil"))

@app.route("/infos")
def infos():
    headers = {"User-Agent": request.headers.get("User-Agent", "Inconnu"),
               "Accept-Language": request.headers.get("Accept-Language", "Inconnu"),
               "Méthode HTTP": request.method,
               "Adresse IP (proxy éventuel)": request.remote_addr}
    return render_template("index.html", page="Informations HTTP", headers=headers)

@app.route("/api/bonjour")
def api_bonjour():
    return jsonify(message="Bonjour depuis l'API Flask !", date=datetime.now().isoformat(timespec="seconds"), succes=True)

@app.errorhandler(403)
def error403(error):
    return render_template("index.html", page="Erreur 403", message="403 : accès interdit."), 403

@app.errorhandler(404)
def error404(error):
    return render_template("index.html", page="Erreur 404", message="404 : cette page n'existe pas."), 404

if __name__ == "__main__":
    app.run(debug=True)
