#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    newlist = []
    for i in range(list_length):
        try:
            divs = my_list_1[i] / my_list_2[i]
        except ZeroDivisionError:
            print("division by 0")
            divs = 0
        except TypeError:
            print("wrong type")
            divs = 0
        except IndexError:
            print("out of range")
            divs = 0
        finally:
            newlist.append(divs)
    return newlist
