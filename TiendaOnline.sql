CREATE DATABASE TiendaOnline;
GO
USE TiendaOnline;
GO

CREATE TABLE Productos (
    ProductoID INT PRIMARY KEY IDENTITY(1,1),
    Nombre NVARCHAR(100) ,
    Precio DECIMAL(10, 2),
    Stock INT NOT NULL
);

CREATE TABLE Clientes (
    ClienteID INT PRIMARY KEY IDENTITY(1,1),
    Nombre NVARCHAR(100) NOT NULL,
    Email NVARCHAR(100) NOT NULL UNIQUE
);

-- Tabla Pedidos
CREATE TABLE Pedidos (
    PedidoID INT PRIMARY KEY IDENTITY(1,1),
    ClienteID INT NOT NULL,
    FechaPedido DATETIME NOT NULL,
    FOREIGN KEY (ClienteID) REFERENCES Clientes(ClienteID)
);

-- Tabla Detalles de Pedido
CREATE TABLE DetallesPedido (
    DetalleID INT PRIMARY KEY IDENTITY(1,1),
    PedidoID INT,
    ProductoID INT,
    Cantidad INT,
    Precio DECIMAL(10, 2),
    FOREIGN KEY (PedidoID) REFERENCES Pedidos(PedidoID),
    FOREIGN KEY (ProductoID) REFERENCES Productos(ProductoID)
);

-- Tabla Auditoria
CREATE TABLE Auditoria (
    AuditoriaID INT PRIMARY KEY IDENTITY(1,1),
    Tabla NVARCHAR(100),
    Operacion NVARCHAR(100),
    Fecha DATETIME,
    Detalle NVARCHAR(MAX)
);

CREATE VIEW VistaClientePedidos AS
SELECT 
    c.Nombre AS NombreCliente,
    p.PedidoID,
    p.FechaPedido,
    d.ProductoID,
    d.Cantidad,
    d.Precio
FROM 
    Clientes c
    JOIN Pedidos p ON c.ClienteID = p.ClienteID
    JOIN DetallesPedido d ON p.PedidoID = d.PedidoID;

CREATE PROCEDURE RegistrarPedido
    @ClienteID INT,
    @FechaPedido DATETIME,
    @ProductosDetalle AS NVARCHAR(MAX)
AS
BEGIN

    DECLARE @TempProductosDetalle TABLE (ProductoID INT, Cantidad INT, Precio DECIMAL(10, 2));
    
    INSERT INTO @TempProductosDetalle (ProductoID, Cantidad, Precio)
    SELECT ProductoID, Cantidad, Precio
    FROM OPENJSON(@ProductosDetalle)
    WITH (
        ProductoID INT,
        Cantidad INT,
        Precio DECIMAL(10, 2)
    );

    BEGIN TRANSACTION;

    DECLARE @PedidoID INT;

    -- Inserta en la tabla Pedidos
    INSERT INTO Pedidos (ClienteID, FechaPedido)
    VALUES (@ClienteID, @FechaPedido);

    SET @PedidoID = SCOPE_IDENTITY();

    -- Inserta en la tabla DetallesPedido y actualiza stock
    DECLARE @ProductoID INT, @Cantidad INT, @Precio DECIMAL(10, 2);
    
    DECLARE ProductCursor CURSOR FOR
    SELECT ProductoID, Cantidad, Precio FROM @TempProductosDetalle;

    OPEN ProductCursor;
    
    FETCH NEXT FROM ProductCursor INTO @ProductoID, @Cantidad, @Precio;

    WHILE @@FETCH_STATUS = 0
    BEGIN
        INSERT INTO DetallesPedido (PedidoID, ProductoID, Cantidad, Precio)
        VALUES (@PedidoID, @ProductoID, @Cantidad, @Precio);

        UPDATE Productos
        SET Stock = Stock - @Cantidad
        WHERE ProductoID = @ProductoID;

        FETCH NEXT FROM ProductCursor INTO @ProductoID, @Cantidad, @Precio;
    END

    CLOSE ProductCursor;
    DEALLOCATE ProductCursor;

    COMMIT TRANSACTION;
END;

CREATE TRIGGER DisparadorAuditoriaProductos
ON Productos
FOR INSERT, UPDATE, DELETE
AS
BEGIN
    DECLARE @Operacion NVARCHAR(100);
    DECLARE @Detalle NVARCHAR(MAX);
    DECLARE @Fecha DATETIME;

    SET @Fecha = GETDATE();

    IF EXISTS(SELECT * FROM inserted) AND EXISTS(SELECT * FROM deleted)
        SET @Operacion = 'UPDATE';
    ELSE IF EXISTS(SELECT * FROM inserted)
        SET @Operacion = 'INSERT';
    ELSE IF EXISTS(SELECT * FROM deleted)
        SET @Operacion = 'DELETE';

    SET @Detalle = 'Detalles de la operaci�n...';

    INSERT INTO Auditoria (Tabla, Operacion, Fecha, Detalle)
    VALUES ('Productos', @Operacion, @Fecha, @Detalle);
END;
