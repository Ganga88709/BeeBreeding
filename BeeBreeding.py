import sys
coordinates = [[1, 0, -1], [0, 1, -1], [-1, 1, 0], [-1, 0, 1], [0, -1, 1], [1, -1, 0]]
RADIUS = 59    
EDGES = 6

def numberOfMoves(cellsDict, cell_1, cell_2):
    x1, y1, z1 = cellsDict[cell_1]
    x2, y2, z2 = cellsDict[cell_2]
    return (abs(x2 - x1) + abs(y2 - y1) + abs(z2 - z1)) //2
    
def honeyComb(radius):
    cell_count = 1
    cellsDict = {}
    x_axis, y_axis, z_axis = 0, 0, 0
    cellsDict[cell_count] = x_axis, y_axis, z_axis
    for rad in range(radius):
        x_axis = rad
        y_axis = -rad
        z_axis = 0
        for i in range(EDGES):
            for j in range(rad):
                x_axis += coordinates[i][0]
                y_axis += coordinates[i][1]
                z_axis += coordinates[i][2]
                cell_count += 1
               
                cellsDict[cell_count] = x_axis, y_axis, z_axis
   
for i in range(1, len(sys.argv), 2):
    cell_1 = int(sys.argv[i])
    cell_2 = int(sys.argv[i+1])
    if(cell_1 <= 0 or cell_2 <= 0):
        print("1")
    else:
        print(numberOfMoves(honeyComb(RADIUS), cell_1, cell_2))
