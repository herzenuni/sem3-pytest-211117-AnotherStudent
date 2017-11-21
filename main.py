# Есть два списка разной длины. В первом содержатся ключи, а во втором значения.
# Напишите функцию, которая создаёт из этих ключей и значений словарь.
# Если ключу не хватило значения, в словаре должно быть значение None. 
# Значения, которым не хватило ключей, нужно игнорировать.

def createDict(keys, values):
  assert(type(keys) == list)
  assert(type(values) == list)
  
  res = dict.fromkeys(keys, None)
  
  for i, k in enumerate(keys):
    if i < len(values):
      res.update({k : values[i]})
    else:
      break
  
  return res

