def addition(x, y):
    return x + y

def soustraction(x, y):
    return x - y

def multiplication(x, y):
    return x * y

def division(x, y):
    if y == 0:
        return "Erreur : Division par zéro"
    else:
        return x / y

operations = {
    '+': addition,
    '-': soustraction,
    '*': multiplication,
    '/': division
}

while True:
    try:
        x = float(input("Entrez le premier nombre : "))
        y = float(input("Entrez le deuxième nombre : "))
        op = input("Entrez l'opération (+, -, *, /) : ")

        if op in operations:
            resultat = operations
            print("Le résultat est : ", resultat)
        else:
            print("Opération non reconnue")

        continuer = input("Voulez-vous continuer ? (O/N) ")
        if continuer.lower() != 'o':
            break
    except ValueError:
        print("Veuillez entrer un nombre valide")