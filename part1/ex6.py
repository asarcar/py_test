#!/usr/bin/env python

formatter = "%r %r"

print formatter % (1, 2)
print formatter % ("one", "two")

print formatter % (True, False)

print formatter %(formatter, formatter)

print formatter %("Twinkle Twinkle", "Little Star")
