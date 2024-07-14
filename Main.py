import random

class TreeNode:
    def __init__(self, value):
        self.value = value
        self.children = []
        self.h_n = random.randint(1, 6) 
        self.g_n = random.randint(1, 4)

    def add_child(self, child_node):
        self.children.append(child_node)

def build_tree():
    node_a = TreeNode('A')
    node_b = TreeNode('B')
    node_c = TreeNode('C')
    node_d = TreeNode('D')
    node_e = TreeNode('E')
    node_f = TreeNode('F')
    node_g = TreeNode('G')
    node_h = TreeNode('H')
    node_i = TreeNode('I')
    node_j = TreeNode('J')
    node_k = TreeNode('K')
    node_l = TreeNode('L')
    node_m = TreeNode('M')
    node_n = TreeNode('N')
    node_o = TreeNode('O')
    node_p = TreeNode('P')
    node_q = TreeNode('Q')
    node_r = TreeNode('R')
    node_s = TreeNode('S')
    node_t = TreeNode('T')
    node_u = TreeNode('U')
    node_v = TreeNode('V')
    node_w = TreeNode('W')
    node_x = TreeNode('X')
    node_y = TreeNode('Y')
    node_z = TreeNode('Z')

    node_a.add_child(node_b)
    node_a.add_child(node_c)
    node_b.add_child(node_d)
    node_b.add_child(node_e)
    node_c.add_child(node_f)
    node_c.add_child(node_g)
    node_d.add_child(node_h)
    node_d.add_child(node_i)
    node_e.add_child(node_j)
    node_e.add_child(node_k)
    node_f.add_child(node_l)
    node_f.add_child(node_m)
    node_g.add_child(node_n)
    node_g.add_child(node_o)
    node_h.add_child(node_p)
    node_h.add_child(node_q)
    node_i.add_child(node_r)
    node_j.add_child(node_s)
    node_j.add_child(node_t)
    node_l.add_child(node_u)
    node_l.add_child(node_v)
    node_m.add_child(node_w)
    node_n.add_child(node_x)
    node_o.add_child(node_y)
    node_o.add_child(node_z)

    node_a.g_n = 0
    return node_a

print("\n** Tip: Node(x,y) in tree structure refers to, 'x' is the h(n) and 'y' is the g(n) of the node.**\n")

def draw_tree(node, prefix='', is_tail=True):
    if node.value == 'A':
        print("\n" + prefix + '└── ' + node.value)
    else:
        print(prefix + ('└── ' if is_tail else '├── ') + node.value + "(" + str(node.h_n) + "," + str(node.g_n) + ")")

    child_count = len(node.children)
    for index, child in enumerate(node.children):
        draw_tree(child, prefix + ('    ' if is_tail else '│   '), index == child_count - 1)


def calculator(root):
    target_nodes = ['Z', 'X']  
    frontier = [(root, [], 0)]
    min_path = None
    min_f_n = float('inf')

    while frontier:
        node, path, accumulated_g_n = frontier.pop(0)
        
        # If the current node is one of the target nodes and the path is shorter
        if node.value in target_nodes and accumulated_g_n + node.h_n < min_f_n:
            min_f_n = accumulated_g_n + node.h_n +node.g_n
            min_path = path + [node.value]

        # Explore children
        for child in node.children:
            new_g_n = accumulated_g_n + node.g_n
            new_path = path + [node.value]
            # If the new path is shorter, add it to the frontier
            if new_g_n + child.h_n < min_f_n:
                frontier.append((child, new_path, new_g_n))

    if min_path:
        print(f"\nShortest Path: {min_path} with f(n) = {min_f_n}\n")
    else:
        print("No path found.")

def main():
    root = build_tree()
    print("Tree Structure:")
    draw_tree(root)
    calculator(root)

if __name__ == "__main__":
    main()
