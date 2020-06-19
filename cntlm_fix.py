import re
import argparse

rep = {"0":"F","1":"E","2":"D","3":"C","4":"B","5":"A","6":"9","7":"8","8":"7","9":"6","A":"5","B":"4","C":"3","D":"2","E":"1","F":"0"}

parser = argparse.ArgumentParser(description='CNTLM Hash')
parser.add_argument('hash', metavar='HASH',type=str,help='a CNTLM generated hash')

args = parser.parse_args()

rep = dict((re.escape(k), v) for k, v in rep.items()) 
pattern = re.compile("|".join(rep.keys()))
print(pattern.sub(lambda m: rep[re.escape(m.group(0))], args.hash))
