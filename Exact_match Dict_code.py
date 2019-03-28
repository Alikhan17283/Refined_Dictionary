
# -*- coding: utf-8 -*-

import re
Dict={}

list1=[]
for i,v in Dict.iteritems():

    list3=[]#print (i)
    for x in i:
        list2 = []
        for i in v:
            string_no_special_char = re.sub(r'[^a-zA-Z]', ' ', i)
            string_no_numbers = re.sub("\d+", " ", string_no_special_char)

            lowercased = string_no_numbers.lower()
            strip_spaces = lowercased.strip()

            list2.append(strip_spaces)


            for x in list2:
                if x not in list3:
                    list3.append(x)
    print (list3)
    for i in list3:
        print ('"{}",'.format(i))