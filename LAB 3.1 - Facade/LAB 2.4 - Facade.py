import random
class Generator:
    def generate(self, amount):
        return [random.randint(1,9) for num in range(amount)]
class Splitter:
    def split(self, matrix):
        parts = []
        parts.extend(matrix)
        size = len(matrix)
        for j in range(size):
            parts.append([row[j] for row in matrix])
        parts.append([matrix[i][i] for i in range(size)])
        parts.append([matrix[i][size - 1 - i] for i in range(size)])
        return parts   
    
class Verifier:
    def verify(self, parts): 
        if len(set([sum(row) for row in parts])) == 1: return True
        else: return False

class MagicSquareGenerator:
    def generate(self, size):
        run = True
        while run:
            g = Generator()
            numbrid = g.generate(size*size)
            list = []
            for i in range(0, size*size, size):
                list.append(numbrid[i:i+size])
            s = Splitter()
            list_osad = s.split(list)
            v = Verifier()
            kas_tõene = v.verify(list_osad)
            if kas_tõene == True:
                return list
gen = MagicSquareGenerator()
square = gen.generate(3)

for row in square:
    print(row)