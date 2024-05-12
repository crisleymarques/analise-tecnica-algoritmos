def trocaElementos(arr1, arr2):
    soma1 = sum(arr1)
    soma2 = sum(arr2)
    resultado = []

    for i in range(len(arr1)):
      for j in range(len(arr2)):
        if soma1 - arr1[i] + arr2[j] == soma2 - arr2[j] + arr1[i]:
          resultado.append(arr1[i])
          resultado.append(arr2[j])
          return resultado
    return []

print(trocaElementos([0, 2, 2], [1, 2, 3])) # [0, 1]
print(trocaElementos([1, 2, 3], [4, 5])) # [] 
print(trocaElementos([2, 3, 4], [1, 2, 3, 3])) # [2, 2]
print(trocaElementos([1, 5], [3, 3])) # []