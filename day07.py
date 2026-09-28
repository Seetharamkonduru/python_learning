# # Set Methods 
# #add 
# s = set()
# s.add(1) #{1}
# s.add(1.6)# {1, 1.6}
# s.add(2+3j) #{1, (2+3j), 1.6}
# s.add(True) #{1, 1.6, (2+3j)}
# s.add(None) #{1, 1.6, (2+3j), None}
# # s.add([1,2,3]) # unhashable type: 'list'
# s.add((4,5,6)) # {1, 1.6, (2+3j), None, (4, 5, 6)}
# # s.add({7,8,9}) #unhashable type: 'set'
# # s.add({10:'a', 11:'b', 12:'c'}) #unhashable type: 'dict'
# s.add('rakesh') #rakesh
# s.add(range(13,16)) #range(13, 16)
# print(s) #{range(13, 16), 1, 1.6, 'rakesh', (2+3j), (4, 5, 6), None}

# #update
# s = set()
# s.update(1) #error
# s.update(1.6) # 'float' object is not iterable
# s.update(2+3j) # 'complex' object is not iterable
# s.update(True) # 'bool' object is not iterable
# s.update(None) # 'NoneType' object is not iterable
# s.update([1,2,3]) #{1, 2, 3}
# s.update((4,5,6)) #{1, 2, 3, 4, 5, 6}
# s.update({7,8,9}) #{1, 2, 3, 4, 5, 6, 7, 8, 9}
# s.update({10:'a', 11:'b', 12:'c'}) #{1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12}
# s.update('rakesh') #{1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 'r', 'a', 'k', 'e', 's', 'h'}
# s.update(range(13,16)) #{1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 'r', 'a', 'k', 'e', 's', 'h', 13, 14, 15}
# print(s) #{1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 'r', 'a', 'k', 'e', 's', 'h', 13, 14, 15}

# #pop
# s = {1,4,3,2,5,6,7,9}
# print(s) #{1, 2, 3, 4, 5, 6, 7, 9}
# a = s.pop() 
# print(a, s) #1,{2, 3, 4, 5, 6, 7,9 }
# b = s.pop() 
# print(b, s) #2, {3, 4, 5, 6, 7, 9}
# c = s.pop(3)
# print(c, s) #(error)It removes one arbitrary/random element from the set and returns it.

# #remove
# s = {4,3,2,5,8}
# a = s.remove(8) #{4, 3, 2, 5}
# print(a, s)
# b = s.remove(9) 
# print(b, s) #KeyError: 9

# # discard
# s = {4,3,2,5,8}
# a = s.discard(8)
# print(a, s) #None {2, 3, 4, 5}
# b = s.discard(9)
# print(b, s) #None {2, 3, 4, 5}

# # clear
# s = {4,3,5,2,1}
# a = s.clear()
# print(a, s) #None set()

# # union, intersection, differece, symmetric_difference
# s = {1,2,3,4}
# l = [3,4,5,6]
# t = (3,4,5,6)
# s2 = {3,4,5,6}
# d = {3:'c', 4:'d', 5:'e', 6:'f'}
# r = range(3,7)
# w = '3456'
# print('Union:', s.union(l)) #Union: {1, 2, 3, 4, 5, 6}
# print('Intersection:', s.intersection(t)) #Intersection: {3, 4}
# print('Difference:', s.difference(s2)) #Difference: {1, 2}
# print('Symmetric Difference:', s.symmetric_difference(d)) #Symmetric Difference: {1, 2, 5, 6}
# print('Union:', s.union(w)) #Union:  {1, 2, 3, 4, '4', '6', '5', '3'}
# print('Union:', s.union(r)) #Union: {1, 2, 3, 4, 5, 6}


# # Dict Methods 
# d = {}
# d.update(5)          # TypeError: 'int' object is not iterable
# d.update(5.4)        # TypeError: 'float' object is not iterable
# d.update(4+5j)       # TypeError: 'complex' object is not iterable
# d.update(True)       # TypeError: 'bool' object is not iterable
# d.update(None)       # TypeError: 'NoneType' object is not iterable
# d.update([1,2,3])      # TypeError: cannot convert dictionary update sequence element #0 to a sequence
# d.update((4,5,6))      # TypeError: cannot convert dictionary update sequence element #0 to a sequence
# d.update({7,8,9})      # TypeError: cannot convert dictionary update sequence element #0 to a sequence
# d.update('rak')        # TypeError: dictionary update sequence element #0 has length 1; 2 is required
# d.update(range(10,14)) # TypeError: cannot convert dictionary update sequence element #0 to a sequence
# d.update({10:'j', 11:'k', 12:'l'})
# print(d) #{10: 'j', 11: 'k', 12: 'l'}
# d.update([ [1,'a'], (2,'b'), 'ab' ])
# print(d) #{10: 'j', 11: 'k', 12: 'l', 1: 'a', 2: 'b', 'a': 'b'}
# d.update(( 'ra', 'ke', 'sh' ))
# print(d) #{10: 'j', 11: 'k', 12: 'l', 1: 'a', 2: 'b', 'a': 'b', 'r': 'a', 'k': 'e', 's': 'h'}
# d.update({ (3,'c'), (4,'d') })
# print(d)#{10: 'j', 11: 'k', 12: 'l', 1: 'a', 2: 'b', 'a': 'b', 'r': 'a', 'k': 'e', 's': 'h', 3: 'c', 4: 'd'}


# # #pop 
# d = {3:'c', 2:'b', 1:'a', 4:'d'}
# x = d.pop(2)
# print(x) #b
# y = d.pop(100)
# print(y) #KeyError: 100
# z = d.pop(100, -1)
# print(z) #-1

# #popitem
# d = {3:'c', 2:'b', 1:'a', 4:'d'}
# x = d.popitem() 
# print(x, d) # (4, 'd') {3: 'c', 2: 'b', 1: 'a'}
# y = d.popitem()
# print(y, d) # (1, 'a') {3: 'c', 2: 'b'}

# #clear
# d = {3:'c', 2:'b', 1:'a', 4:'d'} 
# d.clear() 
# print(d) #{}

# #get 
# d = {3:'c', 2:'b', 1:'a', 4:'d'}
# x = d.get(2)
# print(x, d) #b {3: 'c', 2: 'b', 1: 'a', 4: 'd'}
# y = d.get(100)
# print(y, d) #None {3: 'c', 2: 'b', 1: 'a', 4: 'd'}
# z = d.get(100, -1)
# print(z, d) #-1 {3: 'c', 2: 'b', 1: 'a', 4: 'd'}

# #setdefault
# d = {3:'c', 2:'b', 1:'a', 4:'d'}
# x = d.setdefault(2, 90)
# print(x, d) #b {3: 'c', 2: 'b', 1: 'a', 4: 'd'}
# y = d.setdefault(100)
# print(y, d) #None {3: 'c', 2: 'b', 1: 'a', 4: 'd', 100: None}
# z = d.setdefault(90, -1)
# print(z, d) #None {3: 'c', 2: 'b', 1: 'a', 4: 'd', 100: None, 90: -1}
# m = d.setdefault(90, -2)
# print(m, d) #-1 {3: 'c', 2: 'b', 1: 'a', 4: 'd', 100: None, 90: -1}

# #keys, values, items
# d = {3:'c', 2:'b', 1:'a', 4:'d'}
# dk = d.keys()
# print(dk, type(dk)) #dict_keys([3, 2, 1, 4]) <class 'dict_keys'>
# dv = d.values()
# print(dv, type(dv))#dict_values(['c', 'b', 'a', 'd']) <class 'dict_values'>
# di = d.items() 
# print(di, type(di))#dict_items([(3, 'c'), (2, 'b'), (1, 'a'), (4, 'd')]) <class 'dict_items'>



