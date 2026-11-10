# Site final — Séquence 4

Ce dossier contient `flask_app.py`, `requirements.txt`, `templates/` et `static/`.

## Déploiement
1. Conservez les fichiers `.github/workflows/` déjà présents dans votre dépôt et les secrets GitHub existants.
2. Téléversez **le contenu** de ce dossier à la racine du dépôt, pas le ZIP lui-même ni un dossier supplémentaire `darine_final`.
3. Remplacez `flask_app.py` et `requirements.txt` ; ajoutez les dossiers `templates` et `static` avec tous leurs fichiers. Les fichiers d'origine `exercices/` peuvent rester.
4. Attendez la coche verte dans GitHub Actions.
5. Dans PythonAnywhere → Web, cliquez sur **Reload**, puis ouvrez le site.
6. Si erreur 500, vérifiez que `templates/` est bien dans `/home/darine2007/mysite/` au même niveau que `flask_app.py`, puis consultez l'Error log.

## Liens de test
`/`, `/presentation`, `/loisirs`, `/bonjour/Darine`, `/calcul?a=3&b=4`, `/calcul?a=6&b=3&op=fois`, `/formulaire`, `/home`, `/secret`, `/page-inexistante`, `/moi`, `/api/heure`, `/horloge`.

## Important
Les observations réelles dans l'onglet Réseau (F12) et les Access logs doivent être effectuées sur votre site publié. Ne partagez pas de mots de passe ni de tokens.
