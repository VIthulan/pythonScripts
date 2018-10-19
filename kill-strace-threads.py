import subprocess

process_id_cmd = "ps -aux | grep strace | grep out | awk '{ print $2 }'"
process_id = subprocess.Popen(process_id_cmd, stdout=subprocess.PIPE, shell=True).stdout.read().rstrip()

if process_id != "":
    subprocess_id_arr = process_id.split("\n")

    for proc_id in subprocess_id_arr:
        stack_trace_cmd = "kill -9 %s" % proc_id
        subprocess.Popen(stack_trace_cmd, stdout=subprocess.PIPE, shell=True)

else:
    print "No strace threads are running!"
