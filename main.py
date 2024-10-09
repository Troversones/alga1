import numpy as np

# Adott munkákhoz tartozó profitok és határidők
profit = np.array([20, 15, 10, 5, 1])
hatarido = np.array([2, 2, 1, 3, 3])

# Az aktuális napok és a megoldás inicializálása
megold = [0, 0, 0, 0, 0]
nap = [0, 0, 0]

def munkautem(profit, hatarido, nap, megold):
    print(nap)
    # Ha már elérkeztünk az utolsó napra, akkor lépjünk ki
    if np.count_nonzero(nap) == len(nap):
        return nap
    # A legnagyobb megszerezhető profit munkájának kiválasztása
    max_ =  np.argmax(profit)
    # Nézzük meg, hogy van-e még időnk erre a munkára a határidőig
    for i in range(hatarido[max_] - 1, -1, -1):
        print(i)
        if nap[i] == 0:
            # A napot a munka profitjával töltjük meg
            nap[i] = profit[max_]
            # A munkát elvégeztük, profitját nullázzuk
            profit[max_] = 0
            return munkautem(profit, hatarido, nap, megold)
    else:
        # Ha nincs elég idő a munkára, akkor eldobjuk, és nézzük a következőt
        profit[max_] = 0
        return munkautem(profit, hatarido, nap, megold)

munkautem(profit, hatarido, nap, megold)
