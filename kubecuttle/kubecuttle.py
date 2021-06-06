from __future__ import absolute_import

from kubernetes import client, config, utils
import json
import os

config.load_kube_config()
api = client.ApiClient()

#file_path = "nginx-deployment.yaml"
#namespace = 'sre-test'


class FileNotFoundError(Exception):
    pass

def skip_if_already_exists(e):    
    info = json.loads(e.api_exceptions[0].body)
    print ("error info is",info)
    if info.get('reason').lower() == 'alreadyexists':
        pass
    else:
        raise e

def apply(filepath):
    if not os.path.exists(filepath):
        raise FileNotFoundError('No such File')
    try:
        utils.create_from_yaml(api, filepath)
    except utils.FailToCreateError as e:
        return skip_if_already_exists(e)
