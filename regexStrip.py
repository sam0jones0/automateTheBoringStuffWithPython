#! python3
# regexStrip.py - Uses regex to emulate the strip() function

import re

workingString = '          this is a test string.        '

def regexStrip(string, sub=' '):
    if len(sub) != 1:
        print('Second argument must be only 1 character')
        return 'Error'
    else:
        leadingSub = re.compile(rf'^({re.escape(sub)}+)([^{re.escape(sub)}].*)', re.DOTALL)
        trailingSub = re.compile(rf'(.*[^{re.escape(sub)}])({re.escape(sub)}+)$', re.DOTALL)
        string = leadingSub.sub(r'\2', string)
        string = trailingSub.sub(r'\1', string)
        return string

print(regexStrip(workingString))
