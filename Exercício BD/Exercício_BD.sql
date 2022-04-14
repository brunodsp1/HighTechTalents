CREATE TABLE `Corretor` (
	`ID` BINARY NOT NULL AUTO_INCREMENT,
	`Nome` varchar(255) NOT NULL,
	`Sobrenome` varchar(255) NOT NULL,
	`ID_Telefone` INT(255) NOT NULL,
	PRIMARY KEY (`ID`)
);

CREATE TABLE `Inquilino` (
	`ID` INT NOT NULL,
	`Nome` varchar(255) NOT NULL,
	`Sobrenome` varchar(255) NOT NULL,
	`CPF` INT(11) NOT NULL,
	`ID_Telefone` INT NOT NULL,
	`ID_Aluguel` BINARY NOT NULL,
	PRIMARY KEY (`ID`)
);

CREATE TABLE `Contrato` (
	`ID` BINARY NOT NULL,
	`Tipo_de_contrato` INT NOT NULL,
	`Fiador` INT NOT NULL,
	`Data_Ínicio` DATE NOT NULL,
	`Data_Fim` DATE NOT NULL,
	PRIMARY KEY (`ID`)
);

CREATE TABLE `Aluguel` (
	`ID` INT NOT NULL AUTO_INCREMENT,
	`ID_Corretor` INT NOT NULL,
	`ID_Imóvel` INT NOT NULL,
	`ID_Contrato` INT NOT NULL,
	`ID_Inquilino` INT NOT NULL,
	`Valor` FLOAT NOT NULL,
	`Exige_calção` BINARY NOT NULL,
	`Aceita_melhorias` BINARY NOT NULL,
	PRIMARY KEY (`ID`)
);

CREATE TABLE `Imóvel` (
	`ID` BINARY NOT NULL AUTO_INCREMENT,
	`ID_Proprietário` BINARY NOT NULL AUTO_INCREMENT,
	`Tipo_imóvel` varchar(255) NOT NULL,
	`Endereço` varchar(255) NOT NULL AUTO_INCREMENT,
	`Garagem_propria` BINARY NOT NULL,
	`Metragem` varchar(255) NOT NULL,
	`Num_salas` INT(255) NOT NULL,
	`Num_banheiros` INT(255) NOT NULL AUTO_INCREMENT,
	`Num_vagas` INT(255) NOT NULL,
	`Num_Elevadores` BINARY NOT NULL,
	`Escada_Incendio` BINARY NOT NULL,
	`Tipo_Recepção` varchar(255) NOT NULL,
	PRIMARY KEY (`ID`)
);

CREATE TABLE `Proprietário` (
	`ID` BINARY NOT NULL AUTO_INCREMENT,
	`Nome` varchar(255) NOT NULL AUTO_INCREMENT,
	`Sobrenome` varchar(255) NOT NULL,
	`CPF` INT(11) NOT NULL,
	`Endereço` varchar(255) NOT NULL,
	`Id_Telefone` varchar(255) NOT NULL,
	PRIMARY KEY (`ID`)
);

CREATE TABLE `Telefones` (
	`ID` INT(255) NOT NULL AUTO_INCREMENT,
	`ID_Telefone` INT NOT NULL AUTO_INCREMENT,
	`Telefone` varchar(255) NOT NULL AUTO_INCREMENT,
	PRIMARY KEY (`ID`)
);

ALTER TABLE `Corretor` ADD CONSTRAINT `Corretor_fk0` FOREIGN KEY (`ID_Telefone`) REFERENCES `Telefones`(`ID_Telefone`);

ALTER TABLE `Inquilino` ADD CONSTRAINT `Inquilino_fk0` FOREIGN KEY (`ID_Telefone`) REFERENCES `Telefones`(`ID_Telefone`);

ALTER TABLE `Inquilino` ADD CONSTRAINT `Inquilino_fk1` FOREIGN KEY (`ID_Aluguel`) REFERENCES ``(``);

ALTER TABLE `Aluguel` ADD CONSTRAINT `Aluguel_fk0` FOREIGN KEY (`ID_Corretor`) REFERENCES `Corretor`(`ID`);

ALTER TABLE `Aluguel` ADD CONSTRAINT `Aluguel_fk1` FOREIGN KEY (`ID_Imóvel`) REFERENCES `Imóvel`(`ID`);

ALTER TABLE `Aluguel` ADD CONSTRAINT `Aluguel_fk2` FOREIGN KEY (`ID_Contrato`) REFERENCES `Contrato`(`ID`);

ALTER TABLE `Aluguel` ADD CONSTRAINT `Aluguel_fk3` FOREIGN KEY (`ID_Inquilino`) REFERENCES `Inquilino`(`ID`);

ALTER TABLE `Imóvel` ADD CONSTRAINT `Imóvel_fk0` FOREIGN KEY (`ID_Proprietário`) REFERENCES `Proprietário`(`ID`);

ALTER TABLE `Proprietário` ADD CONSTRAINT `Proprietário_fk0` FOREIGN KEY (`Id_Telefone`) REFERENCES `Telefones`(`ID_Telefone`);








