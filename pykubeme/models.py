# -*- coding: utf-8 -*-

"""
PyOps
~~~~~
This module contais the PyOps Client class.
:copyright: (c) 2018 by Sergio Ferraresi
:license: Apache2, see LICENSE for more details
"""

from enum import Enum


class Command(Enum):
    CLUSTER_ROLE = 'clusterrole'
    CLUSTER_ROLE_BINDING = 'clusterrolebinding'
    CONFIG_MAP = 'configmap'
    DEPLOYMENT = 'deployment'
    JOB = 'job'
    NAMESPACE = 'namespace'
    POD_DISRUPTION_BUDGET = 'poddisruptionbudget'
    PRIORUTY_CLASS = 'priorityclass'
    QUOTA = 'quota'
    ROLE = 'role'
    ROLE_BINDING = 'rolebinding'
    SECRET = 'secret'
    SERVICE = 'service'
    SA = 'serviceaccount'
    SERVICE_ACCOUNT = 'serviceaccount'

class Resource(Enum):
    BINDINGS = {
        'name': 'bindings',
        'shortname': [],
        'apigroup': [''],
        'namespaced': True ,
        'kind': 'Binding'
    }
    COMPONENT_STATUSES = {
        'name': 'componentstatuses',
        'shortname': ['cs'],
        'apigroup': [''],
        'namespaced': False,
        'kind': 'ComponentStatus'
    }
    CONFIG_MAPS = {
        'name': 'configmaps',
        'shortname': ['cm'],
        'apigroup': [''],
        'namespaced': True,
        'kind': 'ConfigMap'
    }
    ENDPOINTS = {
        'name': 'endpoints',
        'shortname': ['ep'],
        'apigroup': [''],
        'namespaced': True,
        'kind': 'Endpoints'
    }
    EVENTS = {
        'name': 'events',
        'shortname': ['ev'],
        'apigroup': ['', 'events.k8s.io'],
        'namespaced': True,
        'kind': 'Event'
    }
    LIMIT_RANGES = {
        'name': 'limitranges',
        'shortname': ['limits'],
        'apigroup': [''],
        'namespaced': True,
        'kind': 'LimitRange'
    }
    NAMESPACES = {
        'name': 'namespaces',
        'shortname': ['ns'],
        'apigroup': [''],
        'namespaced': False,
        'kind': 'Namespace'
    }
    NODES = {
        'name': 'nodes',
        'shortname': ['no'],
        'apigroup': [''],
        'namespaced': False,
        'kind': 'Node'
    }
    PERSISTENT_VOLUME_CLAIMS = {
        'name': 'persistentvolumeclaims',
        'shortname': ['pvc'], 'apigroup': [''],
        'namespaced': True,
        'kind': 'PersistentVolumeClaim'
    }
    PERSISTENT_VOLUMES = {
        'name': 'persistentvolumes',
        'shortname': ['pv'],
        'apigroup': [''],
        'namespaced': False,
        'kind': 'PersistentVolume'
    }
    PODS = {
        'name': 'pods',
        'shortname': ['po'],
        'apigroup': [''],
        'namespaced': True,
        'kind': 'Pod'
    }
    POD_TEMPLATES = {
        'name': 'podtemplates',
        'shortname': [],
        'apigroup': [''],
        'namespaced': True,
        'kind': 'PodTemplate'
    }
    REPLICATION_CONTROLLERS = {
        'name': 'replicationcontrollers',
        'shortname': ['rc'],
        'apigroup': [''],
        'namespaced': True,
        'kind': 'ReplicationController'
    }
    RESOURCE_QUOTAS = {
        'name': 'resourcequotas',
        'shortname': ['quota'],
        'apigroup': [''],
        'namespaced': True,
        'kind': 'ResourceQuota'
    }
    SECRETS = {
        'name': 'secrets',
        'shortname': [],
        'apigroup': [''],
        'namespaced': True,
        'kind': 'Secret'
    }
    SERVICE_ACCOUNTS = {
        'name': 'serviceaccounts',
        'shortname': ['sa'],
        'apigroup': [''],
        'namespaced': True,
        'kind': 'ServiceAccount'
    }
    SERVICES = {
        'name': 'services',
        'shortname': ['svc'],
        'apigroup': [''],
        'namespaced': True ,
        'kind': 'Service'
    }
    MUTATING_WEBHOOK_CONFIGURATIONS = {
        'name': 'mutatingwebhookconfigurations',
        'shortname': [],
        'apigroup': ['admissionregistration.k8s.io'],
        'namespaced': False,
        'kind': 'MutatingWebhookConfiguration'
    }
    VALIDATING_WEBHOOK_CONFIGURATIONS = {
        'name': 'validatingwebhookconfigurations',
        'shortname': [],
        'apigroup': ['admissionregistration.k8s.io'],
        'namespaced': False,
        'kind': 'ValidatingWebhookConfiguration'
    }
    CUSTOM_RESOURCE_DEFINITIONS = {
        'name': 'customresourcedefinitions',
        'shortname': ['crd', 'crds'],
        'apigroup': 'apiextensions.k8s.io',
        'namespaced': False,
        'kind': 'CustomResourceDefinition'
    }
    API_SERVICES = {
        'name': 'apiservices',
        'shortname': [],
        'apigroup': ['apiregistration.k8s.io'],
        'namespaced': False,
        'kind': 'APIService'
    }
    CONTROLLER_REVISIONS = {
        'name': 'controllerrevisions',
        'shortname': [],
        'apigroup': ['apps'],
        'namespaced': True,
        'kind': 'ControllerRevision'
    }
    DAEMON_SETS = {
        'name': 'daemonsets',
        'shortname': ['ds'],
        'apigroup': ['apps', 'extensions'],
        'namespaced': True,
        'kind': 'DaemonSet'
    }
    DEPLOYMENTS = {
        'name': 'deployments',
        'shortname': ['deploy'],
        'apigroup': ['apps', 'extensions'],
        'namespaced': True,
        'kind': 'Deployment'
    }
    REPLICA_SETS = {
        'name': 'replicasets',
        'shortname': ['rs'],
        'apigroup': ['apps', 'extensions'],
        'namespaced': True,
        'kind': 'ReplicaSet'
    }
    STATEFUL_SETS = {
        'name': 'statefulsets',
        'shortname': ['sts'],
        'apigroup': ['apps'], 'namespaced': True,
        'kind': 'StatefulSet'
    }
    TOKEN_REVIEWS = {
        'name': 'tokenreviews',
        'shortname': [],
        'apigroup': ['authentication.k8s.io'],
        'namespaced': False,
        'kind': 'TokenReview'
    }
    LOCAL_SUBJECT_ACCESS_REVIEWS = {
        'name': 'localsubjectaccessreviews',
        'shortname': [],
        'apigroup': ['authorization.k8s.io'],
        'namespaced': True,
        'kind': 'LocalSubjectAccessReview'
    }
    SELF_SUBJECT_ACCESS_REVIEWS = {
        'name': 'selfsubjectaccessreviews',
        'shortname': [],
        'apigroup': ['authorization.k8s.io'],
        'namespaced': False,
        'kind': 'SelfSubjectAccessReview'
    }
    SELF_SUBJECT_RULES_REVIEWS = {
        'name': 'selfsubjectrulesreviews',
        'shortname': [],
        'apigroup': ['authorization.k8s.io'],
        'namespaced': False,
        'kind': 'SelfSubjectRulesReview'
    }
    SUBJECT_ACCESS_REVIEWS = {
        'name': 'subjectaccessreviews',
        'shortname': [],
        'apigroup': ['authorization.k8s.io'],
        'namespaced': False,
        'kind': 'SubjectAccessReview'
    }
    H_POD_AUTOSCALERS = {
        'name': 'horizontalpodautoscalers',
        'shortname': ['hpa'],
        'apigroup': ['autoscaling'],
        'namespaced': True,
        'kind': 'HorizontalPodAutoscaler'
    }
    CRON_JOBS = {
        'name': 'cronjobs',
        'shortname': ['cj'],
        'apigroup': ['batch'],
        'namespaced': True,
        'kind': 'CronJob'
    }
    JOBS = {
        'name': 'jobs',
        'shortname': [],
        'apigroup': ['batch'],
        'namespaced': True,
        'kind': 'Job'
    }
    CERTIFICATE_SIGNING_REQUESTS = {
        'name': 'certificatesigningrequests',
        'shortname': ['csr'],
        'apigroup': ['certificates.k8s.io'],
        'namespaced': False,
        'kind': 'CertificateSigningRequest'
    }
    LEASES = {
        'name': 'leases',
        'shortname': [],
        'apigroup': ['coordination.k8s.io'],
        'namespaced': True,
        'kind': 'Lease'
    }
    INGRESSES = {
        'name': 'ingresses',
        'shortname': ['ing'],
        'apigroup': ['extensions'],
        'namespaced': True,
        'kind': 'Ingress'
    }
    NETWOR_POLICIES= {
        'name': 'networkpolicies',
        'shortname': ['netpol'],
        'apigroup': ['extensions', 'networking.k8s.io'],
        'namespaced': True,
        'kind': 'NetworkPolicy'
    }
    POD_SECURITY_POLICIES = {
        'name': 'podsecuritypolicies',
        'shortname': ['psp'],
        'apigroup': ['extensions', 'policy'],
        'namespaced': False,
        'kind': 'PodSecurityPolicy'
    }
    POD_DISRUPTION_BUDGETS = {
        'name': 'poddisruptionbudgets',
        'shortname': ['pdb'],
        'apigroup': ['policy'],
        'namespaced': True,
        'kind': 'PodDisruptionBudget'
    }
    CLUSTER_ROLE_BINDINGS = {
        'name': 'clusterrolebindings',
        'shortname': [],
        'apigroup': ['rbac.authorization.k8s.io'],
        'namespaced': False,
        'kind': 'ClusterRoleBinding'
    }
    CLUSTER_ROLES = {
        'name': 'clusterroles',
        'shortname': [],
        'apigroup': ['rbac.authorization.k8s.io'],
        'namespaced': False,
        'kind': 'ClusterRole'
    }
    ROLE_BINDINGS = {
        'name': 'rolebindings',
        'shortname': [],
        'apigroup': ['rbac.authorization.k8s.io'],
        'namespaced': True,
        'kind': 'RoleBinding'
    }
    ROLES = {
        'name': 'roles',
        'shortname': [],
        'apigroup': ['rbac.authorization.k8s.io'],
        'namespaced': True,
        'kind': 'Role'
    }
    PRIORITY_CLASSES = {
        'name': 'priorityclasses',
        'shortname': ['pc'],
        'apigroup': ['scheduling.k8s.io'],
        'namespaced': False,
        'kind': 'PriorityClass'
    }
    STORAGE_CLASSES = {
        'name': 'storageclasses',
        'shortname': ['sc'],
        'apigroup': ['storage.k8s.io'],
        'namespaced': False, 'kind': 'StorageClass'
    }
    VOLUME_ATTACHMENTS = {
        'name': 'volumeattachments',
        'shortname': [],
        'apigroup': ['storage.k8s.io'],
        'namespaced': False,
        'kind': 'VolumeAttachment'
    }
