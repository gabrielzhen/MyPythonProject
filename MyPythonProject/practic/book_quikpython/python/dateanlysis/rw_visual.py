import matplotlib.pyplot as plt
from random_walk import RandomWalk
while True:
    rw=RandomWalk()
    rw.fill_walk()
    point_numbers=list(range(rw.num_points))
    plt.scatter(rw.x_values,rw.y_values,c=point_numbers,s=10)
    plt.show()

    keep_walking=input("Make another walk?")
    if keep_walking=='n':
        break