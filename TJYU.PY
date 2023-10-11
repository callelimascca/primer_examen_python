def new_array(array,num):
  nuevo=[]
  for i in range(len(array)):
    if i ==2:
      nuevo.append(num)
      nuevo.append(array[i])
      return nuevo
original=[1,2,4,]
numeronuevo=3
nuevo=new_array(original, numeronuevo)
print(f"original: {original}")
print(f"nuevo: {nuevo}")