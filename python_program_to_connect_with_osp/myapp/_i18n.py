import os

import oslo_i18n

oslo_i18n.enable_lazy()
DOMAIN = "oc"
"""


"""
os.environ['LANGUAGE'] = "ja"
os.environ['OC_LOCALDIR'] = os.path.dirname(os.path.realpath(__file__))
os.environ["MYAPP_LOCALEDIR"] = '.'
os.environ['OSLO_POLICY_LOCALEDIR']= "myapp"

_translators = oslo_i18n.TranslatorFactory(domain=DOMAIN)

_ = _translators.primary

_C = _translators.contextual_form

_P = _translators.plural_form

_LI = _translators.log_info
_LW = _translators.log_warning
_LE = _translators.log_error
_LC = _translators.log_critical


def get_available_languages():
    return oslo_i18n.get_available_languages(DOMAIN)



