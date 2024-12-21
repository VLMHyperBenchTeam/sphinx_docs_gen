# Описание

Проект содержит `Docker`-образ для генерации документации из `markdown` файлов в виде:
* статического html-сайта
* pdf-файла документации

с помощью `Sphinx`(https://www.sphinx-doc.org/en/master/index.html).

# Компоненты документации Sphinx

## Создаем проект Sphinx:

Если в проекте еще не инциализирован проект Sphinx, то переходим в корневую папку нашего репозитория и выполняем команду:
   
```bash
sphinx-quickstart
```

Следуем инструкциям, чтобы настроить базовый проект Sphinx.

## Оглавление документации

Sphinx-документация представляет собой книгу.

У данной книги есть оглавление указанное в файле:
```
source/index.md
```

* у pdf - документации данный файл задает оглавление
* для html-сайта он задает его `home page`

## Настройки генерации документации

Настройки генерации документации представлены в файле:
```
source/conf.py
```

# Docker образ для локальной сборки документации

Docker-образ опубликован на `GitHub Packages Container Registry` ([ссылка](https://github.com/orgs/VLMHyperBenchTeam/packages/container/package/sphinx_docs_gen)).

## Запуск генерации статичного сайта и pdf c документацией

Команды для запуска генерации статичного html-сайта и pdf-документации будут автоматически выполнены при запуске Docker-контейнера:

* Linux / MacOs
```
docker run -it --rm -v $(pwd):/workspace ghcr.io/vlmhyperbenchteam/sphinx_docs_gen:0.1.0
```

* Windows (CMD)
```
docker run -it --rm -v %cd%:/workspace ghcr.io/vlmhyperbenchteam/sphinx_docs_gen:0.1.0
```

* Windows (PowerShell)
```
docker run -it --rm -v ${PWD}:/workspace ghcr.io/vlmhyperbenchteam/sphinx_docs_gen:0.1.0
```

После запуска контейнера документация будет располагаться:
* `build/html` для статичного сайта
* `build/latex` для pdf-документации

## Запуск Docker Container

Бывает полезно произвести отладку генерации документации.

Для этого можно запустить `Docker`-контейнер с выполнением команды запуска терминала:

* Linux / MacOs
```
docker run -it -v $(pwd):/workspace ghcr.io/vlmhyperbenchteam/sphinx_docs_gen:0.1.0 sh
```

* Windows (CMD)
```
docker run -it -v %cd%:/workspace ghcr.io/vlmhyperbenchteam/sphinx_docs_gen:0.1.0 sh
```

* Windows (PowerShell)
```
docker run -it -v $(PWD):/workspace ghcr.io/vlmhyperbenchteam/sphinx_docs_gen:0.1.0 sh
```

После этого можно выполнять в терминале Docker-контейнера команды:

* для очистки результатов генерации:
```
make clean
```

* для генерации статичного сайта из html:
```
make html
```

* для генерации документации в виде pdf:
```
make latexpdf
```

## Build Docker image

Для сборки Docker image выполним команду:
```
docker build -t ghcr.io/vlmhyperbenchteam/sphinx_docs_gen:0.1.0 -f docker/Dockerfile .
```