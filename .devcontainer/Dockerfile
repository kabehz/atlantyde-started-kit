FROM python:3.10-slim

# Herramientas esenciales
RUN apt-get update && apt-get install -y make curl git && \
    pip install --no-cache-dir mkdocs mkdocs-material

# Instalar CodeQL CLI
RUN curl -sSL https://github.com/github/codeql-cli-binaries/releases/latest/download/codeql-linux64.zip -o codeql.zip && \
    apt-get install -y unzip && \
    unzip codeql.zip -d /opt && rm codeql.zip && \
    ln -s /opt/codeql/codeql /usr/local/bin/codeql

# Instalar OPA
RUN curl -L -o /usr/local/bin/opa https://openpolicyagent.org/downloads/latest/opa_linux_amd64 && \
    chmod +x /usr/local/bin/opa
