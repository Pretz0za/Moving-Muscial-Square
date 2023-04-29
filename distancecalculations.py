from miditotext import output

points = [(0, 0)]
velx, vely = 15, 10

for time in output:
        if time == 0:
            continue
        points.append((points[-1][0]+(velx*time*30), points[-1][1]+(vely*time*30)))
        velx *=-1

output = ''

for point in points:
    output += '{x: ' + str(point[0]) + ', y: ' + str(point[1]) + '},'

print(output)
