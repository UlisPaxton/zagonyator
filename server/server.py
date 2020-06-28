"""
Запускать только от имени администратора!!!
"""
import os
import cherrypy
from subprocess import check_output
from cherrypy.lib import static



#cmd = f"djoin /provision /domain zdomain.ru /machine edial /savefile C:\\Users\Admin\Desktop\\invites/{computername}.invite".split(' ')
#print(cmd)
#os.system(cmd)
#check_output(cmd, shell=True)


current_dir = os.path.dirname(os.path.abspath(__file__))
print(current_dir)
invites_dir = current_dir + '\\invites'

if not os.path.exists(invites_dir):
    os.mkdir(invites_dir)


cherrypy.config.update({'server.socket_host': '0.0.0.0', 'server.socket_port': 80})

# conf = {'/invites': {
#             'tools.staticdir.on':True,
#             'tools.staticdir.dir': invites_dir,
#                     }
#         }

class Zagonyator_WebApp:

    @cherrypy.expose
    def auth(self, login, password):
        code = '1'
        return code


    @cherrypy.expose
    def invite(self, computername, domain):
        # run djoin
        cmd = f"djoin /provision /domain {domain} /machine {computername} /savefile {invites_dir}\\{computername}.invite /reuse".split(' ')
        #cmd = "djoin /provision"
        print(cmd)
        #os.system(cmd)
        output = check_output(cmd, shell=True)
        print(output)
        return static.serve_file(invites_dir + '\\'+ computername +'.invite', 'application/x-download', 'attachment',
                                 computername + '.invite')


cherrypy.quickstart(Zagonyator_WebApp(),'/')