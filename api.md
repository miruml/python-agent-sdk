# Health

Types:

```python
from miru_agent.types import HealthCheckResponse
```

Methods:

- <code title="get /health">client.health.<a href="./src/miru_agent/resources/health.py">check</a>() -> <a href="./src/miru_agent/types/health_check_response.py">HealthCheckResponse</a></code>

# Version

Types:

```python
from miru_agent.types import VersionRetrieveResponse
```

Methods:

- <code title="get /version">client.version.<a href="./src/miru_agent/resources/version.py">retrieve</a>() -> <a href="./src/miru_agent/types/version_retrieve_response.py">VersionRetrieveResponse</a></code>

# Device

Types:

```python
from miru_agent.types import DeviceRetrieveResponse, DeviceSyncResponse
```

Methods:

- <code title="get /device">client.device.<a href="./src/miru_agent/resources/device.py">retrieve</a>() -> <a href="./src/miru_agent/types/device_retrieve_response.py">DeviceRetrieveResponse</a></code>
- <code title="post /device/sync">client.device.<a href="./src/miru_agent/resources/device.py">sync</a>() -> <a href="./src/miru_agent/types/device_sync_response.py">DeviceSyncResponse</a></code>
