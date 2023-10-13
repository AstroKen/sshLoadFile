import numpy as np
import paramiko

class sshLoadFile:
    def __init__(self, hostname, usename, key_filename):
        self.client = paramiko.SSHClient()
        self.client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        self.client.connect(
                hostname=hostname,
                username=usename,
                key_filename=key_filename
                )
        self.sftp = self.client.open_sftp()

    def sshloadtxt(self, filename):
        with self.sftp.open(filename, 'r') as f:
            data = np.loadtxt(f)
        return data

    def __del__(self):
        self.client.close()
        print('ssh conection is closed.')
