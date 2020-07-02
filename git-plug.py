import os
import ranger.api
from ranger.api.commands import Command


class git(Command):
    """:git <command>

    """
    modes = {
        'clone': 'URL',
        'init': '',
    }

    def execute(self):
        if not self.arg(1):
            self.fm.notify("Usage: git <command>", bad=True)
        
        URL = self.arg(2)
        if self.arg(1) and not URL:
            self.fm.notify("error", bad=True)
           
        if self.arg(1) == "clone" and URL:
            os.system('git clone {} --quiet'.format(URL))
            self.fm.notify("Done!")

        if self.arg(1) == "init":
            os.system('git init --quiet')
            self.fm.notify("Done!")

    def tab(self, tabnum):
        return (
            self.start(1) + mode for mode
            in sorted(self.modes.keys())
            if mode
        )

# NOTES:
# nothing interesting just my comments 
# git --> raise error syntax
# git + tab --> show avaible commands
# git + <clone> --> raise error, url not defined
# git + <clone> + <URL> --> clone repo into current path
#
#
