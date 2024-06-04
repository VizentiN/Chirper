# Nome do Projeto: Chirper

## Descrição

Chirper é uma plataforma inspirada no Twitter que permite aos usuários postar mensagens curtas chamadas "chirps". Este projeto foi criado para explorar funcionalidades de redes sociais com um foco em simplicidade e eficácia.

## Tecnologias Utilizadas

- Django: Framework web para Python que oferece uma solução completa para desenvolvimento rápido.
- JavaScript: Para interações dinâmicas no cliente e validação de formulários.
- HTML/CSS: Para estruturação e estilização das páginas.

## Funcionalidades

- Cadastro e autenticação de usuários.
- Postagem de mensagens curtas.
- Visualização de mensagens de todos os usuários.
- Validação dinâmica de senha no cadastro.

## Instalação

### Pré-requisitos

Certifique-se de ter Python e Django instalados em sua máquina. Recomenda-se usar um ambiente virtual para a instalação das dependências.


### Clonando o Repositório
```shell
git clone https://github.com/VizentiN/chirper.git
cd chirper
```

### Instalando Dependências
```shell
pip install -r requirements.txt
```

### Configurando o Projeto
```shell
python manage.py migrate
python manage.py createsuperuser
python manage.py collectstatic
```

### Executando o Servidor
```shell
python manage.py runserver
```

Agora, acesse `http://localhost:8000/` para ver o projeto em ação.

## Como Contribuir

Contribuições são sempre bem-vindas! Veja abaixo como você pode contribuir:

1. Fork o projeto.
2. Crie uma nova branch com sua feature ou correção de bugs (`git checkout -b feature/branch-name`).
3. Faça commit de suas alterações (`git commit -am 'Add some feature'`).
4. Faça push para a branch (`git push origin feature/branch-name`).
5. Crie um novo Pull Request.

## Licença

Este projeto está licenciado sob a Licença MIT - veja o arquivo [LICENSE.md](LICENSE) para detalhes.

---

### Contato

- Nome do Autor: Lucas Vizentin
- Email: lucasvizentin.developer@gmail.com