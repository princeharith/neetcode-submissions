class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        count = collections.Counter(hand)
        for card in sorted(count):
            cur_count = count[card]
            if cur_count > 0:
                for i in range(groupSize):
                    count[card+i] -= cur_count
                    if count[card+i] < 0:
                        return False

        # for card in sorted(count):
        #     if count[card] > 0:
        #         for i in range(groupSize):
        #             count[card+i] -= count[card]
        #             if count[card+i] < 0:
        #                 return False
        
        return True