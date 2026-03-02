class Solution(object):
    def subarraySum(self, nums, k):
        hash={0:1}
        count=0
        currents=0

        for i in nums:
            currents+=i
            if currents-k in hash:
                count += hash[currents-k]

            hash[currents]=hash.get(currents,0)+1
        return count