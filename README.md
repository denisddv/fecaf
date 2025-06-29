# Captador de Temperatura de São Paulo

Projeto acadêmico que automatiza a coleta de **temperatura** e **umidade do ar** na cidade de São Paulo.

## Tecnologias

- **Python 3.11+**
- **Selenium** para navegação e scraping.
- **openpyxl** para leitura/escrita em Excel.
- **Tkinter** para interface gráfica.

## Como executar

1. Instale as dependências:

```bash
pip install -r requirements.txt
```

2. Baixe o **chromedriver** compatível com sua versão do Chrome e coloque na pasta `driver/` ou defina a variável de ambiente `PATH` para incluí‑lo.

3. Rode o aplicativo:

```bash
python main.py
```

Cada clique em **Buscar Previsão**:
- Abre o site Climatempo (modo headless).
- Captura temperatura e umidade atuais.
- Salva a informação em `temperatura.xlsx` (criando o arquivo se necessário).

Fluxograma do funcionamento disponível em `fluxograma.pdf`.
