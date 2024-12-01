import pathlib
import sys

class SolutionInput:
    def __init__(self):
        self.list1 = []
        self.list2 = []
    
    def addToLists(self, values):
        self.list1.append(int(values[0]))
        self.list2.append(int(values[1]))

    def sortLists(self):
        self.list1.sort()
        self.list2.sort()

def parse(input):
    """ Parsing the input file """
    #print(f"{input}")
    lines = input.split('\n')
    solInput = SolutionInput()

    for line in lines:
        values = line.split()
        solInput.addToLists(values)
    
    return solInput

def solution(input):
    """first get the frequencies of the numbers in list 2"""
    frequencies = dict()
    for element in input.list2:
        if element in frequencies:
            frequencies[element] = frequencies[element] + 1
        else:
            frequencies[element] = 1

    """then calculate the similarities"""
    similarity_score = 0
    for element in input.list1:
        if element in frequencies:
            similarity_score += element * frequencies[element]

    return similarity_score

if __name__ == "__main__":
    for path in sys.argv[1:]:
        print(f"\n{path}:")

        puzzle_input = pathlib.Path(path).read_text().strip()
        input = parse(puzzle_input)

        print(f"{solution(input)}")