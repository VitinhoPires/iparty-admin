iParty Admin

Este projeto é uma aplicação Flask que serve como painel administrativo para o aplicativo iParty. Ele permite que administradores verifiquem e aprovem documentos enviados pelos usuários, como CPF, RG e fotos tiradas diretamente pelo aplicativo Flutter.​
🧰 Tecnologias Utilizadas

    -Python 3.8+

    -Flask

    -Docker & Docker Compose

    -SQLite (pode ser substituído por PostgreSQL)

    -Integração com Flutter via API REST

📁 Estrutura do Projeto

    iparty-admin/
    ├── app/
    │   ├── __init__.py
    │   ├── routes.py
    │   ├── models.py
    │   └── templates/
    ├── static/
    ├── Dockerfile
    ├── docker-compose.yml
    ├── requirements.txt
    └── README.md

🚀 Como Executar o Projeto
Pré-requisitos

    Docker instalado

    Docker Compose instalado

Passos para Execução
Clone o repositório:​

    git clone https://github.com/VitinhoPires/iparty-admin.git
    cd iparty-admin

Construa e inicie os containers:​

    docker-compose up --build

Acesse a aplicação no navegador:​

    http://localhost:5000

📦 Implantação com Docker

Para garantir que a aplicação funcione em qualquer ambiente, utilizamos o Docker. Isso permite que você execute o projeto em qualquer máquina com Docker instalado, sem se preocupar com configurações específicas do sistema operacional.​
🔄 Integração com o Aplicativo Flutter

O aplicativo Flutter se conecta a esta API para:​

    Autenticar usuários
    Enviar documentos (CPF, RG) e fotos tiradas na hora
    Receber status de aprovação ou rejeição​

Após a aprovação, o usuário pode utilizar o aplicativo normalmente.​
🛠️ Contribuindo

Contribuições são bem-vindas! Sinta-se à vontade para abrir issues ou enviar pull requests.​

📄 Licença

Este projeto está licenciado sob a MIT License.​
