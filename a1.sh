rem This adds slave nodes to hadoop slave file.
rem Adds sourcing commands for swift access to .bashrc file.
rem Install needed sw packages.
echo host-10-0-100-125.openstacklocal >/usr/local/hadoop/etc/hadoop/slaves
echo host-10-0-100-121.openstacklocal >>/usr/local/hadoop/etc/hadoop/slaves
echo "source /home/ubuntu/g2015016-openrc.sh   </home/ubuntu/mipwd" >>.bashrc
echo $OS_PASSWORD >mipwd
echo Y >Yes
sudo apt-get install python-swiftclient <Yes
sudo apt-get install zlib1g-dev
sudo pip install pysam

