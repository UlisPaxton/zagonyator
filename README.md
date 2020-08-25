# zagonyator. Набор утилит для быстрого и удобного ввода windows-ПК в Windows-Домен.
Как это работает? Сервер является web-api для вызова утилиты DJOIN и передаёт ей имя ПК, введённое на клиенте. Утилита DJOIN формирует файл ответа для офлайн ввода ПК в домен и отдаёт на скачивание клиенту.
Клиент размещает этот файл в C:\temp\temp.invite. Однако, имеются проблемы с запуском DJOIN из клиента и потому это было вынесенно в start_client.bat. После завершения работы клиента следует перезагрузить комп, он будет присоединён к домену и переименован.


# Server, установка
1)Скопируйте папку server на контроллер домена. Можно скопировать только файл server.py если на котроллере установлен python3.8+. Если нет - используйте portable python.  
2)Установите библиотеку cherrypy - pip3 install cherrypy.  
3)Запустите выполнение файла server.py  

# client
1)Файлы client.exe/client.py и start_client.bat скопируйте на флешку.  
2)После запуска client.exe укажите ip/FQDN контроллера домена, укажите имя домена и укажите имя ПК под которым его следует ввести в домен.  
3)При успешном завершении клиент закроется. Запустите ОТ ИМЕНИ АДМИНИСТРАТОРА файл start_client.bat
4)Перезагрузите ПК.

# Возможные проблемы:
1)Клиент: недоступность контроллера домена.  
2)Клиент: выдаёт виндовое окно с ошибкой - установите свежий Visual C++ redistributable.  

На сервере проблем не наблюдал ни разу, полтора месяца с portable python - полёт нормальный.
# Замечания:
1)Отсутствие https. Это не критично поскольку подразумевается доверенный сетевой сегмент.  
2)Отсутсвие проверки подлинности клиента. По идее можно сделать доп. 2 параметра аналогичных логину и паролю, но микрософт всё равно сделал клиентский ввод пк в домен и такие меры теряют смысл.  

