import os

from sneak.query import ListQuerySet

from models import FileSystemElement


class FileSystemQuerySet(ListQuerySet):

    def filter(self, *args, **kwargs):

        fs = []

        path = os.path.dirname(__file__)
        path = os.path.join(path, 'fs')
        path = os.path.realpath(path)

        def populate(path):
            for f in os.listdir(path):
                p = os.path.join(path, f)
                if os.path.isdir(p):
                    fs.append(FileSystemElement(p))
                    populate(p)
                else:
                    fs.append(FileSystemElement(p))
        populate(path)
        return FileSystemQuerySet(fs)
