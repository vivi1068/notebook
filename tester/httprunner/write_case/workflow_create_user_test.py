# NOTE: Generated By HttpRunner v3.1.6
# FROM: workflow-create-user.yml


import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))


from httprunner import HttpRunner, Config, Step, RunRequest, RunTestCase

from login_test import TestCaseLogin as Login

from create_user_test import TestCaseCreateUser as CreateUser

from list_users_test import TestCaseListUsers as ListUsers

from logout_test import TestCaseLogout as Logout


class TestCaseWorkflowCreateUser(HttpRunner):

    config = Config("workflow global variable")

    teststeps = [
        Step(
            RunTestCase("login")
            .with_variables(
                **{
                    "host": "http://127.0.0.1:8888",
                    "username": "zhangsan",
                    "password": "zhangsan123",
                    "status_code": 200,
                    "body_status": 200,
                    "body_msg": "login success",
                }
            )
            .call(Login)
        ),
        Step(
            RunTestCase("create user")
            .with_variables(
                **{
                    "host": "http://127.0.0.1:8888",
                    "username": "lisi",
                    "status_code": 200,
                    "body_status": 200,
                    "body_msg": "user ${username} create success.",
                }
            )
            .call(CreateUser)
        ),
        Step(
            RunTestCase("get all users")
            .with_variables(
                **{
                    "host": "http://127.0.0.1:8888",
                    "status_code": 200,
                    "body_status": 200,
                    "body_msg": ["zhangsan", "lisi"],
                }
            )
            .call(ListUsers)
        ),
        Step(
            RunTestCase("logout")
            .with_variables(
                **{
                    "host": "http://127.0.0.1:8888",
                    "status_code": 200,
                    "body_status": 200,
                    "body_msg": "logout success",
                }
            )
            .call(Logout)
        ),
        Step(
            RunTestCase("get all users")
            .with_variables(
                **{
                    "host": "http://127.0.0.1:8888",
                    "status_code": 200,
                    "body_status": 400,
                    "body_msg": "permission deny.",
                }
            )
            .call(ListUsers)
        ),
    ]


if __name__ == "__main__":
    TestCaseWorkflowCreateUser().test_start()
