from pykwalify.core import Core


class TestSchemas:
    PATH = "./yaml_schemas/foo"
    SCHEMAS = [f"{PATH}/definition.yaml"]

    def test_good_schema(self):
        data = f"{self.PATH}/good_example.yaml"
        c = Core(source_file=data, schema_files=self.SCHEMAS)
        c.validate(raise_exception=True)

    def test_bad_schema(self):
        data = f"{self.PATH}/bad_example.yaml"
        c = Core(source_file=data, schema_files=self.SCHEMAS)
        c.validate(raise_exception=True)
