# HillClimbingSearch - Traveling Salesman Problem Solver

HillClimbingSearch is a Python module that provides a simple implementation of the hill climbing algorithm to solve the Traveling Salesman Problem (TSP). The TSP is a classic optimization problem that seeks to find the shortest possible route that visits a set of cities exactly once and returns to the origin city. In this implementation, we use a random start and iteratively improve the solution using local search.

## Installation

Before using this module, ensure that you have the required dependencies installed. You can install them using `pip`:

```bash
pip install numpy networkx
```

## Example Usage

Here's an example of how to use the `hill_climbing` function to solve a TSP with a list of city coordinates:


```python
import random import numpy as np from HillClimbingSearch import hill_climbing  


# Define your city coordinates 
city_coordinates = [     [0, 0],     [1, 2],     [3, 1],     [2, 3],     [4, 4], ]  
# Solve the TSP using the hill climbing algorithm 
shortest_path_length, best_solution = hill_climbing(city_coordinates)  print("Shortest Path Length:", shortest_path_length) print("Best Solution Order:", best_solution)
```

## Functions

### `hill_climbing(coordinate)`

Solves the TSP using the hill climbing algorithm.

- `coordinate`: A list of coordinates representing the cities.

Returns the shortest path length and the best solution order.

### `generate_matrix(coordinate)`

Generates an adjacency matrix for a weighted graph based on the given coordinates.

- `coordinate`: A list of coordinates representing the cities.

Returns a square matrix where each element represents the distance between two cities.

### `solution(matrix)`

Finds a random solution to the TSP.

- `matrix`: The adjacency matrix of the cities.

Returns a random order in which cities are visited.

### `path_length(matrix, solution)`

Calculates the length of the path based on a given solution.

- `matrix`: The adjacency matrix of the cities.
- `solution`: The order in which cities are visited.

Returns the total length of the path.

### `neighbors(matrix, solution)`

Generates neighbors of a given solution by swapping cities and returns the best neighbor.

- `matrix`: The adjacency matrix of the cities.
- `solution`: The order in which cities are visited.

Returns the best neighbor solution and its length.

## License

This module is available under the MIT License.

Feel free to use and modify this code for your own projects. If you find any issues or have suggestions for improvements, please create an issue or a pull request on [GitHub](https://github.com/Quantlight/Hill-Climbing-Search.git).

## Author

This module was created by Quantlight and is maintained on [GitHub](https://github.com/Quantlight/Hill-Climbing-Search.git).

## Acknowledgments

This implementation is inspired by the classic Traveling Salesman Problem and the hill climbing optimization algorithm. It's a simple example and may not be the most efficient solution for large-scale TSP instances.
