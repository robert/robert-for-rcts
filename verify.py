import hashlib
import random
import csv
import os
import sys

input_path = sys.argv[1]

print "Verifying assignments for %s..." % input_path

with open(input_path) as f:
    r = csv.reader(f)
    input_assignments = [l for l in r]

participants = [a[0] for a in input_assignments]

h = hashlib.sha256()
h.update('\n'.join(participants))
i = int(h.hexdigest(), 16)

random.seed(i)

def randgroup():
    return 'CONTROL' if random.randint(1, 2) == 1 else 'TREATMENT'

generated_assignments = map(lambda p: [p, randgroup()], participants)

if input_assignments == generated_assignments:
    print "Assignments are valid!"
else:
    print "!!!! Assignments are not valid !!!!"
    print "You gave me:"
    print input_assignments
    print ""
    print "I generated:"
    print generated_assignments
