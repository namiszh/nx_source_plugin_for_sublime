import sublime
import sublime_plugin
# import os.path
import datetime

SETTINGS_FILE = 'nxdev.sublime-settings'

class HistoryLineCommand(sublime_plugin.TextCommand):
    def run(self, edit):

        region = self.view.find("$HISTORY$", 0, sublime.LITERAL)
        if region:
            today = datetime.date.today()
            date = today.strftime("%d-%B-%Y")

            userName = sublime.load_settings(SETTINGS_FILE).get("display_name")
            userName += ' ' *(24 - len(userName) ) # make sure the indent is correct no matter the display name length is
            content = date + "  " + userName

            pt = region.begin()
            self.view.insert(edit, pt, '\n')    # insert line before $HISTORY$

            self.view.sel().clear()
            self.view.sel().add(sublime.Region(pt))
            self.view.insert(edit, pt, content)
            self.view.show(pt)
