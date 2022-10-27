import numpy as np
import matplotlib.pyplot as plt
 
a = {'person': 29381,
 'car': 136663,
 'truck': 5669,
 'bicycle': 13798,
 'traffic light': 18228,
 'motorcycle': 14164,
 'bus': 3607,
 'train': 1273,
 'airplane': 428,
 'boat': 220}

b = {'motorcycle': 3365,
 'car': 28571,
 'person': 5613,
 'truck': 1236,
 'traffic light': 2586,
 'bicycle': 2040,
 'airplane': 143,
 'bus': 442,
 'train': 264,
 'boat': 35} 

plt.bar(0, a.values())
plt.savefig('adam.png')