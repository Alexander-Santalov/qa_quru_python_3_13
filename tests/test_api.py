import requests
from pytest_voluptuous import S
from schemas.schemas import *

base_url = "https://reqres.in/"


def test_create_user():
    created_user = requests.post(f"{base_url}api/users", {"name": "Alex", "job": "Tester"})

    assert created_user.status_code == 201
    assert S(create_user) == created_user.json()
    assert created_user.json()["name"] == "Alex"
    assert created_user.json()["job"] == "Tester"


def test_update_user_by_put():
    update_user = requests.put(f"{base_url}api/users/2", {"name": "sant", "job": "aqa"})

    assert update_user.status_code == 200
    assert S(create_update_user) == update_user.json()
    assert update_user.json()["name"] == "sant"
    assert update_user.json()["job"] == "aqa"


def test_update_user_by_patch():
    update_user = requests.put(f"{base_url}api/users/2", {"name": "asantalov", "job": "manual_tester"})

    assert update_user.status_code == 200
    assert S(create_update_user) == update_user.json()
    assert update_user.json()["name"] == "asantalov"
    assert update_user.json()["job"] == "manual_tester"


def test_delete_user():
    delete_user = requests.delete(f"{base_url}api/users/2")

    assert delete_user.status_code == 204


def test_successful_register():
    user_register = requests.post(f"{base_url}api/register", {"email": "eve.holt@reqres.in", "password": "pistol"})

    assert user_register.status_code == 200
    assert S(register_user) == user_register.json()
    assert user_register.json()['id']
    assert user_register.json()['token']


def test_unsuccessful_register():
    user_register = requests.post(f"{base_url}api/register", {"email": "sydney@fife"})

    assert user_register.status_code == 400
    assert S(unregister_user) == user_register.json()
    assert user_register.json()['error'] == 'Missing password'
