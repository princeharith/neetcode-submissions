class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        #compare the first number of new_interval w/ the start_i's

        #if new_interval[1] < curr_intervals start, we can append new interval and everything after

        #if new_interval[0] > curr_intervals end, we can append the curr_interval

        #othwerwise we have a merge

        #otherwise we create a new interval

        n = len(intervals)
        i = 0
        res = []

        #if 
        while i < n and intervals[i][1] < newInterval[0]:
            res.append(intervals[i])
            i+=1
        '''
        otherwise, that means the newInterval's startpoint is less than the curr's endpoint

        to check if we have a merge, we check if the new's endpoint is greater than or equal
        curr's start
        '''
        while i < n and newInterval[1] >= intervals[i][0]:
            newInterval = [min(newInterval[0], intervals[i][0]), max(newInterval[1], intervals[i][1])]
            i+=1
        res.append(newInterval)
        
        while i < n:
            res.append(intervals[i])
            i+=1
        
        return res

        
        