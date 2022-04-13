#!/bin/bash
################################################################################################################
## Script para parar e subir todos os servicos hadoop* e hive*
## caminho: /etc/rc.d/init.d/
## rodar com root
########################################################

data=`date '+%d/%m/%Y %H:%M:%S'`

echo "****  Inicio do stop/start all services hadoop e hive ****"
echo $data

sleep 2

echo "****  Inicio service hadoop* stop all ****"

nohup service hadoop-hdfs-datanode stop > /home/cloudera/logs_hadoop/$data_stop_datanode.log 2>&1 </dev/null
sleep 30

nohup hadoop-hdfs-journalnode stop > /home/cloudera/logs_hadoop/$data_stop_journalnode.log 2>&1 </dev/null
sleep 30

nohup hadoop-hdfs-namenode stop > /home/cloudera/logs_hadoop/$data_stop_namenode.log 2>&1 </dev/null
sleep 30

nohup hadoop-hdfs-secondarynamenode stop > /home/cloudera/logs_hadoop/$data_stop_secondarynamenode.log 2>&1 </dev/null
sleep 30

nohup hadoop-hdfs-httpfs stop > /home/cloudera/logs_hadoop/$data_stop_httpfs.log 2>&1 </dev/null
sleep 30

nohup hadoop-hdfs-historyserver stop > /home/cloudera/logs_hadoop/$data_stop_historyserver.log 2>&1 </dev/null
sleep 30

nohup hadoop-hdfs-nodemanager stop > /home/cloudera/logs_hadoop/$data_stop_nodemanager.log 2>&1 </dev/null
sleep 30

nohup hadoop-yarn-proxyserver stop > /home/cloudera/logs_hadoop/$data_stop_yarnproxyserver.log 2>&1 </dev/null
sleep 30

nohup hadoop-yarn-resourcemanager stop > /home/cloudera/logs_hadoop/$data_stop_yarnresourcemanager.log 2>&1 </dev/null
sleep 30

echo "****  Fim service hadoop* stop all ****"

sleep 10

echo "****  Inicio service hadoop* status all ****"

nohup service hadoop-hdfs-datanode status > /home/cloudera/logs_hadoop/$data_status_datanode.log 2>&1 </dev/null
sleep 10

nohup hadoop-hdfs-journalnode status > /home/cloudera/logs_hadoop/$data_status_journalnode.log 2>&1 </dev/null
sleep 10

nohup hadoop-hdfs-namenode status > /home/cloudera/logs_hadoop/$data_status_namenode.log 2>&1 </dev/null
sleep 10

nohup hadoop-hdfs-secondarynamenode status > /home/cloudera/logs_hadoop/$data_status_secondarynamenode.log 2>&1 </dev/null
sleep 10

nohup hadoop-hdfs-httpfs status > /home/cloudera/logs_hadoop/$data_status_httpfs.log 2>&1 </dev/null
sleep 10

nohup hadoop-hdfs-historyserver status > /home/cloudera/logs_hadoop/$data_status_historyserver.log 2>&1 </dev/null
sleep 10

nohup hadoop-hdfs-nodemanager status > /home/cloudera/logs_hadoop/$data_status_nodemanager.log 2>&1 </dev/null
sleep 10

nohup hadoop-yarn-proxyserver status > /home/cloudera/logs_hadoop/$data_status_yarnproxyserver.log 2>&1 </dev/null
sleep 10

nohup hadoop-yarn-resourcemanager status > /home/cloudera/logs_hadoop/$data_status_yarnresourcemanager.log 2>&1 </dev/null
sleep 10

echo "****  Fim service hadoop* status all ****"

sleep 5

echo "****  Variaveis hadoop ****"
echo $HADOOP_HOME
echo $HADOOP_MAPRED_HOME
echo $HADOOP_LIBEXEC_DIR
echo $HADOOP_CONF_DIR
echo $HADOOP_CLASSPATH

sleep 2

echo "****  Inicio service hadoop* start all ****"

nohup service hadoop-hdfs-datanode start > /home/cloudera/logs_hadoop/$data_start_datanode.log 2>&1 </dev/null
sleep 30

nohup hadoop-hdfs-journalnode start > /home/cloudera/logs_hadoop/$data_start_journalnode.log 2>&1 </dev/null
sleep 30

nohup hadoop-hdfs-namenode start > /home/cloudera/logs_hadoop/$data_start_namenode.log 2>&1 </dev/null
sleep 30

nohup hadoop-hdfs-secondarynamenode start > /home/cloudera/logs_hadoop/$data_start_secondarynamenode.log 2>&1 </dev/null
sleep 30

nohup hadoop-hdfs-httpfs start > /home/cloudera/logs_hadoop/$data_start_httpfs.log 2>&1 </dev/null
sleep 30

nohup hadoop-hdfs-historyserver start > /home/cloudera/logs_hadoop/$data_start_historyserver.log 2>&1 </dev/null
sleep 30

nohup hadoop-hdfs-nodemanager start > /home/cloudera/logs_hadoop/$data_start_nodemanager.log 2>&1 </dev/null
sleep 30

nohup hadoop-yarn-proxyserver start > /home/cloudera/logs_hadoop/$data_start_yarnproxyserver.log 2>&1 </dev/null
sleep 30

nohup hadoop-yarn-resourcemanager start > /home/cloudera/logs_hadoop/$data_start_yarnresourcemanager.log 2>&1 </dev/null
sleep 30

echo "****  Fim service hadoop* start all ****"

echo "****  Variaveis hadoop ****"
echo $HADOOP_HOME
echo $HADOOP_MAPRED_HOME
echo $HADOOP_LIBEXEC_DIR
echo $HADOOP_CONF_DIR
echo $HADOOP_CLASSPATH

sleep 10

echo "****  Inicio service hadoop* status all ****"

nohup service hadoop-hdfs-datanode status > /home/cloudera/logs_hadoop/$data_status_datanode.log 2>&1 </dev/null
sleep 5

nohup hadoop-hdfs-journalnode status > /home/cloudera/logs_hadoop/$data_status_journalnode.log 2>&1 </dev/null
sleep 5

nohup hadoop-hdfs-namenode status > /home/cloudera/logs_hadoop/$data_status_namenode.log 2>&1 </dev/null
sleep 5

nohup hadoop-hdfs-secondarynamenode status > /home/cloudera/logs_hadoop/$data_status_secondarynamenode.log 2>&1 </dev/null
sleep 5

nohup hadoop-hdfs-httpfs status > /home/cloudera/logs_hadoop/$data_status_httpfs.log 2>&1 </dev/null
sleep 5

nohup hadoop-hdfs-historyserver status > /home/cloudera/logs_hadoop/$data_status_historyserver.log 2>&1 </dev/null
sleep 5

nohup hadoop-hdfs-nodemanager status > /home/cloudera/logs_hadoop/$data_status_nodemanager.log 2>&1 </dev/null
sleep 5

nohup hadoop-yarn-proxyserver status > /home/cloudera/logs_hadoop/$data_status_yarnproxyserver.log 2>&1 </dev/null
sleep 5

nohup hadoop-yarn-resourcemanager status > /home/cloudera/logs_hadoop/$data_status_yarnresourcemanager.log 2>&1 </dev/null
sleep 5

echo "****  Fim service hadoop* status all ****"

sleep 10

echo "****  Inicio service hive* stop all ****"

nohup hive-metastore stop > /home/cloudera/logs_hadoop/$data_stop_hivemetastore.log 2>&1 </dev/null

sleep 30

nohup hive-server2 stop > /home/cloudera/logs_hadoop/$data_stop_hiveserver2.log 2>&1 </dev/null

echo "****  Fim service hive* stop all ****"

sleep 30

echo "****  Inicio service hive* start all ****"

nohup hive-metastore start > /home/cloudera/logs_hadoop/$data_start_hivemetastore.log 2>&1 </dev/null

sleep 30

nohup hive-server2 start > /home/cloudera/logs_hadoop/$data_start_hiveserver2.log 2>&1 </dev/null

echo "****  Fim service hive* start all ****"

sleep 10

echo "****  Inicio service hive* status all ****"

nohup hive-metastore status > /home/cloudera/logs_hadoop/$data_status_hivemetastore.log 2>&1 </dev/null
sleep 5

nohup hive-server2 status > /home/cloudera/logs_hadoop/$data_status_hiveserver2.log 2>&1 </dev/null

echo "****  Fim service hive* status all ****"

wait

echo "****  Fim do stop/start all services hadoop e hive ****"
date
