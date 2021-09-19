SELECT 'CONSULTA 1';
SELECT nombre from alumno ORDER BY cod_ord ASC;
SELECT 'CONSULTA 2';
/*SELECT modulo.nombre FROM modulo JOIN profesor_modulo USING(codigo) JOIN profesor USING(rfc) WHERE rfc = 4;*/
SELECT modulo.nombre FROM modulo WHERE modulo.codigo = 1;
SELECT 'CONSULTA 3';
/*SELECT alumno.control, alumno.nombre, alumno.apellido, alumno.fecha_nacimiento, modulo.nombre FROM alumno JOIN modulo ON (modulo.relacion_alumno = alumno.control) WHERE modulo.nombre = "Electivas";*/
SELECT alumno.control, alumno.nombre, alumno.apellido, alumno.fecha_nacimiento, modulo.nombre FROM alumno, modulo WHERE alumno.control = 3 AND modulo.codigo = 1;
