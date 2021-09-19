CREATE TABLE profesor (
    rfc INT PRIMARY KEY,
    nombre CHAR(20) NOT NULL,
    direccion CHAR(20) NOT NULL,
    telefono BIGINT NOT NULL
);

INSERT INTO profesor (rfc, nombre, telefono, direccion) VALUES (1, "Susana Perez", 555555, 'CLL 54 16-7');
INSERT INTO profesor (rfc, nombre, telefono, direccion) VALUES (2, "Pedro Palacio", 8526789, 'Crr 56 18-7');
INSERT INTO profesor (rfc, nombre, telefono, direccion) VALUES (3, "Liliana Loaiza", 6384386, 'Transversal 54 16-7');
INSERT INTO profesor (rfc, nombre, telefono, direccion) VALUES (4, "Camilo Rincon", 8985432, 'Crr 20 17-7');
INSERT INTO profesor (rfc, nombre, telefono, direccion) VALUES (5, "Paula Restrepo", 89754465, 'Crr 56 16-7');
