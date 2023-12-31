# Mobile-App-API
API for a mobile application in which the customer's field employee will perform visits to stores.

+ User: admin
+ Password: admin

ТЗ:
-----

Создать простое API для мобильного приложения, в котором полевой сотрудник заказчика будет выполнять визиты в магазины.
Создать сущности

1. "Работник", с полями:

○ имя – char 255

○ номер телефона – char 255

2. "Торговая точка"

○ название

○ ForeignKey к "Работник" (обязательно к заполнению)

3. "Посещение"

○ дата/время

○ ForeignKey к "Торговая точка"

○ latitude – float

○ longitude – float

Сделать методы:

Для упрощения задания, вместо полноценной авторизации передавать в каждый запрос номер телефона Работника.

1. получить список Торговых точек привязанных к переданному номеру телефона

○ в ответе список Торговых точек:

■ PK

○ Название

2. выполнить посещение в Торговую точку

○ принимает:

■ PK Торговой точки

■ координаты

○ в ответе:

■ PK Посещения

■ Дата/время

○ проверять, что переданный номер телефона Работника привязан к указанной ТТ, в противном случае возвращать ошибку

○ при создании Посещения в дата/время сохранить текущие дату/время

Админка:

● Работник

○ создание

○ редактирование

○ удаление

○ поиск по имени

● Торговая точка

○ создание

○ редактирование

○ удаление

○ поиск по названию

● Посещение

○ просмотр

○ поиск по имени Работника

○ поиск по названию Торговой точки


# Tests:

Тесты для API сервиса для управления данными о магазинах, работниках и посещениях.

● В классе StoreAPITestCase определены тесты для создания, получения, обновления и удаления магазинов.

  В методе setUp() создаются объекты Worker и Store, которые используются в тестах. 
  В методе test_create_store() проверяется, что при отправке POST-запроса на URL /stores/ с данными о новом магазине, сервис возвращает статус 201 Created и создает новый объект Store в базе данных.
  В методе test_retrieve_store() проверяется, что при отправке GET-запроса на URL /stores/<store_id>/ сервис возвращает данные о магазине с указанным идентификатором.
  В методе test_update_store() проверяется, что при отправке PUT-запроса на URL /stores/<store_id>/ с данными о магазине, сервис возвращает статус 200 OK и обновляет данные о магазине в базе данных.
  В методе test_delete_store() проверяется, что при отправке DELETE-запроса на URL /stores/<store_id>/ сервис возвращает статус 204 No Content и удаляет объект Store из базы данных.

● В классе VisitAPITestCase определены тесты для просмотра и поиска посещений.

  В методе setUp() создаются объекты Worker, Store и Visit, которые используются в тестах.
  В методе test_list_visits() проверяется, что при отправке GET-запроса на URL /visits/ сервис возвращает список всех посещений.
  В методе test_filter_visits_by_worker_name() проверяется, что при отправке GET-запроса на URL /visits/?worker_name=<worker_name> сервис возвращает список посещений, связанных с указанным работником.
  В методе test_filter_visits_by_store_name() проверяется, что при отправке GET-запроса на URL /visits/?store_name=<store_name> сервис возвращает список посещений, связанных с указанным магазином.

● В классе VisitAPITestCase определены тесты для создания, получения, обновления и удаления посещений.

  В методе setUp() создаются объекты Worker, Store и Visit, которые используются в тестах.
  В методе test_create_visit() проверяется, что при отправке POST-запроса на URL /visits/ с данными о новом посещении, сервис возвращает статус 201 Created и создает новый объект Visit в базе данных.
  В методе test_retrieve_visit() проверяется, что при отправке GET-запроса на URL /visits/<visit_id>/ сервис возвращает данные о посещении с указанным идентификатором.
  В методе test_update_visit() проверяется, что при отправке PUT-запроса на URL /visits/<visit_id>/ с данными о посещении, сервис возвращает статус 200 OK и обновляет данные о посещении в базе данных.
  В методе test_delete_visit() проверяется, что при отправке DELETE-запроса на URL /visits/<visit_id>/ сервис возвращает статус 204 No Content и удаляет объект Visit из базы данных.
