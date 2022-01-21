# projeto-pcti
# Instalar Python
# Configurar variáveis de ambiente adicionando no Path o caminho de onde está o Python instalado e a tambpem da pasta Script
# Set no Powershell (Set-ExecutionPolicy Unrestricted)
# Instalar Pycharm
# Instalar Git
# Clone projeto do GitHUB

# No powersehll
python -m venv venv
.\venv\Scripts\activate
pip install --upgrade pip --user
pip install --upgrade virtualenv 
pip install --upgrade virtualenvwrapper-win
pip install django
pip install django-crispy-forms
pip install django-braces

Config Server in paycharm
Interpretador
Varialveis de desenvolvimento: PYTHONUNBUFFERED=1;DJANGO_SETTINGS_MODULE=pcti.settings