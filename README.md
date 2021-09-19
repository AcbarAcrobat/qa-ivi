# qa-ivi

Первым делом нужно переименовать файл ``.secrets-example.toml`` в ``.secrets.toml`` и заменить значения на реальных пользователей

## Скопируйте проект

```sh
$ git clone  https://github.com/AcbarAcrobat/qa-ivi.git
```

## Установите poetry
```sh
$ https://python-poetry.org/docs/#osx--linux--bashonwindows-install-instructions
```

# Поставте необходимые зависимости
```sh
$ poetry install
```

# Активируйте окружение для тестов
```sh
$ poetry shell
```

## Запуск тестов
```sh
$ pytest # all
```

## Установите аллюр 
Install [Allure](https://github.com/allure-framework/allure2/releases)

После выполнения всех тестов:
```sh
$ allure serve allure_dir
```
