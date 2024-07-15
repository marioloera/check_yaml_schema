# TEST YAML SCHEMAS

## set up python virtual environment
´´´
    python3 -m venv venv
    source venv/bin/activate
    make install
´´´

## all the code is in yaml_schemas directory
the example used a schema type foo
* definition.yaml
* good_example.yaml
* bad_example.yaml

## testing schemas
´´´
    pytest
´´´