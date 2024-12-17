'''
Создайте новое приложение FastAPI и сделайте CRUD запросы.
Создайте словарь users = {'1': 'Имя: Example, возраст: 18'}
Реализуйте 4 CRUD запроса:
get запрос по маршруту '/users', который возвращает словарь users.
post запрос по маршруту '/user/{username}/{age}', который добавляет в словарь по максимальному по значению ключом значение строки "Имя: {username}, возраст: {age}". И возвращает строку "User <user_id> is registered".
put запрос по маршруту '/user/{user_id}/{username}/{age}', который обновляет значение из словаря users под ключом user_id на строку "Имя: {username}, возраст: {age}". И возвращает строку "The user <user_id> is updated"
delete запрос по маршруту '/user/{user_id}', который удаляет из словаря users по ключу user_id пару.
Выполните каждый из этих запросов по порядку. Ответы должны совпадать:
1. GET '/users'
{
"1": "Имя: Example, возраст: 18"
}
2. POST '/user/{username}/{age}' # username - UrbanUser, age - 24
"User 2 is registered"
3. POST '/user/{username}/{age}' # username - NewUser, age - 22
"User 3 is registered"
4. PUT '/user/{user_id}/{username}/{age}' # user_id - 1, username - UrbanProfi, age - 28
"User 1 has been updated"
5. DELETE '/user/{user_id}' # user_id - 2
"User 2 has been deleted"
6. GET '/users'
{
"1": "Имя: UrbanProfi, возраст: 28",
"3": "Имя: NewUser, возраст: 22"
'''

from typing import Annotated

from fastapi import FastAPI,Path

# Создаем экземпляр приложения FastAPI uvicorn module_16_1:app --reload
app = FastAPI()

users = {'1': 'Имя: Example, возраст: 18'}
# Определение базового маршрута
@app.get("/")
async def root():
    return {"Главная страница"}

@app.get("/users")
async def get_users():
    return users

@app.post("/user/{username}/{age}")
async def new_user(
        username: Annotated[str,Path(min_lenght=5,max_length=20,description="Enter username", examples="Andrey")],
        age:Annotated[int,Path(ge=18,le=120,description="Enter age", examples="33")]):

    key_num=str((int(max(users,key=int))) + 1)
    users[key_num]=f'Имя {username}, Возраст: {age}'
    return {"messege": f"{username}: UserID: {key_num}"}




@app.put("/user/{user_id}/{username}/{age}")
async def upd_user(
        user_id:Annotated[str,Path(min_lenght=1, max_length=5,description="Enter userID", examples="1")],
        username: Annotated[str, Path(min_lenght=5, max_length=20, description="Enter username", examples="Andrey")],
        age: Annotated[int, Path(ge=18, le=120, description="Enter age", examples="33")]):

    users[user_id] = f'Имя {username}, Возраст: {age}'

    return {f"The user {user_id} is updated "}


@app.delete('/user/{user_id}')
async def del_user(user_id:Annotated[str,Path(min_lenght=1, max_length=5,description="Enter userID", examples="1")]):

    users.pop(user_id)
    return f"Пользователь {user_id} удален"