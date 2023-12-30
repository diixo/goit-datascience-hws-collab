import numpy as np

######################################################## 1.
arr1 = np.arange(1, 11, 1, dtype=int)
print(arr1)

arr1 = np.linspace(1, 10, num=10, endpoint=True, dtype=int)
print(arr1)

######################################################### 2.

m = np.zeros((3, 3), dtype=int)
print(m)

######################################################### 3.
m = np.random.randint(1, 10+1, size=(5, 5))
print(m)
######################################################### 4.
m = np.random.rand(4, 4)
print(m)
######################################################### 5.

arr1 = np.random.randint(1, 10+1, size=5)
arr2 = np.random.randint(1, 10+1, size=5)

print(arr1, arr2)
result = arr1 + arr2
print(result)
result = arr1 - arr2
print(result)
result = arr1 * arr2
print(result)
######################################################### 6.

arr1 = np.random.rand(7)
arr2 = np.random.rand(7)
result = np.dot(arr1, arr2)

######################################################### 7.

m1 = np.random.randint(1, 10+1, size=(2, 2))
m2 = np.random.randint(1, 10+1, size=(2, 3))
result = np.dot(m1, m2)
print(result)

######################################################### 8.

m = np.random.randint(1, 10+1, size=(3, 3))
m_inv = np.linalg.inv(m)
print(m_inv)

######################################################### 9.
m = np.random.rand(4, 4)
m_T = m.T
print(m_T)

######################################################## 10.
# (m, n)*(n, p) = (m, p)
m = np.random.randint(1, 10+1, size=(3, 4))
v = np.random.randint(1, 10+1, size = 4)
result = np.dot(m, v)
print(result)

######################################################### 11.
m = np.random.rand(2, 3)
v = np.random.rand(3)
result = np.dot(m, v)
print(result)

######################################################### 12.
m1 = np.random.randint(1, 10+1, size=(2, 2))
m2 = np.random.randint(1, 10+1, size=(2, 2))
result = m1 * m2
print(result)

######################################################### 13.
m1 = np.random.randint(1, 10+1, size=(2, 2))
m2 = np.random.randint(1, 10+1, size=(2, 2))
result = np.dot(m1, m2)
print(result)

######################################################### 14.
m = np.random.randint(1, 100+1, size=(5, 5))
print(m, m.sum())

######################################################### 15.
m1 = np.random.randint(1, 10+1, size=(4, 4))
m2 = np.random.randint(1, 10+1, size=(4, 4))
print(m1 - m2)

######################################################### 16.
m = np.random.rand(3, 3)
print(m)
v = np.sum(m, axis=1)
print(v)

######################################################### 17.
m = np.random.randint(1, 10+1, size=(3, 4))
print(m)
result = m * m
print(result)

######################################################### 18.
v = np.random.randint(1, 50+1, size=4)
print(v)
result = np.sqrt(v)
print(result)
