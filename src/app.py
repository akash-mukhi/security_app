from flask import Flask, jsonify, request
import ssh_connect

# import packet_capturer

app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'GET':
        data = "Hackathon"
        return jsonify({'data': data})


@app.route('/GetSecurityPolicyForAllNs', methods=['GET'])
def get_pod_security_policy():
    if request.method == 'GET':
        ssh = ssh_connect.ssh_conncet()
        data = ssh.run_command_to_sde_machine('kubectl get psp --all-namespaces -o json')
        return jsonify(data)


# @app.route('/name', methods=['GET'])
# def get_cve_vulnerability():
#     name = 'mysql'
#     # vf=vulneribility_finder.cve_vulneribility_finder()
#     # full_version_cve_list, given_version_cve_list= vf.get_vulnerability(name)
#     # print(full_version_cve_list, given_version_cve_list)
#     # return full_version_cve_list, given_version_cve_list
#     cve = CVESearch('https://cve.circl.lu/')
#     a=cve.search('mysql')
#     print(a)

@app.route('/GetAllPod', methods=['GET'])
def get_all_pods():
    if request.method == 'GET':
        ssh = ssh_connect.ssh_conncet()
        data = ssh.run_command_to_sde_machine('kubectl get pods --all-namespaces -o json')
        return jsonify(data)


# @app.route('/Getpackets', methods=['GET'])
# def get_packets():
#     if request.method == 'GET':
#         ssh = ssh_connect.ssh_conncet()
#         packet=packet_capturer.PacketTracer()
#         data = packet.get_network_packet()
#         return jsonify(data)


@app.route('/GetAllDeployment', methods=['GET'])
def get_all_deployment():
    if request.method == 'GET':
        ssh = ssh_connect.ssh_conncet()
        data = ssh.run_command_to_sde_machine('kubectl get deployment --all-namespaces -o json')

        return jsonify(data)


def create_all_deployment_file():
    out = []
    buff = []
    ssh = ssh_connect.ssh_conncet()
    data = ssh.run_command_to_sde_machine('kubectl get deployment | awk \'{print $1}\'')
    print(data)
    for c in data:
        if c == '\n':
            out.append(''.join(buff))
            buff = []
        else:
            buff.append(c)
    else:
        if buff:
            out.append(''.join(buff))
    print(out)
    out= out[1:]
    for i in out:
        ssh.run_command_to_sde_machine('kubectl get deployment cloud-volumes-infrastructure -o yaml --export  > /tmp/sharma/{}.yaml'.format(i))
    print('Creation Done')


@app.route('/GetDeploymentInfo', methods=['GET'])
def get_kube_sec_info():
    ssh =ssh_connect.ssh_conncet()
    name='meteorqloud.yaml'
    data= ssh.run_command_to_sde_machine('curl -sSX POST --data-binary @/tmp/sharma/{} http://localhost:8080/scan'.format(name))
    print(data)
    return jsonify(data)


# driver function
if __name__ == '__main__':
    # create_all_deployment_file()
    app.run(host="0.0.0.0", port=5000)
