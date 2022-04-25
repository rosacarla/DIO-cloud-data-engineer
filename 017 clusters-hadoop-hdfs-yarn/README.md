# Monitoramento de clusters Hadoop de alto nível com HDFS e YARN  

## Conteúdos do curso:  

* Teoria e Prática com HDFS  
    - Introdução, objetivos e requisitos básicos  
    - Conceito de big data, escalabilidade e cluster  
    - O que é Hadoop  
    - O que é HDFS  
    - Configuração inicial da VM  
    - Principais comandos - Parte 1  
    - Principais comandos - Parte 2  
    - Preparação da aula  
* Teoria e Prática com YARN  
    - Introdução a YARN e primeiros comandos  
    - Comandos com YARN - Parte 2  
    - Comandos com YARN - Parte 3  
    - Resumo do curso  
    - Dúvidas e comentários extras  

---

## Principais práticas realizadas

* Comandos com HDFS - Parte 1  
```
[everis@bigdata-srv ~]$ hdfs dfs -get /tmp/file_teste.txt
get: `file_teste.txt': File exists
[everis@bigdata-srv ~]$
[everis@bigdata-srv ~]$
[everis@bigdata-srv ~]$ sudo service hadoop-hdfs-namenode start
[sudo] password for everis:
starting namenode, logging to 
/var/log/hadoop-hdfs/hadoop-hdfs-namenode-bigdata-srv.out
Started Hadoop namenode: [ OK ]
[everis@bigdata-srv ~]$ sudo service hadoop-hdfs-secondarynamenode start
starting secondarynamenode, logging to 
/var/log/hadoop-hdfs/hadoop-hdfs-secondarynamenode-bigda
Started Hadoop secondarynamenode: [ OK ]
[everis@bigdata-srv ~]$ ll
total 3648
-rw-r--r--. 1 everis everis 4784 Jan 15 2021 file_teste.txt
-rw-r--r--. 1 everis everis 1341 Jan 14 2021 hive-site.xml
drwxrwxr-x. 2 everis everis 184 Jan 15 2021 script_apoio
-rwx------. 1 everis everis 3722067 Jan 14 2021 tmp  
```

* Comandos com HDFS - Parte 2  
```
[everis@bigdata-srv ~]$ hdfs dfsadmin -safemode leave
safemode: Access denied for user everis. Superuser privilege is required
[everis@bigdata-srv ~]$ sudo -u hdfs hdfs dfsadmin -safemode leave
Safe mode is OFF
[everis@bigdata-srv ~]$ hdfs dfs -put file_teste.txt /user/everis-bigdata/
[everis@bigdata-srv ~]$ hdfs dfs -mkdir /tmp/delete
[everis@bigdata-srv ~]$ hdfs dfs -ls /tmp
Found 7 items
drwxr-xr-x - everis supergroup 0 2022-04-10 21:45 /tmp/delete
-rw-r--r-- 3 everis supergroup 4784 2021-01-15 11:00 /tmp/file_teste.txt
drwxr-xr-x - yarn supergroup 0 2021-01-19 16:44 /tmp/hadoop-yarn
drwx-wx-wx - hive supergroup 0 2021-01-15 11:34 /tmp/hive
-rw-r--r-- 3 everis supergroup 1341 2021-01-15 10:54 /tmp/hive-site.xml
drwxr-xr-x - hdfs supergroup 0 2021-01-19 19:41 
/tmp/wordcount00002.ou t
drwxr-xr-x - root supergroup 0 2021-01-19 18:26 /tmp/wordcount012.out  
```

* Primeiros comandos com YARN  
```  
[everis@bigdata-srv ~]$ sudo sed -i 's|hdfs://|hdfs://bigdata-srv:8020/|g' 
/etc/hadoop/con f/yarn-site.xml
[sudo] password for everis:
[everis@bigdata-srv ~]$ cat /etc/hadoop/conf/yarn-site.xml |grep bigdata-srv
 <value>bigdata-srv</value>
 
<value>hdfs://bigdata-srv:8020/bigdata-srv:8020/var/log/hadoop-yarn/apps</value>
```  

* Comandos com YARN - Parte 2  
```
[everis@bigdata-srv ~]$ sudo -u hdfs yarn jar 
/usr/lib/hadoop-mapreduce/hadoop-mapreduce-examples.jar wordcount 
/tmp/file_teste.txt /tmp/wc_output
22/04/10 23:27:43 INFO client.RMProxy: Connecting to ResourceManager at 
/0.0.0.0:8032
22/04/10 23:27:47 INFO input.FileInputFormat: Total input paths to process : 1
22/04/10 23:27:47 INFO mapreduce.JobSubmitter: number of splits:1
22/04/10 23:27:47 INFO mapreduce.JobSubmitter: Submitting tokens for job: 
job_1649633181319_0001
22/04/10 23:27:49 INFO impl.YarnClientImpl: Submitted application 
application_1649633181319_0001
22/04/10 23:27:49 INFO mapreduce.Job: The url to track the job: 
http://bigdata-srv:8088/proxy/application_1649633181319_0001/
22/04/10 23:27:49 INFO mapreduce.Job: Running job: job_1649633181319_0001
22/04/10 23:28:05 INFO mapreduce.Job: Job job_1649633181319_0001 running in uber 
mode : false
22/04/10 23:28:05 INFO mapreduce.Job: map 0% reduce 0%
22/04/10 23:28:16 INFO mapreduce.Job: map 100% reduce 0%
22/04/10 23:28:31 INFO mapreduce.Job: map 100% reduce 100%
22/04/10 23:28:35 INFO mapreduce.Job: Job job_1649633181319_0001 completed 
successfully
22/04/10 23:28:35 INFO mapreduce.Job: Counters: 49  
```  

* Comandos com YARN - Parte 3  
```  
[everis@bigdata-srv ~]$ sudo -u hdfs yarn logs -applicationId 
application_1649633181319_0001 |m
[sudo] password for everis:
22/04/11 00:16:07 INFO client.RMProxy: Connecting to ResourceManager at 
/0.0.0.0:8032  
```

---

## Links úteis  

[Azure HDInsight](https://azure.microsoft.com/pt-br/services/hdinsight/#overview)
[Hadoop Cluster](https://alissonmachado.com.br/hadoop-cluster/)
[VirtualBox](https://www.treinaweb.com.br/blog/criando-uma-maquina-virtual-com-a-virtualbox)
[VM Everis](https://drive.google.com/file/d/1CsHc311jp4EuZ8be5KGaumniGAafa8sC/view?usp=sharing)

---
