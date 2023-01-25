"""
Multi-Level Cache, having support for LRU eviction Algorithm.

Multi-Level Cache's read world application is CPU cache,
for example MacOS has L1, L2 Cache at processor-level
"""

import time
from collections import deque


"""
CacheService tracks statistics, time_taken logs etc
"""
class CacheService():

    def __init__(self):
        self.read_time_logs = []
        self.write_time_logs = []

    def log_time_taken(self, time_taken, operation):
        if operation == "GET":
            self.read_time_logs.append(time_taken)
        if operation == "PUT":
            self.write_time_logs.append(time_taken)

    def avg_time_stats(self, operation):
        if operation == "GET":
            try:
                return sum(self.read_time_logs) / len(self.read_time_logs)
            except:
                return 0
        if operation == "PUT":
            try:
                return sum(self.write_time_logs) / len(self.write_time_logs)
            except:
                return 0

    def cache_stats(self):
        avg_write = self.avg_time_stats("PUT")
        avg_read  = self.avg_time_stats("GET")
        print "Average Read time: {}".format(avg_read)
        print "Average Write time: {}".format(avg_write)




class Cache():
    
    def __init__(self, capacity, level):
        self.capacity  = capacity
        self.level = level
        self.current_size = 0
        self.storage = {}
        self.lru_deque = deque([])
    
    def put(self, key, value):
        if self.storage.get(key)  != None:
            self.update(key, value)
        elif self.current_size < self.capacity:
            self.storage[key] = value
            self.current_size += 1
            self.lru_deque.appendleft(key)
        else:
            LR_key = self.lru_deque.pop()  
            print "cache is full, performing eviction on {}".format(LR_key)  # remove least recently used key
            self.storage.pop(LR_key)
            self.current_size -= 1
            self.storage[key] = value   
            self.current_size += 1
            self.lru_deque.appendleft(key)
        return "success {}".format(key)
        
    
    def get(self, key):
        val = self.storage.get(key)
        if val:
            self.lru_deque.remove(key)
            self.lru_deque.appendleft(key)
        return val
    
    
    def delete(self, key):
        if self.storage.get(key):
            self.storage.pop(key)
            self.lru_deque.remove(key)  # remove from dque
            self.current_size -= 1
            return "success"
        return "Key does not exist"
        
    
    def update(self, key, value):
        self.storage[key] = value
        self.lru_deque.remove(key)
        self.lru_deque.appendleft(key)
        return "success"

    
    def print_all(self):
        print "\n============================="
        print "CACHE_LEVEL: {}".format(self.level)
        print "STORAGE: ", self.storage
        print "size: {}".format(self.current_size)
        print "Deque ", self.lru_deque
        print "=============================\n"



class MultiLevelCache():
    
    def __init__(self, total_level, capacity_list=[]):
        self.total_level = total_level
        self.capacity_list = capacity_list
        self.c1 = Cache(capacity_list[0], 1)
        self.c2 = Cache(capacity_list[1], 2)
        self.c3 = Cache(capacity_list[2], 3)
        self.cache_service = CacheService()


    def level_put(self, key, value):
        try:
            write_start = time.time()

            if self.c1.get(key) != value:
                self.c1.put(key, value)
            if self.c2.get(key) != value:
                self.c2.put(key, value)
            if self.c3.get(key) != value:
                self.c3.put(key, value)

            write_end = time.time()
            time_taken = write_end - write_start
            self.cache_service.log_time_taken(time_taken, "PUT")
        except Exception as e:
            return "write failed: {}".format(e), time.time() - write_start
        return "OK", time_taken

    
    def level_get(self, key):
        read_start = time.time()
        res = "nil"
        c1_outp = self.c1.get(key)
        if c1_outp:
            res = self.c1.get(key)
        c2_outp = self.c2.get(key)
        if c2_outp:
            res = c2_outp
            self.c1.put(key, res)        #  make entry in higher layer
        c3_outp = self.c3.get(key)
        if c3_outp:
            res = c3_outp
            self.c2.put(key, res)
            self.c1.put(key,res)         # make entry in higher layer    
        read_end = time.time()
        time_taken = read_end - read_start
        self.cache_service.log_time_taken(time_taken, "GET")   
        return res, time_taken

    
    def print_caches_stats(self):
        print "\n----------------- Cache Statistics -----------------"
        self.c1.print_all()
        self.c2.print_all()
        self.c3.print_all()
        self.cache_service.cache_stats()

        print "------------------- END ----------------------------"

        

    def level_delete(self, key):
        pass

        
        

def main():
   cache = MultiLevelCache(3, [2, 3, 5])
   print cache.level_put("A", "manis")
   print cache.level_put("B", "rvi")
   print cache.level_put("C", "ankus")

   cache.print_caches_stats()

   print cache.level_put("D" , "chint")
   print cache.level_get("C")
   cache.print_caches_stats()




if __name__ ==  "__main__":
    main()


    
