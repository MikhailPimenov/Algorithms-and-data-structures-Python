import copy
import unittest
from .solve import solve as algorithm
from others.loopover.simulator.simulator import simulator as simulator_algorithm


def print_board(board: list):
    for i in range(len(board)):
        for j in range(len(board[i])):
            print(f'{board[i][j]:<5}', end='')
        print()


class MyTestCase(unittest.TestCase):
    def test_something(self):
        total_steps = 0

        pattern = [
            ['1', '2'],
            ['3', '4'],
        ]
        solved_pattern = [
            ['1', '2'],
            ['3', '4'],
        ]
        board_for_moves = copy.deepcopy(pattern)
        moves = algorithm(board_for_moves, solved_pattern)
        if moves is not None:
            total_steps += len(moves)


        board_for_simulator = copy.deepcopy(pattern)
        simulator_algorithm(board_for_simulator, moves)
        self.assertEqual(solved_pattern, board_for_simulator, 'test #2')

        pattern = [
            ['4', '2'],
            ['3', '1'],
        ]
        solved_pattern = [
            ['1', '2'],
            ['3', '4'],
        ]
        board_for_moves = copy.deepcopy(pattern)
        moves = algorithm(board_for_moves, solved_pattern)
        if moves is not None:
            total_steps += len(moves)


        board_for_simulator = copy.deepcopy(pattern)
        simulator_algorithm(board_for_simulator, moves)
        self.assertEqual(solved_pattern, board_for_simulator, 'test #3')

        pattern = [
            ['A', 'C', 'D', 'B', 'E'],
            ['F', 'G', 'H', 'I', 'J'],
            ['K', 'L', 'M', 'N', 'O'],
            ['P', 'Q', 'R', 'S', 'T'],
        ]
        solved_pattern = [
            ['A', 'B', 'C', 'D', 'E'],
            ['F', 'G', 'H', 'I', 'J'],
            ['K', 'L', 'M', 'N', 'O'],
            ['P', 'Q', 'R', 'S', 'T'],
        ]
        board_for_moves = copy.deepcopy(pattern)
        moves = algorithm(board_for_moves, solved_pattern)
        if moves is not None:
            total_steps += len(moves)

        # print(moves)

        board_for_simulator = copy.deepcopy(pattern)
        simulator_algorithm(board_for_simulator, moves)
        self.assertEqual(solved_pattern, board_for_simulator, 'test #4')

        pattern = [
            ['A', 'C', 'D', 'B', 'E'],
            ['F', 'G', 'H', 'I', 'J'],
            ['K', 'L', 'M', 'N', 'O'],
            ['P', 'Q', 'R', 'S', 'T'],
            ['U', 'V', 'W', 'X', 'Y'],
        ]
        solved_pattern = [
            ['A', 'B', 'C', 'D', 'E'],
            ['F', 'G', 'H', 'I', 'J'],
            ['K', 'L', 'M', 'N', 'O'],
            ['P', 'Q', 'R', 'S', 'T'],
            ['U', 'V', 'W', 'X', 'Y'],
        ]
        board_for_moves = copy.deepcopy(pattern)
        moves = algorithm(board_for_moves, solved_pattern)
        if moves is not None:
            total_steps += len(moves)

        # print(moves)

        board_for_simulator = copy.deepcopy(pattern)
        simulator_algorithm(board_for_simulator, moves)
        self.assertEqual(solved_pattern, board_for_simulator, 'test #5')

        pattern = [
            ['A', 'B', 'C', 'D', 'E'],
            ['K', 'G', 'H', 'I', 'J'],
            ['P', 'L', 'M', 'N', 'O'],
            ['F', 'Q', 'R', 'S', 'T'],
            ['U', 'V', 'W', 'X', 'Y'],
        ]
        solved_pattern = [
            ['A', 'B', 'C', 'D', 'E'],
            ['F', 'G', 'H', 'I', 'J'],
            ['K', 'L', 'M', 'N', 'O'],
            ['P', 'Q', 'R', 'S', 'T'],
            ['U', 'V', 'W', 'X', 'Y'],
        ]
        board_for_moves = copy.deepcopy(pattern)
        moves = algorithm(board_for_moves, solved_pattern)
        if moves is not None:
            total_steps += len(moves)

        # print(moves)

        board_for_simulator = copy.deepcopy(pattern)
        simulator_algorithm(board_for_simulator, moves)
        self.assertEqual(solved_pattern, board_for_simulator, 'test #6')

        pattern = [
            ['C', 'W', 'M', 'F', 'J'],
            ['O', 'R', 'D', 'B', 'A'],
            ['N', 'K', 'G', 'L', 'Y'],
            ['P', 'H', 'S', 'V', 'E'],
            ['X', 'T', 'Q', 'U', 'I'],
        ]
        solved_pattern = [
            ['A', 'B', 'C', 'D', 'E'],
            ['F', 'G', 'H', 'I', 'J'],
            ['K', 'L', 'M', 'N', 'O'],
            ['P', 'Q', 'R', 'S', 'T'],
            ['U', 'V', 'W', 'X', 'Y'],
        ]
        board_for_moves = copy.deepcopy(pattern)
        moves = algorithm(board_for_moves, solved_pattern)
        if moves is not None:
            total_steps += len(moves)

        # print(moves)

        board_for_simulator = copy.deepcopy(pattern)
        simulator_algorithm(board_for_simulator, moves)
        self.assertEqual(solved_pattern, board_for_simulator, 'test #7')

        pattern = [
            ['W', 'C', 'M', 'D', 'J'],
            ['O', 'R', 'F', 'B', 'A'],
            ['K', 'N', 'G', 'L', 'Y'],
            ['P', 'H', 'V', 'S', 'E'],
            ['T', 'X', 'Q', 'U', 'I'],
        ]
        solved_pattern = [
            ['A', 'B', 'C', 'D', 'E'],
            ['F', 'G', 'H', 'I', 'J'],
            ['K', 'L', 'M', 'N', 'O'],
            ['P', 'Q', 'R', 'S', 'T'],
            ['U', 'V', 'W', 'X', 'Y'],
        ]
        board_for_moves = copy.deepcopy(pattern)
        moves = algorithm(board_for_moves, solved_pattern)
        if moves is not None:
            total_steps += len(moves)

        # print(moves)

        board_for_simulator = copy.deepcopy(pattern)
        simulator_algorithm(board_for_simulator, moves)
        self.assertNotEqual(solved_pattern, board_for_simulator, 'test #8')

        pattern = [
            ['W', 'C', 'M', 'D', 'J', '0'],
            ['O', 'R', 'F', 'B', 'A', '1'],
            ['K', 'N', 'G', 'L', 'Y', '2'],
            ['P', 'H', 'V', 'S', 'E', '3'],
            ['T', 'X', 'Q', 'U', 'I', '4'],
            ['Z', '5', '6', '7', '8', '9'],
        ]
        solved_pattern = [
            ['A', 'B', 'C', 'D', 'E', 'F'],
            ['G', 'H', 'I', 'J', 'K', 'L'],
            ['M', 'N', 'O', 'P', 'Q', 'R'],
            ['S', 'T', 'U', 'V', 'W', 'X'],
            ['Y', 'Z', '0', '1', '2', '3'],
            ['4', '5', '6', '7', '8', '9'],
        ]
        board_for_moves = copy.deepcopy(pattern)
        moves = algorithm(board_for_moves, solved_pattern)
        if moves is not None:
            total_steps += len(moves)

        # print(moves)

        board_for_simulator = copy.deepcopy(pattern)
        simulator_algorithm(board_for_simulator, moves)
        self.assertEqual(solved_pattern, board_for_simulator, 'test #9')

        pattern_string = 'DE\nAC\nBF'
        pattern = list(map(list, pattern_string.splitlines()))

        solved_pattern_string = 'AB\nCD\nEF'
        solved_pattern = list(map(list, solved_pattern_string.splitlines()))

        board_for_moves = copy.deepcopy(pattern)
        moves = algorithm(board_for_moves, solved_pattern)
        if moves is not None:
            total_steps += len(moves)

        # print(moves)

        board_for_simulator = copy.deepcopy(pattern)
        simulator_algorithm(board_for_simulator, moves)
        self.assertEqual(solved_pattern, board_for_simulator, 'test #10')

        pattern = [['C', 'A'], ['D', 'B']]
        solved_pattern = [['A', 'B'], ['C', 'D']]
        board_for_moves = copy.deepcopy(pattern)
        moves = algorithm(board_for_moves, solved_pattern)
        if moves is not None:
            total_steps += len(moves)

        # print(moves)

        board_for_simulator = copy.deepcopy(pattern)
        simulator_algorithm(board_for_simulator, moves)
        self.assertEqual(solved_pattern, board_for_simulator, 'test #11')

        pattern = [
            ['B', 's', 'g', 'i', 'b', 'Z', 'Q', 'd', 'h'],
            ['j', 'Y', 'l', 'O', 'D', 'W', 'X', 'E', 'P'],
            ['e', 'R', 'H', 'k', 'm', 'o', 'I', 'V', 'M'],
            ['f', 'r', 'a', 'N', 'L', 'K', 'J', 'G', 'A'],
            ['p', 'C', 'c', 'n', 'S', 'U', 'T', 'q', 'F']
        ]
        solved_pattern = [
            ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I'],
            ['J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R'],
            ['S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', 'a'],
            ['b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j'],
            ['k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's']
        ]
        board_for_moves = copy.deepcopy(pattern)
        moves = algorithm(board_for_moves, solved_pattern)
        if moves is not None:
            total_steps += len(moves)

        # print(moves)

        board_for_simulator = copy.deepcopy(pattern)
        simulator_algorithm(board_for_simulator, moves)
        self.assertNotEqual(solved_pattern, board_for_simulator, 'test #12')

        pattern = [
            ['W', 'Z', 'C', 'Y', 'e'],
            ['I', 'J', 'A', 'E', 'V'],
            ['T', 'h', 'c', 'P', 'U'],
            ['i', 'F', 'D', 'L', 'G'],
            ['O', 'X', 'R', 'a', 'g'],
            ['H', 'd', 'M', 'B', 'b'],
            ['K', 'Q', 'S', 'N', 'f']
        ]
        solved_pattern = [
            ['A', 'B', 'C', 'D', 'E'],
            ['F', 'G', 'H', 'I', 'J'],
            ['K', 'L', 'M', 'N', 'O'],
            ['P', 'Q', 'R', 'S', 'T'],
            ['U', 'V', 'W', 'X', 'Y'],
            ['Z', 'a', 'b', 'c', 'd'],
            ['e', 'f', 'g', 'h', 'i']
        ]
        board_for_moves = copy.deepcopy(pattern)
        moves = algorithm(board_for_moves, solved_pattern)
        if moves is not None:
            total_steps += len(moves)

        # print(moves)

        board_for_simulator = copy.deepcopy(pattern)
        simulator_algorithm(board_for_simulator, moves)
        self.assertEqual(solved_pattern, board_for_simulator, 'test #13')

        pattern = [
            ['J', 'F', 'V'],
            ['R', 'I', 'W'],
            ['U', 'S', 'C'],
            ['N', 'A', 'Q'],
            ['P', 'G', 'K'],
            ['E', 'H', 'X'],
            ['L', 'T', 'B'],
            ['D', 'M', 'O']
        ]
        solved_pattern = [
            ['A', 'B', 'C'],
            ['D', 'E', 'F'],
            ['G', 'H', 'I'],
            ['J', 'K', 'L'],
            ['M', 'N', 'O'],
            ['P', 'Q', 'R'],
            ['S', 'T', 'U'],
            ['V', 'W', 'X']
        ]
        board_for_moves = copy.deepcopy(pattern)
        moves = algorithm(board_for_moves, solved_pattern)
        if moves is not None:
            total_steps += len(moves)

        # print(moves)

        board_for_simulator = copy.deepcopy(pattern)
        simulator_algorithm(board_for_simulator, moves)
        self.assertEqual(solved_pattern, board_for_simulator, 'test #14')

        pattern = [
            ['Q', 'P', 'B', 'N', 'E', 'L', 'D'],
            ['K', 'A', 'O', 'U', 'G', 'C', 'F'],
            ['M', 'I', 'T', 'R', 'J', 'H', 'S']
        ]
        solved_pattern = [
            ['A', 'B', 'C', 'D', 'E', 'F', 'G'],
            ['H', 'I', 'J', 'K', 'L', 'M', 'N'],
            ['O', 'P', 'Q', 'R', 'S', 'T', 'U']
        ]
        board_for_moves = copy.deepcopy(pattern)
        moves = algorithm(board_for_moves, solved_pattern)
        if moves is not None:
            total_steps += len(moves)

        # print(moves)

        board_for_simulator = copy.deepcopy(pattern)
        simulator_algorithm(board_for_simulator, moves)
        self.assertNotEqual(solved_pattern, board_for_simulator, 'test #15')

        pattern = [
            ['Y', 'β', 'j', 'O', 'K', 'i', 'Z', 'α'],
            ['J', 'D', '8', 'E', 'f', 'p', 'g', 'o'],
            ['A', 'w', 'B', '4', 'U', 'C', 'q', 'd'],
            ['L', 'V', 'H', 'b', 'h', 'R', 'x', 'W'],
            ['c', 't', '3', 'k', 'v', '1', '2', 'F'],
            ['I', 's', 'N', 'S', 'T', '0', 'y', '6'],
            ['l', '7', 'G', 'm', 'a', 'r', 'P', 'X'],
            ['e', 'z', '5', 'u', '9', 'Q', 'n', 'M']
        ]
        solved_pattern = [
            ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H'],
            ['I', 'J', 'K', 'L', 'M', 'N', 'O', 'P'],
            ['Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X'],
            ['Y', 'Z', 'a', 'b', 'c', 'd', 'e', 'f'],
            ['g', 'h', 'i', 'j', 'k', 'l', 'm', 'n'],
            ['o', 'p', 'q', 'r', 's', 't', 'u', 'v'],
            ['w', 'x', 'y', 'z', '0', '1', '2', '3'],
            ['4', '5', '6', '7', '8', '9', 'α', 'β']
        ]
        board_for_moves = copy.deepcopy(pattern)
        moves = algorithm(board_for_moves, solved_pattern)
        if moves is not None:
            total_steps += len(moves)

        # print(moves)

        board_for_simulator = copy.deepcopy(pattern)
        simulator_algorithm(board_for_simulator, moves)
        self.assertEqual(solved_pattern, board_for_simulator, 'test #16')

        pattern = [
            ['Z', 'X', 'e', 'h', 'I', 'N'],
            ['K', 'a', 'H', 'j', 'T', 'C'],
            ['c', 'E', 'F', 'U', 'D', 'R'],
            ['d', 'L', 'Y', 'Q', 'V', 'O'],
            ['S', 'b', 'M', 'A', 'P', 'J'],
            ['g', 'i', 'W', 'B', 'f', 'G']
        ]
        solved_pattern = [
            ['A', 'B', 'C', 'D', 'E', 'F'],
            ['G', 'H', 'I', 'J', 'K', 'L'],
            ['M', 'N', 'O', 'P', 'Q', 'R'],
            ['S', 'T', 'U', 'V', 'W', 'X'],
            ['Y', 'Z', 'a', 'b', 'c', 'd'],
            ['e', 'f', 'g', 'h', 'i', 'j']
        ]
        board_for_moves = copy.deepcopy(pattern)
        moves = algorithm(board_for_moves, solved_pattern)
        if moves is not None:
            total_steps += len(moves)

        # print(moves)

        board_for_simulator = copy.deepcopy(pattern)
        simulator_algorithm(board_for_simulator, moves)
        self.assertEqual(solved_pattern, board_for_simulator, 'test #17')

        pattern = [
            ['L', 'I', 'H', 'G', 'B', 'E', 'N'],
            ['K', 'F', 'D', 'M', 'A', 'J', 'C']
        ]
        solved_pattern = [
            ['A', 'B', 'C', 'D', 'E', 'F', 'G'],
            ['H', 'I', 'J', 'K', 'L', 'M', 'N']
        ]
        board_for_moves = copy.deepcopy(pattern)
        moves = algorithm(board_for_moves, solved_pattern)
        if moves is not None:
            total_steps += len(moves)

        # print(moves)

        board_for_simulator = copy.deepcopy(pattern)
        simulator_algorithm(board_for_simulator, moves)
        self.assertEqual(solved_pattern, board_for_simulator, 'test #18')

        pattern = [
            ['V', 'T', 'E', 'S', 'D'],
            ['O', 'W', 'K', 'N', 'J'],
            ['A', 'Y', 'B', 'X', 'F'],
            ['H', 'G', 'M', 'C', 'I'],
            ['L', 'P', 'Q', 'R', 'U']
        ]
        solved_pattern = [
            ['A', 'B', 'C', 'D', 'E'],
            ['F', 'G', 'H', 'I', 'J'],
            ['K', 'L', 'M', 'N', 'O'],
            ['P', 'Q', 'R', 'S', 'T'],
            ['U', 'V', 'W', 'X', 'Y']
        ]
        board_for_moves = copy.deepcopy(pattern)
        moves = algorithm(board_for_moves, solved_pattern)
        if moves is not None:
            total_steps += len(moves)

        # print(moves)

        board_for_simulator = copy.deepcopy(pattern)
        simulator_algorithm(board_for_simulator, moves)
        self.assertEqual(solved_pattern, board_for_simulator, 'test #19')

        pattern = [
            ['d', 'F', 'Q', 'e', 'T', 'G'],
            ['E', 'l', 'p', 'A', 'N', 'c'],
            ['C', 'W', 'R', 'O', 'B', 'f'],
            ['U', 'm', 'g', 'H', 'j', 'n'],
            ['a', 'h', 'M', 'K', 'b', 'k'],
            ['J', 'I', 'Y', 'V', 'X', 'S'],
            ['D', 'P', 'L', 'o', 'i', 'Z']
        ]
        solved_pattern = [
            ['A', 'B', 'C', 'D', 'E', 'F'],
            ['G', 'H', 'I', 'J', 'K', 'L'],
            ['M', 'N', 'O', 'P', 'Q', 'R'],
            ['S', 'T', 'U', 'V', 'W', 'X'],
            ['Y', 'Z', 'a', 'b', 'c', 'd'],
            ['e', 'f', 'g', 'h', 'i', 'j'],
            ['k', 'l', 'm', 'n', 'o', 'p']
        ]
        board_for_moves = copy.deepcopy(pattern)
        moves = algorithm(board_for_moves, solved_pattern)
        if moves is not None:
            total_steps += len(moves)

        # print(moves)

        board_for_simulator = copy.deepcopy(pattern)
        simulator_algorithm(board_for_simulator, moves)
        self.assertEqual(solved_pattern, board_for_simulator, 'test #20')

        pattern = [
            ['P', 'T', 'H'],
            ['C', 'O', 'M'],
            ['A', 'K', 'I'],
            ['B', 'E', 'R'],
            ['U', 'N', 'W'],
            ['S', 'D', 'X'],
            ['J', 'Q', 'L'],
            ['G', 'V', 'F']
        ]
        solved_pattern = [
            ['A', 'B', 'C'],
            ['D', 'E', 'F'],
            ['G', 'H', 'I'],
            ['J', 'K', 'L'],
            ['M', 'N', 'O'],
            ['P', 'Q', 'R'],
            ['S', 'T', 'U'],
            ['V', 'W', 'X']
        ]
        board_for_moves = copy.deepcopy(pattern)
        moves = algorithm(board_for_moves, solved_pattern)
        if moves is not None:
            total_steps += len(moves)

        # print(moves)

        board_for_simulator = copy.deepcopy(pattern)
        simulator_algorithm(board_for_simulator, moves)
        self.assertEqual(solved_pattern, board_for_simulator, 'test #21')


        pattern = [
            ['L', 'N', 'W', 'F', 'U'],
            ['O', 'D', 'K', 'C', 'V'],
            ['Q', 'X', 'G', 'H', 'J'],
            ['S', 'M', 'E', 'I', 'R'],
            ['B', 'A', 'T', 'Y', 'P']
        ]
        solved_pattern = [
            ['A', 'B', 'C', 'D', 'E'],
            ['F', 'G', 'H', 'I', 'J'],
            ['K', 'L', 'M', 'N', 'O'],
            ['P', 'Q', 'R', 'S', 'T'],
            ['U', 'V', 'W', 'X', 'Y']
        ]
        board_for_moves = copy.deepcopy(pattern)
        moves = algorithm(board_for_moves, solved_pattern)
        if moves is not None:
            total_steps += len(moves)

        # print(moves)

        board_for_simulator = copy.deepcopy(pattern)
        simulator_algorithm(board_for_simulator, moves)
        self.assertEqual(solved_pattern, board_for_simulator, 'test #22')

        pattern = [
            ['C', 'E', 'Q', 'A'],
            ['H', 'S', 'M', 'F'],
            ['O', 'I', 'R', 'G'],
            ['D', 'B', 'T', 'P'],
            ['N', 'L', 'J', 'K']
        ]
        solved_pattern = [
            ['A', 'B', 'C', 'D'],
            ['E', 'F', 'G', 'H'],
            ['I', 'J', 'K', 'L'],
            ['M', 'N', 'O', 'P'],
            ['Q', 'R', 'S', 'T']
        ]
        board_for_moves = copy.deepcopy(pattern)
        moves = algorithm(board_for_moves, solved_pattern)
        if moves is not None:
            total_steps += len(moves)

        # print(moves)

        board_for_simulator = copy.deepcopy(pattern)
        simulator_algorithm(board_for_simulator, moves)
        self.assertEqual(solved_pattern, board_for_simulator, 'test #23')

        pattern = [
            ['U', 'c', 'S', 'X', 'T'],
            ['Q', 'I', 'F', 'L', 'Z'],
            ['R', 'D', 'A', 'K', 'W'],
            ['Y', 'V', 'M', 'N', 'J'],
            ['O', 'd', 'G', 'C', 'P'],
            ['H', 'B', 'a', 'E', 'b']
        ]
        solved_pattern = [
            ['A', 'B', 'C', 'D', 'E'],
            ['F', 'G', 'H', 'I', 'J'],
            ['K', 'L', 'M', 'N', 'O'],
            ['P', 'Q', 'R', 'S', 'T'],
            ['U', 'V', 'W', 'X', 'Y'],
            ['Z', 'a', 'b', 'c', 'd']
        ]
        board_for_moves = copy.deepcopy(pattern)
        moves = algorithm(board_for_moves, solved_pattern)
        if moves is not None:
            total_steps += len(moves)

        # print(moves)

        board_for_simulator = copy.deepcopy(pattern)
        simulator_algorithm(board_for_simulator, moves)
        self.assertEqual(solved_pattern, board_for_simulator, 'test #24')

        pattern = [
            ['R', 'a', 'B', 'O', 'S', 'N', 'V'],
            ['J', 'I', 'U', 'A', 'P', 'X', 'Q'],
            ['H', 'M', 'K', 'C', 'F', 'L', 'Y'],
            ['G', 'T', 'E', 'W', 'Z', 'b', 'D']
        ]
        solved_pattern = [
            ['A', 'B', 'C', 'D', 'E', 'F', 'G'],
            ['H', 'I', 'J', 'K', 'L', 'M', 'N'],
            ['O', 'P', 'Q', 'R', 'S', 'T', 'U'],
            ['V', 'W', 'X', 'Y', 'Z', 'a', 'b']
        ]
        board_for_moves = copy.deepcopy(pattern)
        moves = algorithm(board_for_moves, solved_pattern)
        if moves is not None:
            total_steps += len(moves)

        # print(moves)

        board_for_simulator = copy.deepcopy(pattern)
        simulator_algorithm(board_for_simulator, moves)
        self.assertEqual(solved_pattern, board_for_simulator, 'test #25')

        pattern = [
            ['a', 'T', 'k', 'Y', 'g', 'i', '1', 'v'],
            ['c', 'd', 'B', 'O', 'Q', 't', 'N', 'L'],
            ['o', 'm', 'P', 'u', 'G', 'y', '2', 'F'],
            ['e', 'H', 'r', 'l', 'j', 'U', 'A', 'M'],
            ['E', 'x', 'w', 'Z', 'q', 'D', 'n', 's'],
            ['p', 'J', 'C', 'h', 'K', 'V', 'S', 'R'],
            ['X', 'I', 'f', 'b', 'W', 'z', '0', '3']
        ]
        solved_pattern = [
            ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H'],
            ['I', 'J', 'K', 'L', 'M', 'N', 'O', 'P'],
            ['Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X'],
            ['Y', 'Z', 'a', 'b', 'c', 'd', 'e', 'f'],
            ['g', 'h', 'i', 'j', 'k', 'l', 'm', 'n'],
            ['o', 'p', 'q', 'r', 's', 't', 'u', 'v'],
            ['w', 'x', 'y', 'z', '0', '1', '2', '3']
        ]
        board_for_moves = copy.deepcopy(pattern)
        moves = algorithm(board_for_moves, solved_pattern)
        if moves is not None:
            total_steps += len(moves)

        # print(moves)

        board_for_simulator = copy.deepcopy(pattern)
        simulator_algorithm(board_for_simulator, moves)
        self.assertEqual(solved_pattern, board_for_simulator, 'test #26')

        pattern = [
            ['D', 'P', 'I', 'J', 'C', 'H', 'B', 'A'],
            ['O', 'M', 'K', 'E', 'G', 'N', 'L', 'F']
        ]
        solved_pattern = [
            ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H'],
            ['I', 'J', 'K', 'L', 'M', 'N', 'O', 'P']
        ]
        board_for_moves = copy.deepcopy(pattern)
        moves = algorithm(board_for_moves, solved_pattern)
        if moves is not None:
            total_steps += len(moves)

        # print(moves)

        board_for_simulator = copy.deepcopy(pattern)
        simulator_algorithm(board_for_simulator, moves)
        self.assertEqual(solved_pattern, board_for_simulator, 'test #27')

        pattern = [
            ['d', 'A', 'j', 'T', 't', 'L', 'V', 'D'],
            ['E', 'q', 'f', 'e', 'Z', 'p', 'l', 'Y'],
            ['G', 'h', 'O', 'S', 'v', 'c', 'n', 'm'],
            ['W', 'i', 'K', 'a', 'I', 'N', 'Q', 'g'],
            ['k', 'X', 'C', 'b', 'J', 'r', 'P', 'u'],
            ['B', 'F', 'H', 'M', 'U', 'o', 'R', 's']
        ]
        solved_pattern = [
            ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H'],
            ['I', 'J', 'K', 'L', 'M', 'N', 'O', 'P'],
            ['Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X'],
            ['Y', 'Z', 'a', 'b', 'c', 'd', 'e', 'f'],
            ['g', 'h', 'i', 'j', 'k', 'l', 'm', 'n'],
            ['o', 'p', 'q', 'r', 's', 't', 'u', 'v']
        ]
        board_for_moves = copy.deepcopy(pattern)
        moves = algorithm(board_for_moves, solved_pattern)
        if moves is not None:
            total_steps += len(moves)

        # print(moves)

        board_for_simulator = copy.deepcopy(pattern)
        simulator_algorithm(board_for_simulator, moves)
        self.assertEqual(solved_pattern, board_for_simulator, 'test #28')

        pattern = [
            ['C', 'B', 'X', 'U'],
            ['H', 'A', 'Q', 'N'],
            ['I', 'J', 'V', 'D'],
            ['T', 'E', 'F', 'S'],
            ['M', 'K', 'R', 'G'],
            ['W', 'O', 'P', 'L']
        ]
        solved_pattern = [
            ['A', 'B', 'C', 'D'],
            ['E', 'F', 'G', 'H'],
            ['I', 'J', 'K', 'L'],
            ['M', 'N', 'O', 'P'],
            ['Q', 'R', 'S', 'T'],
            ['U', 'V', 'W', 'X']
        ]
        board_for_moves = copy.deepcopy(pattern)
        moves = algorithm(board_for_moves, solved_pattern)
        if moves is not None:
            total_steps += len(moves)

        # print(moves)

        board_for_simulator = copy.deepcopy(pattern)
        simulator_algorithm(board_for_simulator, moves)
        self.assertEqual(solved_pattern, board_for_simulator, 'test #29')

        pattern = [
            ['m', 'h', 'w', 'q', 'z', 'M', 'Y'],
            ['s', 'P', 'R', 't', 'x', 'Q', 'j'],
            ['g', 'b', 'i', 'V', 'r', 'A', 'X'],
            ['I', 'U', 'c', 'd', 'u', 'E', 'n'],
            ['G', 'p', 'e', '0', 'f', 'B', '1'],
            ['y', 'C', 'Z', 'O', 'H', 'l', '3'],
            ['T', 'k', 'S', 'F', 'o', 'J', 'N'],
            ['D', 'L', 'K', 'v', '2', 'W', 'a']
        ]
        solved_pattern = [
            ['A', 'B', 'C', 'D', 'E', 'F', 'G'],
            ['H', 'I', 'J', 'K', 'L', 'M', 'N'],
            ['O', 'P', 'Q', 'R', 'S', 'T', 'U'],
            ['V', 'W', 'X', 'Y', 'Z', 'a', 'b'],
            ['c', 'd', 'e', 'f', 'g', 'h', 'i'],
            ['j', 'k', 'l', 'm', 'n', 'o', 'p'],
            ['q', 'r', 's', 't', 'u', 'v', 'w'],
            ['x', 'y', 'z', '0', '1', '2', '3']
        ]
        board_for_moves = copy.deepcopy(pattern)
        moves = algorithm(board_for_moves, solved_pattern)
        if moves is not None:
            total_steps += len(moves)

        # print(moves)

        board_for_simulator = copy.deepcopy(pattern)
        simulator_algorithm(board_for_simulator, moves)
        self.assertEqual(solved_pattern, board_for_simulator, 'test #30')

        pattern = [
            ['B', 'O', 'S', 'E', 'T', 'H', 'X', 'R'],
            ['K', 'F', 'M', 'P', 'C', 'L', 'Q', 'U'],
            ['J', 'W', 'A', 'D', 'N', 'V', 'G', 'I']
        ]
        solved_pattern = [
            ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H'],
            ['I', 'J', 'K', 'L', 'M', 'N', 'O', 'P'],
            ['Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X']
        ]
        board_for_moves = copy.deepcopy(pattern)
        moves = algorithm(board_for_moves, solved_pattern)
        if moves is not None:
            total_steps += len(moves)

        # print(moves)

        board_for_simulator = copy.deepcopy(pattern)
        simulator_algorithm(board_for_simulator, moves)
        self.assertEqual(solved_pattern, board_for_simulator, 'test #31')

        pattern = [
            ['L', 'K'],
            ['F', 'J'],
            ['G', 'M'],
            ['B', 'P'],
            ['E', 'C'],
            ['N', 'O'],
            ['D', 'H'],
            ['I', 'A']
        ]
        solved_pattern = [
            ['A', 'B'],
            ['C', 'D'],
            ['E', 'F'],
            ['G', 'H'],
            ['I', 'J'],
            ['K', 'L'],
            ['M', 'N'],
            ['O', 'P']
        ]
        board_for_moves = copy.deepcopy(pattern)
        moves = algorithm(board_for_moves, solved_pattern)
        if moves is not None:
            total_steps += len(moves)
        # print(moves)

        board_for_simulator = copy.deepcopy(pattern)
        simulator_algorithm(board_for_simulator, moves)
        self.assertEqual(solved_pattern, board_for_simulator, 'test #32')

        print('total_steps =', total_steps)

if __name__ == '__main__':
    unittest.main()
