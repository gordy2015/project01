
import paramiko

class SSHConnect(object):
    def __init__(self,hostname,port,user,passwd,pk):
        self.host = hostname
        self.port = port
        self.user = user
        self.passwd = passwd
        self.pk = pk



    def cmd(self):
        tr = paramiko.Transport(self.host, self.port)
        tr.connect(username=self.user, password=self.passwd)
        ssh = paramiko.SSHClient()
        ssh._transport = transport
        command = raw_input()
        stdin,stdout, stderr = ssh.exec_command(A)
        print(str(stdout.read()))
        tr.close()


s = SSHConnect('192.168.2.11','root','!@abce')
s.cmd('ls')