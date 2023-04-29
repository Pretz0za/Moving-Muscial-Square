from distancecalculations import points

odds = []
evens = []

vertices = [points[0]]

for i, point in enumerate(points):
    if (i+1) % 2 == 0:
        evens.append(point)
    else:
        odds.append(point)

for i in range(len(odds)):
    if odds[i] == odds[-1]:
        continue
    if odds[i][0] == odds[i+1][0]:
        continue
    if odds[i][0] > odds[i+1][0]:
        vertices.append(odds[i])
        vertices.append((odds[i+1][0], odds[i][1]))       
    else:
        vertices.append((odds[i][0], odds[i+1][1]))
        vertices.append(odds[i+1])

    
if len(odds) > len(evens):
    vertices.append((evens[-1][0], odds[-1][1]))
else:
    vertices.append((odds[-1][0], evens[-1][1]))


vertices.append(points[-1])

evens.reverse()

for i in range(len(evens)):
    if evens[i] == evens[-1]:
        continue
    if evens[i][0] == evens[i+1][0]:
        continue
    if evens[i] == evens[-1]:
        continue
    if evens[i][0] == evens[i+1][0]:
        continue
    if evens[i][0] > evens[i+1][0]:
        right = evens[i]
        left = evens [i+1]
        vertices.append((right[0], left[1]))
        vertices.append(left)
        
    else:
        right = evens[i+1]
        left = evens[i]    
        vertices.append(left)    
        vertices.append((right[0], left[1]))
        



vertices.append((points[1][0], 0))



output = ''

for vertex in vertices:
    output += f'vertex{vertex}; \n'
print(output)
