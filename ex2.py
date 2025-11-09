import json
from datetime import datetime

# Classe de base
class Document:
    def __init__(self, titre, annee):
        self.titre = titre
        self.annee = annee

    def afficher(self):
        print(f"{self.titre} ({self.annee})")

    def est_recent(self):
        """Retourne True si le document a moins de 5 ans."""
        annee_actuelle = datetime.now().year
        return annee_actuelle - self.annee <= 5

    def to_dict(self):
        """Convertit l'objet en dictionnaire pour la sérialisation JSON."""
        return {
            "type": self.__class__.__name__,
            "titre": self.titre,
            "annee": self.annee
        }


# Classe dérivée : Livre
class Livre(Document):
    def __init__(self, titre, annee, auteur):
        super().__init__(titre, annee)
        self.auteur = auteur

    def afficher(self):
        print(f"Livre: {self.titre} par {self.auteur} ({self.annee})")

    def to_dict(self):
        data = super().to_dict()
        data["auteur"] = self.auteur
        return data


# Classe dérivée : Magazine
class Magazine(Document):
    def __init__(self, titre, annee, numero):
        super().__init__(titre, annee)
        self.numero = numero

    def afficher(self):
        print(f"Magazine: {self.titre} No. {self.numero} ({self.annee})")

    def to_dict(self):
        data = super().to_dict()
        data["numero"] = self.numero
        return data


# Classe Bibliotheque
class Bibliotheque:
    def __init__(self):
        self.documents = []

    def ajouter(self, document):
        self.documents.append(document)

    def afficher_tous(self):
        for doc in self.documents:
            doc.afficher()

    def rechercher(self, titre):
        """Recherche un document par titre (insensible à la casse)."""
        for doc in self.documents:
            if doc.titre.lower() == titre.lower():
                return doc
        return None

    def sauvegarder_json(self, fichier):
        """Sauvegarde la liste des documents dans un fichier JSON."""
        data = [doc.to_dict() for doc in self.documents]
        with open(fichier, "w", encoding="utf-8") as f:
            json.dump(data, f, ensure_ascii=False, indent=4)
        print(f"Bibliothèque sauvegardée dans {fichier}")


# Programme principal
if __name__ == "__main__":
    biblio = Bibliotheque()

    biblio.ajouter(Livre("1984", 1949, "George Orwell"))
    biblio.ajouter(Magazine("Science & Vie", 2023, 456))
    biblio.ajouter(Livre("Le Petit Prince", 1943, "Antoine de Saint-Exupéry"))

    print("\n Liste des documents :")
    biblio.afficher_tous()

    print("\n Recherche du titre '1984' :")
    doc = biblio.rechercher("1984")
    if doc:
        doc.afficher()
        print("Est récent :", "Oui" if doc.est_recent() else "Non")
    else:
        print("Document non trouvé.")

    # Sauvegarde en JSON
    biblio.sauvegarder_json("bibliotheque.json")
