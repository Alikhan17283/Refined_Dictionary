
# -*- coding: utf-8 -*-

import re


list1=[]
for i,v in Exact_match_Dictionary.iteritems():

    list3=[]
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

    fw=open("dictionary_Exact.txt","a")
    print (list3)
    fw.write("=============================================================================\n")
    fw.write("=============================================================================\n")
    for i in list3:
        a=('"{}",'.format(i))
        print(a)
        fw.write(a+"\n")
