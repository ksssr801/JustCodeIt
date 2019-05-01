# Contains basic utility functions.


class Utility:
    def __init__(self):
        pass

    def str_to_list_conv(self, str_val=''):
        # Converting string to list
        # Input : 'a,b,c' or '[a,b,c]' or '1,2,3' or '[1,2,3]'
        # Output : ['a','b','c'] or [1,2,3]
        if str_val[0] is '[' and str_val[-1] is ']':
            edited_list = str_val[1:-1].split(',')
        else:
            edited_list = str_val.split(',')
        try:
            final_list = map(int, edited_list)
            return final_list
        except ValueError:
            final_list = edited_list
            return final_list
