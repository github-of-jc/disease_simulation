import random
import math
from matplotlib import pyplot as plt

def normpdf(x, mean, sd):
    """
    Return the value of the normal distribution
    with the specified mean and standard deviation (sd) at
    position x.
    You do not have to understand how this function works exactly.
    """
    var = float(sd)**2
    denom = (2*math.pi*var)**.5
    num = math.exp(-(float(x)-float(mean))**2/(2*var))
    return num/denom


recovery_time = 4 # recovery time in time-steps
virality = 0.2    # probability that a neighbor cell is infected in
                  # each time step

class Cell(object):

    def __init__(self,x, y):
        self.x = x
        self.y = y
        self.state = "S" # can be "S" (susceptible), "R" (resistant = dead), or
                         # "I" (infected)

    def infect(self):
        self.state = "I"

    def process(self, adjacent_cells):
        pass

    #def __repr__(self):
    #    return self.__str__

#    def __str__(self):
#        return "{}, {}".format(self.x, self.y)

class Map(object):

    def __init__(self):
        self.height = 150
        self.width = 150
        self.cells = {}

    def add_cell(self, cell):
        self.cells[(cell.x, cell.y)] = cell

    def display(self):
        #(0.0, 0.0, 0.0): black pixel
        #(1.0, 0.0, 0.0): red pixel
        #(0.0, 1.0, 0.0): green pixel
        #(0.5, 0.5, 0.5): gray pixel
        #image is a list of lists of lists

        image = [[(0.0,0.0,0.0) for x in range(150)] for y in range(150)]

        for x,y in self.cells:
            image[x][y] = (0.0,1.0,0.0)

        plt.imshow(image)
        return image


    def adjacent_cells(self,x,y):
        cell_list = []

        cell_list.append(Cell(x,y+1))
        cell_list.append(Cell(x,y-1))
        cell_list.append(Cell(x-1,y))
        cell_list.append(Cell(x+1,y))

        return cell_list


def read_map(filename):

    m = Map()

    # ... Write this function
    f = open(filename, 'r')
    for line in f:
        line = line.strip()
        fields = line.split(',')

        x = int(fields[0].strip())
        y = int(fields[1].strip())

        print("adding", Cell(x,y))
        m.add_cell(Cell(x,y))

    return m


if __name__ == '__main__':
    m = read_map('nyc_map.csv')
    image = m.display()
