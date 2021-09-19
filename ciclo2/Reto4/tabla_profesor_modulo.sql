CREATE TABLE profesor_modulo (
	rfc INT NOT NULL,
    codigo INT NOT NULL,
    FOREIGN KEY (rfc) REFERENCES profesor(rfc),
    FOREIGN KEY (codigo) REFERENCES modulo(codigo)
);

INSERT INTO profesor_modulo (rfc, codigo) VALUES (1, 1);
INSERT INTO profesor_modulo (rfc, codigo) VALUES (2, 2);
INSERT INTO profesor_modulo (rfc, codigo) VALUES (3, 3);
INSERT INTO profesor_modulo (rfc, codigo) VALUES (5, 4);
