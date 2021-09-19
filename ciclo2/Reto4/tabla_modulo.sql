CREATE TABLE modulo (
	codigo INT PRIMARY KEY,
    nombre CHAR(20) NOT NULL,
    relacion_alumno INT NOT NULL,
    FOREIGN KEY (relacion_alumno) REFERENCES alumno(control)
);

INSERT INTO modulo (codigo, nombre, relacion_alumno) VALUES (1, 'Electivas', 3);
INSERT INTO modulo (codigo, nombre, relacion_alumno) VALUES (2, 'Optativas', 1);
INSERT INTO modulo (codigo, nombre, relacion_alumno) VALUES (3, 'Fundamentacion', 2);
INSERT INTO modulo (codigo, nombre, relacion_alumno) VALUES (4, 'Disciplinares', 4);
