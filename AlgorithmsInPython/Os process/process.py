import psutil
import datetime
#this program is psutil module of python that deal with operatin system process
#currently running this module give information about then and can terminate process as well


#listingn all the process running in the operating system

def running_process():
    i = psutil.get_pid_list()       #processes list running in operating system

    for a in i:                     #looping throgh process
       # try:
                    #try block for printing process names
            p = psutil.Process(a).pid
            print p
        #    name=psutil.Process(p).name()
         #   status=psutil.Process(p).status()
          #  print name ," ",status
        #except:
         #   pass



#searching for process in memory and print available information
def process_exists(process):
    '''

    '''
    i = psutil.get_pid_list()       #list of process running in memory

    for a in i:                     #loop throught list of process running in memory
        try:
            #try block for handle exception
           p = psutil.Process(a).pid        #getting process id
           name=psutil.Process(p).name()    #getting process name

           if name==process+'.exe':             #if this is process we are look for print information availble with process
             print "process name ",name
             print "process status ",psutil.Process(p).status()
             print "created date ",datetime.datetime.fromtimestamp(psutil.Process(p).create_time()).strftime("%Y-%m-%d %H:%M:%S")
             print  "username ",psutil.Process(p).username()
             print "process cmd line path :",psutil.Process(p).cmdline()
             print "cpu time",psutil.Process(p).cpu_times()
             print "memory pecent of process",psutil.Process(p) .memory_percent()
             print "process conection",psutil.Process(p) .  connections()
             print "number of thread process has ",psutil.Process(p)  .num_threads()
             print "name of thread ",psutil.Process(p)  .threads()
             psutil.Process(p)  .  suspend()
             print "process status ",psutil.Process(p).status()
             psutil.Process(p)  .  resume()

        except:
           pass


#function for termination of process
def terminate(process):
    i = psutil.get_pid_list()   #getting list of all proecess
    for a in i:         #loop to find a give proces
        try:        #try block for some process did not have name property try will filter that process

           p = psutil.Process(a).pid    #getting process id
           name=psutil.Process(p).name()    #getting process name
           if name==process+'.exe':         #if this is process we are looking for terminate it
              psutil.Process(p).terminate()
        except:
            pass



if __name__ == '__main__':

     repeat=True
     while repeat !=False:
            print ("press 1 to check number of process running")
            print ("press 2 for geting information about process")
            print ("press 3 for running  os test")
            print ("press 4 for running  ternminate a process")
            print ("press 5 to exit  ")
            option=int(raw_input());

            if option==1:
                running_process()

            elif option ==2:
                name=raw_input("enter name of process :")
                process_exists(name)

            elif option==3:
                print  psutil.test();

            elif option==4:
                name=raw_input("enter name of process :")
                terminate(name)

            if option==5:
                repeat=False
