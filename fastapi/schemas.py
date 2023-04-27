from pydantic import BaseModel

class CarFeatures(BaseModel):
    etat_de_route: int
    turbo: str
    type_vehicule: str
    roues_motrices: str
    emplacement_moteur: str
    marque: str
    modele: str
    empattement: float
    longueur_voiture: float
    largeur_voiture: float
    poids_vehicule: float
    taille_moteur: int
    taux_alésage: float
    chevaux: int
    consommation_ville: float
    consommation_autoroute: float