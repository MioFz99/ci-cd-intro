import math

from app.schema import TspSolverInput, Position


def convert_to_square_matrix(solver_input: TspSolverInput) -> list[list[float]]:
    """
    Builds an NxN distance matrix from the given 2D positions.
    Distance = Euclidean distance, diagonal = 0.0, symmetric.
    """
    pts = solver_input.positions
    n = len(pts)
    if n == 0:
        return []

    dist = [[0.0] * n for _ in range(n)]
    for i in range(n):
        xi, yi = pts[i].x, pts[i].y
        for j in range(i + 1, n):
            dx = xi - pts[j].x
            dy = yi - pts[j].y
            d = math.hypot(dx, dy)
            dist[i][j] = d
            dist[j][i] = d

    return dist


def convert_route_to_positions(solver_input: TspSolverInput, route: list[int]) -> list[Position]:
    """
    Converts a route (list of indices) to a list of Positions.
    """

    return [solver_input.positions[i] for i in route]
