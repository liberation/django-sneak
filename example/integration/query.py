import os

from sneak.query import ListQueryResult

from models import FileSystemElement


class FileSystemQuerySet(object):

    def filter(self, *args, **kwargs):

        class QueryResult(ListQueryResult):
            # this does no filtering, ordering or delete
            # it's just for the purpose of a simple example
            def filter(self, *args, **kwargs):
                return self

            def order_by(self, *args, **kwargs):
                return self

            def delete(self):
                return len(self.value)

        fs = []

        path = os.path.dirname(__file__)
        path = os.path.join(path, '..', 'fs')
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
        return QueryResult(fs)

