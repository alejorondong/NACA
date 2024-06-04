import numpy as np
import matplotlib.pyplot as plt


def calculer_coord_profil(NACA, c, nb_points, distribution):
    t = int(NACA) % 100 / 100
    xc = np.linspace(0, 1, nb_points)

    if distribution == 'linéaire':
        q = np.pi * np.linspace(0, 1, nb_points)
        xc = 0.5 * (1 - np.cos(q))

    yt = 5 * t * (0.2969 * np.sqrt(xc) - 0.1260 * xc - 0.3516 * xc ** 2 + 0.2843 * xc ** 3 - 0.1036 * xc ** 4)
    xup = xc * c
    yup = yt * c
    xdown = xc * c
    ydown = -yt * c

    return xup, yup, xdown, ydown


def afficher_profil(NACA, c, nb_points, distribution):
    xup, yup, xdown, ydown = calculer_coord_profil(NACA, c, nb_points, distribution)

    plt.plot(xup, yup, label='Extrados')
    plt.plot(xdown, ydown, label='Intrados')
    plt.xlabel('Position le long de la corde (m)')
    plt.ylabel('Épaisseur du profil (m)')
    plt.title('Profil NACA ' + NACA)
    plt.grid(True)
    plt.legend()
    plt.show()


def calculer_epaisseur_max(NACA, c, nb_points, distribution):
    xup, yup, _, _ = calculer_coord_profil(NACA, c, nb_points, distribution)
    ymax_index = np.argmax(yup)
    x_max = xup[ymax_index]
    y_max = yup[ymax_index]
    return y_max, x_max


# Demander les entrées à l'utilisateur
NACA = input("Entrez le numéro du profil NACA 4 chiffres symétrique : ")
c = float(input("Entrez la corde du profil (en mètre) : "))
nb_points = int(input("Entrez le nombre de points le long de la corde pour le tracé : "))
distribution = input("Entrez le type de distribution de points le long de la corde (linéaire ou non-uniforme) : ")

# Afficher le profil
afficher_profil(NACA, c, nb_points, distribution)

# Calculer et afficher l'épaisseur maximale et sa position
epaisseur_max, position_max = calculer_epaisseur_max(NACA, c, nb_points, distribution)
print("Épaisseur maximale du profil : ", epaisseur_max, " m")
print("Position de l'épaisseur maximale le long de la corde : ", position_max, " m")
