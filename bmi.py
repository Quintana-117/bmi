peso = float(input("INGRESE SU PESO: "))  
altura = float(input("Ingrese su altura: "))  

bmi = peso / (altura ** 2)  # Eliminamos indentación incorrecta

if bmi < 18.5:
    categoria = "bajo peso"
elif 18.5 <= bmi < 24.9:
    categoria = "peso normal"
elif 25 <= bmi < 29.9:
    categoria = "sobrepeso"
else:
    categoria = "obesidad"  # Corregí "onesidad" a "obesidad"

print(f"Tu masa corporal es {bmi:.2f}, lo que indica: {categoria}.")
