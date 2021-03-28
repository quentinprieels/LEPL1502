# Import
import numpy as np
import csv
import matplotlib.pyplot as plt


# One signal file
def one_signal(filename, title, precision=1, legend="$V_{out}$"):
    # --- 1. Lecture du fichier csv ---
    x = []
    y = []

    with open(filename) as file:
        l_num = 1
        for line in file:

            # 2 ligne => unités
            if l_num == 2:
                l2 = line.strip().split(";")
                axe_x_units = l2[0]
                axe_y_units = l2[1]

            # 4 ligne -> end => values
            elif l_num >= 4 and l_num % precision == 0:
                l_more = line.strip().split(";")
                x.append(float(l_more[0].replace(',', '.')))
                y.append(float(l_more[1].replace(',', '.')))

            l_num += 1

    # --- 2. Plot ---
    plt.title(title)
    plt.plot(x, y, label=legend)
    plt.xlabel("Temps " + axe_x_units)
    plt.ylabel("Tension " + axe_y_units)
    plt.legend()
    # plt.axis([-200, 200, -550, 550])
  #  plt.savefig("graphes/" + title + ".eps", format='eps')
    plt.show()


# Two signal file
def two_signal(filename, title, precision=1, legend1="$V_{out}$", legend2="$V_{in+}$"):
    # --- 1. Lecture du fichier csv ---
    x = []
    y1 = []
    y2 = []

    with open(filename) as file:
        l_num = 1
        for line in file:

            # 2 ligne => unités
            if l_num == 2:
                l2 = line.strip().split(";")
                axe_x_units = l2[0]
                axe_y_units = l2[1]

            # 4 ligne -> end => values
            elif l_num >= 4 and l_num % precision == 0:
                l_more = line.strip().split(";")
                x.append(float(l_more[0].replace(',', '.')))
                y1.append(float(l_more[1].replace(',', '.')))
                y2.append(float(l_more[2].replace(',', '.')))

            l_num += 1

    # --- 2. Plot ---
    plt.title(title)
    plt.plot(x, y2, label=legend2)
    plt.plot(x, y1, label=legend1)
    plt.xlabel("Temps " + axe_x_units)
    plt.ylabel("Tension (V)")
    plt.legend()
   # plt.axis([-120, 80, -1.5, 5.5])
  #  plt.savefig("graphes/" + title + ".eps", format='eps')
    plt.show()


# Four signals file
def four_signal(filename, title, precision=1, legend1="$V_{out}$", legend2="$V_{in+}$", legend3="$$", legend4="$$"):
    # --- 1. Lecture du fichier csv ---
    x = []
    y1 = []
    y2 = []
    y3 = []
    y4 = []

    with open(filename) as file:
        l_num = 1
        for line in file:

            # 2 ligne => unités
            if l_num == 2:
                l2 = line.strip().split(";")
                axe_x_units = l2[0]
                axe_y_units = l2[1]

            # 4 ligne -> end => values
            elif l_num >= 4 and l_num % precision == 0:
                l_more = line.strip().split(";")
                x.append(float(l_more[0].replace(',', '.')))
                y1.append(float(l_more[1].replace(',', '.')))
                y2.append(float(l_more[2].replace(',', '.')))
                y3.append(float(l_more[3].replace(',', '.')))
                y4.append(float(l_more[4].replace(',', '.')))

            l_num += 1

    # --- 2. Plot ---
    plt.title(title)
    plt.plot(x, y2, label=legend2)
    plt.plot(x, y1, label=legend1)
    # plt.plot(x, y3, label=legend3)
    # plt.plot(x, y4, label=legend4)
    plt.xlabel("Temps " + axe_x_units)
    plt.ylabel("Tension " + axe_y_units)
    plt.legend()
    plt.axis([-5, 5, -1.5, 5.5])
    plt.savefig("graphes/" + title + ".png", format='png')
    plt.show()


two_signal("Labo07/trans in_out/trans in_out_10.csv", "", 1, "$V_{in}$", "$V{out}$")