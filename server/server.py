"""
Запускать только от имени администратора!!!
"""
import os
import cherrypy
from subprocess import check_output
from cherrypy.lib import static


current_dir = os.path.dirname(os.path.abspath(__file__))
print(current_dir)
invites_dir = current_dir + '\\invites'

if not os.path.exists(invites_dir):
    os.mkdir(invites_dir)

cherrypy.config.update({'server.socket_host': '0.0.0.0', 'server.socket_port': 80})


class Zagonyator_WebApp:

    @cherrypy.expose
    def auth(self, login, password):
        code = '1'
        return code


    @cherrypy.expose
    def invite(self, computername, domain):
        # run djoin
        cmd = f"djoin /provision /domain {domain} /machine {computername} /savefile {invites_dir}\\{computername}.invite /reuse".split(' ')
        output = check_output(cmd, shell=True)
        return static.serve_file(invites_dir + '\\'+ computername +'.invite', 'application/x-download', 'attachment',
                                 computername + '.invite')


cherrypy.quickstart(Zagonyator_WebApp(),'/')
