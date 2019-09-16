#!/usr/bin/env python3

import sys
import yaml
import json

default_role_path = "default-roles.yml"

try:
    test = sys.argv[1]
except:
        print('need a argument')
        exit(1)

def merge_two_dicts(dict_one, dict_two):
    final_dict = dict_one.copy()

    try:
        final_dict.update(dict_two)
    except:
        this = 'that' #print('no second dict')

    return final_dict

def yaml_to_var(path):
    with open(path, 'r') as stream:
        try:
            yaml_var = yaml.safe_load(stream)
        except yaml.YAMLError as exc:
            print(exc)
    return yaml_var

default_roles = yaml_to_var(default_role_path)

facility_roles = yaml_to_var('../inventories/{0}'.format(sys.argv[1]))

merged_dict = merge_two_dicts(default_roles, facility_roles)

#print(merged_dict)

composer = { "config": { "vendor-dir": "roles" }, "repositories":[], "require": {} }

for role, branch in merged_dict.items():
    composer['repositories'].append({"type": "vcs", "url": "git@github.com:mrscherrycoke/" + role + ".git"})
    composer['require'].update({'{0}'.format( role ): 'dev-{0}'.format( branch )})

composer_file = open("../composer.json","w+")
composer_file.write(json.dumps(composer, sort_keys=True))
composer_file.close()
#print(json.dumps(composer, sort_keys=True))
