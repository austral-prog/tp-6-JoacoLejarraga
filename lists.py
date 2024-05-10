def remove_elements(lista):
	del lista[0]
	del lista [3]
	del lista [3]
	return lista

def add_elements(lista):
	lista.insert(0, "Pink")
	lista.append("Yellow")
	return lista

def is_empty(lista):
	if lista:
		return False
	else:
		return True

def check_lists(lista, lista2):
	if lista[2] == lista2[2]:
		return True
	else:
		return False

def list_of_lists(lista1, lista2, lista3):
	new_lista1 = lista1[0:2]
	new_lista2 = lista2[1:4]
	new_lista3 = lista3[-2:]
	lista_externa = [new_lista1, new_lista2, new_lista3]
	return lista_externa
