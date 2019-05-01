# Implementing Insertion Sort

import utility


class Sorting:
    def __init__(self):
        self.utility_obj = utility.Utility()
        pass

    def insertion_sort(self, value_set=''):
        val_list = self.utility_obj.str_to_list_conv(value_set)
        size = len(val_list)
        for j in range(1, size):
            key = val_list[j]
            i = j - 1
            while i > -1 and val_list[i] > key:
                val_list[i+1] = val_list[i]
                i = i - 1
            val_list[i+1] = key
        return val_list


sort_obj = Sorting()
while True:
    print ('\nSorting\n')
    print ('Input : Only comma separated numbers or characters(It can be within list or can\'t be.)')
    print ('Eg : a,b,c or [a,b,c] or 1,2,3 or [1,2,3]) \n')
    print ('Select from options:')
    print ('1 : Insertion Sort')
    print ('0 : Exit')
    inp = input('Enter your choice : ')
    # inp = map(int, inp)  # python 3.x
    if inp == 0:
        break
    else:
        if inp == 1:
            val_set = raw_input('Enter value set: ')
            # val_set = input('Enter value set: ') # python 3.x
            data_set = sort_obj.insertion_sort(val_set)
            print ('Sorted Set : {}'.format(data_set))  # python < 3.6
            # print f'Sorted Set : {data_set}'  # python > 3.5
        else:
            print ("Wrong Choice!")
