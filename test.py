
def firstandlast(nums,target):
    firstindex=f_index(nums,target)
    lastindex=l_index(nums,target)
    return(firstindex,lastindex)

def f_index(nums,target):
    low=0
    high=len(nums)-1
    mid=(low+high)//2

    while(low<=high):
        if nums[mid]==target:
            if mid==low or nums[mid]>nums[mid-1]:
                return mid
            else:
                    high=mid-1
        elif nums[mid]>target:
            high=mid-1
        else:
            low=mid+1

def l_index(nums,target):
    low=0
    high=len(nums)-1
    mid=(low+high)//2
    while(low<=high):
        if nums[mid]==target:
            if high==mid or nums[mid+1]>nums[mid]:
                return mid
            else:
                low=mid+1
        elif nums[mid]<target:
                low=mid+1
        else:
            high=mid-1

firstandlast([1,1,2,3,4,4,4,4,4,4,4,5],4)