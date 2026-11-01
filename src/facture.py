"""Calcul de factures — code FICTIF de test (aucune donnée réelle)."""

TAUX_TVA = {"normal": 0.20, "intermediaire": 0.10, "reduit": 0.055}


def montant_ttc(montant_ht: float, categorie: str = "normal") -> float:
    taux = TAUX_TVA[categorie]
    return round(montant_ht * (1 + taux), 2)


def total_facture(lignes) -> float:
    return round(sum(montant_ttc(ht, cat) for ht, cat in lignes), 2)


def montant_ttc_remise(montant_ht: float, remise: float, categorie: str = "normal") -> float:
    """Montant TTC après remise commerciale (taux entre 0 et 1). À VALIDER (ESSAI-RELAIS-1)."""
    return round(montant_ttc(montant_ht, categorie) * (1 - remise), 2)
