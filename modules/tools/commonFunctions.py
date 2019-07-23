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

import time

def pressEnter (message="Waiting for user agree...\nPress <ENTER> to continue..."):
    print (message)
    input ()
    return 0

def messageAndSleep (t, message="Sleeping for "+str(t)+" second(s)"):
    print (message)
    time.sleep(t)
    return 0
