import sys
import re
import json

input_ = [line.strip() for line in sys.stdin.readlines()]
required_fields = set(['byr','iyr','eyr','hgt','hcl','ecl','pid','cid'])

valid_count = 0
for line in input_:
    field_names = set([field.split(':')[0] for field in line.split(' ')])
    missing = required_fields - field_names - set(['cid'])
    if not missing:
        valid_count += 1
print(valid_count)


valid_count = 0
for line in input_:
    fields = {}
    for keyval in line.split(' '):
        key,val = keyval.split(':')
        fields[key] = val
    if True \
       and 'byr' in fields and 1920<=int(fields['byr'])<=2002 \
       and 'iyr' in fields and 2010<=int(fields['iyr'])<=2020 \
       and 'eyr' in fields and 2020<=int(fields['eyr'])<=2030 \
       and 'hgt' in fields and (fields['hgt'][-2:]=='cm' and 150<=int(fields['hgt'][:-2])<=193 \
                            or  fields['hgt'][-2:]=='in' and  59<=int(fields['hgt'][:-2])<= 76) \
       and 'hcl' in fields and re.match('^#[0-9a-f]{6}$',fields['hcl']) \
       and 'ecl' in fields and fields['ecl'] in ['amb','blu','brn','gry','grn','hzl','oth'] \
       and 'pid' in fields and re.match('^[0-9]{9}$',fields['pid']):
        valid_count += 1
print(valid_count)
