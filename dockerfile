# Dockerfile pour la documentation Django avec Coolify
FROM python:3.11-slim

# Variables d'environnement
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1
ENV DEBIAN_FRONTEND=noninteractive

WORKDIR /app

# Installer les dépendances système
RUN apt-get update && apt-get install -y \
    build-essential \
    curl \
    && rm -rf /var/lib/apt/lists/*

# Installer les dépendances Python
COPY pyproject.toml ./
RUN pip install --no-cache-dir --upgrade pip && \
    pip install --no-cache-dir Django>=4.2,<6.0 django-cotton>=0.9.0 gunicorn

# Copier le code source
COPY . .

# Installer le package en développement
RUN pip install -e .

# Définir le répertoire de travail pour Django
WORKDIR /app/documentation

# Collecter les fichiers statiques
RUN python manage.py collectstatic --noinput

# Exposer le port 8000
EXPOSE 8000

# Commande de lancement avec gunicorn
CMD ["gunicorn", "documentation.wsgi:application", "--bind", "0.0.0.0:8000", "--workers", "3", "--timeout", "60"]