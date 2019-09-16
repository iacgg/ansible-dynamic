#!/usr/bin/env bash

cd python
./ansible-playbook.py "../inventories/local-test.yml"
cd ..

composer update &> /dev/null

echo '
{"local":
  { "hosts": 
    [
    "localhost"
    ] 
  } 
}
'
