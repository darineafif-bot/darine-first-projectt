from flask import Flask, render_template, request, redirect, abort, jsonify
from datetime import datetime
from zoneinfo import ZoneInfo

app = Flask(__name__)

@app.get('/')
def accueil():
    return render_template('accueil.html')

@app.get('/presentation')
def presentation():
    return render_template('presentation.html', prenom='Darine', nom='Afif', loisirs=['Aviation', 'Voyages', 'Boxe', 'Ingénierie'])

@app.get('/loisirs')
def loisirs():
    return render_template('loisirs.html', loisirs=['Aviation', 'Voyages', 'Boxe', 'Ingénierie'])

@app.get('/bonjour/<path:prenom>')
def bonjour(prenom):
    return render_template('bonjour.html', prenom=prenom)

@app.get('/calcul')
def calcul():
    try:
        a = int(request.args.get('a', 0))
        b = int(request.args.get('b', 0))
    except (ValueError, TypeError):
        return render_template('calcul.html', erreur='Veuillez entrer deux nombres entiers.'), 400
    op = request.args.get('op', 'plus')
    if op == 'fois':
        resultat, symbole = a * b, '×'
    elif op == 'moins':
        resultat, symbole = a - b, '−'
    elif op == 'plus':
        resultat, symbole = a + b, '+'
    else:
        return render_template('calcul.html', erreur='Opération inconnue.'), 400
    return render_template('calcul.html', a=a, b=b, resultat=resultat, symbole=symbole, op=op)

@app.get('/formulaire')
def formulaire():
    return render_template('formulaire.html')

@app.route('/salut', methods=['GET', 'POST'])
def salut():
    valeurs = request.form if request.method == 'POST' else request.args
    prenom = valeurs.get('prenom', 'inconnu')[:80]
    ville = valeurs.get('ville', 'nulle part')[:80]
    couleur = valeurs.get('couleur', 'teal')
    if couleur not in ('tomato', 'teal', 'royalblue'):
        couleur = 'teal'
    return render_template('salut.html', prenom=prenom, ville=ville, couleur=couleur, methode=request.method)

@app.get('/home')
def home():
    return redirect('/')

@app.get('/secret')
def secret():
    abort(403)

@app.errorhandler(403)
def page_interdite(error):
    return render_template('403.html'), 403

@app.errorhandler(404)
def page_introuvable(error):
    return render_template('404.html'), 404

@app.get('/moi')
def moi():
    return render_template('moi.html', ip=request.headers.get('X-Real-IP', request.remote_addr), navigateur=request.headers.get('User-Agent', ''), langues=request.headers.get('Accept-Language', ''), entetes=request.headers)

@app.get('/api/heure')
def api_heure():
    maintenant = datetime.now(ZoneInfo('Europe/Paris'))
    return jsonify({'heure': maintenant.strftime('%H:%M:%S'), 'date': maintenant.strftime('%d/%m/%Y'), 'message': 'Bonjour depuis mon API !'})

@app.get('/horloge')
def horloge():
    return render_template('horloge.html')

if __name__ == '__main__':
    app.run(debug=False)
