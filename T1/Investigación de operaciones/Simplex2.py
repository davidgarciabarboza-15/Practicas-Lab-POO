from scipy.optimize import linprog, linprog_verbose_callback

c = [-5, -4, -3]
A = [[2, 3, 1],
     [4, 1, 2],  # Corregí tu error: tenías [4, 2, 2]
     [3, 4, 2]]
b = [5, 11, 8]

print("--- INICIANDO ITERACIONES DEL MÉTODO SIMPLEX ---")
res = linprog(c, A_ub=A, b_ub=b, bounds=(0, None), 
              method='simplex', callback=linprog_verbose_callback)

print("\n--- RESULTADO ÓPTIMO ---")
print(f"x1 = {res.x[0]:.2f}")
print(f"x2 = {res.x[1]:.2f}")
print(f"x3 = {res.x[2]:.2f}")
print(f"Valor máximo de Z = {-res.fun:.2f}")

