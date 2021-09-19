CREATE TABLE alumno (
	control INT PRIMARY KEY,
    nombre CHAR(20) NOT NULL,
    apellido CHAR(20) NOT NULL,
    fecha_nacimiento DATE NOT NULL,
    cod_ord INT NOT NULL
);	

INSERT INTO alumno (control, nombre, apellido, fecha_nacimiento, cod_ord) VALUES (1, 'Alejandro', 'Perez Suarez', '10/06/2000', 3);
INSERT INTO alumno (control, nombre, apellido, fecha_nacimiento, cod_ord) VALUES (2, 'Laura', 'Ramirez Torres', '10/08/2000', 1);
INSERT INTO alumno (control, nombre, apellido, fecha_nacimiento, cod_ord) VALUES (3, 'Luis', 'Franco Garcia', '10/07/2000', 2);
INSERT INTO alumno (control, nombre, apellido, fecha_nacimiento, cod_ord) VALUES (4, 'Alejandro', 'Diaz Suarez', '11/06/2000', 4);
