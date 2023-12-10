import math

def read_input(file_name):
    with open(file_name, 'r') as file:
        lines = file.readlines()
    instructions = list(lines[0].strip())  # Split the instructions into individual characters
    nodes = {}
    for line in lines[1:]:
        if ' = ' in line:
            node, paths = line.strip().split(' = ')
            nodes[node] = tuple(paths[1:-1].split(', '))
    return instructions, nodes


def navigate(instructions, nodes):
    current_nodes = {node for node in nodes if node.endswith('A')}
    steps = 0
    while not all(node.endswith('Z') for node in current_nodes):
        next_nodes = set()
        for node in current_nodes:
            for instruction in instructions:
                next_node = nodes[node][0 if instruction == 'L' else 1]
                if next_node not in current_nodes:
                    next_nodes.add(next_node)
        if not next_nodes:
            break
        current_nodes = next_nodes
        steps += 1
    return steps


lines = read_input("Input.txt")
instructions, nodes = read_input('Input.txt')  # Verwende die Funktion 'read_input'
total_steps = 1

for node in nodes:  # Ändere 'connections' zu 'nodes'
    if node.endswith('A'):
        print(f"\nNavigating from starting node: {node}")
        steps = navigate(instructions, nodes)  # Verwende die Funktion 'navigate'
        print(f"Steps to reach a node ending with 'Z' from {node}: {steps}")
        total_steps = math.lcm(total_steps, steps)

print("\nPart 2: Total steps for simultaneous navigation:", total_steps)
