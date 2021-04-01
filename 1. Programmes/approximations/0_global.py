import matplotlib.pyplot as plt


def plot_one(x, signal, signalname="$$", xname="$$", yname="$$"):
    plt.plot(x, signal, label=signalname)
    plt.xlabel = xname
    plt.ylabel = yname
    plt.legend()
    plt.show()


def plot_two(x, signal_1, signal_2, signal_1_name="$$", signal_2_name="$$", xname="$$", yname="$$"):
    plt.plot(x, signal_1, label=signal_1_name)
    plot_one(x, signal_2, signal_2_name, xname, yname)


def plot_three(x, signal_1, signal_2, signal_3, signal_1_name="$$", signal_2_name="$$", signal_3_name="$$", xname="$$", yname="$$"):
    plt.plot(x, signal_1, label=signal_1_name)
    plot_two(x, signal_2, signal_3, signal_2_name, signal_3_name, xname, yname)
