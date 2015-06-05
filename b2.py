#!/usr/bin/env python
# For each swift object file in 'filein' file
# swift download | pysam.view | filter BP > 1000; add region | hdfs put
#
import os
import sys
import pysam
import subprocess
import stat
import swiftclient

#
# line  filter function. Writes filterd data to file f and adding region at the end.
#
def fline (line,f,geo):
    w = line.split("\t")
    if ( abs(int(w[8])) > 1000):
        #print line > bphdfs
        f.write(w[0] + '\t' + w[1] + '\t' + w[2] + '\t' + w[3] + '\t' + w[4] + '\t' + w[5] + '\t' + w[6] + '\t' + w[7] + '\t' + w[8] + '\t' + geo + '\n')

#
#
#
def main(BAM):
#   retreive the region from filename
    geo=BAM.split('.')[4]
#   create two pipe files.
    bampipe =  BAM.rsplit('.',1)[0] + '.pipe'
    bampipetohadoop =  BAM.rsplit('.',1)[0] + '.hadooppipe'
    os.mkfifo(bampipe)
    os.mkfifo(bampipetohadoop)
#   Start 2 subprocesses, one to download file fron swift and one to pipe filterd data to hdfs
    command = 'swift download GenomeData ' + BAM + ' -o -  > '  +  bampipe
    p = subprocess.Popen(command, shell=True)
    command2 = '/usr/local/hadoop/bin/hadoop fs -put -f  - < ' + bampipetohadoop +  '  /genome/' + BAM
    p2 = subprocess.Popen(command2, shell=True)
#   open the hadoop pipe
    f=open(bampipetohadoop,'w')
#   read the swift pipe
    rows = pysam.view('-B', bampipe)
#   call the filter function
    for r in rows:
        fline(r,f,geo)
    f.close()
#   remove pipe files.
    os.remove(bampipe)
    os.remove(bampipetohadoop)
#   create and empty file so that the job can be restarted without processing all files again.
    open( BAM,  'w').close()

if __name__ == '__main__':
#
# processes all files in the 'filein' file. Unless the file exists on local file system.
#
    swiftFiles = open('filein','r')
    for l1 in swiftFiles:
         if not os.path.isfile(l1.replace('\n','')):
              print 'processing ' + l1.replace('\n','')
              main(l1.replace('\n',''))
    swiftFiles.close()
