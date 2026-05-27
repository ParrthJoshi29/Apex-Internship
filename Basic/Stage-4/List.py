print("*List Operations*")
# Important List Methods
#Method	     Work

#append()	add item
#remove()	remove item
#insert()	insert item
#pop()	    remove last item
#sort()	    sort list

lst = [1, 2, 3, 4, 5]

lst.append(6)
print("Appended List 6:", lst)

lst.remove(3)
print("After removing 3:", lst)

lst.insert(2, 10)
print("After inserting 10 at index 2:", lst)

lst.pop()
print("After popping last element:", lst)

lst.sort()
print("After sorting:", lst)

