class User:
	def __init__(self, fournisseur, profil, materiel) :
		self.fournisseur = fournisseur
#Attributs
		self.profil = profil
		self.materiel = materiel
		#Getters (obtenir une information)
def get_fournisseur(self) :
	return self.fournisseur
def get_materiel(self) :
	return self.materiel
def get_profil(self):
	return self.profil

  #setters (modifier une information)
	def set_fournisseur(self, fournisseur) :
		self.fournisseur = fournisseur
#Les autres méthodes :
	def Consomme_Energie(self):
		pass

	def Produire_Energie(self):
		pass
	def Stocke_Energie(self):
		pass
#Une importation :
class Foyer (User) :
	def __init__(self, fournisseur,profil,materiel,nbr_Personne ,taux_consommation) :
		super().__init__( fournisseur,profil,materiel)
		self.nbr_Personne = nbr_Personne
		self.taux_consommation = taux_consommation
	def  EstActif(self):
		if self.taux_consommation <30:
			return True
		else:
			return False
	def   Est_NonActif(self):
		pass
	def  Iscouple(self):
		if self.nbr_Personne ==2:
			return "couple"
		else:
			return "Famille"
class Collectivité (User) :
	def  __init__(self, fournisseur,nom,profil,materiel) :
		super().__init__( fournisseur,profil,materiel)
		self.nom = nom
"""
class Couple (Foyer) :
	def  __init__(self, fournisseur, num,profil,nbr_Personne,taux_consommation ) :
		super().__init__( fournisseur, num,profil, nbr_Personne,taux_consommation)

class Famille (Foyer) :
	def  __init__(self, fournisseur, num,profil,nbr_Personne,taux_consommation ) :
		super().__init__( fournisseur, num,profil, nbr_Personne,taux_consommation)
"""
User1 = Foyer("EDF", "D","PV",3, 60)
#User2 = Couple("EDF", 1548,2,"C", 30)

print(User1.materiel)
print(User1.Iscouple())