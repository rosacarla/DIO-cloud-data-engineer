# MySQL

<p align="center"><img src="https://github.com/rosacarla/DIO-cloud-data-engineer/blob/main/013%20mysql/tabelas-cursos1e2.jpg"></p>

A trilha do bootcamp incluiu os seguintes cursos:  
* [MySql - Trabalhando com as suas primeiras tabelas]()  
* [MySql - Explorando relacionamentos com workbench]()
* [MySQL - Consultas com Join]()

---

## Principais práticas realizadas  
```sql
CREATE TABLE pessoa (
    id INT NOT NULL PRYMARY KEY AUTOINCREMENT,
    nome VARCHAR (30) NOT NULL,
    nascimento DATE
)

INSERT INTO pessoa (nome, nascimento) VALUES ('Nathally', '1990-05-22');
INSERT INTO pessoa (nome, nascimento) VALUES ('Pedro', '1995-07-18');
INSERT INTO pessoa (nome, nascimento) VALUES ('Marcela', '2000-04-05');
SELECT nome, nascimento FROM pessoa

UPDATE pessoa SET nome='Nathally Souza';
UPDATE pessoa SET nome='Pedro Rosa' WHERE id=3;
UPDATE pessoa SET nome='Pedro Rivero' WHERE id=3;
UPDATE pessoa SET nome='Marcela Rosa' WHERE id=4;

SELECT * FROM pessoa WHERE id=3;

DELETE FROM pessoa WHERE id=3;
```
```sql
CREATE TABLE videos (
    id_video INT NOT NULL PRYMARY KEY AUTOINCREMENT,
    id_author INT NOT NULL,
    title VARCHAR (30) NOT NULL,
    likes INT NOT NULL,
    dislikes INT NOT NULL 
)

INSERT INTO videos (id_author, title, likes, dislikes) VALUES ('Maria', 'MySQL', 10, 2);
INSERT INTO videos (id_author, title, likes, dislikes) VALUES ('Pedro', 'HTML', 30, 1);
INSERT INTO videos (id_author, title, likes, dislikes) VALUES ('Joao', 'CSS', 18, 3);
INSERT INTO videos (id_author, title, likes, dislikes) VALUES ('Maria', 'JavaScript', 15, 8);
INSERT INTO videos (id_author, title, likes, dislikes) VALUES ('Maria', 'Python', 50, 0);
INSERT INTO videos (id_author, title, likes, dislikes) VALUES ('Joao', 'PHP', 28, 8)
```

```sql
-- Estrutura da tabela `canais`
--

CREATE TABLE `canais` (
  `id_canal` int(11) NOT NULL,
  `nome_canal` varchar(100) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Extraindo dados da tabela `canais`
--

INSERT INTO `canais` (`id_canal`, `nome_canal`) VALUES
(1, 'React'),
(2, 'PHP'),
(3, 'CSS'),
(4, 'HTML');

-- --------------------------------------------------------
```

---

## Ferramentas utilizadas  
[Workbench](https://www.mysql.com/products/workbench/)  
[XAMPP](https://www.apachefriends.org/es/index.html)  

---
             
