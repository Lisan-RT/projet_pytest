def est_ce_qu_il_gele(celsius):
    """Logique : Vérifie si la température est <= 0."""
    return celsius <= 0


# Cette partie ne s'exécute que si tu lances le fichier directement
if __name__ == "__main__":
    print("Météo Norvégienne")
    
    reponse = input("Quelle température fait-il dehors (en °C) ? ")
    
    # On transforme le texte en nombre (float) pour pouvoir calculer
    temperature = float(reponse)
    
    if est_ce_qu_il_gele(temperature):
        print("Résultat : L'eau est gelée. Attention !")
    else:
        print("Résultat : L'eau n'est pas gelée. Il fait doux.")