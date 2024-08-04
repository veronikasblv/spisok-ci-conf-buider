#!/usr/bin/python
import yaml
import os

with open("./sections/proceedings.yml", 'r') as src:
    data = yaml.load(src, Loader=yaml.FullLoader)

sections = data.get('sections')
sec_name_list = [ ]
for sec in sections:
    for key in sec.keys():
        sec_name_list.append(key)

directory = './sections'

for dr in os.listdir(directory):
    if os.isdir(dr):
        if dr not in sec_name_list:
            os.rmdir(os.path.join(directory, dr))

for sec in sec_name_list:
    if sec not in os.listdir(directory):
        os.makedirs(os.path.join(directory, sec))
    sec_dir = os.path.join(directory, sec)
    sec_yml_file = open(os.path.join(sec_dir, "section.yml"), 'w')
    for dicts in sections:
        if sec in dicts.keys():
            file_list = dicts[sec]['files']
            del dicts[sec]['files']
            yaml.dump(dicts[sec], sec_yml_file, allow_unicode=True, default_flow_style=False, sort_keys=False, indent=2)
    for article in file_list:
        os.system(f'cp ./articles/"{article}" ./sections/"{sec}"')
        


        
