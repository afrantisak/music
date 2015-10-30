#!/usr/bin/env python
import fileinput

waves = {}
old_num = None
for line in fileinput.input():
    tokens = line.split()
    num = None
    inst_data = []
    for token in tokens:
        try:
            num = int(token)
            if inst_data:
                waves[old_num] = ' '.join(inst_data)
            old_num = num
            num = None
            inst_data = []
        except:
            inst_data.append(token)
    if inst_data:
        waves[old_num] = ' '.join(inst_data)

for k, v in waves.iteritems():
    print k, v
        
