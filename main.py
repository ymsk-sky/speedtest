# -*- coding: utf-8 -*-

import speedtest

servers = []
threads = 1 # single threaded test

s = speedtest.Speedtest()
s.get_servers(servers)
s.get_best_server()

s.download(threads=threads)
s.upload(threads=threads)

s.results.share()

results_dict = s.results.dict()

# print(results_dict)
print('Download: {}Mbps'.format(results_dict['download']/1024/1024))
print('Upload: {}Mbps'.format(results_dict['upload']/1024/1024))
print('ping: {}ms'.format(results_dict['ping']))
