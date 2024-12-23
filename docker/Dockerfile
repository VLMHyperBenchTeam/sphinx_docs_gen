# Используем базовый образ Python 3.10
FROM python:3.10

# Устанавливаем LaTeX и необходимые пакеты, включая XeLaTeX
RUN apt-get update && apt-get install -y \
    texlive-xetex \
    texlive-latex-extra \
    texlive-fonts-recommended \
    texlive-lang-cyrillic \
    latexmk \
    fonts-dejavu \
    fonts-freefont-otf \
    && rm -rf /var/lib/apt/lists/*

# обновляем кэш шрифтов, чтобы XeLaTeX их увидел.
RUN fc-cache -fv

# Копируем файл pyproject.toml и poetry.lock
COPY pyproject.toml poetry.lock* ./

# Устанавливаем poetry напрямую в системный python
RUN pip install poetry
RUN poetry config virtualenvs.create false

# Устанавливаем зависимости с помощью Poetry
RUN poetry install --no-dev --no-interaction --no-ansi --no-root
RUN rm pyproject.toml poetry.lock*

# Создаем рабочую директорию
WORKDIR /workspace

# Указываем команду по умолчанию
CMD ["sh", "-c", "make clean && make html && make latexpdf"]