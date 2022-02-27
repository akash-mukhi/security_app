import cveSearch
import re
import pyshark
import time
import requests

class cve_vulneribility_finder():

    # def get_vulnerability(self, product_name, version=None):
    #     full_version_cve_list = []
    #     given_version_cve_list = []
    #     cve = cveSearch.CVESearch()
    #     list_of_vulnerabilities = cve.search(product_name)
    #     for i in range(len(list_of_vulnerabilities['data'])):
    #         # regex_patt = re.compile(r'1+.16+.*')
    #         if version is not None:
    #             regex_patt = re.compile(version)
    #             for j in range(len(list_of_vulnerabilities['data'][i]['vulnerable_configuration'])):
    #                 if regex_patt.search(list_of_vulnerabilities['data'][i]['vulnerable_configuration'][j]):
    #                     given_version_cve_list.append(list_of_vulnerabilities['data'][i]['id'])
    #         else:
    #             given_version_cve_list = full_version_cve_list
    #         full_version_cve_list.append(list_of_vulnerabilities['data'][i]['id'])
    #     full_version_cve_list = set(full_version_cve_list)
    #     given_version_cve_list = set(given_version_cve_list)
    #     return full_version_cve_list, given_version_cve_list



    def get_cve_dbInfo(self):
        cve = cveSearch.CVESearch()
        dbInfo=cve.dbinfo()
        return dbInfo

    def get_vulnerability(self):
        cve = cveSearch.CVESearch()
        dbInfo=cve.search('microsoft')
        print (dbInfo)

