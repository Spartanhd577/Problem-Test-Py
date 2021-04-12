
dictionary = [
{'dayOfWeek': 'Thu', 'city': 'Azores', 'timeValue': 1538020800000, 'day': 27, 'country': 'PT'},
{'dayOfWeek': 'Thu', 'city': 'Atafu', 'timeValue': 1538020800000, 'day': 27, 'country': 'TK'},
{'dayOfWeek': 'Thu', 'city': 'California', 'timeValue': 1538020800000, 'day': 27, 'country': 'US'},
{'dayOfWeek': 'Thu', 'city': 'Santiago', 'timeValue': 1536206400000, 'day': 6, 'country': 'DO'},
{'dayOfWeek': 'Thu', 'city': 'Lualaba', 'timeValue': 1538020800000, 'day': 27, 'country': 'CD'},
{'dayOfWeek': 'Thu', 'city': 'Santiago', 'timeValue': 1536811200000, 'day': 13, 'country': 'DO'},
{'dayOfWeek': 'Mon', 'city': 'Santiago', 'timeValue': 1536552000000, 'day': 10, 'country': 'DO'},
{'dayOfWeek': 'Thu', 'city': 'Khabarovsk', 'timeValue': 1538020800000, 'day': 27, 'country': 'RU'},
{'dayOfWeek': 'Fri', 'city': 'California', 'timeValue': 1538107200000, 'day': 28, 'country': 'US'},
{'dayOfWeek': 'Fri', 'city': 'Atafu', 'timeValue': 1538107200000, 'day': 28, 'country': 'TK'},
{'dayOfWeek': 'Tue', 'city': 'California', 'timeValue': 1540872000000, 'day': 30, 'country': 'US'},
{'dayOfWeek': 'Thu', 'city': 'Atafu', 'timeValue': 1540440000000, 'day': 25, 'country': 'TK'},
{'dayOfWeek': 'Fri', 'city': 'California', 'timeValue': 1539921600000, 'day': 19, 'country': 'US'},
{'dayOfWeek': 'Fri', 'city': 'Santiago', 'timeValue': 1539921600000, 'day': 19, 'country': 'DO'},
{'dayOfWeek': 'Mon', 'city': 'California', 'timeValue': 1539576000000, 'day': 15, 'country': 'US'},
{'dayOfWeek': 'Tue', 'city': 'Santiago', 'timeValue': 1539057600000, 'day': 9, 'country': 'DO'},
{'dayOfWeek': 'Thu', 'city': 'California', 'timeValue': 1540440000000, 'day': 25, 'country': 'US'},
{'dayOfWeek': 'Thu', 'city': 'Santiago', 'timeValue': 1539835200000, 'day': 18, 'country': 'DO'},
{'dayOfWeek': 'Fri', 'city': 'California', 'timeValue': 1538712000000, 'day': 5, 'country': 'US'},
{'dayOfWeek': 'Wed', 'city': 'California', 'timeValue': 1540353600000, 'day': 24, 'country': 'US'},
{'dayOfWeek': 'Fri', 'city': 'California', 'timeValue': 1540526400000, 'day': 26, 'country': 'US'},
{'dayOfWeek': 'Mon', 'city': 'Santiago', 'timeValue': 1539576000000, 'day': 15, 'country': 'DO'},
{'dayOfWeek': 'Tue', 'city': 'California', 'timeValue': 1538452800000, 'day': 2, 'country': 'US'},
{'dayOfWeek': 'Thu', 'city': 'California', 'timeValue': 1539835200000, 'day': 18, 'country': 'US'},
{'dayOfWeek': 'Mon', 'city': 'California', 'timeValue': 1540180800000, 'day': 22, 'country': 'US'},
{'dayOfWeek': 'Mon', 'city': 'Atafu', 'timeValue': 1539576000000, 'day': 15, 'country': 'TK'},
{'dayOfWeek': 'Wed', 'city': 'California', 'timeValue': 1538539200000, 'day': 3, 'country': 'US'},
{'dayOfWeek': 'Tue', 'city': 'Atafu', 'timeValue': 1538452800000, 'day': 2, 'country': 'TK'},
{'dayOfWeek': 'Tue', 'city': 'Santiago', 'timeValue': 1540267200000, 'day': 23, 'country': 'DO'},
]


def getDays(day, numeros=[]):
	for day in day:
		numeros.append(day["day"])
	numeros.sort()	
	return numeros


def recursivo(dictionary, i=0, num = getDays(dictionary)):
	#caso base
	if i == len(dictionary):
		return dictionary
	#caso general	
	else:
		dictionary[i]["day"] = num[i]
		return recursivo(dictionary, i+1, num)

print(recursivo(dictionary))


#Hacer una funcion recursiva que reciba 2 parametros y organice un diccionario. El primer parametro debera ser el diccionario a organizar y el segundo parametro sera la llave por la cual se organizara el diccionario.