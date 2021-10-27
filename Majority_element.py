#Given an array nums of size n, return the majority element.

def majorityElement(self, nums):
  l=len(nums)/2
  d={}
  for i in nums:
    d[i]=d.get(i,0)+1
    if d[i]>l:
      return i
