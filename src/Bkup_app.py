from flask import Flask, jsonify, request
import ssh_connect
import vulneribility_finder
from pycvesearch import CVESearch

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



# driver function
if __name__ == '__main__':
    app.run(debug=True)
