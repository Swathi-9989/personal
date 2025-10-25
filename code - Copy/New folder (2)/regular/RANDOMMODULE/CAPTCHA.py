''' 1,2 digits 3UC 4,5digits 6LC '''

import time,random

for i in range(1,11):
    time.sleep(.5)
    print( random.randint(11,99),
                chr( random.randint(65,90) ),
               random.randint(11,99),
                chr( random.randint(97,122) ),sep='')
