carre_un = [0, 1, 2, 9, 10, 11, 18, 19, 20]
carre_deux = [3, 4, 5, 12, 13, 14, 21, 22, 23]
carre_trois = [6, 7, 8, 15, 16, 17, 24, 25, 26]
carre_quatre = [27, 28, 29, 36, 37, 38, 45, 46, 47]
carre_cinq = [30, 31, 32, 39, 40, 41, 48, 49, 50]
carre_six = [33, 34, 35, 42, 43, 44, 51, 52, 53]
carre_sept = [54, 55, 56, 63, 64, 65, 72, 73, 74]
carre_huit = [57, 58, 59, 66, 67, 68, 75, 76, 77]
carre_neuf = [60, 61, 62, 69, 70, 71, 78, 79, 80]


ligne_un = [0, 1, 2, 3, 4, 5, 6, 7, 8]
ligne_deux = [9, 10, 11, 12, 13, 14, 15, 16, 17]
ligne_trois = [18, 19, 20, 21, 22, 23, 24, 25, 26]
ligne_quatre = [27, 28, 29, 30, 31, 32, 33, 34, 35]
ligne_cinq = [36, 37, 38, 39, 40, 41, 42, 43, 44]
ligne_six = [45, 46, 47, 48, 49, 50, 51, 52, 53]
ligne_sept = [54, 55, 56, 57, 58, 59, 60, 61, 62]
ligne_huit = [63, 64, 65, 66, 67, 68, 69, 70, 71]
ligne_neuf = [72, 73, 74, 75, 76, 77, 78, 79, 80]

colonne_un = [0, 9, 18, 27, 36, 45, 54, 63, 72]
colonne_deux = [1, 10, 19, 28, 37, 46, 55, 64, 73]
colonne_trois = [2, 11, 20, 29, 38, 47, 56, 65, 74]
colonne_quatre = [3, 12, 21, 30, 39, 48, 57, 66, 75]
colonne_cinq = [4, 13, 22, 31, 40, 49, 58, 67, 76]
colonne_six = [5, 14, 23, 32, 41, 50, 59, 68, 77]
colonne_sept = [6, 15, 24, 33, 42, 51, 60, 69, 78]
colonne_huit = [7, 16, 25, 34, 43, 52, 61, 70, 79]
colonne_neuf = [8, 17, 26, 35, 44, 53, 62, 71, 80]

def compare(ind, morceau, indexe, elimine):
  for i in morceau:
    if indexe[i][0] != 0 and indexe[i][0] not in elimine:
      elimine.append(indexe[i][0])


def solver(i, indexe, sudoku):
  elimine = []
  ind = i[1]

  if ind in carre_un:
    compare(ind, carre_un, indexe, elimine)
  elif ind in carre_deux:
    compare(ind, carre_deux, indexe, elimine)
  elif ind in carre_trois:
    compare(ind, carre_trois, indexe, elimine)
  elif ind in carre_quatre:
    compare(ind, carre_quatre, indexe, elimine)
  elif ind in carre_cinq:
    compare(ind, carre_cinq, indexe, elimine)
  elif ind in carre_six:
    compare(ind, carre_six, indexe, elimine)
  elif ind in carre_sept:
    compare(ind, carre_sept, indexe, elimine)
  elif ind in carre_huit:
    compare(ind, carre_huit, indexe, elimine)
  else:
    compare(ind, carre_neuf, indexe, elimine)

  if ind in ligne_un:
    compare(ind, ligne_un, indexe, elimine)
  elif ind in ligne_deux:
    compare(ind, ligne_deux, indexe, elimine)
  elif ind in ligne_trois:
    compare(ind, ligne_trois, indexe, elimine)
  elif ind in ligne_quatre:
    compare(ind, ligne_quatre, indexe, elimine)
  elif ind in ligne_cinq:
    compare(ind, ligne_cinq, indexe, elimine)
  elif ind in ligne_six:
    compare(ind, ligne_six, indexe, elimine)
  elif ind in ligne_sept:
    compare(ind, ligne_sept, indexe, elimine)
  elif ind in ligne_huit:
    compare(ind, ligne_huit, indexe, elimine)
  else:
    compare(ind, ligne_neuf, indexe, elimine)

  if ind in colonne_un:
    compare(ind, colonne_un, indexe, elimine)
  elif ind in colonne_deux:
    compare(ind, colonne_deux, indexe, elimine)
  elif ind in colonne_trois:
    compare(ind, colonne_trois, indexe, elimine)
  elif ind in colonne_quatre:
    compare(ind, colonne_quatre, indexe, elimine)
  elif ind in colonne_cinq:
    compare(ind, colonne_cinq, indexe, elimine)
  elif ind in colonne_six:
    compare(ind, colonne_six, indexe, elimine)
  elif ind in colonne_sept:
    compare(ind, colonne_sept, indexe, elimine)
  elif ind in colonne_huit:
    compare(ind, colonne_huit, indexe, elimine)
  else:
    compare(ind, colonne_neuf, indexe, elimine)

  if len(elimine) == 8:
    for i in range(1, 10):
      if i not in elimine:
        sudoku[ind] = i