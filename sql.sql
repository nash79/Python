use db_cours;

create table utilisateur
(
	id int primary key not null,
    nom varchar(100) not null,
    prenom varchar(100) not null,
    email varchar(255) not null,
    date_naissance date not null,
    pays varchar(255) not null,
    ville varchar(255) not null,
    code_postal varchar(5) not null
);

create table groupe
(
	id int primary key not null auto_increment,
    nom varchar(255) not null
);

create table utilisateur_group
(
	id int primary key not null AUTO_INCREMENT,
    idgroup int not null,
    idutilisateur int not null,
    FOREIGN KEY (idgroup) REFERENCES groupe(id),
    FOREIGN KEY (idutilisateur) REFERENCES utilisateur(id)
);

Select count(idgroup) 
FROM utilisateur_group 
where idutilisateur=0;

-- Table Utilisateur
insert into utilisateur (nom, prenom,email,date_naissance,pays, ville, code_postal)
values ('Queen','Oliver','arrow@teamarrow.com','1980-05-28','Na ilha','This City','12345');

update utilisateur
set nom='Chevre',
	prenom='Seguin',
    email='seguin@chevre.com'
where id=0;

truncate utilisateur;

delete from utilisateur
where id=0;

select * from utilisateur;

-- Table groupe
insert into groupe (nom) values ('test')

-- Table Utilisateur_Group
select * from groupe
