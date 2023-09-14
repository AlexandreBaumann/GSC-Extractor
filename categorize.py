import pandas as pd


def add_category():
    # Charger les données à partir des fichiers CSV
    search_data = pd.read_csv('gscData.csv')
    # contient les colonnes 'Remplacer' et 'url'
    categories_data = pd.read_csv('url_replace.csv')

    # Créez un dictionnaire pour la correspondance des URLs à remplacer
    replace_map = dict(
        zip(categories_data['Remplacer'], categories_data['url']))

    # Remplacer les URLs dans search_data selon le dictionnaire
    search_data['Page'] = search_data['Page'].replace(replace_map)

    # Fusionner les deux DataFrames pour catégoriser
    merged_data = pd.merge(search_data, categories_data,
                           left_on='Page', right_on='url', how='left')

    # Supprimer les colonnes 'Remplacer' et 'url' car elles ne sont plus nécessaires
    merged_data.drop(['Remplacer', 'url'], axis=1, inplace=True)

    # Réécrire le fichier avec la nouvelle colonne 'category'
    merged_data.to_csv('categorized_data.csv', index=False)


# Ajouter les catégories aux données de la Search Console
add_category()
