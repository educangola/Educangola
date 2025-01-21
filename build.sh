#!/bin/bash

# Atualiza os pacotes do sistema (opcional, dependendo do seu sistema)
echo "Atualizando pacotes do sistema..."
sudo apt-get update

# Ativa o ambiente virtual (ajuste o caminho conforme necessário)
echo "Ativando o ambiente virtual..."
source venv/bin/activate  # Se estiver usando ambiente virtual

# Instala todas as dependências do requirements.txt
echo "Instalando dependências..."
pip install -r requirements.txt

# Verifique se o processo foi bem-sucedido
if [ $? -eq 0 ]; then
    echo "Dependências instaladas com sucesso!"
else
    echo "Houve um erro durante a instalação."
    exit 1
fi
