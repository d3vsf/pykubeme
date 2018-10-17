# -*- coding: utf-8 -*-

"""
PyKubeme
~~~~~
This module contais the PyKubeme Client class.
:copyright: (c) 2018 by Sergio Ferraresi
:license: Apache2, see LICENSE for more details
"""

import json
import logging
import numbers
import os
import subprocess

from .models import Resource
from enum import Enum

logger = logging.getLogger(__name__)


class Client(object):
    '''
    A user-created :class:`Client <Client>` object.

    Used to prepare a :class:`Client <Client>`, which is used to wrap the Kubernetes' kubectl command.

    :param description_xml_url: description.xml of the OpenSearch endpoint.
    :param search_endpoint: OpenSearch endpoint, if :param:`description_xml_url` not available.
    :param type: OpenSearch endpoint type: results or collection.

    Usage::

        >>> import pykubeme
        >>> from pykubeme import Resource
        >>> client = pykubeme.Client(namespace="my-namespace")
        >>> client.get(Resource.PODS)
    '''

    def __init__(self, namespace=None, output_format='json'):
        self.namespace = namespace
        self.output_format = output_format

        # TODO check if kubectl is installed and configured
    
    def custom(self, string):
        """Custom call to kubectl.

        :param string: command to pass to kubectl.

        Usage::

            >>> client.custom('get pods -n my-namespace')
        """
        if not string:
            return {}  # TODO error

        cmd = ['kubectl'].extend(string.split(' '))
        ret_code = json.loads(subprocess.check_output(cmd))
        print(ret_code)
        return ret_code

    def get(self, resource, filename=None, namespace=None, watch=False, output_format='json'):
        if not resource:
            return {}  # TODO error: not valid resource
        if not isinstance(resource, list) and not isinstance(resource, Resource):
            return {}  # TODO error: not valid resource
        if watch and isinstance(resource, list) and len(resource) > 1:
            return {}  # TODO error: if watch, only one resource can be specified

        res = resource.value['name'] if not isinstance(resource, list) else (',').join([r.value['name'] for r in resource])

        cmd = ['kubectl', 'get', '-o', self.output_format, '--show-kind', res]
        if namespace:
            cmd.extend(['-n', namespace])
        elif self.namespace:
            cmd.extend(['-n', self.namespace])
        if filename:
            cmd.extend(['-f', filename])
        if watch:
            cmd.append('-w')
        ret_code = json.loads(subprocess.check_output(cmd))
        print(ret_code)
        return ret_code
    
    def create(self, filename, namespace=None):
        if not filename:
            return {}  # TODO error
        if not os.path.exists(filename):
            return {}  # TODO error: file not exists
        # TODO filename can be an url

        cmd = ['kubectl', 'create', '-o', self.output_format, '-f', filename]
        if namespace:
            cmd.extend(['-n', namespace])
        elif self.namespace:
            cmd.extend(['-n', self.namespace])
        ret_code = json.loads(subprocess.check_output(cmd))
        print(ret_code)
        return ret_code

    def delete(self, filename=None, namespace=None, resources=[], names=[], selector=None, all=False, now=False):
        resource_list = ''
        name_list = ''

        cmd = ['kubectl', 'delete']
        if namespace:
            cmd.extend(['-n', namespace])
        elif self.namespace:
            cmd.extend(['-n', self.namespace])
        if filename:
            # TODO check existance
            cmd.extend(['-f', filename])
        else:
            if len(resources) > 0:
                for k in resources:
                    resource_list = '%s%s,' % (resource_list, k.value['name'])
                resource_list = resource_list[:-1]
                cmd.append(resource_list)

                if selector:
                    cmd.extend(['-l', selector])

                if len(names) > 0:
                    for n in names:
                        name_list = '%s%s ' % (name_list, n)
                    name_list = name_list[:-1]
                    cmd.append(name_list)
        if all:
            cmd.append('--all')
        if now:
            cmd.append('--now')

        ret_code = subprocess.check_output(cmd)
        print(ret_code)
        return ret_code
    
    def run(self, name, image, namespace=None, replicas=1, port=None, expose=False, service_account=None, envs=[], dry_run=False):
        if not name:
            return {}  # TODO error
        if not image:
            return {}  # TODO error
        if port and not isinstance(port, numbers.Number):
            return {}  # TODO error: not a number

        cmd = ['kubectl', 'run', name, '--image', image, '-o', self.output_format, '--replicas=%d' % replicas]
        if namespace:
            cmd.extend(['-n', namespace])
        elif self.namespace:
            cmd.extend(['-n', self.namespace])
        if port:
            cmd.append('--port=%d' % port)
        if expose:
            cmd.append('--expose')
        if service_account:
            cmd.append('--serviceaccount=%s' % service_account)
        if len(envs) > 0:
            for e in envs:
                cmd.append('--env="%s"' % e)
        if dry_run:
            cmd.append('--dry-run')

        ret_code = json.loads(subprocess.check_output(cmd))
        print(ret_code)
        return ret_code
