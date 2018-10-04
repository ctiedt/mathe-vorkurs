import matplotlib
import matplotlib.pyplot as plt
import numpy as np

params = {"ytick.color" : "w",
          "xtick.color" : "w",
          "axes.labelcolor" : "w",
          "axes.edgecolor" : "w"}
plt.rcParams.update(params)

def cubed(interval = [-3, 3], fn="cubed.png"):
    f = lambda x: x**3
    t = np.arange(*interval, 0.01)
    s = [f(x) for x in t]
    fig, ax = plt.subplots()
    ax.plot(t, s)
    ax.set(xlabel="x", ylabel="y")
    ax.set_title("f(x) = x^3", color="#01ff70")
    ax.grid()
    fig.savefig(fn)

def draw_function(interval=[-10, 10], f = lambda x: x, title_="", accuracy = 0.01, fn="fig.png"):
    t = np.arange(*interval, accuracy)
    s = [f(x) for x in t]
    fig, ax = plt.subplots()
    ax.set_facecolor("#222222")
    fig.patch.set_facecolor("#222222")
    ax.plot(t, s)
    ax.set(xlabel="x", ylabel="y")
    ax.set_title(title_, color="#1d9ce5")
    ax.grid()
    fig.savefig(fn, facecolor=fig.get_facecolor(), transparent=True)

def draw_multiple(interval=[-10, 10], f = [lambda x: x], title_="", accuracy = 0.01, fn="fig.png"):
    t = np.arange(*interval, accuracy)
    fig, ax = plt.subplots()
    ax.set_facecolor("#222222")
    fig.patch.set_facecolor("#222222")
    for fun in f:
        ax.plot(t, [fun(x) for x in t])
    ax.set(xlabel="x", ylabel="y")
    ax.set_title(title_, color="#1d9ce5")
    ax.grid()
    fig.savefig(fn, facecolor=fig.get_facecolor(), transparent=True)

def table(rows):
    print("| " + " | ".join(rows[0]) + " |")
    print("| - " * len(rows[0]) + " |")
    for row in rows[1:]:
        print("| " + " | ".join(row) + " |")

def zeta(x):
        return sum(1/(n**x) for n in range(1, 1000))

parabola = lambda x: (x + 2)**2 + 2 - 4

if __name__ == "__main__":
    draw_function(f= parabola, fn="parabola.png", interval=[-5, 5], title_="f(x) =  (x + 4/2)^2 + 2 - (4/2)^2")
    draw_function(f= lambda x: x**3, fn="cubed.png", interval=[-3, 3], title_="f(x) = x^3")