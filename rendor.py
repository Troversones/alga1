def catch_thieves(police_positions, thief_positions, k):
    # A rendőrök pozícióinak rendezése
    police_positions.sort()
    # A tolvajok pozícióinak rendezése
    thief_positions.sort()

    captured = 0  # A megfogott tolvajok száma
    # A rendőrök, akik már megfogtak tolvajt, kezdetben mind hamis
    police_indices = [False] * len(police_positions)

    # Minden tolvaj pozícióján végigiterálunk
    for thief_position in thief_positions:
        left_bound = thief_position - k  # A bal határ, ahol a rendőrök kereshetnek
        right_bound = thief_position + k  # A jobb határ, ahol a rendőrök kereshetnek

        # Minden rendőr pozícióján végigiterálunk
        for i, police_position in enumerate(police_positions):
            # Ellenőrizzük, hogy a rendőr még nem fogott el tolvajt, és a pozíció a határok között van
            if not police_indices[i] and left_bound <= police_position <= right_bound:
                captured += 1  # Megnöveljük a megfogott tolvajok számát
                police_indices[i] = True  # A rendőrt megjelöljük, hogy már fogott el tolvajt
                break  # Kilépünk a belső ciklusból, mert a tolvaj már meg van fogva

    return captured  # Visszatérünk a megfogott tolvajok számával

# Teszteljük a programot
police_positions = [3, 4, 6]  # A rendőrök pozíciói
thief_positions = [1, 2, 5]    # A tolvajok pozíciói
k = 2  # A hatótávolság

# A funkció hívása és az eredmény kiírása
result = catch_thieves(police_positions, thief_positions, k)
print(f"Rendőrökkel megfogott tolvajok száma: {result}")  # Kiírjuk a megfogott tolvajok számát
