
from mycli.sqlcompleter import SQLCompleter

import base64


from IPython.core.magic import (
    Magics, magics_class, cell_magic, completer_for
)

import sqlite3


    
@magics_class
class SQLMagic(Magics):

    def __init__(self, shell, *args, **kwargs):
        super().__init__(shell, *args, **kwargs)

        comp = SQLCompleter(smart_completion=True)
        self.db = sqlite3.connect('orly.db')
        self.shell = shell

        metadata = {
            'books': ['name','cover', 'color'],
        }


        tables, columns = [], []

        for table, cols in metadata.items():
            tables.append((table,))
            columns.extend([(table, col) for col in cols])

        comp.set_dbname('orly')
        comp.extend_schemata('orly')
        comp.extend_relations(tables, kind='tables')
        comp.extend_columns(columns, kind='tables')
        self.comp = comp


    @completer_for('sql')
    def completer_for_sql(self, line, cell, offset):
        from IPython.core.completer import Completion
        previous = (line+'\n'+cell)[:offset].split()[-1]
        for c in SQLCompleter.find_matches(previous, self.comp.all_completions):
            yield Completion(offset+c.start_position, offset, c.text)

    @cell_magic
    def sql(self, line, cell):
        from IPython.display import Image
        cur = self.db.execute(cell)
        res = []

        def imagify(x):
            if len(x) > 50:
                return Image(x)
            return x
        for c in cur:
            loc = [imagify(x) for x in c]
            if len(loc) == 1:
                loc = loc[0]
            res.append(loc)
        self.shell.user_ns['rly'] = res
        return res



def load_ipython_extension(ipython):
    ipython.register_magics(SQLMagic)

