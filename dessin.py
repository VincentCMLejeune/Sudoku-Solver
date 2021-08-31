def dessine(list):
  local_list = []
  for i in range(81):
    local_list.append(0)

  for i in range(81):
    if list[i] == 0:
      local_list[i] = "."
    else:
      local_list[i] = list[i]

  print("+-----------------------+")
  print("| {} {} {} | {} {} {} | {} {} {} |".format(local_list[0], local_list[1], local_list[2], local_list[3], local_list[4], local_list[5], local_list[6], local_list[7], local_list[8]))
  print("| {} {} {} | {} {} {} | {} {} {} |".format(local_list[9], local_list[10], local_list[11], local_list[12], local_list[13], local_list[14], local_list[15], local_list[16], local_list[17]))
  print("| {} {} {} | {} {} {} | {} {} {} |".format(local_list[18], local_list[19], local_list[20], local_list[21], local_list[22], local_list[23], local_list[24], local_list[25], local_list[26]))
  print("+-----------------------+")
  print("| {} {} {} | {} {} {} | {} {} {} |".format(local_list[27], local_list[28], local_list[29], local_list[30], local_list[31], local_list[32], local_list[33], local_list[34], local_list[35]))
  print("| {} {} {} | {} {} {} | {} {} {} |".format(local_list[36], local_list[37], local_list[38], local_list[39], local_list[40], local_list[41], local_list[42], local_list[43], local_list[44]))
  print("| {} {} {} | {} {} {} | {} {} {} |".format(local_list[45], local_list[46], local_list[47], local_list[48], local_list[49], local_list[50], local_list[51], local_list[52], local_list[53]))
  print("+-----------------------+")
  print("| {} {} {} | {} {} {} | {} {} {} |".format(local_list[54], local_list[55], local_list[56], local_list[57], local_list[58], local_list[59], local_list[60], local_list[61], local_list[62]))
  print("| {} {} {} | {} {} {} | {} {} {} |".format(local_list[63], local_list[64], local_list[65], local_list[66], local_list[67], local_list[68], local_list[69], local_list[70], local_list[71]))
  print("| {} {} {} | {} {} {} | {} {} {} |".format(local_list[72], local_list[73], local_list[74], local_list[75], local_list[76], local_list[77], local_list[78], local_list[79], local_list[80]))
  print("+-----------------------+")