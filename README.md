# nillion-sv-wrappers-py

Python implementation of the Nillion Secret Vault and NilQL wrappers. It is 100% inspired by the [nillion-sv-wrappers](https://github.com/NillionNetwork/nillion-sv-wrappers) repository by NillionNetwork.

## Installation

### From GitHub

```bash
pipenv install -e git+https://github.com/onchain-angels/nillion-sv-wrappers-py.git#egg=nillion-sv-wrappers-py
```

Alternatively, clone the repository and install it:

```bash
git clone https://github.com/onchain-angels/nillion-sv-wrappers-py.git
cd nillion-sv-wrappers-py
pip install -e .
```

## Usage

See the example in [examples/main.py](examples/main.py).

## Features

### SecretVaultWrapper

The SecretVaultWrapper provides an interface for Secret Vault API operations:

#### Authentication
- `init()`: Initializes the wrapper by generating JWT tokens and managing automatic authentication per node

#### Schema Operations
- `create_schema(schema, schema_name)`:
  - Deploys schema to all nodes via `/api/v1/schemas`
  - Allows custom IDs
  - Validates schema structure
  - Distributes to all nodes
- `get_schemas()`:
  - Lists available schemas via `/api/v1/schemas`
  - Retrieves configurations and metadata
- `delete_schema(schema_id)`:
  - Removes schema definition via `/api/v1/schemas`
  - Operates across all nodes preserving integrity

#### Data Operations
- `write_to_nodes(data)`:
  - Sends data via `/api/v1/data/create`
  - Encrypts fields marked with `%allot` and prepares encrypted shares for distribution across nodes.
  - Distributes encrypted shares marked with `$share` across nodes
- `read_from_nodes(filter)`:
  - Retrieves data via `/api/v1/data/read`
  - Recombines encrypted shares from nodes to reconstruct original records (automatically decrypts marked fields)
- `flush_data()`:
  - Removes all documents from the current schema via `/api/v1/data/flush`
  - Operates across all nodes

### NilQLWrapper
- Encrypts data into shares for distributed storage across nodes
- Handles structured data with `$allot` markers for selective encryption
- Recombines shares and decrypts data marked `$share` using unify
- Manages secret keys for encryption/decryption operations
- Recombines and decrypts shares to recover original data
- Maintains compatibility with SecretVault timestamps
- No node configuration required when used standalone


## Configuration

See the example in [examples/nilql_config.py](examples/nilql_config.py).

## Credits

This Python package is inspired by the original [nillion-sv-wrappers](https://github.com/NillionNetwork/nillion-sv-wrappers) repository by NillionNetwork.