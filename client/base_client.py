import allure
from requests import Request, Session

from config import settings as cfg
from helper.logger import LOGGER


class BaseClient:

    RESET = "/v2/reset'"

    def reset_collection(self):
        return self.make_request("POST", self.RESET)

    def __init__(self, base_url: str = "", default_headers: dict = {}):
        self.base_url = base_url
        self.s = Session()
        self.s.headers = default_headers

    def make_request(self, method, relative_url, settings={"verify": False}, **kwargs):
        """
        settings:
            - stream
            - verify
            - proxies
            - cert
            - timeout
        """
        url = self.url_join(self.base_url, relative_url)

        with allure.step(f"{method} {url}"):
            with allure.step(f"session headers = {self.s.headers}"):
                pass
            with allure.step(f"settings = {settings}"):
                pass

            log_msg = "{} :: Выполняем запрос {} {}\n\t|> session headers = {}\n\t|> settings = {}".format(
                self.__class__.__name__, method, url, self.s.headers, settings
            )
            for k, v in kwargs.items():
                with allure.step(f"{k} = {v}"):
                    log_msg += f"\n\t|> {k} = {v}"

            LOGGER.info(log_msg)

            prepped = self.prepare_request(method, url, **kwargs)
            r = self.s.send(prepped, **settings)
            # LOGGER.info(f"Ответ: {r.text}")
            allure.attach(r.text, "Ответ:", allure.attachment_type.TEXT)
            return r

    def url_join(self, base_url, relative_url):
        url = base_url if base_url.endswith("/") else base_url + "/"
        url += relative_url[1:] if relative_url.startswith("/") else relative_url
        return url

    def prepare_request(self, method, url, **kwargs):
        req = Request(method, url, **kwargs)
        return self.s.prepare_request(req)
