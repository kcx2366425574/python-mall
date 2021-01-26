# -*- encoding : utf-8 -*-
"""
@File       : __init__.py.py
@Time       :2021/1/24 14:49
@Author     :kuang congxian
@Contact    :kuangcx@inspur.com
@Description : null
"""
import oslo_i18n

oslo_i18n.enable_lazy()

DOMAIN = "mall"

_translators = oslo_i18n.TranslatorFactory(domain=DOMAIN)

# The primary translation function using the well_known name "_"
_ = _translators.primary

# The contextual translation function using the name "_C"
# requires oslo.i18n >=2.1.0
_C = _translators.contextual_form

# The plural translation function using the name "_P"
# requires oslo.i18n >=2.1.0
_P = _translators.plural_form

# Translators for log levels.
#
# The abbreviated names are meant to reflect the usual use of a short
# name like '_'. The "L" is for "log" and the other letter comes from
# the level.
_LI = _translators.log_info
_LW = _translators.log_warning
_LE = _translators.log_error
_LC = _translators.log_critical


def get_available_languages():
    return oslo_i18n.get_available_languages(DOMAIN)


if __name__ == '__main__':
    print(get_available_languages())
