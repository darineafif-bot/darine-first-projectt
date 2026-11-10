# Séquence 4 — Réponses à intégrer dans CARNET.md

> À fusionner avec le CARNET.md existant. Les observations dépendant du navigateur ou des logs doivent être vérifiées sur le site publié avant remise.

## Exercice 2 — URL et routes
1. Dans `https://www.google.com/maps`, le domaine est `www.google.com` et le chemin `/maps`.
2. « Not Found » indique que le serveur n'a pas trouvé la ressource demandée : il répond généralement avec le statut 404. Le navigateur affiche cette réponse.
3. Deux fonctions de routes Flask portant le même nom créent normalement le même endpoint, ce qui provoque une `AssertionError` lors de l'enregistrement de la seconde route.

## Exercice 3 — HTML
1. Le serveur envoie du texte HTML ; le navigateur interprète les balises pour construire la page affichée.
2. `<h1>` : titre principal ; `<p>` : paragraphe ; `<ul>` : liste non ordonnée ; `<li>` : élément de liste.
3. Le navigateur télécharge l'image directement depuis le serveur indiqué par son URL externe.

## Exercice 4 — Templates
1. Séparer Python et HTML rend le code plus lisible et permet à un développeur et un graphiste de travailler plus facilement sur leurs parties respectives.
2. Les variables `{{ prenom }}` sont remplacées par Jinja2 **sur le serveur**, avant l'envoi au navigateur. Le code source reçu par le navigateur contient le prénom final, pas la variable.

## Exercice 5 — CSS et liens
1. HTML décrit la structure et le contenu ; CSS gère l'apparence (couleurs, tailles, espaces, disposition).
2. **À vérifier dans F12 → Réseau** : au minimum le document HTML et la feuille CSS ; une image externe et d'autres ressources peuvent déclencher des requêtes supplémentaires.
3. Le navigateur peut conserver l'ancienne feuille CSS en cache. Ctrl+F5 force généralement un rechargement plus complet.

## Exercice 6 — Réseau HTTP
1. HTTP signifie HyperText Transfer Protocol. Le navigateur envoie la requête et le serveur envoie la réponse.
2. **À relever dans F12 → Réseau** : nombre exact et noms des requêtes de `/presentation` (document HTML, CSS, logo Python, éventuelle favicon).
3. 200 signifie succès ; 404 signifie ressource introuvable. Une favicon inexistante peut générer 404 si le navigateur la demande.
4. Les changements faits dans l'onglet Éléments modifient seulement le DOM local du navigateur, pas les fichiers du serveur ; les autres visiteurs ne les voient pas.

## Exercice 7 — Paramètres d'URL
1. Dans `https://www.youtube.com/results?search_query=chat`, le paramètre est `search_query` et sa valeur `chat`.
2. `int('bonjour')` déclenche une `ValueError`. Il faut valider les entrées et gérer l'erreur, par exemple avec `try/except` et une réponse 400.
3. Afficher directement une entrée utilisateur comme HTML peut permettre l'injection de balises ou de scripts (XSS). Un template Jinja2 avec échappement automatique limite ce risque.

## Exercice 8 — Formulaires
1. En GET, les données sont visibles dans la barre d'adresse ; en POST, elles sont dans le corps de la requête.
2. GET convient à une recherche partageable ; POST convient à une connexion car le mot de passe n'apparaît pas dans l'URL. Il faut aussi HTTPS et des mesures de sécurité côté serveur.
3. Non, les données POST ne sont pas « secrètes » : elles restent visibles dans les outils réseau du navigateur et accessibles au serveur. HTTPS les protège pendant le transport.

## Exercice 9 — Codes HTTP
1. Les 4xx indiquent une erreur liée à la demande (ex. ressource inexistante, accès refusé) ; les 5xx indiquent une erreur du serveur. La cause réelle n'est pas toujours exclusivement imputable à un seul acteur.
2. Le serveur répond par un code 3xx et un en-tête `Location` ; le **navigateur** effectue ensuite la deuxième requête vers la nouvelle adresse.
3. Exemple : après une connexion réussie, un site peut rediriger vers le tableau de bord.

**Défi :** le code 418 « I'm a teapot » vient d'une plaisanterie du protocole HTCPCP et désigne une théière refusant de préparer du café.

## Exercice 10 — En-têtes et journaux
1. Le serveur peut recevoir l'adresse IP apparente, le User-Agent et les langues préférées (Accept-Language).
2. `Accept-Language` aide un site multilingue à proposer la langue préférée du visiteur.
3. **À relever dans PythonAnywhere → Web → Access log** : une vraie requête au statut 404 et le chemin exact demandé.
4. La navigation privée réduit surtout la conservation locale de l'historique et des cookies entre sessions ; elle ne rend pas invisible au serveur ni au fournisseur d'accès.

## Exercice 11 — API et JSON
1. HTML sert surtout à décrire une page à afficher ; JSON sert à transmettre des données structurées entre programmes.
2. Le serveur exécute Python/Flask et produit le JSON de `/api/heure` ; le navigateur exécute JavaScript, appelle l'API avec `fetch` et met à jour la page.
3. Exemple : une application météo utilise une API pour échanger une localisation et recevoir des prévisions, températures et conditions météo.

## Bilan
Quand on saisit une adresse, le navigateur envoie une requête HTTP au serveur, qui répond avec des ressources ou des données ; le navigateur les interprète pour afficher et actualiser la page.
