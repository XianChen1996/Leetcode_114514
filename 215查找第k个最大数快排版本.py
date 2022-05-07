#没有_init_得重新传self，复制后面数组就行了
#第一次分区查找，我们需要对大小为 n 的数组执行分区操作，需要遍历 n 个元素。第二次分区查找，
# 我们只需要对大小为 n/2 的数组执行分区操作，需要遍历 n/2 个元素。依次类推，分区遍历元素的个数分别为、
# n/2、n/4、n/8、n/16.……直到区间缩小为 1。 如果我们把每次分区遍历的元素个数加起来，就是：n+n/2+n/4+n/8+…+1。
# 这是一个等比数列求和，最后的和等于 2n-1。所以，上述解决思路的时间复杂度就为 O(n)。

class Solution:

    def partition(self, num, low, high):
        pivot = num[low]

        while (low < high):
            while (num[high] >pivot):
                high -= 1
            while(num[low]<pivot):
                low +=1
            num[low],num[high] = num[high],num[low]
        num[high]=pivot
        index = num.index(pivot)
        return index

    def findKthLargest(self,nums: list[int], k:int):
        length = len(nums)
        begin = 0
        end = length - 1
        index = Solution.partition(nums,nums, begin, end)  # 这里的partition函数就是上面快排用到的函数
        while index != length - k:
            if index > length - k:
                end = index - 1
                index = Solution.partition(nums,nums, begin, index - 1)
            else:
                begin = index + 1
                index =Solution. partition(nums,nums, index + 1, end)
        return nums[index]





if __name__ == '__main__':

    a = [23,1,123,45,40,3,98]
    c=Solution.findKthLargest(a,a, 2)


    print(c)