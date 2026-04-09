# 🚗 Car Plate API (Web Scraping)

![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)
![Flask](https://img.shields.io/badge/flask-%23000.svg?style=for-the-badge&logo=flask&logoColor=white)
![Status](https://img.shields.io/badge/Status-Em%20Produção-green?style=for-the-badge)

Esta API realiza o **Web Scraping** de dados automotivos e valores da Tabela FIPE em tempo real. Ela recebe uma placa, processa a requisição utilizando um scraper avançado (capaz de contornar proteções de bots) e devolve um objeto JSON estruturado.

---

## 🛠️ Tecnologias e Bibliotecas

* **Flask**: Micro-framework para construção das rotas e servidor web.
* **Cloudscraper**: Utilizado para realizar as requisições burlando proteções de serviços como Cloudflare.
* **BeautifulSoup4**: Responsável pelo parseamento do HTML e extração precisa dos dados.
* **Requests**: Para chamadas HTTP.

---

## 🚀 Como integrar no Front-end

A API é extremamente simples de consumir. O ponto principal é como você envia os dados através do formulário ou requisição.

### ⚠️ Regra de Integração (Input Name)
Para que a API capture a placa corretamente, o seu campo de entrada de texto **DEVE** ter o atributo `name="p"`. É através deste identificador que o Flask processa a busca na URL.

#### Exemplo de Formulário HTML:
```html
<form method="get" action="/search">
    <input type="text" name="p" placeholder="DIGITE A PLACA" required>
    <button type="submit">BUSCAR</button>
</form>
````
## 🔌 Endpoints

### `GET /search`

**Parâmetros de Query:**

| Parâmetro | Tipo | Descrição |
| :--- | :--- | :--- |
| `p` | `string` | **Obrigatório.** A placa do veículo (sem espaços ou traços). |

**Exemplo de Chamada:**
`GET http://localhost:5000/search?p=BRA2E19`

**Resposta de Sucesso (200 OK):**
```json
{
  "data": {
    "Marca": "Toyota",
    "Modelo": "Corolla Altis 2.0 Flex",
    "Ano": "2023",
    "Cor": "Branco",
    "Cidade": "São Paulo - SP"
  }
}
````
{
  "data": {
    "Marca": "Volkswagen",
    "Modelo": "GOL 1.0 Flex 12V 5p",
    "Ano Modelo": "2023",
    "Valor FIPE": "R$ 58.450,00",
    "Combustível": "Gasolina"
  }
}

## 🏗️ Estrutura do Projeto

* `main.py`: Gerenciamento de rotas e inicialização do servidor Flask.
* `api_plate.py`: Módulo de scraping (BeautifulSoup + Cloudscraper).
* `templates/`: Pasta contendo a interface front-end da aplicação.

## 📦 Instalação e Uso

1. **Clone o repositório:**
   ```bash
   git clone [https://github.com/nielskii/nome-do-seu-repositorio](https://github.com/nielskii/nome-do-seu-repositorio)
   
2. **Instale as dependências**
   ```
   pip install flask cloudscraper beautifulsoup4 requests
   ````
3. **Inicie o servidor**
   ```
    python main.py
   ```
