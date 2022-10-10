import math
import random

from collections import defaultdict
from itertools import chain


def papadimitriou(clauses):
    variables = set(map(abs, chain(*clauses)))
    n = len(variables)
    if n == 0:
        return True

    outer_loop_count = int(math.log(n, 2))
    inner_loop_count = 2 * n**2

    for i in range(outer_loop_count):
        assignment = _choose_random_variables_assignment(variables)

        for j in range(inner_loop_count):
            unsatisfied_clauses = _get_unsatisfied_clauses(clauses, assignment)
            if unsatisfied_clauses == []:
                return True
            elif len(unsatisfied_clauses) == 1:
                # possible loop clause
                x, y = unsatisfied_clauses[0]
                if (
                    ((-x, -y) in clauses or (-y, -x) in clauses)
                    and ((-x, y) in clauses or (y, -x) in clauses)
                    and ((x, -y) in clauses or (-y, x) in clauses)
                ):
                    return False  # unsatisfiable set of clauses (loop)

            random_variable = _pick_random_variable_to_flip(unsatisfied_clauses)
            assignment[random_variable] = not assignment[random_variable]
            assignment[-random_variable] = not assignment[random_variable]

    return False


def reduce_clauses(clauses):
    # if a given variable is always used in only one form (itself or negated)
    # remove all clauses that contain it (can be satisfied with no side effects)

    clauses_dict = defaultdict(set)
    reduced_clauses = clauses
    for x, y in clauses:
        clauses_dict[x].add((x, y))
        clauses_dict[y].add((x, y))

    while True:
        remaining_variables = set(chain(*reduced_clauses))
        variables_to_reduce = [
            x for x in remaining_variables if -x not in remaining_variables
        ]

        if variables_to_reduce == []:
            break

        for singular_form_variable in variables_to_reduce:
            for clause in clauses_dict[singular_form_variable].copy():
                reduced_clauses.remove(clause)
                clauses_dict[clause[0]].remove(clause)
                # cannot remove (x, x) clause twice
                if clause[0] != clause[1]:
                    clauses_dict[clause[1]].remove(clause)

    return reduced_clauses


def _choose_random_variables_assignment(variables):
    assignment = {}
    boolean_sequence = [True, False]
    for variable in variables:
        assignment[variable] = random.choice(boolean_sequence)
        assignment[-variable] = not assignment[variable]

    return assignment


def _get_unsatisfied_clauses(clauses, assignment):
    return [x for x in clauses if not (assignment[x[0]] | assignment[x[1]])]


def _pick_random_variable_to_flip(unsatisfied_clauses):
    random_unsatisfied_clause = random.choice(unsatisfied_clauses)
    return abs(random.choice(random_unsatisfied_clause))
