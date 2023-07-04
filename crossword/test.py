
# def main():
#     x ={Variable(1, 4, 'down', 4): {'FOUR', 'FIVE', 'NINE'}} 
#     y = {Variable(0, 1, 'across', 3): {'TWO', 'TEN', 'ONE', 'SIX'}} 
#     # Variable(4, 1, 'across', 4): {'FOUR', 'FIVE', 'NINE'}, 
#     # Variable(0, 1, 'down', 5): {'THREE', 'SEVEN', 'EIGHT'}

#     print(revise(x,y))
# def revise(x,y):
#     domainx = deepcopy(self.domains[x])
#         domainy = self.domains[y]
#         revised = False
        
#         overlap = self.crossword.overlaps[x, y]
#         if overlap:
#             for elemx in domainx:
#                 counter = 0
#                 for elemy in domainy:
#                     if elemx[overlap[0]] == elemy[overlap[1]]:
#                         counter += 1
#                 if counter == 0:
#                     self.domains[x].remove(elemx)
#                     revised = True
        
#         return revised

# main()
# lis = [(1,2), (3,4)]
# lis1 = [(1,2), (3,4)]
# for queue in lis1:
#     x,y = queue[0],queue[1]
#     lis.remove(queue)
#     print(x,y)

# dt = {"ten":4, "one":6, "two":3}

# sorted_dt = [key for key, value in sorted(dt.items(), key=lambda item: item[1])]


# print(sorted_dt)

# dt = [{(1, 4, 'down', 4): {'NINE', 'FIVE', 'FOUR'}}, {(0, 1, 'across', 3): {'ONE', 'TEN', 'TWO', 'SIX'}, (0, 1, 'down', 5): {'EIGHT', 'THREE', 'SEVEN'}, (4, 1, 'across', 4): {'NINE', 'FIVE', 'FOUR'}]

# {Variable(0, 1, 'across', 3): {'TEN', 'SIX', 'ONE', 'TWO'}, Variable(0, 1, 'down', 5): {'THREE', 'EIGHT', 'SEVEN'}, Variable(4, 1, 'across', 4): {'NINE', 'FIVE', 'FOUR'}, Variable(1, 4, 'down', 4): {'NINE', 'FIVE', 'FOUR'}}
# [{Variable(0, 1, 'across', 3): {1, 4}}, {Variable(0, 1, 'down', 5): {2, 3}}, {Variable(4, 1, 'across', 4): {2, 3}}, {Variable(1, 4, 'down', 4): {1, 3}}]