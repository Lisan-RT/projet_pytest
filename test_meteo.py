from meteo import est_ce_qu_il_gele

def test_gel():
    # On vérifie qu'à -5°C, il gèle bien (True)
    assert est_ce_qu_il_gele(-5) is True
    # On vérifie qu'à 10°C, il ne gèle pas (False)
    assert est_ce_qu_il_gele(10) is False