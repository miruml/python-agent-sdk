# Health

Types:

```python
from miru_agent_sdk.types import HealthCheckResponse
```

Methods:

- <code title="get /health">client.health.<a href="./src/miru_agent_sdk/resources/health.py">check</a>() -> <a href="./src/miru_agent_sdk/types/health_check_response.py">HealthCheckResponse</a></code>

# Version

Types:

```python
from miru_agent_sdk.types import VersionRetrieveResponse
```

Methods:

- <code title="get /version">client.version.<a href="./src/miru_agent_sdk/resources/version.py">retrieve</a>() -> <a href="./src/miru_agent_sdk/types/version_retrieve_response.py">VersionRetrieveResponse</a></code>

# Device

Types:

```python
from miru_agent_sdk.types import DeviceRetrieveResponse, DeviceSyncResponse
```

Methods:

- <code title="get /device">client.device.<a href="./src/miru_agent_sdk/resources/device.py">retrieve</a>() -> <a href="./src/miru_agent_sdk/types/device_retrieve_response.py">DeviceRetrieveResponse</a></code>
- <code title="post /device/sync">client.device.<a href="./src/miru_agent_sdk/resources/device.py">sync</a>() -> <a href="./src/miru_agent_sdk/types/device_sync_response.py">DeviceSyncResponse</a></code>
