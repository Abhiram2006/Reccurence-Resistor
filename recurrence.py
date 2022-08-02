import numpy as np
import matplotlib.pyplot as plt

def deltaY(R):
    return np.prod(R)/np.sum(R)/R # R1, R2, R3 returned if Ra, Rb and Rc inserted

def resistances(k):
    results = []
    Rstrand = 0 # Compounding sum of delta-Y R1
    R = np.ones(3) # Ra, Rb, Rc vector
    for i in range(1, 2*k+1):
        Ry = deltaY(R)
        Rstrand += Ry[0]
        R[1] = Ry[2]+((i+1) % 2)
        R[2] = Ry[1]+(i % 2)
        if(i % 2 == 0): results.append((Rstrand+R[2])/(i/2))

    return results

N_TRIALS = 100
X = np.arange(N_TRIALS)+1
Y = resistances(N_TRIALS)
Y_line = np.full_like(Y, 0.4)

fig, axes = plt.subplots(figsize=(16, 8))

axes.plot(X, Y)
axes.plot(X, Y_line, "--")

axes.set(
    title = "Loss Curve of $\\frac{R_{eff}}{n}$ of Recurrent Resistor Network (size $n$)",
    xlabel = "$n$",
    ylabel = "$\\frac{R_{eff}}{n}$"
)

plt.show()
