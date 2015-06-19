__author__ = 'will'

import sys
import os
import re
import collections


def main(lines):
    pattern =re.compile(r'@[\w]+\.[\w]+')
    records = lines[1:]
    print records
    new_records = []
    for i,r in enumerate(records):
        #Schema: index, email, name, domain,flag
        r = r.split(',')
        email = r[0]
        name = r[1]
        flag = 'NA'
        domain =  re.search(pattern,email)
        record = [i,email,name,domain.group(0),flag]
        new_records.append(record)


    print new_records
    domains = collections.Counter([r[3] for r in new_records])
    names = domains = collections.Counter([r[2] for r in new_records])
    print domains
    print names

    final_records = []
    for i, r in enumerate(new_records):
        domain = r[3]
        name = r[2]
        if domains[domain] > 1 and names[name]>1:
            flag = 1
        else:
            flag = 0
        r[4] = flag
        new_records[i] = r

    print new_records
    return


if __name__ != "__main__":
    f = open(sys.argv[1],'r')
    lines = f.readlines()
    f.close()
    main(lines)
else:
    print os.getcwd()
    f = open('names.csv','r')
    lines = f.readlines()
    f.close()
    main(lines)

