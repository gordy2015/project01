import re,json,os,sys



# os.popen('ps -aux  |sort -gr -k 4 |head -n 10|awk  '{$1=$5=$6=$7=$8=$9=$10="";print $0}'')

with open('psaux','r') as f:
    for line in f.readlines():
        # print(line)
        m = line.split(' ')
        # print(len(m),m)
        q = m[10:int(len(m))]
        # print(type(q),q)
        # print(type(m))
        t = ' '.join(q).strip()
        mc = str(m[2]) + '%'
        mr = str(round(8192 * float(m[3]) * 0.01,2)) + 'M'
        mp = '{"pid": "%s", "cpu_utilization": "%s", "memory_utilization": "%s", "cmd": "%s"}' %(m[1],mc,mr,t)
        md = eval(mp)
        print(md)
        # print(md['pid'])
        # print('{pid: %s, cpu utilization: %s, memory utilization: %s, cmd: %s}' %(m[1],mc,mr,t))
        # for s in m:
        #     print(s)

