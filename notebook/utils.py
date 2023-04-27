#utils.py contient des fonctions utilitaires pour le notebook

def rename_columns(df):
    """
    Renomme les colonnes du DataFrame en français.

    Args:
        df (pandas.DataFrame): Le DataFrame à renommer.

    Returns:
        pandas.DataFrame: Le DataFrame renommé.

    """
    new_column_names = {
        'symboling': 'etat_de_route',
        'CarName': 'marque_voiture',
        'fueltype': 'carburant',
        'aspiration': 'turbo',
        'doornumber': 'nombre_portes',
        'carbody': 'type_vehicule',
        'drivewheel': 'roues_motrices',
        'enginelocation': 'emplacement_moteur',
        'wheelbase': 'empattement',
        'carlength': 'longueur_voiture',
        'carwidth': 'largeur_voiture',
        'carheight': 'hauteur_voiture',
        'curbweight': 'poids_vehicule',
        'enginetype': 'type_moteur',
        'cylindernumber': 'nombre_cylindres',
        'enginesize': 'taille_moteur',
        'fuelsystem': 'systeme_carburant',
        'boreratio': 'taux_alésage',
        'stroke': 'course',
        'compressionratio': 'taux_compression',
        'horsepower': 'chevaux',
        'peakrpm': 'tour_moteur',
        'citympg': 'consommation_ville',
        'highwaympg': 'consommation_autoroute',
        'price': 'prix'
    }
    return df.rename(columns=new_column_names)

def convert_units(df):
    """
    Convertit les unités du dataframe en unités françaises.
    
    Parameters:
    -----------
    df : pandas.DataFrame
        Le dataframe contenant les données à convertir.
        
    Returns:
    --------
    pandas.DataFrame
        Le dataframe avec les unités converties.
    """
    # Convertir le poids du véhicule de lb en kg
    df['poids_vehicule'] = df['poids_vehicule'] * 0.453592
    
    # Convertir les dimensions en pouces en centimètres et arrondir à 1 décimale
    df[['empattement', 'longueur_voiture', 'largeur_voiture', 'hauteur_voiture']] *= 2.54
    df[['empattement', 'longueur_voiture', 'largeur_voiture', 'hauteur_voiture']] = df[['empattement', 'longueur_voiture', 'largeur_voiture', 'hauteur_voiture']].round(1)
    
    # Convertir la consommation de carburant de mpg en L/100km et arrondir à 2 décimales
    df[['consommation_ville', 'consommation_autoroute']] = 235.215 / df[['consommation_ville', 'consommation_autoroute']]
    df[['consommation_ville', 'consommation_autoroute']] = df[['consommation_ville', 'consommation_autoroute']].round(2)
    
    # Convertir le taux d'alésage et la course du moteur de pouces en millimètres et arrondir à 1 décimale
    df['taux_alésage'] = df['taux_alésage'] * 25.4
    df['course'] = df['course'] * 25.4
    df['taux_alésage'] = df['taux_alésage'].round(1)
    df['course'] = df['course'].round(1)
    
    return df

def split_brand_and_model(df):
    """
    Sépare la marque et le modèle de la colonne 'marque_voiture'.

    Args:
        df (pandas.DataFrame): Le dataframe à traiter.

    Returns:
        pandas.DataFrame: Le dataframe avec les colonnes 'marque' et 'modele' séparées.
    """
    # Utilise la méthode str.split() pour séparer la colonne 'marque_voiture' en deux colonnes
    # 'marque' et 'modele' en se basant sur le premier espace rencontré.
    df[['marque', 'modele']] = df['marque_voiture'].str.split(' ', n=1, expand=True)

    # Convertit la chaîne de caractères de la colonne 'marque' en majuscules et supprime les espaces
    # entre les mots pour un formatage uniforme.
    df['marque'] = df['marque'].str.upper().str.replace(' ', '')

    # Convertit la chaîne de caractères de la colonne 'modele' en majuscules et supprime les espaces
    # entre les mots pour un formatage uniforme.
    df['modele'] = df['modele'].str.upper().str.replace(' ', '')

    # Supprime la colonne originale 'marque_voiture' qui n'est plus utile.
    df = df.drop(columns=['marque_voiture'])

    return df

def translate_columns(df):
    """
    Traduit les valeurs des colonnes en français.

    Args:
        df (pandas.DataFrame): Le dataframe à traduire.

    Returns:
        pandas.DataFrame: Le dataframe avec les valeurs traduites.
    """
    # Dictionnaire de traduction
    translation_dict = {
        'gas': 'essence',
        'diesel': 'diesel',
        'std': 'standard',
        'turbo': 'turbo',
        'two': 'deux',
        'four': 'quatre',
        'convertible': 'cabriolet',
        'hatchback': 'hayon',
        'sedan': 'berline',
        'wagon': 'break',
        'hardtop': 'coupé fermé',
        'rwd': 'propulsion',
        'fwd': 'traction',
        '4wd': 'quatre_roues_motrices',
        'front': 'avant',
        'rear': 'arrière'
    }
    # Application de la traduction sur le dataframe
    return df.replace(translation_dict)

def clean_car_brands(brand):
    """Nettoie les noms de marques de voiture en les remplaçant par les noms corrects.

    Args:
        brand (str): Nom de la marque de voiture.

    Returns:
        str: Nom de la marque de voiture nettoyé.

    """
    # Dictionnaire de correspondance entre les noms de marques erronés et les noms de marques corrects
    brand_mapping = {
        "TOYOUTA": "TOYOTA",
        "MAXDA": "MAZDA",
        "VW": "VOLKSWAGEN",
        "VOKSWAGEN": "VOLKSWAGEN",
        "PORCSHCE": "PORSCHE",
        "ALFA-ROMERO": "ALFA-ROMEO"
    }

    # Si la marque de voiture est dans le dictionnaire de correspondance, on la remplace par la valeur correspondante
    if brand in brand_mapping:
        return brand_mapping[brand]
    # Sinon, on retourne la marque de voiture telle quelle
    else:
        return brand
    
def clean_car_models(model):
    """Nettoie le nom du modèle de voiture en remplaçant les valeurs mal écrites par les bonnes valeurs.

    Args:
        model (str): Le nom du modèle de voiture à nettoyer.

    Returns:
        str: Le nom du modèle de voiture nettoyé.
    """
    model_mapping = {
        "5000S(DIESEL)": "5000S DIESEL",
        "ACCORDCVCC": "ACCORD CVCC",
        "COLT(SW)": "COLT SW",
        "CORONETCUSTOM(SW)": "CORONET CUSTOM SW",
        "CIVIC(AUTO)": "CIVIC AUTO",
        "D-MAXV-CROSS": "D-MAX V-CROSS",
        "OPELISUZUDELUXE": "OPEL ISUZU DELUXE",
        "REGALSPORTCOUPE(TURBO)": "REGAL SPORT COUPE TURBO",
        "COROLLALIFTBACK": "COROLLA LIFTBACK",
        "CELICAGTLIFTBACK": "CELICA GT LIFTBACK",
        "COROLLATERCEL": "COROLLA TERCEL",
        "CORONALIFTBACK": "CORONA LIFTBACK",
        "CELICAGT": "CELICA GT",
        "1131DELUXESEDAN": "1131 DELUXE SEDAN",
        "RABBITCUSTOM": "RABBIT CUSTOM",
        "145E(SW)": "145E SW",
        "244DL": "244 DL",
        "264GL": "264 GL",
        "COROLLA1600(SW)": "COROLLA 1600 SW",
        "504(SW)": "504 SW",
        "SATELLITECUSTOM(SW)": "SATELLITE CUSTOM SW"
    }

    if model in model_mapping:  # Vérifie si le modèle est dans le dictionnaire de correspondance
        return model_mapping[model]  # Si oui, retourne le modèle corrigé
    else:
        return model  # Sinon, retourne le modèle tel quel .





