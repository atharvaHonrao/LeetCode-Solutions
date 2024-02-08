class Solution(object):
    def lemonadeChange(self, bills):
        count5 = 0
        count10 = 0
        for i in bills:
            if i == 5:
                count5+=1
            if i == 10:
                if count5==0:
                    return False
                else:
                    count10+=1
                    count5-=1
            if i==20:
                if count5==0:
                    return False
                else:
                    if count10>0:
                        count5-=1
                        count10-=1
                    elif count5>2:
                        count5-=3
                    else:
                        return False
        return True
        
