# def main():    
#     i = 0
#     j = 0
#     cell = (i,j)
#     print(neighbors(cell))
    

# def neighbors(cell):
#     i = cell[0]
#     j = cell[1]
    
#     height = 3
#     width = 3
#     grid = [[0,1,2],
#             [3,4,5],
#             [6,7,8]]
#     n = []

#     # top left corner 
#     if i == 0 and j == 0:

# mat = [[0,1,2,6,7],
#        [3,4,5,8,8]]
# cell = (0,2)

# self_mines = {(0, 3), (1, 3)}
# self_safes = {(0, 1), (1, 2)}
# # a, b = (1, 2) # the index of the element 
# a = cell[0]
# b = cell [1]
# # neighbors = {mat[i][j] for i in range(a-1, a+2) for j in range(b-1, b+2) if i > -1 and j > -1 and j < len(mat[0]) and i < len(mat)}

# # print(neighbors)
# height = 2
# width = 5  
# neighbors = set()
# for i in range(a-1, a+2):
#     for j in range(b-1, b+2):
#         if i > -1 and j > -1 and j < width and i < height and (i != a or j != b):
#             if (i,j) not in self_safes and (i,j) not in self_mines:
#                 neighbors.add((i,j))
#             # neighbors.add(mat[i][j])
# print(neighbors)
import random

all_moves = {1,2,3,4,5,6}
self_moves_made = {1,3,2,6}
self_mines = {4,5,1}

random_moves = all_moves - self_moves_made - self_mines



if not random_moves :
    print("h")
else:
    print(random.choice(list(random_moves)))





