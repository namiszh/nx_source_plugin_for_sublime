
import sublime
import sublime_plugin
import re

class IncludeHeaderCommand(sublime_plugin.TextCommand):
    def run(self, edit):
        sublime.active_window().show_input_panel("Header File", "schema/", self.on_done, None, None)

    def on_done(self, text):
        # The command has returned after the show_input_panel has completed (thus closing the edit object). 
        self.view.run_command("include_header_internal", {"text": text})


class IncludeHeaderInternalCommand(sublime_plugin.TextCommand):
    def run(self, edit, text):
        pos = self.get_last_include_line()
        text = '/'.join(text.split('\\'))
        line = "\n#include <" + text + ">"
        self.view.insert(edit, pos, line)

    def get_last_include_line(self):
        regions = self.view.find_all('^#include\s+<.*>\s*$')

        for region in reversed(regions):
            lines = self.view.lines(region)

            for line in reversed(lines):
                return line.end()

        # if there is no existing '#include', and the include file after
        # history
        region1 = self.view.find("^\$HISTORY\$$", 0)
        region2 = self.view.find("=*/", region1.end(), sublime.LITERAL)
        row, col = self.view.rowcol(region2.begin())
        return self.view.text_point(row+1, 0)
