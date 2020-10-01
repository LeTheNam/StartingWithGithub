from __future__ import print_function
from ortools.linear_solver import pywraplp
import numpy as np

def LinearProgrammingTest():
    solver = pywraplp.Solver.CreateSolver("linear_programming", "GLOP")
    x = solver.NumVar(0, solver.infinity(), 'x')
    y = solver.NumVar(0, solver.infinity(), 'y')

    Constraint1 = solver.Constraint(-solver.infinity(), 7)
    Constraint1.SetCoefficient(x, 2)
    Constraint1.SetCoefficient(y, 1)

    Constraint1 = solver.Constraint(-solver.infinity(), 8)
    Constraint1.SetCoefficient(x, 1)
    Constraint1.SetCoefficient(y, 2)

    Constraint1 = solver.Constraint(-solver.infinity(), 2)
    Constraint1.SetCoefficient(x, 1)
    Constraint1.SetCoefficient(y, -1)

    #objective function
    obj = solver.Objective()
    obj.SetCoefficient(x, 3)
    obj.SetCoefficient(y, 2)
    obj.SetMaximization()

    solver.Solve()
    opt_solution = 3 * x.solution_value() + 2 * y.solution_value()
    print('Number of variables =', solver.NumVariables())
    print('Number of constraints =', solver.NumConstraints())
    # The value of each variable in the solution.
    print('Solution:')
    print('x = ', x.solution_value())
    print('y = ', y.solution_value())
    # The objective value of the solution.
    print('Optimal objective value =', opt_solution)

def LP_TSP(n):
    X = np.array([n, n])



def main():
    # LinearProgrammingTest()
    LP_TSP(5)

if __name__ == '__main__':
    main()