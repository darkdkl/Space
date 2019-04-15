### Загрузка изображений SpaceX и Телескопа Hubble с последующей публикацией в Instagram



#### Описание :
* Программа использует API SpaceX  и API Hubble для загрузки изображений и 
instabot для публикаций изображений в Instagram.

######  API SpaceX 

* по умолчанию загружаются изображения 76го запуска ракеты SpaceX 
Вы можете изменить номер запуска :
модуль <b>fetch_spacex.py</b> переменная <b>launch='76'</b>( от 1го запуска до текущего) 
см. значение ключа <b>"flight_number":</b> по адресу:
``` 
https://api.spacexdata.com/v3/launches

```

* Необходимо обратить внимание,что фотографии последнего запуска размещаются не сразу.


###### API Hubble:
* По умолчанию загружаются изображения из коллекции 'wallpaper'
Вы можете изменить название коллекции:
модуль <b>fetch_hubble.py</b>,переменная <b>collection ='wallpaper'</b>
несколько имен текущих коллекций :<b>'news', 'spacecraft', 'printshop' </b>
#### Установка
* Python3 должен быть уже установлен. Затем используйте pip (или pip3, есть конфликт с Python2) для установки зависимостей: 
```
pip3 install -r requirements.txt
```
#### Запуск программы:
* Программа может запускаться в двух режимах: из среды разработки и из коммандной строки
Если запуск программы будет производится из среды разработки необходимо создать
в каталоге с программой файл .env и указать данные от учетной записи Instagram:
```
LOGIN="User" 
PASSWORD="Password"
```
* При запуске из коммандной строки ,
программа предложит ввести имя пользователя и пароль от учетной записи Instagram с последующей возможностью выбора данной учетной записи либо создания новой

```
$python3 main.py
загрузка файла с именем: 4001 ,пожалуйста подождите...
2019-04-14 23:29:59,798 - INFO - Instabot Started
We need to create a text file 'secret.txt' where we will store your login and password from Instagram.
Don't worry. It will be stored locally.
Enter your login: 
user
Enter your password: 
Password: 
Do you want to add another account? (y/n)
n
Which account do you want to use? (Type number)
1: user
0: add another account.
-1: delete all accounts.
2019-04-14 23:31:43,938 - INFO - Logged-in successfully as 'user'!
Начинаем выгрузку файлов в Instagram  ,пожалуйста подождите...

Analizing `./images/spacex5.jpg`
FOUND w:4465, h:2976, ratio=1.5003360215053763
Horizontal image
Resizing image
Saving new image w:1080 h:720 to `./images/spacex5.jpg.CONVERTED.jpg`
FOUND: w:1080 h:720 r:1.5
2019-04-14 23:31:59,727 - INFO - Photo './images/spacex5.jpg' is uploaded.
....

2019-04-14 23:35:25,675 - INFO - Bot stopped. Worked: 12:05:58.537401
2019-04-14 23:35:25,676 - INFO - Total requests: 70

```
### Цель проекта
* Код написан в образовательных целях на онлайн-курсе для веб-разработчиков dvmn.org.


##### Dark_Dmake
2019