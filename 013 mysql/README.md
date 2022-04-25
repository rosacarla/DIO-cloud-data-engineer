# MySQL  

A trilha do bootcamp incluiu os seguintes cursos:  
* [MySql - Trabalhando com as suas primeiras tabelas](https://github.com/rosacarla/DIO-cloud-data-engineer/tree/main/013%20mysql/sql1)  
* [MySql - Explorando relacionamentos com workbench](https://github.com/rosacarla/DIO-cloud-data-engineer/tree/main/013%20mysql/sql2)
* [MySQL - Consultas com Join](https://github.com/rosacarla/DIO-cloud-data-engineer/tree/main/013%20mysql/sql3)
</br>

<p align="center">
    <img src="https://github.com/rosacarla/DIO-cloud-data-engineer/blob/main/013%20mysql/images/tabelas-cursos1e2.jpg" width="850">
</p>

---

## Principais práticas realizadas  

* Criação de tabelas
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

* Relacionamentos
```sql
ALTER TABLE `videos` ADD CONSTRAINT `fk_author` FOREIGN KEY (`fk_author`) REFERENCES `author` (`id_author`) ON DELETE CASCADE ON UPDATE CASCADE 
/*
cria relacionamento com chave estrangeira na tabela videos, ligada a coluna id_author na tabela author
*/;
SELECT * FROM videos JOIN author ON videos.fk_author = author.id_author
/*
mostra nomes de autores da fk na tabela video, ligado a id author na tab author
*/;
SELECT * FROM videos JOIN author
/*
mostra resultado com tudo misturado
*/;
SELECT videos.title, author.name FROM videos JOIN author ON videos.fk_author = author.id_author
/*
mostra somente titulo do video e nome do autor na tab videos, vinculados a chave estrang(videos) e id author(author)
*/;
```

* JOINS
```sql
SELECT v.nome_video, v.autor_video, c.nome_canal
FROM videos_canais AS vc JOIN videos AS v ON vc.fk_video = v.id_video
JOIN canais AS c ON vc.fk_canal = c.id_canal
/*
Join junta 3 tabelas onde fk_video e id_video sao iguais, traz apenas
colunas nome_video, autor_video, nome.canal
*/;
SELECT * FROM videos_canais AS vc INNER JOIN videos AS v ON vc.fk_video = v.id_video
INNER JOIN canais AS c ON vc.fk_canal = c.id_canal;

-- INNER JOIN junta 3 tabelas onde fk_video e id_video sao iguais, traz apenas
-- colunas nome_video, autor_video, nome.canal, faz mesmas consultas em videos e canais;
-- nao traz campos nulos nem sem relacionamento.
-- 
```

---

## Ferramentas utilizadas  
[Workbench](https://www.mysql.com/products/workbench/)  
[XAMPP](https://www.apachefriends.org/es/index.html)  

---             
