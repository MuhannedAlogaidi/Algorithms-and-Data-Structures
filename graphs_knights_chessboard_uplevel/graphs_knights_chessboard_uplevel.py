# ************************ Graphs: Knights on a Chessboard *********************************
# DAM 12/30/2021
# You are given a rows * cols chessboard and a knight that moves like in normal chess. 
# Currently knight is at starting position denoted by start_row th row and start_col th col, 
# and want to reach at ending position denoted by end_row th row and end_col th col.  
# The goal is to calculate the minimum number of moves that the knight needs to take 
# to get from starting position to ending position.
# start_row, start_col, end_row and end_col are 0-indexed. 

# A chess knight has eight possible moves it can make, as illustrated in "knight.png". 
# Each move is two cells in a cardinal direction, then one cell in an orthogonal direction.

# Each time the knight is to move, it chooses one of eight possible moves uniformly at random
# (even if the piece would go off the chessboard) and moves there.

# The knight continues moving until it has made exactly k moves or has moved off the chessboard.

# ******************************************************************************************
import os
from collections import deque

# Knight directional moves are defined as a list of tuples
DIRECTIONS = [(2, 1), (2, -1), (-2, 1), (-2, -1), (1, 2), (1, -2), (-1, 2), (-1, -2)]


def find_minimum_number_of_moves(rows, cols, start_row, start_col, end_row, end_col):

    # position the knight
    start_cell = start_row, start_col

    # visited dictionary set to keep track of visited cells
    visited = {start_cell}

    # make a queue with cell and number of moves to get to that cell
    q = deque([(start_cell, 0)])

    # while loop for queue
    while q:
        cell, count = q.popleft()
        if cell == (end_row, end_col):
            return count

        # using * operator to convert tuple into 2 arguments as get_neighbors function expects
        for new_cell in get_neighbors(*cell, rows, cols):

            # testing
            #if new_cell == (3, 3):
            #    print("cell (3, 3) reached.")
            #    os.system("pause")

            if new_cell not in visited:
                q.append((new_cell, count + 1))
                visited.add(new_cell)

    return -1

# When a problem presented includes a given graph structured as a grid (rows/columns),
# an adjacency list is not needed and the neighbor vertices can be dynamically calculated by
# a getNeighbors function.

def get_neighbors(r, c, rows, cols):

    # list for neighbor vertices
    neighbors = []

    # iterate through DIRECTIONS list to calculate possible row/column moves 
    for dr, dc in DIRECTIONS:
        # calculate move: add row/column to current square
        new_r, new_c = r + dr, c + dc

        # Is this a legal move (stay within chessboard grid)?
        if 0 <= new_r < rows and 0 <= new_c < cols:
            neighbors.append((new_r, new_c))

    return neighbors


print(find_minimum_number_of_moves(5, 5, 0, 0, 4, 1))