# Цель проекта #
Организовать просмотр видеоконтента на ПК (x32/x64) с управлением через пульт


# pyWink #
Client app for Wink service RT

Клиент для Wink написан на python.
Используем Kivy, ffpyplayer

## Решено ##

* Парсинг JS из главной страницы
* Получения плейлиста из сервиса
* Опреденление url адреса медиапотока
 
## Текущие проблемы ##

* Решить вопрос с HLS шифрованием
* Оформить интерфейс

## Метод авторизации ##
На текущем этапе авторизация происходит через передачу параметров Cookie  

# ENGLISH LANG #

The client for Wink is written in python.
Using Kivy, ffpyplayer

## Solved ##

* Parsing JS from home page
* Retrieving a playlist from the service
* Determining the url of the media stream
 
## Current issues ##

* Solve the issue with HLS encryption
* Design interface

## Authorization method ##
At the current stage, authorization occurs through the transfer of Cookie parameters


# Install and settings  #

На текущий момент прописываем параметр `COOKIE` для авторизации в wink.rt.ru
Как сделаю форму авторизации, так исправлю этот документ  
