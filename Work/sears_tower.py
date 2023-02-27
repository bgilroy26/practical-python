#!/usr/bin/python

bill_thickness_in = 0.0043
bill_thickness_ft = bill_thickness_in / 12.0
height_of_sears_tower_ft = 1450
days = 1
bill_height_ft = 0

while bill_height_ft/2.0 <= height_of_sears_tower_ft:
    bill_height_ft = bill_height_ft + bill_thickness_ft * (2**days)
    days = days + 1

print(f'{days} days to reach Sears\' Tower height')
