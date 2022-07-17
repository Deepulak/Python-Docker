#!/usr/bin/env python

from os import getenv

if getenv('NAME') is None:
	name = 'World!'
else:
	name = getenv('NAME')

print("Hello {}".format(name))