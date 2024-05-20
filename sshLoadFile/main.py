import numpy as np
import paramiko

class sshLoadFile:
    def __init__(self, hostname, usename, port, key_filename):
        self.client = paramiko.SSHClient()
        self.client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        self.client.connect(
                hostname=hostname,
                username=usename,
                port=port,
                key_filename=key_filename
                )
        self.sftp = self.client.open_sftp()

    def sshloadtxt(self, filename, nskip):
        with self.sftp.open(filename, 'r') as f:
            data = np.loadtxt(f, skiprows=nskip)
        return data

    def __del__(self):
        self.client.close()
        print('ssh conection is closed.')
