# encoding=utf8
# author:Star
# time:08/05/2018
import pickle
from CodexMRS.vendor.LSI_TFIDF import LSI_TFIDF
from CodexMRS.base.network import Server
from CodexMRS.base.network import Client


class Worker:
    __port = 9609
    __name = ''
    __ip = ''
    __master = ('137.43.92.45', 9609)
    __server = None

    #
    def start_up(self, port, name, ip):
        self.__server = Server(self.__task, ip, port=port, max_node_num=20)
        self.__name = name
        self.__ip = ip
        self.__server.start_listening()

    def __task(self, message, __shared_variable):
        query = message['query']
        timestamp = message['timestamp']
        print("start computing...")
        result = LSI_TFIDF().getResult(query=query)
        print("end computing...")
        result = result.to_dict()
        client = Client(self.__master[0], self.__ip, self.__master[1],
                        {'query': query, 'timestamp': timestamp, 'name': self.__name, 'result': result,
                         'operate_type': 2})
        client.send_message()
