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
                next_nodes.add(next_node)
        current_nodes = next_nodes
        steps += 1
    return steps


instructions, nodes = read_input('Input.txt')
steps = navigate(instructions, nodes)
print(f'It takes {steps} steps to reach ZZZ.')
