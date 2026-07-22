class Solution:
    def findWinners(self, matches: List[List[int]]) -> List[List[int]]:
        zero_loss, one_loss, more_loss = set(), set(), set()

        for match in matches:
            winner = match[0]
            loser = match [1]

            if winner not in one_loss and winner not in more_loss:
                zero_loss.add(winner)
            
            if loser in zero_loss:
                zero_loss.remove(loser)
                one_loss.add(loser)
            elif loser in one_loss:
                one_loss.remove(loser)
                more_loss.add(loser)
            elif loser in more_loss:
                continue
            else:
                one_loss.add(loser)
            
        return [sorted(list(zero_loss)), sorted(list(one_loss))]
        


        