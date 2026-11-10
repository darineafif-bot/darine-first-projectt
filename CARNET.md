# 📒 Mon carnet de bord

**Nom :** 
AFIF
**Prénom :** 
Darine
**Adresse de mon site :** https://darine2007.pythonanywhere.com

> Modifiez ce fichier directement sur GitHub (icône crayon ✏️) pour répondre aux questions de chaque exercice.
> Écrivez avec vos propres mots : une réponse courte et juste vaut mieux qu'un long copier-coller ! 🙂

---

## 🟢 Exercice 1 — Mon premier déploiement

1. Où se trouve physiquement le code qui fabrique votre page : sur votre ordinateur, sur GitHub ou sur PythonAnywhere ?

   > _Ma réponse : Le code se trouve sur PythonAnywhere, où il est exécuté pour afficher mon site. Une copie est également stockée sur GitHub.

2. Pourquoi votre voisin(e) peut-il voir votre site, alors que vous n'avez rien installé sur son ordinateur ?

   > _Ma réponse :_ Parce que mon site est hébergé sur un serveur accessible par Internet. Il suffit d’avoir un navigateur et l’adresse URL pour le consulter.

---

## 🟢 Exercice 2 — Les URL et les routes

1. Dans l'URL `https://www.google.com/maps`, quel est le nom de domaine ? Quel est le chemin ?

   > _Ma réponse :_   Le nom de domaine est www.google.com et le chemin est /maps. Le protocole utilisé est HTTPS.

2. Que veut dire le message *Not Found* ? Qui l'a envoyé : votre navigateur ou le serveur ?

   > _Ma réponse :_ Le message « Not Found » signifie que le serveur n’a pas trouvé la page demandée. C’est le serveur qui envoie cette réponse au navigateur, généralement avec le code HTTP 404.

3. Que se passe-t-il si deux fonctions portent le même nom dans `flask_app.py` ? (Indice : essayez, puis lisez l'Error log.)

   > _Ma réponse :_ Si deux fonctions utilisées comme routes Flask portent le même nom, Flask peut provoquer une erreur AssertionError, car les deux routes utilisent le même nom de point d’accès (endpoint). L’application risque alors de ne pas démarrer correctement.

---

## 🔵 Exercice 3 — Le langage HTML

1. Quelle est la différence entre ce que le serveur **envoie** et ce que le navigateur **affiche** ?

   > _Ma réponse :_ Le serveur envoie du code HTML sous forme de texte.

Le navigateur interprète ce code et affiche une page structurée contenant des titres, des paragraphes, des listes et des images.

2. À quoi servent les balises `<h1>`, `<p>`, `<ul>` et `<li>` ?

   > _Ma réponse :_ <h1> : définit le titre principal d’une page.
<p> : définit un paragraphe.
<ul> : crée une liste non ordonnée.
<li> : représente un élément d’une liste.

3. Pourquoi l'image s'affiche-t-elle alors qu'elle n'est pas sur votre serveur ?

   > _Ma réponse :_ L’image s’affiche parce que son attribut src contient l’adresse d’une ressource hébergée sur un serveur externe.

Le navigateur télécharge directement cette image depuis son adresse URL et l’intègre dans la page.

---

## 🔵 Exercice 4 — Les templates

1. Pourquoi est-ce une bonne idée de séparer le code Python et le HTML ? (Pensez à une équipe avec un développeur et un graphiste.)

   > _Ma réponse :_ Séparer Python et HTML permet de mieux organiser le projet.

Python gère la logique de l’application, tandis que HTML définit la structure et la présentation des pages.

Cette séparation facilite la maintenance et permet à plusieurs personnes de travailler sur le même projet.


2. Les `{{ prenom }}` sont-ils remplacés par le serveur ou par le navigateur ? Comment l'avez-vous vérifié ?

   > _Ma réponse :_ Les variables sont remplacées par le serveur grâce au moteur de templates Jinja2.

Le serveur insère les valeurs dans le HTML avant d’envoyer la page au navigateur.

On peut le vérifier en affichant le code source avec Ctrl + U : les variables Jinja2 ont disparu et ont été remplacées par leurs valeurs.

---

## 🔵 Exercice 5 — Le CSS et les liens

1. Quelle est la différence de rôle entre le HTML et le CSS ?

   > _Ma réponse :_  Le CSS définit son apparence : couleurs, polices, marges, espacements et disposition des éléments.

Le HTML représente donc la structure du site, tandis que le CSS permet de le rendre visuellement agréable.

2. Pour afficher votre page `/presentation`, combien de fichiers le navigateur doit-il télécharger ? (Vous pourrez le vérifier à l'exercice suivant !)

   > _Ma réponse :_ Dans la version simple de l’exercice, le navigateur doit récupérer au minimum deux ressources :

Le document HTML.
Le fichier CSS.
Si la page contient une image externe, le navigateur doit également récupérer cette image.

Le nombre exact de requêtes dépend des autres ressources utilisées et du cache du navigateur.

3. Pourquoi faut-il parfois faire **Ctrl + F5** pour voir les changements de CSS ?

   > _Ma réponse :_ Le navigateur conserve parfois une ancienne version du fichier CSS dans sa mémoire cache.

Le raccourci Ctrl + F5 force généralement un rechargement plus complet de la page et de ses ressources.

Cela permet de récupérer la nouvelle version du CSS.

---

## 🟣 Exercice 6 — Espionner le navigateur

1. Que signifie HTTP ? Qui envoie la **requête** et qui envoie la **réponse** ?

   > _Ma réponse :_ HTTP signifie HyperText Transfer Protocol.

C’est le protocole qui permet la communication entre un navigateur et un serveur Web.

Le navigateur envoie une requête HTTP au serveur.

Le serveur traite cette demande et renvoie une réponse HTTP.

2. Combien de requêtes votre page `/presentation` a-t-elle déclenchées ? Lesquelles ?

   > _Ma réponse :_ Dans la version simple de l’exercice, les principales requêtes sont :

Une requête GET pour récupérer /presentation.
Une requête GET pour récupérer /static/style.css.
Une requête GET pour récupérer l’image externe, si elle est présente.
Le navigateur peut également demander /favicon.ico.

Le nombre exact doit être vérifié dans l’onglet Réseau des outils de développement.

3. Que signifie le code `200` ? Et le code `404` de la favicon ?

   > _Ma réponse :_ Le code HTTP 200 signifie que la requête a été traitée avec succès.

Le code HTTP 404 signifie que la ressource demandée est introuvable.

Si le navigateur demande /favicon.ico et reçoit une erreur 404, cela signifie que le serveur n’a pas trouvé l’icône du site.

4. Pourquoi les modifications faites dans l'onglet Éléments ne sont-elles pas visibles par les autres visiteurs ?

   > _Ma réponse :_ Les modifications effectuées dans l’onglet Éléments changent uniquement la représentation locale de la page dans le navigateur.

Elles ne modifient pas les fichiers du serveur.

Les autres visiteurs reçoivent donc toujours la version originale du site.

---

## 🟣 Exercice 7 — Envoyer des informations dans l'URL

1. Dans l'URL `https://www.youtube.com/results?search_query=chat`, quel est le nom du paramètre ? Quelle est sa valeur ?

   > _Ma réponse :_ Le nom du paramètre est search_query.

Sa valeur est chat.

Ce paramètre permet de transmettre au serveur le texte recherché.

2. Pourquoi le serveur plante-t-il avec `a=bonjour` ? Que faudrait-il faire pour l'éviter ?

   > _Ma réponse :_ Le serveur rencontre une erreur parce que le programme essaie de convertir le texte « bonjour » en nombre entier avec la fonction int().

Cette conversion est impossible et provoque une exception ValueError.

Pour éviter ce problème, il faut vérifier les données reçues et gérer les erreurs de conversion.

3. Pourquoi est-il dangereux d'afficher **tel quel** ce que l'utilisateur envoie ?

   > _Ma réponse :_ Il est dangereux d’afficher directement les données d’un utilisateur, car elles peuvent contenir du code HTML ou JavaScript malveillant.

Cela peut entraîner une faille de sécurité appelée XSS (Cross-Site Scripting).

---

## 🟣 Exercice 8 — Les formulaires

1. Quelle est la différence visible entre GET et POST ?

   > _Ma réponse :_ Avec la méthode GET, les données du formulaire apparaissent dans l’URL après le symbole ?.

Avec la méthode POST, les données sont envoyées dans le corps de la requête HTTP et n’apparaissent pas directement dans l’URL.

2. Pour un formulaire de **recherche**, quelle méthode choisiriez-vous ? Et pour un formulaire de **connexion avec mot de passe** ? Pourquoi ?

   > _Ma réponse :_ Pour un formulaire de recherche, je choisirais GET, car les paramètres peuvent être conservés dans l’URL et partagés facilement.

Pour un formulaire de connexion avec un mot de passe, je choisirais POST, car les données ne sont pas placées directement dans l’URL.

Il faut également utiliser HTTPS pour protéger leur transmission.

3. Les données envoyées en POST sont-elles vraiment « secrètes » ? (Pensez à ce que vous avez vu dans l'onglet Réseau.)

   > _Ma réponse :_ Non, les données envoyées avec POST ne sont pas automatiquement secrètes.

Elles ne sont pas visibles dans l’URL, mais elles restent accessibles dans les outils de développement du navigateur et peuvent être traitées ou enregistrées par le serveur.



---

## 🔴 Exercice 9 — Les codes de statut

1. Quelle est la différence entre une erreur `4xx` et une erreur `5xx` ? Qui est « fautif » dans chaque cas ?

   > _Ma réponse :_ Les codes 4xx indiquent qu’une requête ne peut pas être satisfaite, généralement en raison d’un problème lié à la demande ou aux droits d’accès du client.

Par exemple, 404 signifie qu’une ressource est introuvable.

Les codes 5xx indiquent que le serveur a rencontré un problème lors du traitement d’une requête. 

2. Comment fonctionne une redirection ? Qui fait la deuxième requête : le serveur ou le navigateur ?

   > _Ma réponse :_ Lorsqu’un serveur souhaite rediriger un utilisateur, il renvoie une réponse HTTP contenant un code de redirection, comme 302, ainsi qu’un en-tête Location.

Cet en-tête indique la nouvelle adresse.

Le navigateur lit cette information et envoie lui-même une nouvelle requête vers cette adresse.

3. Donnez un exemple de situation où un vrai site utilise une redirection.

   > _Ma réponse :_ Un site peut utiliser une redirection lorsqu’un utilisateur essaie d’accéder à une page réservée aux personnes connectées.

Il est alors redirigé vers une page de connexion.


---

## 🔴 Exercice 10 — Ce que le serveur sait de vous

1. Citez trois informations que le serveur connaît sur vous, sans que vous ayez rien rempli.

   > _Ma réponse :_ Le serveur peut notamment connaître :

L’adresse IP utilisée pour la connexion.
Le navigateur et certaines informations sur le système d’exploitation.
Les langues préférées transmises par le navigateur.

2. À quoi peut servir l'en-tête `Accept-Language` pour un site comme Wikipédia ?

   > _Ma réponse :_ L’en-tête Accept-Language indique les préférences linguistiques du navigateur.

Un site comme Wikipédia peut utiliser cette information pour proposer une langue adaptée à l’utilisateur.

Par exemple, un navigateur configuré en français peut recevoir une suggestion d’affichage en français.

3. Dans l'Access log, retrouvez une requête qui a reçu un code `404`. Quelle page était demandée ?

   > _Ma réponse :_ Cette réponse doit être complétée à partir du véritable journal d’accès de PythonAnywhere.

Page demandée : [à relever dans l’Access log]

Code HTTP observé : 404.

4. Après cet exercice, que pensez-vous de la notion de « navigation anonyme » ?

   > _Ma réponse :_ La navigation privée protège surtout la confidentialité locale, mais ne garantit pas l’anonymat sur le réseau.

---

## 🔴 Exercice 11 — Le Web des machines : API et JSON

1. Quelle est la différence entre une page HTML et une réponse JSON ? À qui chacune est-elle destinée ?

   > _Ma réponse :_ Une page HTML contient des éléments permettant au navigateur de construire une interface visuelle destinée principalement aux utilisateurs humains.

Une réponse JSON contient des données structurées, généralement sous forme de paires clé-valeur.

Elle est principalement destinée à être interprétée par des programmes ou des applications.

2. Dans la page `/horloge`, quel code s'exécute sur le **serveur** et quel code s'exécute dans le **navigateur** ?

   > _Ma réponse :_ Le code Python Flask s’exécute sur le serveur.

Il récupère l’heure actuelle et la renvoie au format JSON grâce à une API.

Le code JavaScript s’exécute dans le navigateur.

3. Citez une application de votre téléphone qui, selon vous, utilise une API. Quelles données échange-t-elle ?

   > _Ma réponse :_ Une application météo utilise une API pour récupérer des informations météorologiques.

---

## 🏁 Pour conclure

En quelques phrases, expliquez à un ami ce qui se passe entre le moment où il tape une adresse dans son navigateur et celui où la page s'affiche :

> _Ma réponse :_ 
