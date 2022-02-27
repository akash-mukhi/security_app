import paramiko


class ssh_conncet():
    nbytes = 4096
    hostname = '10.193.57.131'
    port = 22
    input_username = 'root'
    input_password = 'netapp1!'
    command = 'ls'

    def run_command_to_sde_machine(self, command):
        try:
            client = paramiko.SSHClient()
            client.load_system_host_keys()
            client.set_missing_host_key_policy(paramiko.WarningPolicy)

            client.connect(self.hostname, port=22, username=self.input_username, password=self.input_password)

            stdin, stdout, stderr = client.exec_command(command)
            return stdout.read().decode('UTF-8')

        finally:
            client.close()



