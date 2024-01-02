from abc import ABC, abstractmethod

class ObjetPostal(ABC):
    def __init__(self, nom_destinataire, adresse_destinataire, code_postal, ville_destination, recommande):
        self.nom_destinataire = nom_destinataire
        self.adresse_destinataire = adresse_destinataire
        self.code_postal = code_postal
        self.ville_destination = ville_destination
        self.recommande = recommande

    @abstractmethod
    def prix(self):
        pass


class Lettre(ObjetPostal):
    def __init__(self, nom_destinataire, adresse_destinataire, code_postal, ville_destination, recommande, urgence):
        super().__init__(nom_destinataire, adresse_destinataire, code_postal, ville_destination, recommande)
        self.urgence = urgence

    def prix(self):
        prix_base = 0.53
        if self.recommande == "oui":
            surcout_recommande = 1.5
        elif self.recommande =="non":
            surcout_recommande = 0.0
        
        #surcout_recommande = 1.5 if self.recommande else 0.0
        if self.urgence == "oui":
            surcout_urgence = 1.5
        elif self.urgence =="non":
            surcout_urgence = 0.0
        return prix_base + surcout_recommande + surcout_urgence


class Colis(ObjetPostal):
    def __init__(self, nom_destinataire, adresse_destinataire, code_postal, ville_destination, recommande, poids):
        super().__init__(nom_destinataire, adresse_destinataire, code_postal, ville_destination, recommande)
        self.poids = poids

    def prix(self):
        prix_base = 0.8 
        if self.recommande == "oui":
            surcout_recommande = 3.0
        elif self.recommande =="non":
            surcout_recommande = 0.0
        

     
        #surcout_recommande = 3.0 if self.recommande else 0.0
        poids_unite = 100
        unites_poids = self.poids / poids_unite
        return prix_base * unites_poids + surcout_recommande


def afficher_menu():
    print("1. Envoyer une lettre")
    print("2. Envoyer un colis")
    print("0. Quitter")


while True:
    afficher_menu()
    choix = input("Choisissez une option (1, 2, ou 0 pour quitter): ")

    if choix == "1":
        nom_destinataire = input("Nom du destinataire : ")
        adresse_destinataire = input("Adresse du destinataire : ")
        code_postal = int(input("Code postal : "))
        ville_destination = input("Ville destination : ")
        recommande = input("Envoyer en recommandé ? (Oui/Non) : ").lower() == "oui"
        urgence = input("Envoyer en urgence ? (Oui/Non) : ").lower() == "oui"

        lettre = Lettre(nom_destinataire, adresse_destinataire, code_postal, ville_destination, recommande, urgence)
        print("Prix à payer :", lettre.prix())

    elif choix == "2":
        nom_destinataire = input("Nom du destinataire : ")
        adresse_destinataire = input("Adresse du destinataire : ")
        code_postal = int(input("Code postal : "))
        ville_destination = input("Ville destination : ")
        recommande = input("Envoyer en recommandé ? (Oui/Non) : ").lower() == "oui"
        poids_colis = float(input("Poids du colis en grammes : "))

        colis = Colis(nom_destinataire, adresse_destinataire, code_postal, ville_destination, recommande, poids_colis)
        print("Prix à payer :", colis.prix())

    elif choix == "0":
        break

    else:
        print("Option invalide. Veuillez choisir une option valide.")
