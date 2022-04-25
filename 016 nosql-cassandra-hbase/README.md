# Explorando o poder do NoSQL com Cassandra e HBase  

## Conteúdos do curso:  

* Conceitos de NoSQL e Arquitetura
    - Introdução, objetivos e requisitos básicos
    - Introdução a NoSQL
    - Relacional x NoSQL
    - Tipos de NoSQL
    - Teorema de CAP
    - Por que NoSQL no Big Data
    - O que é Apache HBase
    - Arquitetura do HBase
    - O que é Apache Cassandra, sua arquitetura e componentes
* Comandos Gerais  
    - Introdução aos comandos no HBase
    - Visão geral do HBase shell
    - Comando para criação de manipulação de tabelas
    - Conceitos básicos dos comandos no Cassandra
    - Cenários de utilização
    - Apresentação do material extra para estudo
    - Dúvidas e comentários finais
    - GitHub: [DIO-Aceleracao-4-HBase-Cassandra](https://github.com/rosacarla/DIO-Aceleracao-4-HBase-Cassandra)

---

# Principais práticas realizadas  

<<<<<<< Updated upstream
[em edição...]  
[em edição...]  
[em edição...]  
=======
* Comandos do HBase  
```
hbase(main):008:0> create 'funcionario', 'pessoais', 'profissionais'
0 row(s) in 5.3410 seconds
=> Hbase::Table - funcionario
hbase(main):009:0> put 'funcionario', '1', 'pessoais:nome', 'Maria'
0 row(s) in 0.5310 seconds
hbase(main):010:0> scan 'funcionario'
ROW COLUMN+CELL
 1 column=pessoais:nome, timestamp=1650843647702, value=Maria
1 row(s) in 0.3590 seconds
hbase(main):011:0> put 'funcionario', '1', 'pessoais:cidade', 'Sao Paulo'
0 row(s) in 0.1290 seconds
hbase(main):012:0> scan 'funcionario'
ROW COLUMN+CELL
 1 column=pessoais:cidade, timestamp=1650844066348, value=Sao
 Paulo
 1 column=pessoais:nome, timestamp=1650843647702, value=Maria
1 row(s) in 0.0740 seconds
```  

* Comandos do Cassandra (ambiente interativo Bash Terminal do curso [Cassandra Query Language (CQL)](https://www.katacoda.com/datastax/courses/cassandra-try-it-out/try-cql))  
</br>

<p align="center">
	<img src="">
</p>
>>>>>>> Stashed changes

---

# Links úteis  

[Apache Cassandra | versão Cassandra As A Service da DATASTAX](https://datastax.com)  
[Apache HBase Reference Guide](https://hbase.apache.org/book.html)  
[Apache Phoenix](https://phoenix.apache.org)  
[Apache Spark](https://spark.apache.org/)  
[Cliente Beeline](https://docs.microsoft.com/pt-br/azure/hdinsight/hadoop/connect-install-beeline#install-beeline-client)  
[¿Cómo se Aplica el Teorema CAP Y El Reto de la Escalabilidad en las RDBMS y NoSQL?](http://asesoftware.com/como-se-aplica-el-teorema-cap-y-el-reto-de-la-escalabilidad-en-las-rdbms-y-nosql/)
[E-book "Cassandra: The Definitive Guide - 3rd Edition | O'Reilly"](https://www.datastax.com/resources/ebook/oreilly-cassandra-the-definitive-guide)  
[LDAP X Kerberos](https://www.geeksforgeeks.org/difference-between-ldap-and-kerberos/)  
[MobaXterm](https://mobaxterm.mobatek.net/download-home-edition.html)  
[Who is using Apache Phoenix?](https://phoenix.apache.org/who_is_using.html)  

---
