```mermaid
flowchart TB
    %% Actores
    C["👤 Cliente"]
    A["👤 Administrador"]

    %% Límite del Sistema
    subgraph Sistema["Sistema Postrería Dulces Deseos"]
        %% Precondiciones generales
        REG(["Registrarse"])
        LOGIN(["Iniciar sesión"])

        %% Casos de uso - Cliente
        VC(["Visualizar el catálogo"])
        VD(["Verificar disponibilidad"])
        RP(["Realizar pedido"])
        CP(["Confirmar el pedido"])
        CHP(["Consultar historial de pedidos"])

        %% Casos de uso - Administrador
        AC(["Administrar catálogo"])
        APU(["Administrar los perfiles de los usuarios"])
        VHP(["Visualizar el historial de los pedidos de los clientes"])
        RPV(["Registrar los productos vendidos"])
    end

    %% Relaciones directas (Quién puede hacer qué)
    C --- REG
    C --- LOGIN
    C --- VC
    C --- VD
    C --- RP
    C --- CP
    C --- CHP

    A --- LOGIN
    A --- AC
    A --- APU
    A --- VHP
    A --- RPV

    %% Relaciones de dependencia / Precondiciones (<<include>>)
    %% Recuerda: La flecha viaja DESDE la acción HACIA el requisito previo
    LOGIN -. "<<include>>" .-> REG
    
    %% Precondiciones para las acciones del Cliente
    RP -. "<<include>>" .-> LOGIN
    CP -. "<<include>>" .-> LOGIN
    CHP -. "<<include>>" .-> LOGIN

    %% Precondiciones para las acciones del Administrador
    AC -. "<<include>>" .-> LOGIN
    APU -. "<<include>>" .-> LOGIN
    VHP -. "<<include>>" .-> LOGIN
    RPV -. "<<include>>" .-> LOGIN

    %% Estilo: Flechas y trazos en color blanco
    linkStyle default stroke:#ffffff,stroke-width:2px;