def remove_elements(list1):
	del list1[0:1]
	del list1[3:4]
	del list1[3:4]
	return list1

def add_elements(list2):
	list2.insert(0, "Pink")
	list2.append("Yellow")
	return list2

def is_empty(list3):
	if list3:
		return False
	else:
		return True

def check_lists(list4, list5):
	if is_empty(list4) or is_empty(list5):
		return False
	else:
		if list4[2:3] == list5[2:3]:
			return True
		else:
			return False

def list_of_lists(lista):
	new_lista1 = lista[0][0:2]
	new_lista2 = lista[1][1:4]
	new_lista3 = lista[2][-2:]
	lista_externa = [new_lista1, new_lista2, new_lista3]
	return lista_externa

