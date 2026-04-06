# input_Str = "akashk"
# count = 0
# length = len(input_Str)

# for chai in input_Str:
#     for i in range(0,length):
#         if chai == input_Str[i]:
#             count+=1
#             if count == 2:
#                 break
        
#         print(chai)


#CORRECT WAY----------------------------------------------
input_Str = "Leecher"


for chai in input_Str:
    if input_Str.count(chai) ==1:
        print("Character is :", chai)





#Better Way-------------------------------------------------
# input_Str = "teeteracdacd"


# for chai in input_Str:
#     if input_Str.count(chai) ==1:
#         print("Character is :", chai)
#         break


#break will stop loop as soon as first non-repeated char is found ie iteration won't happen for "acdacd" ie rest of string