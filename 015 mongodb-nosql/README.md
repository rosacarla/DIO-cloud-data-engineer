# Introdução ao MongoDB e Banco de Dados NoSQL  

## Conteúdos do curso:  

* Introdução ao NoSQL  
	- Apresentação do curso
	- Introdução
* Conhecendo os tipos de bancos de dados NOSQL  
	- Tipos de bancos NoSQL
	- Coluna/Família de colunas
	- Chave-valor 
	- Documento 
* Introdução ao MongoDB e instalação  
	- Introdução ao MongoDB
	- Instalação
	- MongoDB Cloud
* Schema Design e boas práticas  
	- Schema Design
	- Boas práticas
	- JSON vs BSON
* Alguns conceitos na prática  
	- Operaçoes de manipulação de dados
	- Performance e índices
	- Agregações

---

## Principais práticas realizadas  

* **Neo4j Sandbox (banco de dados orientado a grafos)**  
```
/*
:server connect

Connect to Neo4j

Database access might require an authenticated connection
You are connected as user neo4j
to ...
Connection credentials are stored in your web browser.
*/

-- Server version	Neo4j/4.4.5
-- Server address	...

-- Query 1
CREATE (:Client {name: "Bob Esponja", age: 28, hobbies:['Caça água-viva, comer hamburger']})

-- Query 2
MATCH (bob_esponja) RETURN bob_esponja;

-- Query 3
CREATE (:Client {name: "Lula Molusco", age: 30, hobbies: ['Tocar clarinete']}) - [:Bloqueado]->(:Client {name: "Patrick", hobbies:['Caçar água-viva']})

-- Query 4
MATCH (todos) RETURN todos;
```

* **Cassandra CQL (banco de dados orientado a colunas)**  
</br>

<p align="center">
	<img src="https://github.com/rosacarla/DIO-cloud-data-engineer/blob/main/015%20mongodb-nosql/scripts/cassandra1-cql.jpg">
</p>

* **Try Redis (banco de dados de chave-valor)**  
```
Welcome to Try Redis, a demonstration of the Redis database!

Please type TUTORIAL to begin a brief tutorial, HELP to see a list of supported commands, or any valid Redis command to play with the database.


> SET user1:name "Bob Esponja"
OK
> GET user1:name
"Bob Esponja"
> SET user '{"name": "Patrick", "age": 31}'
OK
> GET user1:name
"Bob Esponja"
> GET user
"{\"name\": \"Patrick\", \"age\": 31}"
> SET user2:name "Lula Molusco" EX 10
OK
```

* **MongoDB Cloud (banco de dados orientado a documentos)**  
```
use fenda_bikini

show databases;

show collections;

for(var i=0; i< 10000; i++){
	db.clients.insert({name: "Cliente" + i, age:i});
}

db.getCollection('clientes').count({})

db.getCollection('clients').count({})

db.getCollection('clientes').find({})

db.getCollection('clientes').find({_id: ObjectId("625075ca638fffbf8c4502e0")}).explain(true)

db.getCollection('clientes').find({name: "Cliente0"}).explain(true)

db.getCollection('clientes').createIndex({name : 1}, {"name": "idx_name"})

db.getCollection('clientes').find({name: "Cliente0"}).explain(true)

```

---

## Links úteis  

[Cassandra Query Language](https://www.katacoda.com/datastax/courses/cassandra-try-it-out/try-cql)  
[Compose file versions and upgrading | Docker Documentation](https://docs.docker.com/compose/compose-file/compose-versioning/)  
[Docker Hub](https://hub.docker.com/)  
[MongoDB Cloud](https://www.mongodb.com/cloud)  
[MongoDB Community Download](https://www.mongodb.com/try/download/community)  
[Neo4j Sandbox](https://sandbox.neo4j.com)  
[Robomongo | Robo 3T](https://robomongo.org/)  
[Sublime Text](https://www.sublimetext.com/)  
[Try Redis](https://try.redis.io/)  

---
