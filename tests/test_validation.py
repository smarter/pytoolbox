# -*- coding: utf-8 -*-

#**********************************************************************************************************************#
#                                        PYTOOLBOX - TOOLBOX FOR PYTHON SCRIPTS
#
#  Main Developer : David Fischer (david.fischer.ch@gmail.com)
#  Copyright      : Copyright (c) 2012-2013 David Fischer. All rights reserved.
#
#**********************************************************************************************************************#
#
# This file is part of David Fischer's pytoolbox Project.
#
# This project is free software: you can redistribute it and/or modify it under the terms of the EUPL v. 1.1 as provided
# by the European Commission. This project is distributed in the hope that it will be useful, but WITHOUT ANY WARRANTY;
# without even the implied warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.
#
# See the European Union Public License for more details.
#
# You should have received a copy of the EUPL General Public License along with this project.
# If not, see he EUPL licence v1.1 is available in 22 languages:
#     22-07-2013, <https://joinup.ec.europa.eu/software/page/eupl/licence-eupl>
#
# Retrieved from https://github.com/davidfischer-ch/pytoolbox.git

from __future__ import absolute_import, division, print_function, unicode_literals

from nose.tools import raises
from pytoolbox.validation import validate_list


class TestValidation(object):

    def test_validate_list(self):
        regexes = [r'\d+', r"call\(\[u*'my_var', recursive=(True|False)\]\)"]
        validate_list([10, "call([u'my_var', recursive=False])"], regexes)

    @raises(IndexError)
    def test_validate_list_fail_size(self):
        validate_list([1, 2], [1, 2, 3])

    @raises(ValueError)
    def test_validate_list_fail_value(self):
        regexes = [r'\d+', r"call\(\[u*'my_var', recursive=(True|False)\]\)"]
        validate_list([10, u"call([u'my_var', recursive='error'])"], regexes)
