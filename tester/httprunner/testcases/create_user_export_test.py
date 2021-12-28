# NOTE: Generated By HttpRunner v3.1.6
# FROM: testcases/create-user-export.yml


import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent.parent))


from httprunner import HttpRunner, Config, Step, RunRequest, RunTestCase

from apis.login_export_test import TestCaseLoginExport as LoginExport


class TestCaseCreateUserExport(HttpRunner):

    config = Config("testcases module variable")

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
            .call(LoginExport)
        ),
        Step(
            RunRequest("create user")
            .with_variables(
                **{
                    "host": "http://127.0.0.1:8888",
                    "username": "${body2}",
                    "status_code": 200,
                    "body_status": 200,
                    "body_msg": "user ${username} create success.",
                }
            )
            .post("${host}/user")
            .with_headers(
                **{
                    "User-Agent": "HttpRunner/${get_httprunner_version()}",
                    "Content-Type": "application/x-www-form-urlencoded",
                }
            )
            .with_data("username=${username}")
            .validate()
            .assert_equal("status_code", "${status_code}")
            .assert_equal("body.status", "${body_status}")
            .assert_equal("body.msg", "${body_msg}")
        ),
    ]


if __name__ == "__main__":
    TestCaseCreateUserExport().test_start()