#!/bin/bash
#
# For each slave in /usr/local/hadoop/etc/hadoop/slaves
# copy data etc and prepare for a run.
for x in $(cat /usr/local/hadoop/etc/hadoop/slaves)
do
    echo $x
    rcp mipwd   $x:/home/ubuntu/
    rcp g2015016-openrc.sh   $x:/home/ubuntu/
    rcp Yes   $x:/home/ubuntu/
    rcp .bashrc  $x:/home/ubuntu/
    rsh $x 'sudo apt-get install python-swiftclient <Yes'
    rsh $x 'sudo apt-get install zlib1g-dev'
    rsh $x 'sudo pip install pysam'
    find genomeData | cpio -ocv | rsh $x '  cpio -icv'
    rsh $x 'crontab /home/ubuntu/genomeData/ctab'
done
