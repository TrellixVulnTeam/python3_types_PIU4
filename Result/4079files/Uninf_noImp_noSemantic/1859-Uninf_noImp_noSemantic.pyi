from traitlets import HasTraits

class Feature(HasTraits):
    environment: YuunoIPythonEnvironment = ...
    @classmethod
    def feature_name(cls): ...
    def initialize(self) -> None: ...
    def deinitialize(self) -> None: ...
