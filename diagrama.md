```mermaid
graph TD
    A[Inicio] --> B[Iniciar sesión]
    B --> C{¿Es Administrador?}
    C -- Sí --> D[Gestionar Catálogo de Postres]
    D --> E[Ver Pedidos]
    C -- No --> F[Ver Catálogo]
    F --> G[Realizar Pedido]
    E --> H[Fin]
    G --> H