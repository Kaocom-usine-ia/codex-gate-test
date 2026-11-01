from src.facture import montant_ttc, total_facture


def test_ttc_normal():
    assert montant_ttc(100.0) == 120.0


def test_total():
    assert total_facture([(100.0, "normal"), (50.0, "reduit")]) == 172.75
