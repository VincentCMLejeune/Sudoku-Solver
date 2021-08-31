import dessin
import solver

sudoku = []
continuer = True

indices_seuls = []
for i in range(81):
  indices_seuls.append(i)

# Supprimer une fois tests reussis
print("\n\nSUDOKU SOLVER\n\nConstruisons le sudoku : renseigne les chiffres de chaque ligne (s'il est inconnu, écris 0)")
for i in range(1, 10):
  row = input("Tape les 9 chiffres de la ligne " + str(i) + "\n> ")
  for i in row:
    valeur = int(i)
    sudoku.append(valeur)

# Supprimer une fois tests reussis
print("Sudoku avant résolution")
dessin.dessine(sudoku)


while continuer == True:
  indexe = []
  for i in range(81):
    indexe.append([sudoku[i], i])

  index = -1
  for i in indexe:
    index += 1
    if i[0] != 0:
      continue
    else:
      pass
      solver.solver(i, indexe, sudoku)

  if 0 not in sudoku:
    continuer = False

print("Sudoku après résolution")
dessin.dessine(sudoku)
# dessin.dessine(indices_seuls)
# dessin.dessine(indexe)