"""Calcul de factures — code FICTIF de test (aucune donnée réelle)."""

TAUX_TVA = {"normal": 0.20, "intermediaire": 0.10, "reduit": 0.055}


def montant_ttc(montant_ht: float, categorie: str = "normal") -> float:
    """Montant TTC arrondi au centime."""
    taux = TAUX_TVA[categorie]
    return round(montant_ht * (1 + taux), 2)


def total_facture(lignes) -> float:
    return round(sum(montant_ttc(ht, cat) for ht, cat in lignes), 2)
