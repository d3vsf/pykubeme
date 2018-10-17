# -*- coding: utf-8 -*-

"""Test for pykubeme."""

import logging
import sys
import unittest

sys.path.append('../')

import pykubeme
from pykubeme import Resource


class KubemeTest(unittest.TestCase):

    def test_001(self):
        client = pykubeme.Client()
        # client.get(resource='pods') # ERROR

    def test_002(self):
        print('\n> Get pods and services...')
        client = pykubeme.Client(namespace='geodamp')
        client.get(resource=[Resource.PODS, Resource.SERVICES])

    def test_003(self):
        print('\n> Get pods and create deploy (dry run)...')
        client = pykubeme.Client(namespace='geodamp')
        client.run('ngix', 'ngix', replicas=2, dry_run=True)
        client.get(resource=Resource.PODS)
        pass

    def test_004(self):
        print('\n> Get pods and create deploy...')
        client = pykubeme.Client(namespace='geodamp')
        # client.run('ngix', 'ngix', replicas=1)
        client.get(resource=Resource.PODS)
        pass
    
    def test_005(self):
        print('\n> Get pods and delete deploy...')
        client = pykubeme.Client(namespace='geodamp')
        # client.delete(resources=[Resource.DEPLOYMENTS], names=['ngix'], now=True)
        client.get(resource=Resource.PODS)


if __name__ == "__main__":
    suite = unittest.TestLoader().loadTestsFromTestCase(KubemeTest)
    unittest.TextTestRunner(verbosity=2).run(suite)
