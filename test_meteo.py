from meteo import celsius_to_fahrenheit, est_ce_qu_il_gele

def test_conversion():
    # On vérifie que 0°C donne bien 32°F
    assert celsius_to_fahrenheit(0) == 32

def test_gel():
    # On vérifie qu'à -5°C, il gèle bien (True)
    assert est_ce_qu_il_gele(-5) is True
    # On vérifie qu'à 10°C, il ne gèle pas (False)
    assert est_ce_qu_il_gele(10) is False