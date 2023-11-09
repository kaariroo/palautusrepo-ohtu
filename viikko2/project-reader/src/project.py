class Project:
    def __init__(self, name, description, dependencies, dev_dependencies, license, authors):
        self.name = name
        self.description = description
        self.dependencies = dependencies
        self.dev_dependencies = dev_dependencies
        self.license = license
        self.authors = authors

    def _stringify_dependencies(self, dependencies):
        dependencies2 = []
        for d in dependencies:
            d = "-" + str(d)
            dependencies2.append(d)
        string = f"\n".join(dependencies2) if len(dependencies2) > 0 else "-"
        return string

    def __str__(self):
        return (
            f"Name: {self.name}"
            f"\nDescription: {self.description or '-'}"
            f"\nLicense: {self.license}"
            f"\n"
            f"\nAuthors: \n{self._stringify_dependencies(self.authors)}"
            f"\n"
            f"\nDependencies: \n{self._stringify_dependencies(self.dependencies)}"
            f"\n"
            f"\nDevelopment dependencies: \n{self._stringify_dependencies(self.dev_dependencies)}"
        )
