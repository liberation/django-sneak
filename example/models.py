from sneak.models import SneakModel


class FileSystemElement(SneakModel):

    def __init__(self, path):
        super(SneakModel, self).__init__()
        self._path = path

    def path(self):
        return self._path

