# Sistema de Estação Meteorológica IoT - Rafael Cabral

## Descrição

Este projeto implementa um sistema completo de Internet das Coisas (IoT) para simulação de uma estação meteorológica. A aplicação é composta por um backend em Flask, um banco de dados SQLite e uma interface web para visualização e gerenciamento das leituras.

Os dados de temperatura e umidade foram simulados utilizando o script `serial_reader.py`, substituindo temporariamente o uso de hardware físico (Arduino e sensores). Essa decisão foi tomada para garantir o funcionamento completo do sistema mesmo sem dispositivos físicos disponíveis. Apesar disso, o código INO foi desenvolvido apenas para validação de conhecimento sobre hardware, a maior alteração foi a troca de `delay()` por uma regra de negócio usando `millis()` que torna o hardware mais eficiente, sem pausar o sistema causando perda de dados;

---

## Tecnologias Utilizadas

* Python 3
* Flask
* SQLite
* HTML, CSS e JavaScript
* Chart.js

---

## Estrutura do Projeto

```
projeto/
├── firmware/
│   └── hardware.ino
│    
├── src/
│   ├── app.py
│   ├── database.py
│   ├── serial_reader.py
│   ├── schema.sql
│   ├── dados.db
│   ├── templates/
│   │   ├── base.html
│   │   ├── editar.html
│   │   ├── historico.html
│   │   └── index.html
│   └── statics/
│       └── css/
│           └──style.css
│  
├── requirements.txt
└── README.md
```

---

## Instalação

### 1. Clonar o repositório

```
git clone https://github.com/Cabral-rcs/ponderada_IOT_estacao_meteorologica.git
```

### 2. Criar ambiente virtual

```
python -m venv venv
```

### 3. Ativar o ambiente virtual

Windows:

```
venv\Scripts\activate
```

Linux/Mac:

```
source venv/bin/activate
```

### 4. Instalar dependências

```
pip install -r requirements.txt
```

---

## Execução do Projeto

### 1. Iniciar o servidor Flask

Dentro da pasta `src`:

```
python app.py
```

O servidor estará disponível em:

```
http://127.0.0.1:5000
```

---

### 2. Gerar dados simulados

Em outro terminal, também dentro da pasta `src`:

```
python serial_reader.py
```

Esse script simula um dispositivo físico enviando leituras de temperatura e umidade para a API a cada poucos segundos.

---

## Banco de Dados

O banco de dados utilizado é o SQLite, armazenado no arquivo:

```
dados.db
```

A tabela principal é `leituras`, contendo:

* id
* temperatura
* umidade
* pressao (opcional)
* localizacao
* timestamp

O arquivo já é entregue com mais de 30 leituras conforme exigido.

---

## Rotas da API

### GET /

Exibe o painel principal com as últimas leituras.

---

### GET /leituras

Exibe o histórico completo das leituras em formato de tabela.

---

### POST /leituras

Recebe dados no formato JSON e insere uma nova leitura no banco.

Exemplo de corpo da requisição:

```
{
  "temperatura": 25.5,
  "umidade": 60
}
```

---

### GET /leituras/<id>

Retorna a página de edição de uma leitura específica.

---

### PUT /leituras/<id>

Atualiza os valores de temperatura e umidade de uma leitura.

---

### DELETE /leituras/<id>

Remove uma leitura do banco de dados.

---

### GET /api/leituras

Retorna todas as leituras em formato JSON.

---

### GET /api/estatisticas

Retorna estatísticas das leituras:

* média de temperatura
* temperatura mínima
* temperatura máxima
* média de umidade

---

## Observações

* O projeto foi desenvolvido seguindo uma arquitetura simples de três camadas: simulação de dados, backend e interface web.
* A simulação substitui o Arduino, mas a estrutura permite integração futura com hardware real.
* O banco SQLite foi configurado para suportar múltiplas escritas utilizando o modo WAL.

---

## Conclusão

O sistema implementa um fluxo completo de coleta, armazenamento e visualização de dados, atendendo aos requisitos propostos para uma aplicação IoT com API REST, banco de dados relacional e interface web.
