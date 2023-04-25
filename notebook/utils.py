# utils.py

def rename_columns(df):
    """Renomme les colonnes du dataframe en français."""
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
    """Convertit les unités du dataframe en unités françaises."""
    df['poids_vehicule'] = df['poids_vehicule'] * 0.453592
    df[['empattement', 'longueur_voiture', 'largeur_voiture', 'hauteur_voiture']] *= 2.54
    df[['empattement', 'longueur_voiture', 'largeur_voiture', 'hauteur_voiture']] = df[['empattement', 'longueur_voiture', 'largeur_voiture', 'hauteur_voiture']].round(1)
    df[['consommation_ville', 'consommation_autoroute']] = 235.215 / df[['consommation_ville', 'consommation_autoroute']]
    df[['consommation_ville', 'consommation_autoroute']] = df[['consommation_ville', 'consommation_autoroute']].round(2)
    return df

def split_brand_and_model(df):
    """Sépare la marque et le modèle de la colonne 'marque_voiture'."""
    df[['marque', 'modele']] = df['marque_voiture'].str.split(' ', n=1, expand=True)
    df['marque'] = df['marque'].str.upper().str.replace(' ', '')
    df['modele'] = df['modele'].str.upper().str.replace(' ', '')
    df = df.drop(columns=['marque_voiture'])
    return df

def translate_columns(df):
    """Traduit les valeurs des colonnes en français."""
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
    return df.replace(translation_dict)
