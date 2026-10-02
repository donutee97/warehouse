# WAREHOUSE

## Sistema de inventario warehouse

### Módulos/apps:

- productos/
    - Catálogo base, SKUs, imágenes, precios, stock actual
    - LOGICA CRUD: Alta/edición de ítems, asignación de código de barras, alertas de stock mínimo.
- categorias/
    - Jerarquías, familias de productos, atributos y marcas
    - LOGICA CRUD: Gestión del árbol de categorías, filtrado y etiquetado de productos.
- proveedores/
    - Directorio de suplidores, datos de contacto, tiempos de entrega
    - LOGICA CRUD: Gestión de la agenda de suplidores y productos ofertados por cada uno.
- clientes/
    - Registro de compradores, historial de compras, datos de facturación
    - LOGICA CRUD: Base de datos de clientes corporativos/personales y sus direcciones.
- almacenes/
    - Ubicaciones físicas, bodegas, pasillos, estantes y zonas
    - LOGICA CRUD: Registro de sedes/bodegas y desglose de estantes/racks.
- compras/
    - Ordenes de compra a proveedores, entrada de stock e historial
    - LOGICA CRUD: Registro de entradas de inventario desde proveedores e impacto en el stock.
- ventas/
    - Órdenes de venta/salida de mercancía, facturación básica
    - LOGICA CRUD: Registro de salidas de mercancía enviadas a clientes.
- movimientos/
    - Transferencias entre almacenes, ajustes de inventario, bajas/merma
    - LOGICA CRUD: Traspasos entre bodegas (ej. Almacén A $\rightarrow$ Almacén B) y registro de mermas/pérdidas.
- reportes/
    - Métricas, dashboards de stock crítico, rotación de productos
    - LOGICA CRUD: Consultas agregadas (Count, Sum, Avg), productos más vendidos y valorización del stock.