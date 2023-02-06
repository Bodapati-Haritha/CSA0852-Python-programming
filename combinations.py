num=int(input("Enter the number of elements:"))
my_nums=[]
for i in range(num):
    a=int(input("enter the elements:"))
    my_nums.append(a)
def permute(nums):
  result_perms = [[]]
  for n in nums:
    new_perms = []
    for perm in result_perms:
      for i in range(len(perm)+1):
        new_perms.append(perm[:i] + [n] + perm[i:])
        result_perms = new_perms
  return result_perms
print("THE Given Elements:\n ",my_nums)
print("Collection of Numbers:\n",permute(my_nums))
