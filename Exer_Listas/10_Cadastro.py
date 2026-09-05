notas = [7.5, 8.0, 9.0, 10.0]

print("Notas:", notas)

media = sum(notas) / len(notas)

print(f"Media: {media:.2f}")

print("Maior: ", max(notas))
print("Menor: ", min(notas))

if media >= 7:
    print("Aprovado")
else:
    print("Reprovado")