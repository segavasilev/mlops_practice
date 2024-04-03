# Скрипт последовательно запускает все py-файлы из папки lab1
# В консоль выводится результат выполнения каждого скрипта и его код завершения

# Список скриптов в порядке их выполнения
# shellcheck disable=SC2054
scripts=(lab1/data_creation.py, lab1/model_preprocessing.py, lab1/model_preparation.py, lab1/model_testing.py)

# Запуск всех скриптов
# shellcheck disable=SC2068
for script in ${scripts[@]}; do
    python3 "$script"
done