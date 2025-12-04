# calculadora.py
# Script básico para operaciones matemáticas
numero_1 = float(input("Primer número: "))
numero_2 = float(input("Segundo número: "))
operacion = input("Operación (+, -, *, /): ")
if operacion == '+':
print("Resultado:", numero_1 + numero_2)
elif operacion == '-':
print("Resultado:", numero_1 - numero_2)
elif operacion == '*':
print("Resultado:", numero_1 * numero_2)
elif operacion == '/':
if b != 0:
print("Resultado:", numero_1 / numero_2)
else:
print("Error: no se puede dividir por cero.")
4. Guardar, hacer commit y subir a GitHub:
5. Agregar mejoras y subir una segunda versión:
6. Entregar la URL del repositorio.
else:
print("Operación no válida.")
git add .
git commit -m "Primer commit: calculadora básica"
git remote add origin https://github.com/tuusuario/calculadora_basica.git
git push -u origin 
