from pykwalify.core import Core


class TestSchemas:
    PATH = "./yaml_schemas/foo"
    SCHEMAS = [f"{PATH}/definition.yaml"]

    def test_good_schema(self):
        yamls = [
            f"{self.PATH}/good_example.yaml",
        ]

        for data in yamls:
            print(data)
            c = Core(source_file=data, schema_files=self.SCHEMAS)
            c.validate(raise_exception=True)

    def test_bad_schema(self):
        schemas = [f"{self.PATH}/definition.yaml"]
        yamls = [
            f"{self.PATH}/bad_example.yaml",
        ]

        for data in yamls:
            print(data)
            c = Core(source_file=data, schema_files=self.SCHEMAS)
            # c.validate(raise_exception=True)

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