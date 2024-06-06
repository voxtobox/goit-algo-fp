from task_4 import Node, add_edges, draw_tree, array_to_heap, build_max_heap
import matplotlib.pyplot as plt
import networkx as nx
import colorsys

def generate_color_palette(num_colors):
    colors = []
    for i in range(num_colors):
        lightness = 0.3 + 0.7 * (i / num_colors)  # Від темного до світлого
        r, g, b = colorsys.hsv_to_rgb(0.6, 1, lightness)  # Синій колір (hue=0.6)
        colors.append('#%02x%02x%02x' % (int(r * 255), int(g * 255), int(b * 255)))
    return colors

def bfs(root):
    queue = [root]
    order = []
    while queue:
        node = queue.pop(0)
        order.append(node)
        if node.left:
            queue.append(node.left)
        if node.right:
            queue.append(node.right)
    return order

def dfs(root):
    stack = [root]
    order = []
    while stack:
        node = stack.pop()
        order.append(node)
        if node.right:
            stack.append(node.right)
        if node.left:
            stack.append(node.left)
    return order

def visualize_traversal(root, traversal_func):
    order = traversal_func(root)
    colors = generate_color_palette(len(order))
    node_colors = {node.id: colors[i] for i, node in enumerate(order)}
    draw_tree_with_colors(root, node_colors)

def draw_tree_with_colors(tree_root, node_colors):
    tree = nx.DiGraph()
    pos = {tree_root.id: (0, 0)}
    tree = add_edges(tree, tree_root, pos)

    colors = [node_colors[node[0]] for node in tree.nodes(data=True)]
    labels = {node[0]: node[1]['label'] for node in tree.nodes(data=True)}

    plt.figure(figsize=(8, 5))
    nx.draw(tree, pos=pos, labels=labels, arrows=False, node_size=2500, node_color=colors)
    plt.show()

if __name__ == "__main__":
  # Масив для побудови бінарної купи
  arr = [3, 1, 6, 5, 2, 4]

  # Побудова максимальної купи з масиву
  build_max_heap(arr)

  # Створення бінарної купи з масиву
  heap_root = array_to_heap(arr)

  # Візуалізація BFS
  print("BFS Traversal:")
  visualize_traversal(heap_root, bfs)

  # Візуалізація DFS
  print("DFS Traversal:")
  visualize_traversal(heap_root, dfs)
