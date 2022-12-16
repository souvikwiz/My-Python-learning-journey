#!/usr/bin/env python
# coding: utf-8

# # First to last according relevel classes.

# In[110]:


#BODMAS
3*4+(5-2)*(9/3 * (5-3))


# In[ ]:


# single value 10 added to variable x.
# singel string hello added to variable y.
x = 10
y = "hello"
print(x,y)


# In[9]:


# string data type sample.

string_expample = "this is a sample of string, double qoutes are use ful when text has single qoute with in the text's"


# In[12]:


# len function.

len("souvik")

# len works on the value allotet to the veriable.

sample_len = "sardar"
len(sample_len)


# In[20]:


sample_index_number = "this is for sample index number"

# getting h from "this" and i from "is" by providing the index number of the value.
# postion starts from 0, -1 means the last eliment so r is from number.

sample_index_number[1], sample_index_number[5], sample_index_number[-1]


# In[26]:


# [1:4] index exldues the last value of the veriable, to include the last value +1.
# +1 or increasing the value works same.

sample_index_number[0:4], sample_index_number[0:3+1]


# In[31]:


# using fix index number with len function to get all from given start index number.
# 0: will start from start eliment to given last index.

sample_index_number[8: len(sample_index_number)], sample_index_number[0:11]


# In[51]:


# slicing using index numbers

slicing_example = "sample for slicing with indexing"

# to get "index" from indexing in the entire sentence. 

sliced = slicing_example[-8:-3]
print(sliced)


# In[55]:


# to check some eliment is persent of not. using "in" function.

"sample" in slicing_example


# In[56]:


# to check some eliment is persent of not, using "not" function.

"for" not in slicing_example


# In[59]:


# methods are funtions associated with a data type in python.
# all string methods are can be get by dir(str) code.
# to get help on string data type code is help(str)

methods_example = "souvik sardar"

methods_example.upper(), methods_example.title()


# In[61]:


# putting range of values to a single veriable,
# range function exclues the last value.

for raw_data in range(10):
    print(raw_data)


# In[88]:


# data cleaning using strip tool to clean extra spaces.

sample_strip = "   sample for strip tool    "
sample_strip2 = "sample for ! strip tool!"

# strip(!) inside eliment exclues only from first and last from the whole string value.
# strip to trim both side, rstrip is for right strip. lstrip is left strip.

sample_strip.rstrip(), sample_strip.strip(), sample_strip2.strip("!")


# In[87]:


# data cleaning using replace method.

sample_strip2.replace("!","<replaced_str>")


# In[89]:


# replace works on the first similar eliment.

sample_strip2.replace("le","<replaced>")


# In[82]:


# to get the index number of particular value of variable.
# using find method. returns the first occurrence.

sample_find = "sample for find"
sample_find.find("f") , sample_find.find("find")

# for "find" it refers to the starting index.


# In[84]:


# find method eroor to avoid 

error_find_sample = "this is me"
error_find_sample.find("is")

# here "is" index refers to the "is" from "this".


# In[85]:


# string --- immutable-- ""
# numbers -- immutable
# list ----- mutable --- []
# tuple ---- immutable - () *for one element (<data>,)
# dict ----- mutable --- {}


# # list data type

# In[94]:


# list data type, 0 based indexing. can contain multiple data type.

name_list = ["souvik", "soumik", "annesha", "promila"]
name_list[0], name_list[0:3]


# In[96]:


# getting the vale of a list value.
name_list[0][0]


# In[99]:


# replacing value of a list.

name_list[1] = "soumik_sarkar"
print(name_list)


# In[101]:


# adding new eliment to a list.
# using append methos.

name_list.append("pushpal")
name_list


# In[107]:


# combining two list using append method. 

sample_list_for_append = [1,2,3,4,5]
sample_list2_for_append = ["a","b","c","d","e"]

sample_list_for_append.append(sample_list2_for_append)
sample_list_for_append

# problem with append is it creates a list with in a list.
# second list acts as a separate list.


# In[109]:


# combining two list using extend method. 

sample_list_for_extend = [1,2,3,4,5]
sample_list2_for_extend = ["a","b","c","d","e"]

sample_list_for_extend.extend(sample_list2_for_extend)
sample_list_for_extend

# extend merge two separte list to a single list.
# append & extend both add the second list values from the last eliment of first list.


# In[114]:


# sorting list.

classmates = ["debanjon", "koushik", "saumik", "kiran","sachitha"]
classmates.sort()
classmates


# In[125]:


# creating list with in list, inner 2nd list is an eliment to the first outer list.

nested_list_sample = [1,["a","b","c"],"sample_nested_list"]
nested_list_sample2 = [2,["x",["aa","bb"],"y"],"sample_nested_list"]


# In[120]:


#type is used to check the data type.
type(nested_list_sample[1])


# In[126]:


# fetching "bb" from triple layer neasted list.

nested_list_sample2[1][1][1]


# In[130]:


# adding single elemnet to a list using extend.
nested_list_sample.extend(["<new data entry>"])
nested_list_sample


# In[132]:


# list slicing, to get 2-5

sample_list_slicing = [1,2,3,4,5,6,7,8,9]
sample_list_slicing[1:5]


# In[135]:


# Aggregations on list

sample_agg = [0,1,2,3,4,5,6,7,8,9]
max(sample_agg), min(sample_agg)


# In[138]:


# find max, min of a string by the lenth of a string in a list.
# key=len is counting the characters or laters.

sample_max_str = ["AAAA","AA","A","AAA"]
max(sample_max_str, key=len), min(sample_max_str, key=len)


# In[140]:


# converting string to list
list("souvik")


# In[142]:


sample_str_to_convert = "sardar"
list(sample_str_to_convert)


# # Tuple data type

# In[3]:


# tuple same as list but unmutable
single_element_tuple = (1,)
single_element_tuple


# In[5]:





# In[5]:


sample_tuple = (0,"hello")
type(sample_tuple)


# In[2]:


# type casting 

## implicit when python automataclly indentifies data type.
# int + float = float, exp: 1+1.5 = 2.5
## explicit when python dont get the data type. 
# string + int, exp: "10"+10 = error 


# In[7]:


# changing data type, explicit type casting.
string_to_convert = "10"
sample_int = 10
sum_of_samples = int(string_to_convert) + sample_int
sum_of_samples


# In[13]:


##polymorphism


# In[ ]:


# polymorphism means multiple forms
## + operator can do diffarent things depending on the data type.
# for int sum, for string concatination, for list join.


# In[16]:


#concat strings using + operator
first_name = "souvik"
Last_name = "sardar"
first_name + " " + Last_name


# In[17]:


#joining list by + operator 
list_to_join = [1,2,3] 
list_to_join2 = ["x","y"]

list_to_join + list_to_join2


# In[18]:


[1,2,3] + ["x","y"] + [["a","b"]]


# In[19]:


["s",["o",["u"]]] + [1,2] + ["b",["a"]]


# In[24]:


#Function 
# function is a template to do something. 
# def <name of the function> (parameters and separated by ",")
# ":" what to do with the parameters
# <body>
# return will give out put

def get_sum_of_two_numbers(num_1, num_2):
    result = num_1 + num_2
    return result


# In[26]:


#calling a function
# num_1 is called arguments which holds the place.

get_sum_of_two_numbers(num_1 = 1, num_2 = 2)


# In[27]:


sum_of_two_num = get_sum_of_two_numbers(num_1 = 1, num_2 = 2)
sum_of_two_num


# In[29]:


# raw data for function understaing 
name_1 = "souvik"
name_2 = "sardar"
name_3 = "soumi"


# In[33]:


# slow method one by one
name_1 = name_1.upper()
name_1 = name_1 + "::"
name_1


# In[41]:


# same with using functions at ones
def clean_name (first_name):
    first_name_upper = first_name.upper() 
    first_name_upper_with_colons = first_name_upper + "::"
    return first_name_upper_with_colons


# In[47]:


print(clean_name(first_name = name_1))
print(clean_name(first_name = name_2))
print(clean_name(first_name = name_3))


# In[56]:


# function name should be descriptive.
# to debug use print in every staement 
# like : print(result = first_name.upper)

def full_name_upper_with_colons (first_name, last_name):
    result = first_name.upper() + ":::" + last_name
    return result


# In[58]:


full_name_upper_with_colons(first_name = "souvik", last_name = "sardar")


# In[59]:


# methods are .upper .lower etc.


# In[2]:


##list comprehension class 30th 


# In[4]:


sample_strings = "Relevel"
list(sample_strings)

# not a desired output.


# In[11]:


# .split() methods of string 
# spliting strings and converting them to list.

string_sample_split = "Relevel is awesome"
string_sample_split.split()


# # join

# In[9]:


"".join(string_sample_split)
#getting back the string type from list. 


# In[16]:


sample_slipt_to_join = "Ufaber is good"
# have to put veriable to save the code to join correctly.
split2join = sample_slipt_to_join.split()
split2join


# In[17]:


"_".join(split2join)


# # Dictionary

# In[19]:


dic_to_separate_later = {"index_1":[1,2,3,3,4],
                         "index_2":[9,8,7,65,3]
                        }


# In[20]:


##key_words
dic_to_separate_later.keys()


# In[21]:


##values
dic_to_separate_later.values()


# In[24]:


## All items in dict.
dic_to_separate_later.items()


# In[ ]:





# # set
# 
# 
# 

# In[11]:


set_example = {1,2,3,4,5,6,7}
set_example


# In[40]:


List_for_converting_to_sets = [1,2,3,4,4,4,6,7]
List_for_converting_to_sets_1 = [2,3,9,8,7,4]
set_1 = set(List_for_converting_to_sets)
## it only takes unique values, even if it comes from a list,
##it will remove duplicates with in the list)
print(set_1)


# In[41]:


## defining set to a veriable
set_2 = set(List_for_converting_to_sets_1)
set_2


# In[33]:


##Union, all commons & unique from both sets
set_1.union(set_2)


# In[38]:


##Intersection, all commons from left or first set only.
set_1.intersection(set_2)


# In[45]:


## All un-matched from left table only.
set_1.difference(set_2) 


# # IF

# In[ ]:


## if else same like excel, just follow alliengment 
## input is just a textbox for user
## int for defining age as interger so that can be use in if for this particular calculation.
age = int(input("Please enter your age downer below: "))
if age>=18:
    print("Eligible to vote")
else:
    print("Not-Eligible")


# In[ ]:


age_int = int(input("Please enter your age downer below: "))

if age_int>0 and age_int <=12:
    print("you are a kid")
elif age_int>12 and age_int <=19:
    print("teenager")
elif age_int> 19 and age_int <=50:
    print("middle aged")   
elif age_int> 50 and age_int <=150:
    print("elderly person")  
else:
    print("invalid")


# In[ ]:


### Technical issue, working in colab. #currect code

age_input_by_user = input("Enter age")

age_input_by_user_as_int = int(age_input_by_user)

if age_input_by_user_as_int >= 0 and age_input_by_user_as_int <=12:
    print("kid")
    
elif age_input_by_user_as_int > 12 and age_input_by_user_as_int <=19:
    print("teenager")
elif age_input_by_user_as_int > 19 and age_input_by_user_as_int <=50:
    print("elder")
else:
    print("invalid age")
    


# In[2]:


1:53 oct 1st DUE


# In[33]:


#practice class 03/12
import pandas as pd
import numpy as np 
rand_nums = np.random.randint(1,100, size=(4,5)) 
rand_nums
##type(rand_nums)


# In[ ]:





# In[31]:


dict_a = {"name":["souvik","abudabi","laden","che gouvera"],
         "start_time":[1200,1400,1600],
          "end_time":[2300,2100,2300]}
dict_a


# In[ ]:




