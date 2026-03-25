def celsius_to_fahrenheit(celsius):
    """Convertit les Celsius en Fahrenheit."""
    return (celsius * 9/5) + 32

def est_ce_qu_il_gele(celsius):
    """Renvoie True si la température est à 0 ou en dessous."""
    return celsius <= 0