def max_product_of_three(nums):
    if len(nums)<3:
        return None
    nums.sort()
    
#case 1 : all positive numbers

    max_product = nums[-1]* nums[-2] *nums[-3]

#case 2 : two negative numbers and one positive number

    max_product = max(max_product, nums[0] * nums[1] * nums[-1])
    
    return max_product

#test the function
nums = [-10,-3,5,2,7,8]
print(max_product_of_three(nums))