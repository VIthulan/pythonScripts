from threading import Thread
import subprocess

process = "pulse-agent"
process_id_cmd = "pgrep %s" % process
process_id = subprocess.Popen(process_id_cmd, stdout=subprocess.PIPE, shell=True).stdout.read().rstrip()

if process_id != "" :
    subprocess_id_cmd = "ps -T -p %s | awk '{ print $2 }'" % process_id
    subprocess_id = subprocess.Popen(subprocess_id_cmd, stdout=subprocess.PIPE, shell=True).stdout.read().rstrip()
    subprocess_id_arr = subprocess_id.split("\n")


    def get_stacktrace_of_process(i, proc_id):
        stack_trace_cmd = "strace -s4096 -p%s -o out_%s.txt" % (proc_id, i)
        subprocess.Popen(stack_trace_cmd, stdout=subprocess.PIPE, shell=True)


    i = 1
    for proc_id in subprocess_id_arr:
        if i > 1:
            t = Thread(target=get_stacktrace_of_process, args=(i, proc_id))
            t.start()
        i = i + 1
else:
    print "Pulse Agent is not running!"
