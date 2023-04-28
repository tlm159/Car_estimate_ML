from pydantic import BaseModel

class CarFeatures(BaseModel):
    """
    Classe représentant les caractéristiques d'une voiture.

    Attributes:
    -----------
    type_vehicule : str
        Le type de véhicule (berline, SUV, etc.).
    roues_motrices : str
        Le type de roues motrices (avant, arrière, propulsion, 4 roues motrices, etc.).
    modele : str
        Le modèle de la voiture.
    marque : str
        La marque de la voiture.
    empattement : float
        L'empattement de la voiture (en cm).
    longueur_voiture : float
        La longueur de la voiture (en cm).
    largeur_voiture : float
        La largeur de la voiture (en cm).
    poids_vehicule : float
        Le poids de la voiture (en kg).
    taille_moteur : int
        La taille du moteur de la voiture (en cm3).
    taux_alésage : float
        Le taux d'alésage du moteur de la voiture.
    chevaux : int
        Le nombre de chevaux de la voiture.
    consommation_ville : float
        La consommation de carburant en ville (en L/100km).
    consommation_autoroute : float
        La consommation de carburant sur autoroute (en L/100km).
    """

    type_vehicule: str
    roues_motrices: str
    modele: str
    marque: str
    empattement: float
    longueur_voiture: float
    largeur_voiture: float
    poids_vehicule: float
    taille_moteur: int
    taux_alésage: float
    chevaux: int
    consommation_ville: float
    consommation_autoroute: float