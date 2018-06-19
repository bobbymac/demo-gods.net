#!/usr/bin/python

with open('fr.3', 'r') as f:
    for i, line in enumerate(f, start=2):
        print'{} IN A 10.0.120.{}'.format(line.strip(), i+1)
