import numpy as np
import random
from settings import BOARD_SIZE


class GameLogic:
    def __init__(self):
        self.gameboard = np.zeros((BOARD_SIZE, BOARD_SIZE), dtype=int)
    

    def __str__(self):
        """Str representation of the 2048 gameboard."""
        return str(self.gameboard)
    

    def place_random(self, n=1):
        """Places an even integer between 2 or 4 into a randomly selected empty cell."""
        empty_cells = list(zip(*np.where(self.gameboard == 0)))
        for cell in random.sample(empty_cells, k=n):
            self.gameboard[cell] = 4 if (random.random() < .1) else 2
    
    @staticmethod
    def gather_nums(gameboard) -> np.ndarray:
        curr_nums = gameboard[gameboard != 0]
        updated_nums = []
        skip = False
        
        for j in range(len(curr_nums)):
            if (skip):
                skip = False
                continue
            if (j != len(curr_nums) - 1) and (curr_nums[j] == curr_nums[j+1]):
                updated_nums.append(curr_nums[j] * 2)
                skip = True
            else:
                updated_nums.append(curr_nums[j])
        return np.array(updated_nums)

    def move(self, direction: str):
        for i in range(4):
            curr_sequence = self.gameboard[i, :] if (direction == 'a') else self.gameboard[:, i]
            reverse = False
            
            if (direction == 'd'):
                reverse = True
                curr_sequence = curr_sequence[::-1]
            
            curr_nums = GameLogic.gather_nums(curr_sequence)
            updated_board = np.zeros_like(curr_sequence)
            updated_board[:len(curr_nums)] = curr_nums
            
            if (reverse):
                curr_nums = curr_nums[::-1]
            if (direction == 'a'):
                self.gameboard[i, :] = curr_nums
            else:
                self.gameboard[:, i] = curr_nums
            
    

    def run(self):
        """Main loop of the running game."""
        self.place_random(2)

        while True:
            print(self.gameboard)

            cmd = input("Enter w, a, s, d, or q to quit: ")
            if (cmd == 'q'):
                break
            
            self.move(cmd)
            self.place_random()
            



if __name__ == "__main__":
    test = np.zeros( (4, 4), dtype=int)
    
    test[1][1] = 8
    test[1][3] = 2
    print(test, "\n")
    testcopy = test[1, :]
    
    test3 = testcopy[testcopy != 0]
    test4 = np.zeros_like(testcopy)
    test4[:len(test3)] = test3
    
    test[1, :] = test4
    print(type(test))
    


