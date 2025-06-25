n1 = int(input("Digite o numero 1:"))

n2 = int(input("Digite o numero 2:"))

n3 = int(input("Digite o numero 3:"))

if n1 >= n2 and n1 >= n3:
    print(f"O maior valor é {n1}")
elif n2 >= n1 and n2 >= n3:
    print(f"O maior valor é {n2}")
elif n3 >= n1 and n3 >= n2:
    print(f"O maior valor é {n3}")

# maior = max(n1,n2,n3)
# print(f"O maior valor é {maior}")