
START_MESSAGE = "Привет!. Я умею обрабатывать звуковые файлы в формате wav. Список команд\n\n" \
                "/reverb - Добавление реверберации в аудиозапись\n " \
                "<насыщеннность звука от 0 до 100, затухание низких частот от 0 до 100, размер помещения от 0 до 100, глубина стереоэффекта от 0 до 100, задержка перед реверберацией в милисекундах, уровень громкости реверберации от 0 до 10>\n\n" \
                "/speed - Изменение скорости аудиозаписи с воздействием на высоты\n" \
                "<множитель, на который надо ускорить аудиозапись>\n\n" \
                "/normalize - Нормализация аудиозаписи\n\n" \
                "/pitch - Изменение тональности в аудиозаписи\n" \
                "<количество полутонов>\n\n" \
                "/bandpass- Удаление шумов и прочих нежелательных звуков в записи\n" \
                "<частота среза фильтра в Гц, ширина полосы пропускания>\n\n" \
                "/tempo - Изменение скорости проигрывания аудиофайла без изменения его высоты\n" \
                "<множитель, на который надо ускорить аудиозапись>"

WARNING_MESSAGE = "Некорректное сообщение. Для начала пришли мне аудиофайл, который нужно обработать."

TOKEN = 'put your Token here'
