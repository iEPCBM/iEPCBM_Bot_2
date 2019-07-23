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
# == GoogleAPI ==
URLGoogleAPI_YTChannels = "https://www.googleapis.com/youtube/v3/channels"

# Contains strings GoogleAPI_key_code and channelsListPage
from hiddenConfig import *
# String channelsListPage contains title of page that contains tabular data with
# basic information of YouTube channels (channel title and channel ID) and
# titles to pages for collect statistics (views and subscribers) as tabular data

# == Save description ==
saveDescPrefix       = u"Bot: "
saveDescMaxLen       = 255
saveDescTextOverflow = u"…" # text overflow symbol(s)
saveDescEndingPlural = u"s: "
saveDescStrBase      = u"update statistics of channel "

# == Local time quotas (sec) ==
wikiLocalQuota = 5
GoogleAPI_LocalQuota = 0

unknownCount = -1

isDebug = True

dictTabDataTemplate = {
    "license": "CC0-1.0",
    "description": {
        "en": ""
    },
    "sources": "",
    "schema": {
        "fields": [
            {
                "name": "timestamp",
                "type": "number",
                "title": {
                    "en": "timestamp (Unix time)"
                }
            },
            {
                "name": "subscribers",
                "type": "number",
                "title": {
                    "en": "number of subscribers"
                }
            },
            {
                "name": "views",
                "type": "number",
                "title": {
                    "en": "views"
                }
            }
        ]
    },
    "data": []
}

tabDataDescriptionTemplate = "subscribers and views of YouTube channel "
tabDataSourceTemplate = "Copied from "
YTChannelBaseLink = "https://www.youtube.com/channel/"
