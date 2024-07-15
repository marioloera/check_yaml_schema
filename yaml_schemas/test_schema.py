from pykwalify.core import Core

def test_schema():
    schemas = ["schema_definition.yaml"]
    yamls = [
        "good_example.yaml",
        "bad_example.yaml",
    ]

    for data in yamls:
        print(s)
        break
        c = Core(source_file=data, schema_files=schemas)
        c.validate(raise_exception=True)
