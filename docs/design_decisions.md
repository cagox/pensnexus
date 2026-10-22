Here I will note some of my design decisions.  Some of these decisions may not be fully realized until later, but they need to be considered from the beginning when making other decisions.

# Redis
This one is pretty simple. I will use redis as a caching layer. Most things can be cached in redis. If it is not ther, then they will be pulled from the database. If it is pulled from the database, it will then be cached in redis. Especialy for items expected to be used often.

# Database replication
The project will start with a single node, but I do hope for it to grow someday. If it is to grow, then it needs to be able to function in a distributed way. I will take the following steps to facilitate this from the start.

- First, the config file will have a unique integer node_id.
- instead of BIGINT, the index key for objects will be a UUID.
- I will use UUID 6 so that the UUID can incorporate the node_id.

This way when data replication takes place, it does not depend on an ID number that might be accidentally created on two systems at the same time. Collision is 'unlikely' on a small scale system, but much more likely on a larger system with multiple machine generating data.

# Environmental Variables
The location of the config file will be an environmental variable "PENS_CONF"

The various cryptographic secrets will be stored using systemd-creds. If a future user wants to install the software on a system that does not support systemd, we can figure that out when it's needed.
