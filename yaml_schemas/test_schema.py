from pykwalify.core import Core

def test_good_schema():
    path = "./yaml_schemas/foo"
    schemas = [f"{path}/definition.yaml"]
    yamls = [
        f"{path}/good_example.yaml",
    ]

    for data in yamls:
        print(data)
        c = Core(source_file=data, schema_files=schemas)
        c.validate(raise_exception=True)

def test_bad_schema():
    path = "./yaml_schemas/foo"
    schemas = [f"{path}/definition.yaml"]
    yamls = [
        f"{path}/bad_example.yaml",
    ]

    for data in yamls:
        print(data)
        c = Core(source_file=data, schema_files=schemas)
        c.validate(raise_exception=True)

# def test_schema():
#     path = "./yaml_schemas/foo"
#     schemas = [f"{path}/definition.yaml"]
#     yamls = [
#         f"{path}/good_example.yaml",
#         f"{path}/bad_example.yaml",
#     ]

#     for data in yamls:
#         print(data)
#         c = Core(source_file=data, schema_files=schemas)
#         #c.validate(raise_exception=True)