CREATE TABLE pessoa (
    id INT NOT NULL PRYMARY KEY AUTOINCREMENT,
    nome VARCHAR (30) NOT NULL,
    nascimento DATE
)

INSERT INTO pessoa (nome, nascimento) VALUES ('Nathally', '1990-05-22');
INSERT INTO pessoa (nome, nascimento) VALUES ('Pedro', '1995-07-18');
INSERT INTO pessoa (nome, nascimento) VALUES ('Marcela', '2000-04-05');

SELECT * FROM pessoa;
SELECT nome FROM pessoa;
SELECT nascimento FROM pessoa;
SELECT nome, nascimento FROM pessoa

UPDATE pessoa SET nome='Nathally Souza';
UPDATE pessoa SET nome='Pedro Rosa' WHERE id=3;
UPDATE pessoa SET nome='Pedro Rivero' WHERE id=3;
UPDATE pessoa SET nome='Marcela Rosa' WHERE id=4;

SELECT * FROM pessoa WHERE id=3;

DELETE FROM pessoa WHERE id=3;

INSERT INTO pessoa (nome, nascimento) VALUES ('Pedro Rivero', '1995-07-18');
INSERT INTO pessoa (nome, nascimento) VALUES ('Flavio Mota', '2002-12-01');

SELECT * FROM pessoa ORDER BY nome; 
SELECT * FROM pessoa ORDER BY nome DESC;

ALTER TABLE pessoa ADD genero VARCHAR(1) NOT NULL AFTER nascimento; 

UPDATE pessoa SET genero='F' WHERE id=1; 
UPDATE pessoa SET genero='F' WHERE id=4;
UPDATE pessoa SET genero='M' WHERE id=5;
UPDATE pessoa SET genero='M' WHERE id=6;

SELECT COUNT(id), genero FROM pessoa GROUP BY genero; 

INSERT INTO pessoa (nome, nascimento, genero) VALUES ('Paula Dutra', '1998-10-30', 'F');


CREATE TABLE cursos (id_curso INT NOT NULL PRIMARY KEY AUTO_INCREMENT, nome VARCHAR(10));

INSERT INTO cursos (nome) VALUES ('MySQL');
INSERT INTO cursos (nome) VALUES ('HTML');

SELECT * FROM cursos;

UPDATE cursos SET nome='HTML 5' WHERE id_curso=2;

SELECT * FROM cursos;

INSERT INTO cursos (nome) VALUES ('Economia');

SELECT * FROM cursos;

SELECT * FROM cursos WHERE nome='Economia';

DELETE FROM cursos WHERE nome='Economia';

ALTER TABLE cursos ADD carga_horaria INT(2);

SELECT * FROM cursos;

UPDATE cursos SET carga_horaria=20;

SELECT * FROM cursos;

UPDATE cursos SET carga_horaria=40 WHERE id_curso=2;

SELECT * FROM cursos;

CREATE TABLE usuarios (id_user INT NOT NULL PRIMARY KEY AUTO_INCREMENT, nome VARCHAR(30));

DROP TABLE usuarios;
