from __future__ import print_function

import logging
import os.path
import sys
import string
# Main method, just run "python presplit.py
if __name__ =='__main__':
    program = os.path.basename(sys.argv[0])
    logger = logging.getLogger(program)

    logging.basicConfig(format='%(asctime)s: %(levelname)s: %(message)s')
    logging.root.setLevel(level=logging.INFO)
    logger.info("running %s" % ' '.join(sys.argv))

   # sentence = "Comtech International HK Co Ltd"
    if len(sys.argv) != 3:
        print("Using: python presplit.py Comen.txt Comstr.txt")
        sys.exit(1)
    inp,outp  = sys.argv[1:3]
    str = ''
    f = open(inp,'r')
    lines = f.readlines()
    for line in lines:
        str += line.strip() + " "
    f.close()
    result = str.upper()
    print(result)
    output = open(outp,'w')
    output.write(''.join(result))
    output.close
    logger.info("The Company String is " + ''.join(result))
