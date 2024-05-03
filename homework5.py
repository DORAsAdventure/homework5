#immutable_var=(1, 2, 'cat', True)
#print(immutable_var)
#immutable_var[2]='dog'
#print(immutable_var) #кортеж не поддерживает обращение по элементам
mutable_list=['cat','dog','panda','lamb']
mutable_list[0]='kitty'
mutable_list.append('animal')
print(mutable_list)
