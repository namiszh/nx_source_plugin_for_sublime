import sublime
import sublime_plugin
import os.path
from datetime import date

class FileHeaderCommand(sublime_plugin.TextCommand):
    def run(self, edit):
        snippet = 'Packages/DevOps/file_header.sublime-snippet'
        filePath, fileName = os.path.split(self.view.file_name())
        shortName = os.path.splitext(fileName)[0].strip().upper()
        extName = os.path.splitext(fileName)[1][1:].strip().upper()
        if extName == 'H':
            extName = 'HHH'
        components = filePath.split(os.sep)
        library = components[components.index("src")+1].upper()
        today = datetime.date.today()
        year=today.year
        date = today.strftime("%d-%B-%Y")
        userName ='Marvin'
        self.view.run_command('insert_snippet', {'name': snippet, 'FILE_NAME' : shortName, 'EXT_NAME' : extName, 'LIB_NAME' : library, 'YEAR' : year, 'DATE' : date, 'USER_NAME' : userName})

