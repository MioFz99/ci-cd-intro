from pydantic import BaseModel


class Position(BaseModel):
    x: float
    y: float


class TspSolverInput(BaseModel):
    positions: list[Position]


class TspSolverResult(BaseModel):
    min_distance: float
    route: list[Position]
    optimal: bool
