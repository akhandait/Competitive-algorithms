# Hackerrank Connected Cells in a Grid problem from Search division
# I have used the recursive flood fill algorithm


n = int(input().strip())
m = int(input().strip())
mat = []
for i in range(n):
    templ = list(map(int, input().strip().split(' ')))
    mat.append(templ)

# adding an outer layer of zeros to avoid corner check everywhere
templ = [0] * m
mat = [templ] + mat + [templ]
mat = [[0] + x + [0] for x in mat]

regionl = []

def checkreg(posx, posy):
    if mat[posx][posy] == 0:
        return 0
    mat[posx][posy] = 0
    r = checkreg(posx + 1, posy)
    lr = checkreg(posx + 1, posy + 1)
    b = checkreg(posx, posy + 1)
    ll = checkreg(posx - 1, posy + 1)
    l = checkreg(posx - 1, posy)
    ul = checkreg(posx - 1, posy - 1)
    u = checkreg(posx, posy - 1)
    ur = checkreg(posx + 1, posy - 1)
    
    total = 1 + r + lr + b + ll + l + ul + u + ur
    
    return total

for i in range(n):
    for j in range(m):
        regionl.append(checkreg(i, j))
        
print(max(regionl))        
    