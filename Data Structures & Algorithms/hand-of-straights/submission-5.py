class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        import collections
        hashmap = collections.Counter(hand)

        if len(hand) % groupSize != 0:
            return False

        num_groups = len(hand) // groupSize
        hand.sort()

        hands_made = 0


        for i in range(len(hand)):
            if hands_made == num_groups:
                break
            num = hand[i]
            print("i is: " + str(i))
            print(num)

            if num not in hashmap:
                return False
            if hashmap[num] == 0:
                continue
            for j in range(num, num+groupSize):
                if j not in hashmap or hashmap[j] == 0:
                    return False
                hashmap[j] -= 1

            hands_made += 1
        
        # if hands_made < num_groups:
        #     return False
        
        return True

        