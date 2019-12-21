def otvet(h1, h2, m1, m2, s1, s2):
    raznica = (((h1 - h2) * 3600) + ((m1 - m2) * 60) + (s1 - s2))
    print(raznica)
otvet(6, 6, 2, 1, 10, 30)