# Simple api properties

## API REST que gerencia imóveis

#### INSTALAÇÃO

***Clonar o projeto para seu ambiente local***
```
git clone 'project'
```
***Criar e ativar ambiente virtual***
```
virtualenv .venv
source .venv/bin/activate
```
***Instale todas as dependências do projeto***
```
pip install -r spotippos/requirements.txt
```
***Criar as migrações do banco de dados(sqlite)***
```
make migrations
```

#### EXECUTANDO A APLICAÇÃO
> Não esqueça de rodar as migrações da aplicação antes de executar o código abaixo

```
make run
```

#### EXECUTANDO OS TESTES
***Testes Unitários***
```
make test
```
***Testes com informações de cobertura***
```
make test-coverage
```
-------------------------------------------------------------------------------------

## API REST

#### Buscar determinado imóvel

***Rota***
`/api/v1/properties/{id}` GET

Retorno 

- **HTTP 200 Response** 
  - Lista de um imóvel especifico

#### Cadastra um novo imóvel na aplicação

***Rota***
`/api/v1/properties` POST

**Parâmetros**

```
*title* - Titulo do imóvel
*price* - Preço do imóvel em decimal
*description* - Descrição do imóvel
*bed* - Número de quartos do imóvel. Minimo 1 máximo 5.
*bath* - Número de banheiros do imóvel. Minimo 1 máximo 4.
*squareMeters* - Metros quadrados do imóvel. Minimo 20 máximo 240.
*cordinate_x* - Cordenada x
*cordinate_y* - Cordenada y
```

Retornos 

- **HTTP 201 Response** 
  - Imóvel cadastrado com sucesso.
- **HTTP 400 Response** - 
  - Erro ao cadastrar imóvel, verificar mensagem de erro.

#### Busca um imóvel por uma área

***Rota***
`/api/v1/properties/cordinates/{ax}/{ay}/{bx}/{by}` GET

Retornos 

- **HTTP 200 Response** 
  - Listagem dos imóveis encontrados.
- **HTTP 404 Response** 
  - Nenhum imóvel encontrado.
