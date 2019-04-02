#!/usr/bin/env python3
"""
Author : emilyenglish
Date   : 2019-03-31
Purpose: date parsing
"""

import os
import sys
import re

# --------------------------------------------------
def main():
    args = sys.argv[1:]

    if len(args) != 1:
        print('Usage: dates.py DATE'.format(os.path.basename(sys.argv[0])))
        sys.exit(1)
    #date0_re = re.compile('(\d{4})''[/-]''(\d{1,2})')
    date_re = re.compile('(\d{4})'    # capture year (group 1)
                     '[/-]'       # separator
                     '(\d{1,2})'  # capture month (group 2)
                     '[/-]'       # separator
                     '(\d{0,2})') # capture day (group 3)
    date2_re = re.compile('(\d{4})''(\d{2})''(\d{2})')
    date3_re = re.compile('(\d{4})''[/-]''(\d{1,2})')
    date7_re = re.compile('(\d{4})''[/-]''(\d{1,2})''[//]''(\d{4})''[/-]''(\d{1,2})')   
    date4_re = re.compile('(\d{1,2})''[//]''(\d{2})')
    date5_re = re.compile('(January|Jan|February|Feb|March|Mar|April|Apr|May|June|Jun|July|Jul|August|Aug|September|Sep|October|Oct|Nov|November|December|Dec)''[/-]''(\d{4})')
    date6_re = re.compile('(January|Jan|February|Feb|March|Mar|April|Apr|May|June|Jun|July|Jul|August|Aug|September|Sep|October|Oct|Nov|November|December|Dec)''[/,]''[ ]''(\d{4})')
    dates = args
    for d in dates:
        match = date_re.match(d)
        match2 = date2_re.match(d)
        match3 = date3_re.match(d)
        match4 = date4_re.match(d)
        match5 = date5_re.match(d)
        match6 = date6_re.match(d)
        match7 = date7_re.match(d)
        if match7:
            day = '01'
            if len(match7.group(2)) == 1:
                month='0'
                print('{}-{}-{}'.format(match7.group(1), month+match7.group(2), day))     
            else:  
                print('{}-{}-{}'.format(match7.group(1), match7.group(2), day))
        else:
            if match:
                if len(match.group(2)) == 1:
                    month='0'
                    if len(match.group(3)) == 1:
                        day = '0'
                        print('{}-{}-{}'.format(match.group(1), month+match.group(2), day+match.group(3)))
                    else:
                        print('{}-{}-{}'.format(match.group(1), month+match.group(2), match.group(3)))
                else:
                    if len(match.group(3)) == 1:
                        day = '0'
                        print('{}-{}-{}'.format(match.group(1), match.group(2), day+match.group(3))) 
                    else:
                        print('{}-{}-{}'.format(match.group(1), match.group(2), match.group(3)))
            elif match2:
                print('{}-{}-{}'.format(match2.group(1), match2.group(2), match2.group(3)))
            elif match3:
                day = '01'
                month = '0'
                if len(match3.group(2)) == 1:
                    print('{}-{}-{}'.format(match3.group(1), month+match3.group(2), day))
                else:
                    print('{}-{}-{}'.format(match3.group(1), match3.group(2), day))
        #elif match7:
            #day = '01'
            #print('{}-{}-{}'.format(match7.group(1), match7.group(2), day))
            elif match4:
                day = '01'
                year = '20'
                month = '0'
                if len(match4.group(1)) == 1:
                    print('{}-{}-{}'.format(year + match4.group(2),month+ match4.group(1), day))
                else:
                    print('{}-{}-{}'.format(year + match4.group(2), match4.group(1), day))
            elif match5:
                day = '01'
                if match5.group(1) == 'Jan' or match5.group(1) == 'January':
                    month = '01'
                    print('{}-{}-{}'.format(match5.group(2), month, day))
                if match5.group(1) == 'Feb' or match5.group(1) == 'February':
                    month = '02'
                    print('{}-{}-{}'.format(match5.group(2), month, day))
                if match5.group(1) == 'Mar' or match5.group(1) == 'March':
                    month = '03'
                    print('{}-{}-{}'.format(match5.group(2), month, day))
                if match5.group(1) == 'Apr' or match5.group(1) == 'April':
                    month = '04'
                    print('{}-{}-{}'.format(match5.group(2), month, day))
                if match5.group(1) == 'May':
                    month = '05'
                    print('{}-{}-{}'.format(match5.group(2), month, day))
                if match5.group(1) == 'Jun' or match5.group(1) == 'June':
                    month = '06'
                    print('{}-{}-{}'.format(match5.group(2), month, day))
                if match5.group(1) == 'Jul' or match5.group(1) == 'July':
                    month = '07'
                    print('{}-{}-{}'.format(match5.group(2), month, day))
                if match5.group(1) == 'Aug' or match5.group(1) == 'August':
                    month = '08'
                    print('{}-{}-{}'.format(match5.group(2), month, day))
                if match5.group(1) == 'Sep' or match5.group(1) == 'September':
                    month = '09'
                    print('{}-{}-{}'.format(match5.group(2), month, day))
                if match5.group(1) == 'Oct' or match5.group(1) == 'October':
                    month = '10'
                    print('{}-{}-{}'.format(match5.group(2), month, day))
                if match5.group(1) == 'Nov' or match5.group(1) == 'November':
                    month = '11'
                    print('{}-{}-{}'.format(match5.group(2), month, day))
                if match5.group(1) == 'Dec' or match5.group(1) == 'December':
                    month = '12'
                    print('{}-{}-{}'.format(match5.group(2), month, day))
            elif match6:
                day = '01'
                if match6.group(1) == 'Jan' or match6.group(1) == 'January':
                    month = '01'
                    print('{}-{}-{}'.format(match6.group(2), month, day))
                if match6.group(1) == 'Feb' or match6.group(1) == 'February':
                    month = '02'
                    print('{}-{}-{}'.format(match6.group(2), month, day))
                if match6.group(1) == 'Mar' or match6.group(1) == 'March':
                    month = '03'
                    print('{}-{}-{}'.format(match6.group(2), month, day))
                if match6.group(1) == 'Apr' or match6.group(1) == 'April':
                    month = '04'
                    print('{}-{}-{}'.format(match6.group(2), month, day))
                if match6.group(1) == 'May':
                    month = '05'
                    print('{}-{}-{}'.format(match6.group(2), month, day))
                if match6.group(1) == 'Jun' or match6.group(1) == 'June':
                    month = '06'
                    print('{}-{}-{}'.format(match6.group(2), month, day))
                if match6.group(1) == 'Jul' or match6.group(1) == 'July':
                    month = '07'
                    print('{}-{}-{}'.format(match6.group(2), month, day))
                if match6.group(1) == 'Aug' or match6.group(1) == 'August':
                    month = '08'
                    print('{}-{}-{}'.format(match6.group(2), month, day))
                if match6.group(1) == 'Sep' or match6.group(1) == 'September':
                    month = '09'
                    print('{}-{}-{}'.format(match6.group(2), month, day))
                if match6.group(1) == 'Oct' or match6.group(1) == 'October':
                    month = '10'
                    print('{}-{}-{}'.format(match6.group(2), month, day))
                if match6.group(1) == 'Nov' or match6.group(1) == 'November':
                    month = '11'
                    print('{}-{}-{}'.format(match6.group(2), month, day))
                if match6.group(1) == 'Dec' or match6.group(1) == 'December':
                    month = '12'
                    print('{}-{}-{}'.format(match6.group(2), month, day))
            else:
                print("No match")
         
 
# ---------- ----------------------------------------
main()
