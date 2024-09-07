create table MaquinaAductores(
    id INT PRIMARY KEY NOT NULL AUTO_INCREMENT,
    peso INT DEFAULT 0 CHECK(peso%5==0 AND peso>=0 AND peso<=100),
    posicion VARCHAR(50) DEFAULT "ADUCTORES"
)
 INSERT INTO MaquinaAductores (peso,posicion) VALUES
 (50,"ADUCTORES"),
 (10,"ABDUCTORES"),
 (15,"ADUCTORES"),
 (5,"ADUCTORES"),
 (35,"ABDUCTORES"),
 (70,"ABDUCTORES"),
 (90,"ADUCTORES"),
 (25,"ADUCTORES"),
 (0,"ADUCTORES"),
 (100,"ABDUCTORES");

 SELECT * FROM MaquinaAductores WHERE peso = 25;
 SELECT * FROM MaquinaAductores WHERE peso between 60 AND 100;
 SELECT posicion FROM MaquinaAductores WHERE id = 2;
 SELECT peso FROM MaquinaAductores WHERE posicion = "ADUCTORES";
 SELECT * FROM MaquinaAductores WHERE posicion = "ABDUCTORES";