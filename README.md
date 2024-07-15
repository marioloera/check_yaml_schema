# TEST YAML SCHEMAS
using python [pykwalify](https://pypi.org/project/pykwalify/)

## Example of the schema
```yaml
dataProductName: review
sourceConfigs:
  - inputTopic: data.input.1
    fieldMapping:
      inputField: message
      targetField: message
  - inputTopic: data.input.2
    fieldMapping:
      inputField: from
      targetField: from
favoriteColor: BLUE
```

## Example of the schema definition
full schema yaml_schemas/foo/definition.yaml
```yaml
type: map
mapping:
  dataProductName:
    required: true
    type: str

  sourceConfigs:
    required: false
    type: seq
    sequence:
      - type: 
        include: sourceConfig

  favoriteColor:
    required: false
    type: str
    enum: ['BLUE', 'RED']
```

## set up python virtual environment
```
python3 -m venv venv
source venv/bin/activate
make install
```

## all the code is in yaml_schemas directory
the example used a schema type foo
* definition.yaml
* good_example.yaml
* bad_example.yaml

## testing schemas
```
    pytest
```
