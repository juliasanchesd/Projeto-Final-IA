import numpy as np
from sentence_transformers import SentenceTransformer
from jinja2 import Template

model = SentenceTransformer("all-MiniLM-L6-v2")

jobs = [
    "Desenvolvedor Frontend",
    "Desenvolvedor Backend",
    "Desenvolvedor Fullstack",
    "Desenvolvedor Mobile Android",
    "Desenvolvedor Mobile iOS",
    "Engenheiro de Software",
    "Engenheiro de Dados",
    "Cientista de Dados",
    "Analista de Dados",
    "Analista de Business Intelligence",
    "Analista de Suporte Técnico",
    "Analista de Infraestrutura",
    "Administrador de Sistemas",
    "Administrador de Redes",
    "Analista de Segurança da Informação",
    "Engenheiro de Segurança da Informação",
    "DevOps Engineer",
    "Site Reliability Engineer",
    "Product Owner",
    "Product Manager em TI",
    "Scrum Master",
    "QA Tester",
    "Analista de Qualidade de Software",
    "Automação de Testes",
    "Designer UX/UI",
    "Arquiteto de Software",
    "Arquiteto de Soluções",
    "Desenvolvedor Python",
    "Desenvolvedor Java",
    "Desenvolvedor JavaScript",
    "Desenvolvedor Node.js",
    "Desenvolvedor React",
    "Desenvolvedor .NET",
    "Desenvolvedor PHP"
]

embeddings = model.encode(jobs)
THRESHOLD = 0.55

OUTPUT_TEMPLATE = Template("""
Encontrei {{ vagas|length }} vaga{{ 's' if vagas|length > 1 else '' }} compatíve{{ 'is' if vagas|length > 1 else 'l' }} com o seu perfil:<br><br>

{% for vaga, similaridade in vagas %}
<div class="job-card">
  <strong>{{ vaga }}</strong><br>
  <span class="compat">Compatibilidade: {{ similaridade }}%</span>
</div>
<br>
{% endfor %}
""".strip())

def find_jobs(user_cv, embeddings=embeddings, jobs=jobs):
    target_embedding = model.encode(user_cv)
    similarities = model.similarity(target_embedding, embeddings)[0]

    matches = [
        (jobs[idx], round(100 * similarities[idx].item(), 2))
        for idx in np.argsort(-similarities)
        if similarities[idx] > THRESHOLD
    ]

    if matches:
        return OUTPUT_TEMPLATE.render(vagas=matches)

    return "Que pena! Não há vagas compatíveis no momento."
