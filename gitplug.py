import os
import subprocess
from ranger.api.commands import Command


class git(Command):

    cmds = 'init status clone add rm restore commit remote push'.split()
    # git \ git init \ git status \ git clone \ git add \ git rm \ git restore \ git commit \ git push \ 


    def execute(self):
        # git 
        if not self.arg(1):
            return self.fm.notify("Sytax: git <command>")

        # git INIT +
        if self.arg(1) == self.cmds[0]:
            os.system('git init --quiet')
            return self.fm.notify("Done!")

        # git STATUS +
        if self.arg(1) == self.cmds[1]:
            output = subprocess.check_output(['git', 'status']).decode()
            with open('/tmp/ranger-gitplug-status', 'w') as out:
                out.write(output)
            return self.fm.edit_file('/tmp/ranger-gitplug-status')

        # git CLONE +
        # TIP: 
        #      to clone private repositories you have to store your data
        #      using <git config> in terminals commandline (not rangers)

        if self.arg(1) == self.cmds[2] and not self.arg(2):
            return self.fm.notify("Syntax: git clone <URL>")

        if self.arg(1) == self.cmds[2] and self.arg(2):
            URL = self.arg(2)
            #useless line
            self.fm.notify("Cloning into repository: {}".format(URL))
            os.system("git clone {} --quiet".format(URL))
            return self.fm.notify("Done!")

        # git ADD + 
        if self.arg(1) == self.cmds[3] and not self.arg(2):
            return self.fm.notify("Syntax: git add <FILE>", bad=True)
        
        if self.arg(1) == self.cmds[3] and self.arg(2):

            os.system('git add {0}/{1}'.format(self.fm.thisdir.path, self.arg(2)))

            return self.fm.notify('Done!')
        
        # git RM +
        if self.arg(1) == self.cmds[4] and not self.arg(2):
            
            return self.fm.notify("Syntax: git rm <FILE>", bad=True)

        if self.arg(1) == self.cmds[4] and self.arg(2):
            
            os.system('git rm {0}/{1} --quiet'.format(self.fm.thisdir.path, self.arg(2)))
            
            return self.fm.notify("Done!")

        # git RESTORE + 
        if self.arg(1) == self.cmds[5] and not self.arg(2):

            return self.fm.notify("Syntax: git restore <FILE>", bad=True)

        if self.arg(1) == self.cmds[5] and self.arg(2):

            os.system('git restore --staged {0}/{1} --quiet'.format(self.fm.thisdir.path, self.arg(2)))

            return self.fm.notify("Done!")


        # git COMMIT +
        if self.arg(1) == self.cmds[6] and not self.arg(2):
            return self.fm.notify('Syntax: git commit <text>')

        if self.arg(1) == self.cmds[6] and self.rest(2):
            #fname = os.path.join(self.fm.thisdir.path, os.path.expanduser(self.rest(2)))
            text = self.rest(2)
            os.system('git commit --quiet -m {}'.format(text))
            return self.fm.notify("Done!")


        # GIT REMOTE
        if self.arg(1) == self.cmds[7]:
            
            # GIT REMOTE ADD <NAME> <URL>
            if self.arg(2) == "add" and not self.arg(3):
                return self.fm.notify("Syntax: git remote add <name> <url>")
                
            if self.arg(2) == "add" and self.arg(3) and self.arg(4):
                os.system("git remote add {} {}".format(self.arg(3), self.arg(4)))
                return self.fm.notify("Done!")

            # GIT REMOTE RM <NAME> 
            if self.arg(2) == "rm" and self.arg(3):
                os.system("git remote rm {}".format(self.arg(3)))
                return self.fm.notify("Done!")

            if self.arg(2) == "rm" and not self.arg(3):
                return self.fm.notify("Syntax: git remote remove <name>")

            return self.fm.notify("Syntax: git remote add/rm <name> <url>")

        # GIT PUSH
        if self.arg(1) == self.cmds[8]:

            os.system("git push -u origin master --quiet")

            return self.fm.notify("Done!")
