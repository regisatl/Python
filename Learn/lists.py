myList = [1, 2, 3, 4, 5] # déclaration de la list

myList.append(6) # append() permet d'ajouter un élément à la suite de la liste

myList.insert(2, 3.5) # insert() permet d'ajouter un élément à une position donnée dans la liste

myList.remove(5) # remove() permet de supprimer un élément spécifique de la liste que l'on doit préciser

myList.pop(5) # pop() permet de supprimer un élément spécifique de la liste avec son index

myList[2] = 100 # on n'a remplaçer à la position 2 dans la liste l'élément par 100

print(myList) # imprimer la liste
print(len(myList)) # imprimer la longueur de la liste