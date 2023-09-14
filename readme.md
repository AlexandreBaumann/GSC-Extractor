////////////////
Configuration API Google
////////////////

Avant tout, vous devez configurer vos comptes Google pour créer une API qui permettra l'extraction.

Je vous ai fait un tutoriel dans la première partie de cet article :

https://www.uniteinnovation.com/seo/outils/google-search-console/tuto-export-javascript-php-python/

///////////////////
Tutoriel pour le GSC-Extractor
//////////////////

Maintenant que votre Search Console est configurée, on va pouvoir extraire les données s'y trouvant, mais pas seulement. En effet, nous voulons retravailler ces données de plusieurs façons:

- Extraire les données par semaine pour pouvoir visualiser l'évolution

- Consolider les données entre différentes URL, par exemple s'il y a eu une redirection (optionnel)

- Créer des catégories de pages (optionnel)

Il se fait en deux étapes: l'extraction, avec weekExtractor.py, puis le retraitement, avec categorize.py.

////////////////
Extraction
////////////////

- Télécharger le programme

- Installer Python 3 si ce n'est pas déjà fait.

- Installer les modules nécessaires : "pip install pandas google-auth google-auth-oauthlib"

- Créer votre tableau de correspondance (optionnel)

- Placer le fichier d'informations d'identification de l'API Google dans le dossier approprié (idéalement le même que le programme) et renseignez le chemin pour l'atteindre (ici : KEY_FILE_PATH = r'../projet-gsc-dtg.json').

- Renseigner le nom de votre propriété. Ici, il s'agit d'une propriété de domaine : SITE_URL = 'sc-domain:discoverthegreentech.com'.

- Exécuter le script avec les arguments appropriés pour la date de début et le nombre de semaines : "python weekExtractor.py --start_date YYYY-MM-DD --weeks_count N" en remplaçant bien sûr YYYY-MM-DD par la date de début et N par le nombre de semaines.

Vous obtenez search_console_data.csv.

////////////////
Retraitement - catégorisation
////////////////

- Renseigner le chemin pour la table de correspondance/remplacement et ce que vous avez extrait de la Google Search Console. (ici search_data = pd.read_csv('search_console_data.csv') et categories_data = pd.read_csv('url_replace.csv') ).

- Exécuter categorize.py.

C'est fait, vous avez récupéré votre fichier "categorized_data.csv".

Notez que créer des catégories de pages est souvent très utile. Par exemple, dans Discover The Greentech, j'ai des pages "dossiers" (ex: /hydrogene/utilisations/decarboner-production-acier/ ) et des pages entreprises (ex: /boston-metal-lelectrolyse-pour-decarboner-lacier/ ). Même si elles portent sur le même sujet, leur URL n'a rien à voir. Pour visualiser les progrès de tel ou tel thème, tel ou tel bloc de pages, j'aurai besoin d'une catégorisation spécifique.
