

import sys
import os
import subprocess

__author__ = "___"
__license__ = "GPLv3"

test_main_url = "https://author/python/tests/common/test_main.py"
app_path = os.path.abspath(os.path.dirname(sys.argv[0]))
test_main_filename = os.path.join(app_path, "test_main.py")

try:
    import requests
except ImportError:
    print("Перед запуском проверки откройте терминал в папке с файлом " +
          "test.py и выполните команду\npip install -r requirements.txt\n" +
          "после чего снова запустите проверку.")
    sys.exit()


if __name__ == "__main__":
    try:
        # 1. Загрузка test_main
        session = requests.session()
        session.verify = True

        r = session.get(test_main_url)
        if r.status_code == requests.codes.ok:
            with open(test_main_filename, "wb") as f:
                f.write(r.content)
        else:
            raise r.raise_for_status()

        # 2. Запуск test_main
        subprocess.run([sys.executable, test_main_filename,
                        " ".join(sys.argv[1:])])
    except Exception as err:
        print("При запуске тестов произошла ошибка:", err,
              "\nОбратитесь к автору курса.")
    finally:
        try:
            os.remove(test_main_filename)
        except Exception:
            pass
