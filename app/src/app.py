# -*- coding: utf-8 -*-
from logging import getLogger, config, StreamHandler, DEBUG
import os

import sys
sys.path.append('./')
from logutil import LogUtil
from importenv import ImportEnvKeyEnum
import importenv as setting

PYTHON_APP_HOME = os.getenv('PYTHON_APP_HOME')
logger = getLogger(__name__)
log_conf = LogUtil.get_log_conf(PYTHON_APP_HOME + '/config/log_config.json')
config.dictConfig(log_conf)
handler = StreamHandler()
handler.setLevel(DEBUG)
logger.setLevel(DEBUG)
logger.addHandler(handler)
logger.propagate = False

from googleapiclient.discovery import build

def youtube_channel_detail(channel_id, api_key):
  api_service_name = 'youtube'
  api_version = 'v3'
  youtube = build(api_service_name, api_version, developerKey=api_key)
  search_response = youtube.channels().list(
    part='snippet,statistics',
    id=channel_id,
  ).execute()

  return search_response['items'][0]

if __name__ == '__main__':

  args = sys.argv
  channel_id = args[1]

  logger.info('channel_id : {}'.format(channel_id))
  d = youtube_channel_detail(channel_id, setting.ENV_DIC[ImportEnvKeyEnum.API_KEY.value])
  logger.info(d['snippet']['title'])
  logger.info(d['statistics']['subscriberCount'])