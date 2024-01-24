from pulp import LpProblem, LpMaximize, LpVariable


def run():
    lp_problem = LpProblem("Maximize_Production", LpMaximize)

    x1 = LpVariable("Lemonade", lowBound=0, cat="Integer")
    x2 = LpVariable("FruitJuice", lowBound=0, cat="Integer")

    lp_problem += x1 + x2, "Total_Production"

    water = 2 * x1 + x2 <= 100
    sugar = x1 <= 50
    lemon_juice = x1 <= 30
    fruit_puree = 2 * x2 <= 40

    lp_problem += water, "Water_Constraint"
    lp_problem += sugar, "Sugar_Constraint"
    lp_problem += lemon_juice, "LemonJuice_Constraint"
    lp_problem += fruit_puree, "FruitPuree_Constraint"

    lp_problem.solve()

    print("status:", lp_problem.status)
    print("Total_Production:", x1.varValue + x2.varValue)
    print("Lemonade_Production:", x1.varValue)
    print("FruitJuice_Production:", x2.varValue)


if __name__ == "__main__":
    run()