# Agente de Recomendação de Vagas com Similaridade Semântica

Este projeto implementa um agente de Inteligência Artificial que utiliza busca semântica baseada em embeddings para recomendar vagas da área de Tecnologia da Informação.
O sistema converte o texto digitado pelo usuário e as descrições das vagas em vetores numéricos e calcula a similaridade do cosseno entre eles.
A partir dessa comparação vetorial, o agente identifica e retorna as vagas cujo significado apresenta maior proximidade com o perfil informado.

---

## Objetivo

O objetivo do projeto é demonstrar como técnicas de IA podem ser usadas para comparar textos de forma semântica, permitindo que o sistema identifique vagas compatíveis mesmo quando o usuário não utiliza exatamente os mesmos termos presentes na lista de vagas.

---

## Como o Sistema Funciona

1. O usuário descreve seu perfil profissional em texto livre.  
2. O sistema converte o texto do usuário e todas as vagas cadastradas em **vetores (embeddings)** usando o modelo `all-MiniLM-L6-v2`.  
3. Para cada vaga, é calculada a **similaridade do cosseno** entre o vetor da vaga e o vetor do usuário.  
4. As vagas com similaridade acima do limite definido são consideradas compatíveis.  
5. O resultado é ordenado e retornado ao usuário em formato de mensagem.

Este processo caracteriza uma **busca semântica**, pois a comparação é feita pelo significado do texto, e não apenas pelas palavras exatas.

---

## Tecnologias Utilizadas

- **Python 3.x**  
- **Flask** (API e interface web)  
- **SentenceTransformers**  
- **NumPy**  
- **HTML / CSS / JavaScript**

---

## Estrutura do Projeto

/projeto
│
├── app.py                # Aplicação Flask e rota da API
├── agent.py              # Lógica de recomendação e cálculo de similaridade
│
├── templates/
│   └── index.html        # Interface web estilo chat
│
└── static/
    └── style.css         # Arquivo de estilos da interface

---

## Instalação e Execução

### 1. Criar ambiente virtual

```bash
python -m venv venv
source venv/Scripts/activate   # Windows (Git Bash)
```

### 2. Instalar dependências  
Instale manualmente as bibliotecas utilizadas no projeto:

```bash
pip install flask
pip install sentence-transformers
pip install numpy
```

### 3. Executar aplicação

```bash
python app.py
```
