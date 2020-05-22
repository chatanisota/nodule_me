import time

class Debug:

    __is_start_time = False
    __time_value = 0

    @staticmethod
    def timer(str):

        if(Debug.__is_start_time):
            during = time.time() - Debug.__time_value
            print(str+":{0}".format(during) + "[sec]")
            Debug.__time_value = time.time()

        else:
            print(str+": COUNT START")
            Debug.__is_start_time = True
            Debug.__time_value = time.time()

    @staticmethod
    def timer_reset():
        Debug.__is_start_time = False
        print("RESET")
