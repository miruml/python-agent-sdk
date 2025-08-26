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

# ConfigInstances

Types:

```python
from miru_agent.types import ConfigInstanceRetrieveLatestResponse
```

Methods:

- <code title="get /config_instances/deployed">client.config_instances.<a href="./src/miru_agent/resources/config_instances.py">retrieve_latest</a>(\*\*<a href="src/miru_agent/types/config_instance_retrieve_latest_params.py">params</a>) -> <a href="./src/miru_agent/types/config_instance_retrieve_latest_response.py">ConfigInstanceRetrieveLatestResponse</a></code>

# ConfigSchemas

## Hash

Types:

```python
from miru_agent.types.config_schemas import HashSerializeResponse
```

Methods:

- <code title="post /config_schemas/hash/serialized">client.config_schemas.hash.<a href="./src/miru_agent/resources/config_schemas/hash.py">serialize</a>(\*\*<a href="src/miru_agent/types/config_schemas/hash_serialize_params.py">params</a>) -> <a href="./src/miru_agent/types/config_schemas/hash_serialize_response.py">HashSerializeResponse</a></code>

# Device

Types:

```python
from miru_agent.types import DeviceRetrieveResponse, DeviceSyncResponse
```

Methods:

- <code title="get /device">client.device.<a href="./src/miru_agent/resources/device.py">retrieve</a>() -> <a href="./src/miru_agent/types/device_retrieve_response.py">DeviceRetrieveResponse</a></code>
- <code title="post /device/sync">client.device.<a href="./src/miru_agent/resources/device.py">sync</a>() -> <a href="./src/miru_agent/types/device_sync_response.py">DeviceSyncResponse</a></code>

# ExampleError

Types:

```python
from miru_agent.types import ExampleErrorRetrieveResponse
```

Methods:

- <code title="get /example-error">client.example_error.<a href="./src/miru_agent/resources/example_error.py">retrieve</a>() -> <a href="./src/miru_agent/types/example_error_retrieve_response.py">ExampleErrorRetrieveResponse</a></code>
