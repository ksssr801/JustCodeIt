# Implementing hash tables : Open Hashing (Chaining) using Linked List
# In direct addressing: insert, search & delete takes T = O(1) time

# Using Linked List, so
# Insertion : Runs in O(1) time but for given key, T = O(n) in worst case.
# Deletion : Runs in O(1) time but for given key, T = O(n) in worst case.
# Searching : For 'n' size list, T = O(n) in worst case


import linkedlist

class HashObject:
    def __init__(self, value):
        self.data = value
        self.next = None

class Hashing:
    def __init__(self, length):
        self.LL_obj = linkedlist.LinkedList()
        self.table_size = length
        self.hash_table = [None]*length
        self.len_table = [0]*length

    def insert_h_key(self, obj):
        key = obj.data % self.table_size
        if self.hash_table[key] is None:
            self.hash_table[key] = obj
            self.LL_obj.size = self.len_table[key] + 1
        else:
            self.LL_obj.size = self.len_table[key]
            self.LL_obj.head = self.hash_table[key]
            self.LL_obj.insert_LL(obj)
        self.len_table[key] = self.LL_obj.size

    def search_h_key(self, value=None):
        key = value % self.table_size
        print '\nIn the Hash Table, at key %s,' % key
        if value is not None:
            key = value % self.table_size
            self.LL_obj.head = self.hash_table[key]
            self.LL_obj.search_LL(value)
        else:
            print 'Wrong value provided!'

    def delete_h_key(self, value=None):
        key = value % self.table_size
        if self.hash_table[key] is None:
            print '\nGiven value is not present!'
        else:
            self.LL_obj.size = self.len_table[key]
            self.LL_obj.head = self.hash_table[key]
            self.LL_obj.delete_LL(value)
            self.hash_table[key] = self.LL_obj.head
            print '\nFor key %s, after deletion :' % key
            self.LL_obj.print_LL()
        self.len_table[key] = self.LL_obj.size


    def print_hash_table(self):
        flag = False
        for size in self.len_table:
            if size is not 0:
                flag = True
                break
        if flag:
            print '\nIn the Hash Table of size %s : ' % self.table_size
            for key in range(self.table_size):
                if self.hash_table[key] is not None:
                    print '\nFor key %s :' % key
                    self.LL_obj.head = self.hash_table[key]
                    self.LL_obj.size = self.len_table[key]
                    self.LL_obj.print_LL()
            print 'LL Length Table : ',self.len_table
        else:
            print '\nHash table is empty!'

print ('\nHash Table\n')
size_t = input('Enter size: ')
hash_t = Hashing(size_t)
while True:
    print ('\nHash Table\n')
    print ('Select from options:')
    print ('1 : Insert')
    print ('2 : Delete')
    print ('3 : Search')
    print ('4 : Print')
    print ('0 : Exit')
    inp = input('Enter your choice : ')
    if inp == 0:
        break
    else:
        if inp == 1:
            data = input('Enter data: ')
            node = HashObject(data)
            hash_t.insert_h_key(node)
        elif inp == 2:
            val = input('Enter value: ')
            hash_t.delete_h_key(val)
        elif inp == 3:
            val = input('Enter value: ')
            hash_t.search_h_key(val)
        elif inp == 4:
            hash_t.print_hash_table()
        else:
            print ("Wrong Choice!")
