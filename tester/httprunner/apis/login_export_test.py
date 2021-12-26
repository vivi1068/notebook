# NOTE: Generated By HttpRunner v3.1.6
# FROM: apis/login-export.yml


from httprunner import HttpRunner, Config, Step, RunRequest, RunTestCase


class TestCaseLoginExport(HttpRunner):

    config = Config("module variable").variables(
        **{
            "host": "",
            "username": "",
            "password": "",
            "status_code": "",
            "body_status": "",
            "body_msg": "",
        }
    )

    teststeps = [
        Step(
            RunRequest("login")
            .with_variables(**{"good": "good2"})
            .post("${host}/login")
            .with_headers(
                **{
                    "User-Agent": "HttpRunner/${get_httprunner_version()}",
                    "Content-Type": "application/x-www-form-urlencoded",
                }
            )
            .with_data("username=${username}&password=${password}")
            .extract()
            .with_jmespath("good", "body2")
            .validate()
            .assert_equal("status_code", "${status_code}")
            .assert_equal("body.status", "${body_status}")
            .assert_equal("body.msg", "${body_msg}")
        ),
    ]


if __name__ == "__main__":
    TestCaseLoginExport().test_start()
