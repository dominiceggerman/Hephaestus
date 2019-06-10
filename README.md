# Hephaestus
Gas scheduling optimization problem.

## Ideas for gas routing problem
- Create an interconnect matrix, where i (location) connects to j (destination), the lookup will be able to route through the matrix looking for a particular indicies of j.
- Since the paths are static, routes can be pre-built and calculations made based on changing capacities / rates.
- Program to build paths out of the interconnect matrix, with simple logic to not double back (drops j on each move), to check if a move to another j will be profitable (j["price"] > i["price"], and that capacity exists.