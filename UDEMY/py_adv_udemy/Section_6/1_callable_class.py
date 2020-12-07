class MemoryClass:

    def __init__(self,list):
        self.list_of_items = list

    def __call__(self,item):
        self.list_of_items.append(item)


mem = MemoryClass([])


mem('buy sugar')
print(mem.list_of_items)
mem('buy milk')
print(mem.list_of_items)


class NoDuplicates:
    def __init__(self,unique):
        self.unique = unique

    def __call__(self, new_items):
        for i in new_items:
            if i not in self.unique:
                self.unique.append(i)


my_no_dup_list = NoDuplicates([])
my_no_dup_list(['keyboard','mouse'])
print(my_no_dup_list.unique)
my_no_dup_list(['keyboard','mouse','pendrive'])
print(my_no_dup_list.unique)
my_no_dup_list(['charge','pendrive'])
print(my_no_dup_list.unique)