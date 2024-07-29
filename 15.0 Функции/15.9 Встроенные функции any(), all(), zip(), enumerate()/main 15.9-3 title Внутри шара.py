abscissas = [float(i) for i in str(input()).split()]
ordinates = [float(j) for j in str(input()).split()]
applicates = [float(k) for k in str(input()).split()]
R = 2

print(all(map(lambda x : x[0] ** 2 + x[1] ** 2 + x[2] ** 2 <= R ** 2, list(zip(abscissas, ordinates, applicates)))))
