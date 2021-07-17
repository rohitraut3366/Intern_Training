import argparse
import os
import logging
from logging.handlers import TimedRotatingFileHandler

import requests

if not os.path.exists('log/'):
    os.makedirs('log')

formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(name)s -%(message)s')

handler = TimedRotatingFileHandler(filename='log/client.log', when='midnight',
                                   interval=1, encoding='utf8', )

handler.suffix = "%Y-%m-%d %H:%M:%S"
handler.setFormatter(formatter)

logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)
logger.addHandler(handler)


class CommunicateOpenStack:

    def argument_operation(self, argv):
        try:
            response = requests.request(method=argv.method, url=argv.endpoint + argv.api_route,
                                        headers={"X-AUTH-TOKEN": argv.token},
                                        timeout=15)
            if argv.verbose:
                print(response.text)
                return
            print(response.request.url, response.status_code)
            print(response.headers)
            print(response.text)

        except requests.exceptions.Timeout:
            logger.warning("Timeout")
            print("Timeout")
        except requests.exceptions.ConnectionError:
            logger.warning("ConnectionError")
            print("Connection failed")
        except Exception as e:
            logger.warning(f"Exception: {e}")
            print(f"Exception: {e}")

    def add_optional_argument(self, parser):
        parser.add_argument('-v', '--verbose',
                            action="store_false",
                            help="Verbose Output")

        return parser

    def add_position_argument(self, parser):
        parser.add_argument("endpoint",
                            help="API end point")

        parser.add_argument("method",
                            help="HTTP method",
                            type=str,
                            choices=['GET', 'DELETE'])

        parser.add_argument("api_route",
                            help="API route")

        parser.add_argument("token",
                            help="API route")

        return parser

    def main(self):
        parser = argparse.ArgumentParser()
        parser = self.add_optional_argument(parser)
        parser = self.add_position_argument(parser)
        self.argument_operation(parser.parse_args())


if __name__ == "__main__":
    CommunicateOpenStack().main()
