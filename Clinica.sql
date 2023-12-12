CREATE DATABASE IF NOT EXISTS PEPS;
USE PEPS;

CREATE TABLE usuarios(
	usuario VARCHAR(100) NOT NULL PRIMARY KEY,
    clave VARCHAR(255) NOT NULL,
    perfil VARCHAR(100) NOT NULL,
    fechaUltimoAcceso DATE
);

CREATE TABLE pacientes (
    id INT UNSIGNED NOT NULL AUTO_INCREMENT PRIMARY KEY,
    nombre VARCHAR(255) NOT NULL,
    apellido VARCHAR(255) NOT NULL,
    direccion VARCHAR(255),
    telefono VARCHAR(20),
);


CREATE TABLE citas (
    id INT UNSIGNED NOT NULL AUTO_INCREMENT PRIMARY KEY,
    paciente_id INT UNSIGNED NOT NULL,
    fecha_hora DATETIME NOT NULL,
    observaciones TEXT,
    FOREIGN KEY (paciente_id) REFERENCES pacientes(id)
);

CREATE TABLE tratamientos (
    id INT UNSIGNED NOT NULL AUTO_INCREMENT PRIMARY KEY,
    nombre VARCHAR(255) NOT NULL,
    costo DECIMAL(9, 2) NOT NULL
);


INSERT INTO `usuarios` (`usuario`, `clave`, `perfil`, `fechaUltimoAcceso`) VALUES ('root', '1234', 'admin', '2022-03-01');

-- Insertar pacientes de ejemplo
INSERT INTO pacientes (nombre, apellido, fecha_nacimiento, direccion, telefono, usuario)
VALUES
    ('María', 'González', '1985-09-20', 'Avenida Principal 456', '987-654-3210', 'root'),
    ('Juan', 'Pérez', '1990-05-15', 'Calle Secundaria 789', '123-456-7890', 'root');

-- Insertar citas de ejemplo
INSERT INTO citas (paciente_id, fecha_hora, observaciones)
VALUES
    (1, '2023-01-15 10:00:00', 'Examen de rutina para María González.'),
    (2, '2023-02-20 14:30:00', 'Consulta dental para Juan Pérez.');

-- Insertar tratamientos de ejemplo
INSERT INTO tratamientos (nombre, costo)
VALUES
    ('Limpieza dental', 80.00),
    ('Extracción de muelas del juicio', 150.00),
    ('Blanqueamiento dental', 120.00);


