import re
import sys
from httprunner.cli import main


if __name__ == '__main__':
    sys.argv[0] = re.sub(r'(-script\.pyw|\.exe)?$', '', sys.argv[0])
    sys.argv.append("run")
    sys.argv.append("--verbose")

    # sys.argv.append("apis/login-api-v2-success.yml")
    # sys.argv.append("apis/login-api-v3-success.yml")

    # sys.argv.append("testcases/create-user-ref.yml")
    # sys.argv.append("testcases/create-user-extract.yml")
    sys.argv.append("testcases/create-user-export.yml")

    sys.exit(main())
