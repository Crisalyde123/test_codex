"""Script de multiplication de deux nombres demandés à l'utilisateur."""

def demander_nombre(invite: str) -> float:
    """Demande un nombre à l'utilisateur."""
    while True:
        try:
            return float(input(invite))
        except ValueError:
            print("Entrée invalide. Veuillez saisir un nombre.")


def main() -> None:
    """Fonction principale."""
    a = demander_nombre("Premier nombre : ")
    b = demander_nombre("Second nombre : ")
    resultat = a * b
    print(f"Le résultat de {a} multiplié par {b} est {resultat}.")


if __name__ == "__main__":
    main()
