import time
import random
import matplotlib.pyplot as plt
import numpy as np
from pysat.formula import CNF
from pysat.solvers import Solver

def generate_random_3sat(num_vars, num_clauses):
    """Generate a random 3-SAT instance."""
    instance = CNF()
    for _ in range(num_clauses):
        clause = [int(np.random.randint(1, num_vars + 1) * np.random.choice([-1, 1])) for _ in range(3)]
        instance.append(clause)
    return instance

def benchmark_solver(solver_name, instance):
    """Benchmark a SAT solver on a given instance."""
    solver = Solver(name=solver_name)
    for clause in instance.clauses:
        solver.add_clause(clause)

    start_time = time.time()
    result = solver.solve()
    end_time = time.time()

    return {
        'result': result,
        'time': end_time - start_time
    }

def run_benchmarks():
    """Run benchmarks on random 3-SAT instances."""
    num_vars_list = [20, 50, 100, 200]
    num_clauses_list = [90, 200, 400, 800]
    results = []

    for num_vars, num_clauses in zip(num_vars_list, num_clauses_list):
        instance = generate_random_3sat(num_vars, num_clauses)
        result = benchmark_solver('Glucose3', instance)
        results.append((num_vars, num_clauses, result['time']))

    return results

def plot_results(results):
    """Plot benchmark results."""
    x = [r[0] for r in results]  # Number of variables
    y = [r[2] for r in results]  # Time

    plt.plot(x, y, marker='o')
    plt.xlabel('Number of Variables')
    plt.ylabel('Time (s)')
    plt.title('3-SAT Benchmark Results')
    plt.grid(True)
    plt.show()

# Example usage
if __name__ == "__main__":
    results = run_benchmarks()
    plot_results(results)
