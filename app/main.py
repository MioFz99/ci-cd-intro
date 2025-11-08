import asyncio
import os.path

from fastapi import FastAPI
from fastapi.params import Query
from fastapi.responses import FileResponse

from app.mappers import convert_to_square_matrix, convert_route_to_positions
from app.schema import TspSolverInput, TspSolverResult
from app.tsp import tsp_bruteforce

app = FastAPI()


@app.get("/")
async def read_index():
    return FileResponse(os.path.join(os.path.dirname(__file__), '../static/index.html'))


@app.post("/solve")
async def solve(
        solver_input: TspSolverInput,
        timeout_seconds: float = Query(5.0, title="Max seconds allowed for solving (default 5s)", lt=10, ge=0)
) -> TspSolverResult:
    matrix = convert_to_square_matrix(solver_input)

    min_distance, best_route_idx, optimal = await asyncio.wait_for(
        asyncio.to_thread(tsp_bruteforce, matrix, timeout_seconds),
        timeout=timeout_seconds
    )

    return TspSolverResult(
        min_distance=min_distance,
        route=convert_route_to_positions(solver_input, best_route_idx),
        optimal=optimal
    )
