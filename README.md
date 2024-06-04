# Awesome Project: ETL Process for Currency Quotes Data

![Project Status](https://img.shields.io/badge/status-done-brightgreen)
![License](https://img.shields.io/badge/license-MIT-blue) ![GitHub release (latest by date)](https://img.shields.io/github/v/release/IvanildoBarauna/ETL-awesome-api) ![Python Version](https://img.shields.io/badge/python-3.9-blue) ![GitHub Workflow Status](https://github.com/IvanildoBarauna/ETL-awesome-api/actions/workflows/CI-CD.yaml/badge.svg)
[![codecov](https://codecov.io/gh/IvanildoBarauna/ETL-awesome-api/branch/main/graph/badge.svg?token=GEGNHFM6P)](https://codecov.io/gh/IvanildoBarauna/ETL-awesome-api)

## Code Coverage KPI Graph

[![codecov](https://codecov.io/gh/IvanildoBarauna/ETL-awesome-api/graphs/sunburst.svg?token=GEGNHFM6PS)](https://codecov.io/gh/IvanildoBarauna/ETL-awesome-api)

## Project Stack

<img src="https://github.com/devicons/devicon/blob/master/icons/python/python-original.svg" Alt="Python" width="50" height="50"> <img src="https://github.com/devicons/devicon/blob/master/icons/docker/docker-original.svg" Alt="Docker" width="50" height="50"> <img src="https://github.com/devicons/devicon/blob/master/icons/poetry/poetry-original.svg" Alt="Poetry" width="50" height="50"> <img src="https://github.com/devicons/devicon/blob/master/icons/pandas/pandas-original.svg" Alt="Pandas" width="50" height="50"> <img src="https://github.com/devicons/devicon/blob/master/icons/jupyter/jupyter-original.svg" Alt="Jupyter" width="50" height="50"> <img src="https://github.com/devicons/devicon/blob/master/icons/matplotlib/matplotlib-original.svg" Alt="Matplotlib" width="50" height="50"> <img src="https://github.com/devicons/devicon/blob/master/icons/githubactions/githubactions-original.svg" Alt="GitHub Actions" width="50" height="50">

## Descrição do Projeto

O projeto "Awesome Project: ETL Process for Currency Quotes Data" é uma solução completa dedicada à extração, transformação e carregamento (ETL) de dados de cotações de moedas. Este projeto utiliza diversas técnicas e arquiteturas avançadas para garantir a eficiência e a robustez do processo ETL.

## Destaques do Projeto:

- Arquitetura MVC: Implementação da arquitetura Model-View-Controller (MVC), separando a lógica de negócio, a interface do usuário e a manipulação de dados para uma melhor organização e manutenção do código.

- Testes Abrangentes: Desenvolvimento de testes para garantir a qualidade e a robustez do código em diversas etapas do processo ETL

- Paralelismo nos Modelos: Utilização de paralelismo nas etapas de transformação e carregamento dos dados, aumentando a eficiência e reduzindo o tempo de processamento.

- Mensageria Fire-Forget: Uso de mensageria (queue.queue) no modelo fire-forget para gerenciar os arquivos gerados entre as etapas de transformação e carregamento, garantindo um fluxo de dados contínuo e eficiente.

- Validação de Parâmetros: Envio de parâmetros válidos baseados na própria fonte de dados de requisições, garantindo a integridade e a precisão das informações processadas.

- Gestão de Configurações: Utilização de um módulo de configuração para gerenciar endpoints, tempos de retry e quantidade de tentativas, proporcionando flexibilidade e facilidade de ajustes.

- Módulo Comum: Implementação de um módulo comum para reutilização de código em todo o projeto, promovendo a consistência e a redução de redundâncias.

- Views Dinâmicas: Geração de views com index.html utilizando nbConvert, baseado em dados consolidados de um Jupyter Notebook que integra os arquivos gerados em um único dataset para exploração e análise.

# Processo ETL:

- Extração: Uma única requisição é feita a um endpoint específico para obter cotações de múltiplas moedas.
- Transformação: A resposta da requisição é processada, separando cada cotação de moeda e armazenando em arquivos individuais no formato Parquet, facilitando a organização e recuperação dos dados.
- Carregamento: Os arquivos Parquet individuais são consolidados em um único dataset utilizando um Jupyter Notebook, permitindo uma análise abrangente e insights valiosos sobre as cotações de moedas.

Em resumo, o "Awesome Project: ETL Process for Currency Quotes Data" oferece uma solução robusta e eficiente para coleta, processamento e análise de dados de cotações de moedas, utilizando técnicas avançadas de arquitetura e paralelismo para otimizar cada etapa do processo ETL.

  <details>
    <summary>Estrutura do repositório</summary>

- [`data/`](https://github.com/IvanildoBarauna/ETL-awesome-api/tree/main/data): Armazena dados brutos no formato Parquet.
  - ETH-EUR-1713658884.parquet: Exemplo: Dados brutos para cotações ETH-EUR. nome_do_arquivo = símbolo + timestamp unix da extração
- [`notebooks/`](https://github.com/IvanildoBarauna/ETL-awesome-api/tree/main/notebooks): Contém o notebook `data_explorer.ipynb` para exploração de dados.
- [`etl/`](https://github.com/IvanildoBarauna/ETL-awesome-api/tree/main/etl): Contém o código-fonte do projeto.
  - [`run.py`](https://github.com/IvanildoBarauna/ETL-awesome-api/blob/main/etl/run.py): Entrypoint da aplicação
  - [`common/`](https://github.com/IvanildoBarauna/ETL-awesome-api/tree/main/etl/common): Biblioteca para reutilização e padronização de código.
    - [`utils/`](https://github.com/IvanildoBarauna/ETL-awesome-api/tree/main/etl/utils)
      - [`logs.py`](https://github.com/IvanildoBarauna/ETL-awesome-api/blob/main/etl/utils/logs.py): Pacote para gerenciamento de logs.
      - [`common.py`](https://github.com/IvanildoBarauna/ETL-awesome-api/blob/main/etl/utils/common.py): Pacote para tarefas comuns no código como recuperação de diretório de saída ou timestamp default.
    - [`logs/`](https://github.com/IvanildoBarauna/ETL-awesome-api/tree/main/etl/common/logs): Para armazenamento de logs de debug.
  - [`controller/`](https://github.com/IvanildoBarauna/ETL-awesome-api/tree/main/etl/controller)
    - [`pipeline.py`](https://github.com/IvanildoBarauna/ETL-awesome-api/blob/main/etl/controller/pipeline.py): Recebe requisições de extração de dados e orquestra os modelos de ETL.
  - [`models/`](https://github.com/IvanildoBarauna/ETL-awesome-api/tree/main/etl/models):
    - [`extract/`](https://github.com/IvanildoBarauna/ETL-awesome-api/tree/main/etl/models/extract)
      - [`api_data_extractor.py`](https://github.com/IvanildoBarauna/ETL-awesome-api/blob/main/etl/models/extract/api_data_extractor.py): Recebe os parâmetros do controller envia a requisição e retorna em JSON.
    - [`transform/`](https://github.com/IvanildoBarauna/ETL-awesome-api/tree/main/etl/models/transform)
      - [`publisher.py`](https://github.com/IvanildoBarauna/ETL-awesome-api/blob/main/etl/models/extract/publisher.py): Recebe o JSON do extrator, separa o dicionário por moeda e publica cada um deles para uma fila pra serem processados individualmente.
    - [`load/`](https://github.com/IvanildoBarauna/ETL-awesome-api/tree/main/etl/models/load)
      - [`parquet_loader.py`](https://github.com/IvanildoBarauna/ETL-awesome-api/blob/main/etl/models/extract/parquet_loader.py): Em uma thread separada, recebe um novo dicionário da fila que o transformer está publicando e gera arquivos .parquet no diretório padrão.
  - [`views/`](https://github.com/IvanildoBarauna/ETL-awesome-api/tree/main/etl/views): Para armazenamento de análise de dados e visualização.

</details>

<details>
  <summary>Como executar a aplicação localmente</summary>
  
  ## Step by Step
  1. Clone the repository:
     ```sh
     $ git clone https://github.com/IvanildoBarauna/ETL-awesome-api.git
     ```

<details> 
  <summary>Usando virtual enviroment (Python Nativo)</summary>
    Garanta que o Python 3.9 ou superior esteja instalado em sua máquina

```sh
$ cd ETL-awesome-api
$ python -m venv .venv
$ source .venv/bin/activate  # On Windows use `venv\Scripts\activate`
$ .venv/bin/python -m pip install --upgrade pip
$ pip install -e .
$ python etl/run.py
```

Learn more about [venv module in python](https://docs.python.org/pt-br/3/library/venv.html)

  </details>

  <details> 
    <summary>Usando Docker</summary>
    Garanta que o Docker esteja instalado em sua máquina

[`Dockerfile`](https://github.com/IvanildoBarauna/ETL-awesome-api/tree/main/Dockerfile)

```sh
$ docker build -t etl-awesome-api . && docker run etl-awesome-api
```

Ou:

[`docker-compose`](https://github.com/IvanildoBarauna/ETL-awesome-api/tree/main/docker-compose.yml)

```sh
$ docker-compose up --build
```

Saiba mais sobre [docker](https://docs.docker.com/)

</details>

- Ou use o Poetry

  ```sh
  $ poetry install && poetry run python etl/run.py
  ```

  Saiba mais sobre [`poetry`](https://python-poetry.org/)

</details>

## ETL and Data Analysis Results:

You can see the complete data analysis, the Jupyter Notebook is deployed in [GitHub Pages](https://ivanildobarauna.github.io/ETL-awesome-api/)
