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

print(results_dict)
