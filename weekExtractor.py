import datetime
import csv
from google.oauth2 import service_account
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError


def extract_gsc_data(start_date, weeks_count):
    # Remplacez ceci par le chemin vers votre fichier JSON de clés de l'API
    KEY_FILE_PATH = r'../projet-gsc-dtg.json'

    # Configurez les informations d'identification et créez un client de l'API
    credentials = service_account.Credentials.from_service_account_file(
        KEY_FILE_PATH, scopes=['https://www.googleapis.com/auth/webmasters.readonly'])
    webmasters_service = build('searchconsole', 'v1', credentials=credentials)

    # Remplacez ceci par l'URL de votre site Web (doit être vérifié dans la Google Search Console)
    SITE_URL = 'sc-domain:discoverthegreentech.com'

    # Ouvrez le fichier CSV en mode écriture
    with open('search_console_data.csv', 'w', newline='', encoding='utf-8') as csvfile:
        csv_writer = csv.writer(csvfile)
        csv_writer.writerow(
            ['Week', 'Query', 'Page', 'Clicks', 'Impressions', 'CTR', 'Position'])

        # Convertir la date de début en objet datetime
        start_date = datetime.datetime.strptime(start_date, '%Y-%m-%d')

        for week in range(weeks_count):
            # Spécifiez la plage de dates pour les données à récupérer
            end_date = (start_date + datetime.timedelta(days=7 *
                        (week+1))).strftime('%Y-%m-%d')
            start_date_week = (
                start_date + datetime.timedelta(days=7*week)).strftime('%Y-%m-%d')

            # Créez une requête pour extraire les données de la Google Search Console
            request = {
                'startDate': start_date_week,
                'endDate': end_date,
                'dimensions': ['query', 'page'],
                'rowLimit': 10000
            }

            # Exécutez la requête
            try:
                response = webmasters_service.searchanalytics().query(
                    siteUrl=SITE_URL, body=request).execute()

                if 'rows' in response:
                    for row in response['rows']:
                        query = row['keys'][0]
                        page = row['keys'][1]
                        clicks = row['clicks']
                        impressions = row['impressions']
                        ctr = row['ctr']
                        position = row['position']

                        # Écrivez les données dans le fichier CSV avec le numéro de la semaine
                        csv_writer.writerow(
                            [week+1, query, page, clicks, impressions, ctr, position])

                    print(
                        f"Les données de la Google Search Console pour la semaine {week+1} ont été écrites.")
                else:
                    print(f"Aucune donnée trouvée pour la semaine {week+1}.")

            except HttpError as error:
                print(
                    f"Une erreur s'est produite pour la semaine {week+1} : {error}")


# Pour extraire les données de la Google Search Console pour un nombre spécifique de semaines depuis une date de début spécifique
extract_gsc_data('2023-01-01', 35)
