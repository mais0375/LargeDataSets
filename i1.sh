fab create_hdfs_dirs
fab init_cluster
/usr/local/spark/sbin/start-all.sh
hdfs dfs -mkdir /genome
hdfs dfs -mkdir /extention
