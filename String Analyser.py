#!/usr/bin/env python
# coding: utf-8

# In[8]:


def String_Analyser():
    a = input("What is your Input?: ")
#     print("Pick the number corresponding to the option below: ")
#     print("1.Analyze\n2.Repetition of a new character\n3.New Text\n4.Exit")
    length = 0
    words = 1
    repetition = 0
    while True:
        print("Pick the number corresponding to the option below: ")
        print("1.Analyze\n2.Repetition of a new character\n3.New Text\n4.Exit")
        b = input("what is your input?: ")
        if int(b) == 1:
            for i in a.split():
                words += 1
                for a in i:
                    aa = str(len(a))
                    length += 1
            print("lenght of input is {}\nnumber of words is {}".format(length,words-1))
            continue
        elif int(b) == 2:
            user = input("what letter do you want to search for?: ")
            for i in a.split():
                for g in i:
                    if str(g) == user:
                        repetition += 1
            print('The letter {} is repeated {} times'.format(user,repetition))
            continue
        elif int(b)==3:
            String_Analyser()
        elif int(b) == 4:
            print("you have exited the program")
            return False
        break


# In[ ]:


String_Analyser()


# In[ ]:





# In[ ]:





# In[ ]:




