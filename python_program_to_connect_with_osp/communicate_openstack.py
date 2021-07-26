#  Licensed under the Apache License, Version 2.0 (the "License"); you may
#  not use this file except in compliance with the License. You may obtain
#  a copy of the License at
#
#       http://www.apache.org/licenses/LICENSE-2.0
#
#  Unless required by applicable law or agreed to in writing, software
#  distributed under the License is distributed on an "AS IS" BASIS, WITHOUT
#  WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the
#  License for the specific language governing permissions and limitations
#  under the License.

"""
Command-line interface for GET and DELETE requests.
"""

import argparse
import os

import requests
from oslo_config import cfg
from oslo_log import log as logging

from myapp._i18n import _, _LW

CONF = cfg.CONF
DOMAIN = "oc"
logging.register_options(CONF)


def create_log_dir():
    _dir = CONF.log.dir
    if not os.path.exists(_dir):
        os.makedirs(_dir)
    return _dir


def prepare():

    grp = cfg.OptGroup("log")

    opts = [cfg.StrOpt("dir"),
            cfg.StrOpt("file_name"),
            cfg.StrOpt("level"),
            cfg.StrOpt("domain")]

    CONF.register_group(grp)
    CONF.register_opts(opts, grp)

    CONF(default_config_files=["./communicate_openstack.conf"], use_env=False)

    logging.tempest_set_log_file(create_log_dir() + CONF.log.file_name)
    logging.setup(CONF, DOMAIN)


class CommunicateOpenStack(object):

    def argument_operation(self, argv):
        """Execution of operation"""

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
            LOG.warning(_LW("Timeout"))
            print(_("Timeout"))
        except requests.exceptions.ConnectionError:
            LOG.warning(_LW("ConnectionError"))
            print(_("Connection failed"))
        except Exception as e:
            LOG.warning(_LW("Exception: %s"), e)
            print(_(f"Exception: {e}"))

    def add_optional_argument(self, parser):
        """Register optional argument"""
        parser.add_argument('-v', '--verbose',
                            action="store_false",
                            help="Verbose Output")

        return parser

    def add_position_argument(self, parser):
        """Register positional argument"""
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
    prepare()

    LOG = logging.getLogger(__name__)

    CommunicateOpenStack().main()
