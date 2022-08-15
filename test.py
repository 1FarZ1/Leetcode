# def removeElement(nums, val):
#         sum=0
#         for i in range(len(nums)):
#             if nums[i] ==val:
#                 nums[i]=0
#         for i in nums:
#             if i !=0:
#                 sum+=1
#         print(sorted(nums).reverse())
#         return sum
# print(removeElement([3,2,2,3],3)) 

# first_number=int(input(" enter the first number"))
# operation=input("enter the operation")
# second_number=int(input(" enter the second number"))
# if operation=="+":
#     sum1=first_number+second_number
# elif operation=="-":
#       sum1=first_number-second_number
# elif operation=="*":
#       sum1=first_number*second_number
# elif operation=="/":
#     sum1=first_number/second_number
# print(sum1)
def singleNumber( nums):
    i=0
    while i<len(nums):
        
            if sorted(nums)[i] !=sorted(nums)[i+1]:  
                return sorted(nums)[i]
            else:
                j=sorted(nums)[i] 
                while j == sorted(nums)[i] :
                    i=i+1
      

     
print(
    singleNumber(
[4,1,2,1,2]))



              
     