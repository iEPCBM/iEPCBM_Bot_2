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
sys.path.append(os.path.join(os.path.dirname(__file__), "../.."))

import urllib.request
import json
import pywikibot

from bot_config import *


def getChannelData (ChannelID):
    try:
        response = urllib.request.urlopen(URLGoogleAPI_YTChannels+"?part=statistics&id="+ChannelID+"&key="+GoogleAPI_key_code)
    except urllib.error.URLError as err:
        return False
    json_data = response.read().decode('utf8')
    list_data = json.loads(json_data)
    returnObject = {}
    if list_data['pageInfo']['totalResults'] > 0:
        if list_data['items'][0]['statistics']['hiddenSubscriberCount'] is False:
            returnObject = {"subscriberCount": list_data['items'][0]['statistics']['subscriberCount'],
                            "viewCount": list_data['items'][0]['statistics']['viewCount']}
        else:
            returnObject = {"subscriberCount": unknownCount,
                            "viewCount": list_data['items'][0]['statistics']['viewCount']}
    else:
        return "unknownChannel"
    return returnObject
def getChannelList (site):
    returnVal = []
    keys = []
    page = pywikibot.Page(site, channelsListPage)
    dataRaw = json.loads (page.text)
    for dataRawCol in dataRaw["schema"]["fields"]:
        keys.append (dataRawCol["name"])
    for i, dataRawRow in enumerate(dataRaw["data"]):
        returnVal.append ({})
        for j, dataRawCell in enumerate(dataRawRow):
            returnVal[i][keys[j]] = dataRawCell
    return returnVal
def getSubsViewsData (site):
    returnVal = []
    channelList = getChannelList (site)
    for channel in channelList:
        response = getChannelData (channel["channelID"])
        if type(response) is str:
            if response is "unknownChannel":
                print ("unknownChannel")
            else:
                print(response)
        else:
            response["dataPage"] = channel["TabularDataTitle"]
            response["channelName"] = channel["channelName"]
            response["channelID"] = channel["channelID"]
            returnVal.append (response)
    return returnVal
