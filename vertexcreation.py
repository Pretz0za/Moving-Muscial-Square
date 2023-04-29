from distancecalculations import points


vertices = [points[0]]

temp = []

for i in range(0, len(points), 2):
        if i == 0:
            vertices.append(points[i])
        else:
            vertices.append((points[i][0], points[i-1][1]))
        if  points[i] == points[-1]:
             vertices.append(points[i])
        else:
             vertices.append((points[i][0], points[i+1][1]))

for i in range(1, len(points), 2):
        if i == 0:
            temp.append(points[i])
        else:
            temp.append((points[i][0], points[i-1][1]))
        if  points[i] == points[-1]:
             temp.append(points[i])
        else:
             temp.append((points[i][0], points[i+1][1]))

vertices += temp[::-1]

output = ''

for vertex in vertices:
    output += f'vertex{vertex}; \n'
print(output)
