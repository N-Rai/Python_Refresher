list = [ "Bob", "Rolf", "Anne"] # can do everything
tuple = ("Bob", "Rolf", "Anne") # Cannot modify
sets= {"Bob", "Rolf", "Anne"} # cannot have repeatation and doesn't have order
print(list[0])  # [x] subscript notation on list and tuple

list[0] = "Simth"
list.append("Sam")
list.remove("Rolf")
print(list[0])  
print(list)
# tuple[0] = "Simth"
# tuple.append("Smith"), 
 # 'tuple' object does not support item assignment and has no attribut 'append'
#sets[0]= "Simth"
 # 'sets' object does not support item assignment
sets.add("Smith")
print(sets)


