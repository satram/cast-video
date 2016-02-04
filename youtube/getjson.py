#!/usr/bin/env python

import os


ifilename = 'int1.txt'
ofilename = 'int1-out.txt'
prev_emptyline = False

ifp = open(ifilename, 'r')
with open(ofilename, 'w') as ofp:
    for line in ifp:
        content_written = False

        if len(line) > 73:
            content = line[73:]
            # if '.' not in content:
            ofp.write(content.rstrip())
            content_written = True
            prev_emptyline = False

        if content_written is False and prev_emptyline is False:
            ofp.write('\n')
            prev_emptyline = True
ifp.close()

ifilename = 'int1-out.txt'
ofilename = 'int1-out-json.txt'
ifp = open(ifilename, 'r')
with open(ofilename, 'w') as ofp:
    for line in ifp:
        ind = line.find('{')
        if ind != -1:
            ofp.write(line[ind:])
ifp.close()
