"""Calcul de factures — code FICTIF de test (aucune donnée réelle)."""

TAUX_TVA = {"normal": 0.20, "intermediaire": 0.10, "reduit": 0.055}


def montant_ttc(montant_ht: float, categorie: str = "normal") -> float:
    taux = TAUX_TVA[categorie]
    return round(montant_ht * (1 + taux), 2)


def total_facture(lignes) -> float:
    """Somme des montants TTC des lignes (montant HT, catégorie de TVA)."""
    return round(sum(montant_ttc(ht, cat) for ht, cat in lignes), 2)
