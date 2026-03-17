import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle

# given boxes
det = (10, 10, 50, 50)   # (x1, y1, x2, y2)
gt  = (30, 30, 70, 70)

fig, ax = plt.subplots()

# convert (x1,y1,x2,y2) -> (x, y, width, height)
def add_box(ax, box, edgecolor, label):
    x1, y1, x2, y2 = box
    w, h = x2 - x1, y2 - y1
    rect = Rectangle((x1, y1), w, h,
                     linewidth=2,
                     edgecolor=edgecolor,
                     facecolor='none',
                     label=label)
    ax.add_patch(rect)

add_box(ax, det, 'red',  'det')
add_box(ax, gt,  'green','gt')

ax.set_xlim(0, 80)
ax.set_ylim(0, 80)
ax.set_aspect('equal')
ax.grid(True)
ax.legend()
plt.xlabel("x")
plt.ylabel("y")
plt.title("det and gt rectangles")
plt.show()
