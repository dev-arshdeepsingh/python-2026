# l1 = ['mango', 'banana', 'apple', 'orange']
# dup_count = 1

# for item in l1:
#     #print(item)
#     if l1.count(item) > 1:
#         dup_count +=1
#         if dup_count ==2:
#             print("Duplicate Found: ", item)
#             break
# if dup_count == 1:    
#     print("List is Unique: ", l1)


# #ABove is just my verse for fun, its not optimised


#---------------------------------------------------------------------------------

l1 = ['mango', 'banana', 'apple', 'orange', 'orange']
unique_list = []

for item in l1:
    if item in unique_list:    
        print("Duplicate Found: ", item)
        break
    else:    
        unique_list.append(item)
    
if len(l1) == len(unique_list):
    print("List is unique")


# Overall its like same same but different, hitesh sir used set instead of list