# -*- coding: utf-8 -*-
#!/usr/local/bin/python
#Time: 2018/8/23 21:45:03
#Description: 
#File Name: mysshclient.py
 
import paramiko
from chardet.universaldetector import UniversalDetector
detector = UniversalDetector()

conf = {
'192.168.164.41':('dsadm','dsadm'),
'192.168.164.40':('edw','edw'),
}

class SSHConnection(object):
    def __init__(self, host, port):
        self._host = host
        self._port = port
        self._username = conf[host][0]
        self._password = conf[host][1]
        self._transport = None
        self._sftp = None
        self._client = None
        self._connect()  # 建立连接
 
    def _connect(self):
        transport = paramiko.Transport((self._host, self._port))
        transport.connect(username=self._username, password=self._password)
        self._transport = transport
 
    #下载
    def download(self, remotepath, localpath):
        if self._sftp is None:
            self._sftp = paramiko.SFTPClient.from_transport(self._transport)
        self._sftp.get(remotepath, localpath)
 
    #上传
    def put(self, localpath, remotepath):
        if self._sftp is None:
            self._sftp = paramiko.SFTPClient.from_transport(self._transport)
        self._sftp.put(localpath, remotepath)
 
    #执行命令
    def exec_command(self, command):
        if self._client is None:
            self._client = paramiko.SSHClient()
            self._client._transport = self._transport
        stdin, stdout, stderr = self._client.exec_command(command)
        data = stdout.read()
        returncode = stdout.channel.recv_exit_status()
        if len(data) > 0:
            try:
                print(data.decode('utf-8').strip())
            except UnicodeDecodeError:
                print(data.decode('gbk').strip())
            #return data
        err = stderr.read()
        if len(err) > 0:
            try:
                print(err.decode('utf-8').strip())
            except UnicodeDecodeError:
                print(err.decode('gbk').strip())
            #return err
        #print("返回值：",returncode)
        return(returncode)
 
    def close(self):
        if self._transport:
            self._transport.close()
        if self._client:
            self._client.close()


def run_ssh_command(ip,command):
    conn = SSHConnection(ip,22)
    if conn.exec_command(command):
        return 1
    else:
        return 0

if __name__ == "__main__":
    conn = SSHConnection('192.168.164.41', 22)
    conn.exec_command('sh test.sh 0')
    conn.exec_command('sh test.sh 1')
