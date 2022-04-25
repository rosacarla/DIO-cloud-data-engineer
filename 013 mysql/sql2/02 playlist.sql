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

CREATE TABLE author (
    id_author INT NOT NULL PRYMARY KEY AUTOINCREMENT,
    name VARCHAR(30) NOT NULL,
    born DATE 
)

INSERT INTO author (name, born) VALUES ('Maria', '1992-04-10');
INSERT INTO author (name, born) VALUES ('Pedro', '2000-10-12');
INSERT INTO author (name, born) VALUES ('Joao', '1998-03-09');
INSERT INTO author (name, born) VALUES ('Flávia', '1975-04-19')

UPDATE videos SET author=''
/*
atualiza a tabela videos com exclusao de todos os nomes
*/;
UPDATE videos SET author=1 WHERE id_video=1;
UPDATE videos SET author=1 WHERE id_video=2;
UPDATE videos SET author=1 WHERE id_video=3;
UPDATE videos SET author=2 WHERE id_video=4;
UPDATE videos SET author=3 WHERE id_video=5;

SELECT * FROM videos
/*
mostra tabela videos atualizada
*/;

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
UPDATE videos SET fk_seo=1 WHERE id_video=2;
UPDATE videos SET fk_seo=1 WHERE id_video=3;
UPDATE videos SET fk_seo=1 WHERE id_video=4;
UPDATE videos SET fk_seo=2 WHERE id_video=1;
UPDATE videos SET fk_seo=2 WHERE id_video=5;
UPDATE videos SET fk_seo=2 WHERE id_video=6
/*
atualizada categoria na tab videos com chave estrangeira fk_seo para categorias 1 frontend e 2 backend da tabela seo
*/;
ALTER TABLE `videos` ADD CONSTRAINT `fk-seo` FOREIGN KEY (`fk_seo`) REFERENCES `seo`(`id_seo`) ON DELETE CASCADE ON UPDATE CASCADE
/*
cria relacionamento com chave estrang fk_seo na tabela videos, ligada a coluna id_seo na tabela seo
*/;
SELECT * FROM videos JOIN seo ON videos.fk_seo = seo.id_seo
/*chama todos os videos junto com tab seo onde col fk_seo é igual a id_seo na tab seo
*/;
SELECT videos.title, seo.category FROM videos JOIN seo ON videos.fk_seo = seo.id_seo
/*chama todos os videos (titulo e categoria) junto com tab seo onde col fk_seo é igual a id_seo na tab seo
*/;
SELECT videos.title, author.name, seo.category FROM videos JOIN seo ON videos.fk_seo = seo.id_seo
JOIN author ON videos.fk_author = author.id_author
/*
chama todos os videos com titulo, nome e categoria, junto com tab seo onde col fk_seo
é igual a id_seo na tab seo e fk_author é igual a id_author na tab author
*/;
INSERT INTO playlist (name_pl) VALUES ('HTML + CSS');
INSERT INTO playlist (name_pl) VALUES ('HTML + PHP + JS');
INSERT INTO playlist (name_pl) VALUES ('Python + MySQL')
/*
insere nomes das playslist na col name_pl da tab playlist 
*/;
UPDATE playlist SET name_pl = 'Python + PHP' WHERE playlist.id_playlist = 3
/*
altera nome da playlist id 3 para "Python + PHP"
*/;
INSERT INTO videos_playlist (fk_videos, fk_playlist) VALUES (2, 1);
INSERT INTO videos_playlist (fk_videos, fk_playlist) VALUES (3, 1)
/*
insere videos na playlist usando chaves estrang (video e playlist) 
*/;
SELECT * FROM playlist
/*
mostra quais sao todos os  nomes de playlists na tab palylist  
*/;
SELECT * FROM playlist JOIN videos_playlist ON playlist.id_playlist = videos_playlist.fk_playlist
 /*
mostra tudo da playlist junto com videos_playlist onde id_playlist (em playlist) é igual fk_playlist (em videos_playlist)
*/;
SELECT * FROM playlist JOIN videos_playlist ON playlist.id_playlist = videos_playlist.fk_playlist
JOIN videos ON videos.id_video = videos_playlist.fk_videos;
/*
mostra tudo da playlist junto com videos_playlist onde id_playlist é igual fk_playlist (em videos_playlist), 
junto com videos onde id = fk nas tab videos e videos_playlist; apresenta esta ordem de colunas:
id_playlis/name_pl/id_vp/fk_videos/fk_playlist/id_video/fk_author/title/fk_seo/likes/dislikes.
*/
SELECT playlist.name_pl, videos.title FROM playlist
JOIN videos_playlist ON playlist.id_playlist = videos_playlist.fk_playlist
JOIN videos ON videos.id_video = videos_playlist.fk_videos 
/* mostra somente nome da playlist e titulo do video da tab playlist,
junto com videos_playlist onde id_playlist é igual fk_playlist (em videos_playlist),
junto com videos onde id = fk nas tab videos e videos_playlist*/;

SELECT playlist.name_pl, videos.title, author.name FROM playlist 
JOIN videos_playlist ON playlist.id_playlist = videos_playlist.fk_playlist 
JOIN videos ON videos.id_video = videos_playlist.fk_videos
JOIN author ON videos.fk_author = author.id_author 
/*
mostra somente nome da playlist, titulo do video, nome do autor
junto com videos_playlist onde id_playlist é igual fk_playlist (em videos_playlist), 
junto com videos onde id = fk nas tab videos e videos_playlist,
junto com fk e id dat tab videos e author*/; 

ALTER TABLE `playlist` ADD `fk_author` INT NOT NULL AFTER `name_pl`; 
/*
altera a tab playlist inserindo a coluna fk_author 
*/
UPDATE playlist SET fk_author=7 WHERE id_playlist=1
/* 
atualiza tab plylist com nome do autor/criador da playlist id 1
*/; 
UPDATE playlist SET fk_author=3 WHERE id_playlist=2 
/*
 atualiza tab plylist com nome do autor/criador da playlist id 2 
*/; 
UPDATE playlist SET fk_author=1 WHERE id_playlist=3
/*
 atualiza tab plylist com nome do autor/criador da playlist id 3
*/; 
SELECT * FROM playlist JOIN author ON playlist.fk_author = author.id_author
/*
mostra playlist com dados dos autores 
*/;
SELECT author.name, playlist.name_pl FROM playlist JOIN author ON playlist.fk_author = author.id_author
/*
mostra somente nomes de autores e nomes da playlist
*/; 
SELECT playlist.name_pl, author.name FROM playlist
JOIN author ON playlist.fk_author = author.id_author WHERE playlist.id_playlist = 1
/*
mostra nome da playlist e autor da playlist 1
*/;