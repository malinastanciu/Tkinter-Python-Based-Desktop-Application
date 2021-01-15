import json


class Pachet():


    def __init__(self, Ethernet_src='', Ethernet_dst='',
                 IP_dst='', IP_src='', IP_version='', IP_proto='',
                 TCP_sport='', TCP_dport='',
                 UDP_sport='', UDP_dport=''):
        self.Ethernet_src = Ethernet_src
        self.Ethernet_dst = Ethernet_dst
        self.IP_dst = IP_dst
        self.IP_src = IP_src
        self.IP_version = IP_version
        self.IP_proto = IP_proto
        self.TCP_sport = TCP_sport
        self.TCP_dport = TCP_dport
        self.UPD_sport = UDP_sport
        self.UPD_dport = UDP_dport



    def format_json(self):
        json_string = {'Ethernet': {
                       'src': '',
                       'dst': '',
                   },
                   'IP': {'src': '',
                          'dst': '',
                          'version': '',
                          'proto': ''
                          },
                   'TCP': {'sport': '',
                           'dport': ''
                           },
                   'UDP': {'sport': '',
                           'dport': ''}
               }
        return json_string



    def __str__(self, json_string):
        return json.dumps(json_string)



    def file_json(self,json_string,cale):
        with open(cale,'a+') as f:
            json.dump(json_string, f,  sort_keys=True, indent=4)
            f.write("\n")