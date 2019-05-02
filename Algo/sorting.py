# Implementing Insertion Sort

import utility


class Sorting:
    def __init__(self):
        self.utility_obj = utility.Utility()
        pass

    def insertion_sort(self, value_set=''):
        # T = O(n^2) in the worst case and O(1) in best case.
        val_list = self.utility_obj.str_to_list_converter(value_set)
        size = len(val_list)
        if len(val_list) < 2:
            return val_list
        else:
            for j in range(1, size):
                key = val_list[j]
                i = j - 1
                while i > -1 and val_list[i] > key:
                    val_list[i+1] = val_list[i]
                    i = i - 1
                val_list[i+1] = key
            return val_list

    @staticmethod
    def merge(val_list, lt, mid, rt):
        l_len = mid-lt+1
        r_len = rt-mid
        lt_list = [0]*l_len
        rt_list = [0]*r_len
        for i in range(0, l_len):
            lt_list[i] = val_list[lt+i]
        for j in range(0, r_len):
            rt_list[j] = val_list[mid+1+j]
        i = 0
        j = 0
        k = lt
        while i < l_len and j < r_len:
            if lt_list[i] <= rt_list[j]:
                val_list[k] = lt_list[i]
                i += 1
            else:
                val_list[k] = rt_list[j]
                j += 1
            k += 1
        while i < l_len:
            val_list[k] = lt_list[i]
            i += 1
            k += 1
        while j < r_len:
            val_list[k] = rt_list[j]
            j += 1
            k += 1

    def merge_sort(self, val_list, lt, rt):
        if lt < rt:
            mid = (lt+(rt-1))/2
            self.merge_sort(val_list, lt, mid)
            self.merge_sort(val_list, mid+1, rt)
            self.merge(val_list, lt, mid, rt)

    def merge_sort_driver(self, value_set=''):
        # T = O(n*log(n)) in worst case, stable
        # Not in place algorithm, takes O(n) extra space.
        val_list = self.utility_obj.str_to_list_converter(value_set)
        size = len(val_list)
        self.merge_sort(val_list, 0, size-1)
        return val_list


sort_obj = Sorting()
while True:
    print ('\nSorting\n')
    print ('Input : Only comma separated numbers or characters(It can be within list or can\'t be.)')
    print ('Eg : a,b,c or [a,b,c] or 1,2,3 or [1,2,3]) \n')
    print ('Select from options:')
    print ('1 : Insertion Sort')
    print ('2 : Merge Sort')
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
            print ('Insertion Sort, Sorted Set : {}'.format(data_set))  # python < 3.6
            # print f'Sorted Set : {data_set}'  # python > 3.5
        if inp == 2:
            val_set = raw_input('Enter value set: ')
            # val_set = input('Enter value set: ') # python 3.x
            data_set = sort_obj.merge_sort_driver(val_set)
            print ('Merge Sort, Sorted Set : {}'.format(data_set))  # python < 3.6
            # print f'Sorted Set : {data_set}'  # python > 3.5
        else:
            print ("Wrong Choice!")
