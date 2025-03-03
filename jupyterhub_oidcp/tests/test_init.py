import sys
import unittest
from unittest.mock import MagicMock

from jupyterhub_oidcp import configure_jupyterhub_oidcp

class TestConfigureJupyterhubOidcp(unittest.TestCase):
    def test_basic(self):
        c = MagicMock()
        configure_jupyterhub_oidcp(
            c,
            base_url="http://localhost:8000",
            internal_base_url="http://hub:8000",
            port=8089,
            debug=True,
            services=[
                {
                    "oauth_client_id": "TEST_CLIENT_ID",
                    "api_token": "TEST_CLIENT_SECRET",
                    "redirect_uris": ["http://localhost:9001/ep_openid_connect/callback"],
                }
            ],
            vault_path="./tmp/jupyterhub_oid/.vault",
        )
        c.JupyterHub.services.append.assert_called_once_with({
            'name': 'oidcp',
            'admin': False,
            'url': 'http://localhost:8089/services/oidcp',
            'display': False,
            'command': [
                sys.executable,
                '-m',
                'jupyterhub_oidcp.main',
                '--services',
                '[{"oauth_client_id": "TEST_CLIENT_ID", "api_token": "TEST_CLIENT_SECRET", '
                + '"redirect_uris": ["http://localhost:9001/ep_openid_connect/callback"]}]',
                '--port',
                '8089',
                '--base-url',
                'http://localhost:8000',
                '--internal-base-url',
                'http://hub:8000',
                '--vault-path',
                './tmp/jupyterhub_oid/.vault',
                '--debug',
            ],
            'oauth_no_confirm': True,
            'oauth_client_allowed_scopes': ['inherit'],
        })

    def test_service_name(self):
        c = MagicMock()
        configure_jupyterhub_oidcp(
            c,
            service_name="oidcp_test",
            base_url="http://localhost:8000",
            internal_base_url="http://hub:8000",
            port=8089,
            debug=True,
            services=[
                {
                    "oauth_client_id": "TEST_CLIENT_ID",
                    "api_token": "TEST_CLIENT_SECRET",
                    "redirect_uris": ["http://localhost:9001/ep_openid_connect/callback"],
                }
            ],
            vault_path="./tmp/jupyterhub_oid/.vault",
        )
        c.JupyterHub.services.append.assert_called_once_with({
            'name': 'oidcp_test',
            'admin': False,
            'url': 'http://localhost:8089/services/oidcp_test',
            'display': False,
            'command': [
                sys.executable,
                '-m',
                'jupyterhub_oidcp.main',
                '--services',
                '[{"oauth_client_id": "TEST_CLIENT_ID", "api_token": "TEST_CLIENT_SECRET", '
                + '"redirect_uris": ["http://localhost:9001/ep_openid_connect/callback"]}]',
                '--port',
                '8089',
                '--base-url',
                'http://localhost:8000',
                '--internal-base-url',
                'http://hub:8000',
                '--vault-path',
                './tmp/jupyterhub_oid/.vault',
                '--debug',
            ],
            'oauth_no_confirm': True,
            'oauth_client_allowed_scopes': ['inherit'],
        })

    def test_admin_only_with_user_email_pattern(self):
        c = MagicMock()
        with self.assertRaises(ValueError):
            configure_jupyterhub_oidcp(
                c,
                base_url="http://localhost:8000",
                internal_base_url="http://hub:8000",
                port=8089,
                debug=True,
                services=[
                    {
                        "oauth_client_id": "TEST_CLIENT_ID",
                        "api_token": "TEST_CLIENT_SECRET",
                        "redirect_uris": ["http://localhost:9001/ep_openid_connect/callback"],
                    }
                ],
                vault_path="./tmp/jupyterhub_oid/.vault",
                admin_only=True,
                user_email_pattern="{uid}@example.com",
            )

    def test_admin_only(self):
        c = MagicMock()
        configure_jupyterhub_oidcp(
            c,
            admin_only=True,
            base_url="http://localhost:8000",
            internal_base_url="http://hub:8000",
            port=8089,
            debug=True,
            services=[
                {
                    "oauth_client_id": "TEST_CLIENT_ID",
                    "api_token": "TEST_CLIENT_SECRET",
                    "redirect_uris": ["http://localhost:9001/ep_openid_connect/callback"],
                }
            ],
            vault_path="./tmp/jupyterhub_oid/.vault",
        )
        c.JupyterHub.services.append.assert_called_once_with({
            'name': 'oidcp',
            'admin': True,
            'url': 'http://localhost:8089/services/oidcp',
            'display': False,
            'command': [
                sys.executable,
                '-m',
                'jupyterhub_oidcp.main',
                '--services',
                '[{"oauth_client_id": "TEST_CLIENT_ID", "api_token": "TEST_CLIENT_SECRET", '
                + '"redirect_uris": ["http://localhost:9001/ep_openid_connect/callback"]}]',
                '--port',
                '8089',
                '--base-url',
                'http://localhost:8000',
                '--internal-base-url',
                'http://hub:8000',
                '--vault-path',
                './tmp/jupyterhub_oid/.vault',
                '--debug',
            ],
            'oauth_no_confirm': True,
            'oauth_client_allowed_scopes': ['inherit'],
        })
        c = MagicMock()
        configure_jupyterhub_oidcp(
            c,
            admin_only=False,
            base_url="http://localhost:8000",
            internal_base_url="http://hub:8000",
            port=8089,
            debug=True,
            services=[
                {
                    "oauth_client_id": "TEST_CLIENT_ID",
                    "api_token": "TEST_CLIENT_SECRET",
                    "redirect_uris": ["http://localhost:9001/ep_openid_connect/callback"],
                }
            ],
            vault_path="./tmp/jupyterhub_oid/.vault",
        )
        c.JupyterHub.services.append.assert_called_once_with({
            'name': 'oidcp',
            'admin': False,
            'url': 'http://localhost:8089/services/oidcp',
            'display': False,
            'command': [
                sys.executable,
                '-m',
                'jupyterhub_oidcp.main',
                '--services',
                '[{"oauth_client_id": "TEST_CLIENT_ID", "api_token": "TEST_CLIENT_SECRET", '
                + '"redirect_uris": ["http://localhost:9001/ep_openid_connect/callback"]}]',
                '--port',
                '8089',
                '--base-url',
                'http://localhost:8000',
                '--internal-base-url',
                'http://hub:8000',
                '--vault-path',
                './tmp/jupyterhub_oid/.vault',
                '--debug',
            ],
            'oauth_no_confirm': True,
            'oauth_client_allowed_scopes': ['inherit'],
        })
