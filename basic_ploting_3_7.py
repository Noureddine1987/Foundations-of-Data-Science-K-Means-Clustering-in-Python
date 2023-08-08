import matplotlib.pyplot as plt
import matplotlib.patches as patches
import numpy as np
# xs = [10, 100, 25, 67, 74]
# ys = [125, 26, 66, 1, 10]
xyz = [[10, 125], [100, 26], [25, 66], [67, 1], [74, 10]]
xyz = np.array(xyz)
print(xyz)
xx = xyz[:, 0]
yy = xyz[:, 1]
print(xx, '====', yy)
# np.mean(xyz, 0) ==> 0 means per line & 1 means per column
mean_xy = np.mean(xyz, 0)
mean_xy2 = xyz.mean(0)
print('vector_mean list function =', mean_xy2)
print('vector_mean =', mean_xy)
std_dev = np.std(xyz, 0)
print('std dev', std_dev)
ellipse = patches.Ellipse([mean_xy[0], mean_xy[1]], std_dev[0]*3, std_dev[1]*3, alpha=0.25)
fig, graph = plt.subplots()
graph.scatter(xx, yy)
graph.scatter(mean_xy[0], mean_xy[1])
graph.add_patch(ellipse)
# plt.plot() with connection line however plt.scatter print out points
# plt.plot(xs, ys)
# plt.scatter(xs, ys)
plt.show()

# calculate the eucludian distance :
# np.sqrt(np.sum((x1 - x2) * (x1 - x2))) or built-in function np.linalg.norm(x1-x2)
print(xyz[0]-mean_xy)
print('distance btw', xyz[0], 'and ', mean_xy, ':', np.linalg.norm(xyz[0]-mean_xy))
print('distance btw', xyz[1], 'and ', mean_xy, ':', np.linalg.norm(xyz[1]-mean_xy))
print('distance btw', xyz[2], 'and ', mean_xy, ':', np.linalg.norm(xyz[2]-mean_xy))
print('distance btw', xyz[3], 'and ', mean_xy, ':', np.linalg.norm(xyz[3]-mean_xy))
print('='*50)
print(np.linalg.norm(xyz[:, :]-mean_xy))
