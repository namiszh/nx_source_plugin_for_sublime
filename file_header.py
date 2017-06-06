import sublime
import sublime_plugin
import os.path
import datetime

SETTINGS_FILE = 'nxdev.sublime-settings'

class FileHeaderCommand(sublime_plugin.TextCommand):
    def run(self, edit):
        snippet = 'Packages/nxdev/file_header.sublime-snippet'
        dirName, baseName = os.path.split(self.view.file_name())
        shortName = os.path.splitext(baseName)[0].strip()
        extName = os.path.splitext(baseName)[1][1:].strip().upper()
        if extName == 'H': extName = 'HHH'

        parentDirs = dirName.split(os.sep)
        if "src" not in parentDirs or parentDirs.index("src") == (len(parentDirs) - 1):
            print("*** ERROR: Cannot find library name. Please make sure the lib directory is under 'src' directory.")
            return

        library = parentDirs[parentDirs.index("src")+1].upper()

        today = datetime.date.today()
        year = today.year
        date = today.strftime("%d-%B-%Y")
        userName = sublime.load_settings(SETTINGS_FILE).get("display_name")
        # print(userName)
        userName += ' ' *(24 - len(userName) ) # make sure the indent is correct no matter the display name length is

        self.view.run_command('move_to', {"to": "bof"})
        self.view.run_command('insert_snippet', {'name': snippet, 'FILE_NAME' : shortName, 'EXT_NAME' : extName, 'LIB_NAME' : library, 'YEAR' : year, 'DATE' : date, 'USER_NAME' : userName})

