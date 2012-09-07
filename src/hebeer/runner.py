# encoding: utf-8

import os, shutil, threading, time, re
from git import Repo

class AsyncRunner(threading.Thread):
    def __init__(self, repo_id):
        threading.Thread.__init__(self)
        self.repo_id = repo_id

    def run(self):
        """ TODO: use real repo :) """
        name = str(self.repo_id) + '_' + time.strftime("%s")
        path = "https://github.com/grauwoelfchen/rradio.git"
        repo = Repo.clone_from(path, name)
        os.chdir(name)
        print os.getcwd()
        os.system('bundle install --path .bundle/gems > test.log')
        os.system('bundle exec rake spec > test.log')
        f = open('test.log', 'r')
        res = f.read()
        f.close()
        f_m = re.compile("(\d+)\s+failure?").search(res)
        e_m = re.compile("(\d+)\s+error?").search(res)
        f = f_m and int(f_m.group(1)) or 0
        m = e_m and int(e_m.group(1)) or 0
        if f + m > 0:
            print 'Test failed'
        else:
            print 'Test passed'

        os.chdir(os.pardir)
        shutil.rmtree(name)
        print('repo id is %s' % self.repo_id)
