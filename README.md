# zbx_blockdevices_template

Zabbix template for block devices.

Actually all necessary items already supported by the zabbix agent.
This project just provides discovery feature for automatical creation of all block devices found on the system.

In different OS versions zabbix agent supports different block device items
(https://www.zabbix.com/documentation/1.8/manual/config/items#supported_by_platform):
```
OS/Item   |  operations  |  bytes  |  sectors
Linux 2.4 |      X       |    —    |     X
Linux 2.6 |      X       |    —    |     X
FreeBSD   |      X       |    X    |     —
```

This is why the template contains both: bytes and sectors items.


## System requirements

- lsblk (for Ubuntu and Debian: `apt-get install util-linux`)


## Installation

1) Put `zbx_blockdevices.py` into your monitoring scripts path (like: `/usr/local/bin/`)

2) In scripts path (`/usr/local/bin`) do:
```
chmod a+x zbx_blockdevices.py
```

3) Put `userparameter_blockdev.conf` into `/etc/zabbix/zabbix_agentd.d` directory or add it's 
content to the agent's configuration file `/etc/zabbix/zabbix_agentd.conf`

4) Import `zbx_blockdev_template.xml` into zabbix in Tepmplate section web gui

Enjoy :-)

