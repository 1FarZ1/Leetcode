def singleNumber(nums):
        number=[]
        for i in range(len(nums)):
            print(i)
            trouve=False
            if nums[i] not in number:
                for j in range(len(nums)):
                    if nums[i]==nums[j] and  i != j:
                        trouve =True
                        number.append(nums[i])
                if trouve ==False:
                    return nums[i]
print(singleNumber(
[4,1,2,1,2]))