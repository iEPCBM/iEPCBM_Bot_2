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
sys.path.append(os.path.join(os.path.dirname(__file__), ".."))
sys.path.append(os.path.join(os.path.dirname(__file__), "tools"))

import time
import json
import pywikibot

from bot_config import *
from commonFunctions import *
from getData import *

def createTabPage (page, chData):
    parsedNewPageData = dictTabDataTemplate
    parsedNewPageData["description"]["en"] = tabDataDescriptionTemplate + \
        chData["channelName"]
    parsedNewPageData["sources"] = tabDataSourceTemplate + "[" + \
        YTChannelBaseLink + chData["channelID"] + "]" + " (" + \
        chData["channelName"] + ")"
    page.text = json.dumps(parsedNewPageData)

def updateTabData (listData, site):
    for chData in listData:
        print ("Current channel: " + chData["channelName"])
        if (isDebug):
            pressEnter ()
        if chData["dataPage"] == "":
            continue
        if chData["subscriberCount"]>=minSubscribers and chData["viewCount"]>=minViews:
            page = pywikibot.Page(site, chData["dataPage"])
            if len(page.text) == 0:
                createTabPage (page,chData)
            parsedPageData = json.loads (page.text)
            parsedPageData["data"].append ([round(time.time()), int(chData["subscriberCount"]), int(chData["viewCount"])])
            saveDesc = saveDescPrefix + saveDescStrBase + chData["channelName"]
            saveDesc = (saveDesc[:saveDescMaxLen-len(saveDescTextOverflow)] + saveDescTextOverflow) if len(saveDesc) > saveDescMaxLen else saveDesc
            print ("Save description: " + saveDesc)
            page.text = json.dumps(parsedPageData)
            messageAndSleep(wikiLocalQuota, "Sleeping for "+str(wikiLocalQuota)+" second(s)...")
            page.save(saveDesc)
    return True
