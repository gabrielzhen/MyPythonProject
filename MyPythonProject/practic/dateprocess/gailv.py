import pandas as pd,random,numpy as np
import matplotlib.pyplot as plt

def flip_coin(times):
    data_array=np.empty(times)
    weight_array=np.empty(times)
    weight_array.fill(1/times)

    for i in range(0,times):
        data_array[i]=random.randint(0,1)

    print(data_array)
    print(weight_array)

flip_coin(10)