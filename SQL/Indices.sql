-- �ndice para producto_nombre
CREATE INDEX idx_producto_nombre
ON nombre_de_tabla(producto_nombre);

-- �ndice para cliente_email
CREATE INDEX idx_cliente_email
ON nombre_de_tabla(cliente_email);

-- �ndice para pedidos_fechapedido
CREATE INDEX idx_pedidos_fechapedido 
ON nombre_de_tabla(pedidos_fechapedido);
