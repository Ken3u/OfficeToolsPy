#!/bin/bash

# Удаление файла предыдущей версии дополнения
rm OfficeTools.oxt
# Переход в директорию с файлами дополнения
pushd OfficeTools
# Упаковка файлов дополнения в архив формата zip с расширением .oxt
zip -r ../OfficeTools.oxt *
# Возврат в ранее установленную рабочую директорию
popd