row1 = [0,0,0]
row2 = [0,0,0]
row3 = [0,0,0]

map = [row1,row2,row3]

print(f"{row1}\n{row2}\n{row3}")

position = input("Where do you want to put the treasure? (row and column)")

row_pos = int(position[0])-1
column_pos = int(position[1])-1

map[row_pos][column_pos] = 1

print(f"{map[0]}\n{map[1]}\n{map[2]}")