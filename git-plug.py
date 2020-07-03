import os
import ranger.api
from ranger.api.commands import Command
import subprocess



class git(Command):

    cmds = 'init status commit push clone'.split()

    def execute(self):

        # no command
        if not self.arg(1):
            return self.fm.notify("Sytax: git <command>")

        # init
        if self.arg(1) == self.cmds[0]:
            os.system('git init --quiet')
            return self.fm.notify("Done!")

        # status
        if self.arg(1) == self.cmds[1]:
            outp = subprocess.check_output(['git', 'status']).decode()
            with open('/tmp/git-plug-outp', 'w') as out:
                out.write(outp)
            self.fm.edit_file('/tmp/git-plug-outp')

        # clone
        if self.arg(1) == self.cmds[4] and not self.arg(2):
            return self.fm.notify("Syntax: git clone <URL>")

        if self.arg(1) == self.cmds[4] and self.arg(2):
            URL = self.arg(2)
            #useless line
            self.fm.notify("Cloning into repository: {}".format(URL))
            os.system("git clone {} --quiet".format(URL))
            return self.fm.notify("Done!")
            
