# -*- coding: utf-8 -*-

# This file is part of iEPCBM Bot 2 (YaLPD-B2).

# Copyright 2019 Rishat Kagirov (iEPCBM)
# SPDX-License-Identifier: Apache-2.0

'''
    iEPCBM Bot 2 (YaLPD-B2)
    Copyright 2019 Rishat Kagirov (iEPCBM)

    Licensed under the Apache License, Version 2.0 (the "License");
    you may not use this file except in compliance with the License.
    You may obtain a copy of the License at

        http://www.apache.org/licenses/LICENSE-2.0

    Unless required by applicable law or agreed to in writing, software
    distributed under the License is distributed on an "AS IS" BASIS,
    WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
    See the License for the specific language governing permissions and
    limitations under the License.

    ****************************************************************************

    The program uses GoogleAPI.
    GoogleAPIs Terms of Service - <https://developers.google.com/terms/>
'''

import os, sys

curDir = os.path.dirname(__file__)
sys.path.append(os.path.join(curDir, "modules"))
sys.path.append(os.path.join(curDir, "conf"))
sys.path.append(os.path.join(curDir, "modules/tools"))

import pywikibot

from pressEnter import *
from bot_config import *
from getData import *
from updateTabData import *

def main():
    print (__doc__)
    site = pywikibot.Site()
    subsViewsDataList = getSubsViewsData (site)
    updateTabData(subsViewsDataList, site)
    pywikibot.stopme()
    if (isDebug):
        pressEnter ("Done! Press <ENTER> to exit...")
    return 0
if __name__ == "__main__":
    main()
