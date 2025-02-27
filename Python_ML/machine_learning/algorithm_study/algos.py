import tensorflow
import numpy
import sklearn
'''
FROM GPT
'''

'''Search'''
# binary search
def binary_search(arr, target):
    left, right = 0, len(arr) - 1
    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return -1

# KNN
from sklearn.neighbors import KNeighborsClassifier

X_train, y_train = [[1, 2], [3, 4], [5, 6]], [0, 1, 1]
knn = KNeighborsClassifier(n_neighbors=3)
knn.fit(X_train, y_train)
print(knn.predict([[4, 5]]))

'''Sort'''

# merge sort
def merge_sort(arr):
    if len(arr) <= 1:
        return arr
    mid = len(arr) // 2
    left, right = merge_sort(arr[:mid]), merge_sort(arr[mid:])
    return merge(left, right)

def merge(left, right):
    sorted_arr = []
    while left and right:
        sorted_arr.append(left.pop(0) if left[0] < right[0] else right.pop(0))
    return sorted_arr + left + right

'''Graph'''

# BFS
from collections import deque

def bfs(graph, start):
    queue, visited = deque([start]), set()
    while queue:
        node = queue.popleft()
        if node not in visited:
            print(node, end=" ")
            visited.add(node)
            queue.extend(graph[node])

# Dijkstra
import heapq

def dijkstra(graph, start):
    pq, distances = [(0, start)], {node: float('inf') for node in graph}
    distances[start] = 0
    while pq:
        current_dist, current_node = heapq.heappop(pq)
        for neighbor, weight in graph[current_node].items():
            dist = current_dist + weight
            if dist < distances[neighbor]:
                distances[neighbor] = dist
                heapq.heappush(pq, (dist, neighbor))
    return distances

'''Optimization'''

# GD
import numpy as np

def gradient_descent(X, y, learning_rate=0.01, epochs=1000):
    m, n = X.shape
    theta = np.zeros(n)
    for _ in range(epochs):
        gradient = -2/m * X.T @ (y - X @ theta)
        theta -= learning_rate * gradient
    return theta

# simulated annealing ???
import random, math

def simulated_annealing(cost_function, initial_state, temp=1.0, cooling_rate=0.99, min_temp=0.01):
    state = initial_state
    while temp > min_temp:
        new_state = state + random.uniform(-1, 1)
        cost_diff = cost_function(new_state) - cost_function(state)
        if cost_diff < 0 or random.uniform(0, 1) < math.exp(-cost_diff / temp):
            state = new_state
        temp *= cooling_rate
    return state

'''ML'''

# LR
from sklearn.linear_model import LinearRegression

X, y = [[1], [2], [3]], [2, 4, 6]
model = LinearRegression().fit(X, y)
print(model.predict([[4]]))  # Output: [8]

# decision tree
from sklearn.tree import DecisionTreeClassifier

X, y = [[0], [1], [2], [3]], [0, 0, 1, 1]
clf = DecisionTreeClassifier().fit(X, y)
print(clf.predict([[1.5]]))  # Expected: [0]

# svm
from sklearn.svm import SVC

X, y = [[0, 0], [1, 1]], [0, 1]
clf = SVC(kernel='linear').fit(X, y)
print(clf.predict([[0.8, 0.8]]))  # Expected: [1]


'''Neural Nets'''

# basic NN
import numpy as np

def sigmoid(x): return 1 / (1 + np.exp(-x))

X = np.array([[0,0], [0,1], [1,0], [1,1]])
y = np.array([[0], [1], [1], [0]])

weights = np.random.randn(2,1)
for _ in range(1000):
    output = sigmoid(np.dot(X, weights))
    weights += np.dot(X.T, (y - output) * output * (1 - output))

print(output)  # Should approximate XOR

# deep learning
import tensorflow as tf

model = tf.keras.Sequential([
    tf.keras.layers.Dense(10, activation="relu"),
    tf.keras.layers.Dense(1, activation="sigmoid")
])
model.compile(optimizer="adam", loss="binary_crossentropy")

# q-learing (reinforcement)
import numpy as np

Q = np.zeros((5, 2))  # 5 states, 2 actions
alpha, gamma, epsilon = 0.1, 0.9, 0.1

for episode in range(1000):
    state = np.random.randint(0, 5)
    action = np.argmax(Q[state]) if np.random.rand() > epsilon else np.random.randint(0, 2)
    next_state = (state + action) % 5
    reward = 1 if next_state == 4 else 0
    Q[state, action] = Q[state, action] + alpha * (reward + gamma * np.max(Q[next_state]) - Q[state, action])


'''
--Which Algorithms Should You Prioritize--

[For AI & ML Jobs]
- Gradient Descent (optimization, neural networks)
- Decision Trees & SVMs (classification)
- Neural Networks (NumPy, TensorFlow, PyTorch)
- Graph Algorithms (BFS, Dijkstra) (used in AI search problems)
- Reinforcement Learning (Q-Learning, Policy Gradients)

[For Interviews & Coding Challenges]
- Sorting (Merge Sort, Quick Sort)
- Graph Traversal (DFS, BFS, Dijkstra)
- Dynamic Programming (Knapsack, Longest Common Subsequence)
- Matrix Operations (Eigenvalues, Singular Value Decomposition)
- Bit Manipulation (XOR, bitwise tricks)
'''