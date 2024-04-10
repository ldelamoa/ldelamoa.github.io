import matplotlib.pyplot as plt
from matplotlib.patches import Arc
import numpy as np

# Creem una base de dades de relacions laborals
database_connections = [
    ('Alice', 'Bob'), ('Alice', 'Charlie'), ('Alice', 'David'),
    ('Bob', 'Eva'), ('Bob', 'Frank'), ('Bob', 'Grace'),
    ('Charlie', 'David'), ('Charlie', 'Hannah'),
    ('David', 'Eva'), ('David', 'Isabel'),
    ('Eva', 'Jack'), ('Eva', 'Kim'), ('Eva', 'Liam'),
    ('Frank', 'Grace'), ('Frank', 'Hannah'),
    ('Grace', 'Peter'), ('Grace', 'Quinn'),
    ('Hannah', 'Isabel'), ('Hannah', 'Jack'),
    ('Isabel', 'Kim'), ('Isabel', 'Liam')]

# Extraiem els nodes únics, els ordenem i creem mapes de les posicions
nodes = sorted(set(sum(database_connections, ())))
node_positions = {node: pos for pos, node in enumerate(nodes)}

plt.figure(figsize=(15, 8))
ax = plt.gca()

# Posicions i color dels nodes
colors = plt.cm.tab20b(np.linspace(0, 1, len(nodes)))
node_colors = {node: colors[i] for i, node in enumerate(nodes)}
x = np.linspace(0, 1, len(nodes))
y = np.zeros(len(nodes))

# Dibuixem els nodes amb els seus colors
for i, node in enumerate(nodes):
    plt.scatter(x[i], y[i], s=200, color='grey', zorder=3)
    plt.annotate(node, (x[i], y[i]), textcoords="offset points", xytext=(0, -20), ha='center', fontsize=10)

# Dibuixem els arcs amb els colors corresponents al node d'origen
for start, end in database_connections:
    start_pos = node_positions[start]
    end_pos = node_positions[end]
    arc_height = abs(end_pos - start_pos) / 3.0  # Adjust arc height if necessary
    arc = Arc([(x[start_pos] + x[end_pos]) / 2, 0], x[end_pos] - x[start_pos], arc_height,
              angle=0, theta1=0, theta2=180, color=node_colors[start], lw=3, zorder=2)
    plt.gca().add_patch(arc)

# Fixem els límits i aspecte de la gràfica
plt.xlim(-0.1, 1.1)
plt.ylim(-0.5, 1.5)  # Increase the y-limit to fit arcs
plt.axis('off')
plt.gca().spines[['top', 'right', 'bottom', 'left']].set_visible(False)

# Afegim un títol
plt.title('Connexions laborals', fontsize=20, pad=20)

# Guardem la gràfica amb un fons blanc
plt.savefig('connexions_laborals.png', bbox_inches='tight', facecolor='white')

# Mostrem la gràfica
plt.show()
