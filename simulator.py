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
virality = 0.8   # probability that a neighbor cell is infected in
                  # each time step

class Cell(object):

    def __init__(self,x, y):
        self.x = x
        self.y = y
        self.state = "S" # can be "S" (susceptible), "R" (resistant = dead), or
                         # "I" (infected)
        self.count = 0

    def infect(self):
        self.state = "I"

    def process(self, adjacent_cells):
        #print("CALL PROCESS")
        if self.state == "I":
            print("=== now the state is:", self.state)
            print(adjacent_cells)
            for cell in adjacent_cells:
                if cell.state == "S":
                    ran = random.random()
                    print("random number is: ", ran)
                    if ran < virality:
                        print("infect!")
                        cell.infect()
                        print(cell)
            self.count += 1
            if self.count > recovery_time:
                print("recover after", recovery_time, "steps")
                self.state = "S"

        else:
            pass



    def __repr__(self):
        return self.__str__()

    def __str__(self):
        return "<{}, {}, {}, {}>".format(self.x, self.y, self.state, self.count)

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
            if self.cells[(x,y)].state == 'S':
                image[x][y] = (0.0,1.0,0.0)
            if self.cells[(x,y)].state == 'I':
                print("CHANGE {},{} TO RED".format(x,y))
                image[x][y] = (1.0,0.0,0.0)
            if self.cells[(x,y)].state == 'R':
                print("CHANGE {},{} TO RED".format(x,y))
                image[x][y] = (0.5,0.5,0.5)


        plt.imshow(image)
        return image


    def adjacent_cells(self,x,y):
        cell_list = []

        try:
            if y+1 <= 150:
                cell_list.append(m.cells[(x,y+1)])
            if y-1 >= 0:
                cell_list.append(m.cells[(x,y-1)])
            if x-1 >= 0:
                cell_list.append(m.cells[(x-1,y)])
            if x+1 <= 150:
                cell_list.append(m.cells[(x+1,y)])
        except KeyError:
            pass

        return cell_list

    def time_step(self):
        print("IM IN TIME STEP")
        for x,y in self.cells:
            #print(self.cells[(x,y)])
            self.cells[(x,y)].process(self.adjacent_cells(x,y))
        self.display()


def read_map(filename):

    m = Map()

    # ... Write this function
    f = open(filename, 'r')
    for line in f:
        line = line.strip()
        fields = line.split(',')

        x = int(fields[0].strip())
        y = int(fields[1].strip())

        #print("adding", Cell(x,y))
        m.add_cell(Cell(x,y))

    return m



if __name__ == '__main__':
    m = read_map('nyc_map.csv')
    m.cells[(82,122)].infect()
    m.cells[(60,90)].infect()
    print(m.cells[(82,122)].state)
    print(m.cells[(60,90)].state)
    m.display()

#m.time_step()