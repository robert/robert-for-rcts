import hashlib
import random
import csv
import os
import sys

input_path = sys.argv[1]

print "Generating assignments for %s..." % input_path
print "========"

input_dir, input_fname = os.path.split(input_path)
input_noext = os.path.splitext(input_fname)[0]
output_fname = '%s-output.csv' % input_noext
output_path = os.path.join(input_dir, output_fname)

with open(input_path) as f:
    r = csv.reader(f)
    participants = [l[0] for l in r]

h = hashlib.sha256()
h.update('\n'.join(participants))
i = int(h.hexdigest(), 16)

random.seed(i)

def randgroup():
    return 'CONTROL' if random.randint(1, 2) == 1 else 'TREATMENT'

assignments = map(lambda p: [p, randgroup()], participants)

with open(output_path, 'w') as f:
    writer = csv.writer(f)
    for a in assignments:
        writer.writerow(a)
        print "%s, %s" % (a[0], a[1])

print "========"
print "Wrote output to: %s" % output_path
