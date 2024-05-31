import tomllib
from dnschef import __version__
from dnschef.logger import log
from dnslib import RDMAP

header  = "-------------------------------------------------------------
header += "-------------------------------------------------------------
header += "-------------------------------------------------------------
header += "-------------------------------------------------------------
header += "-------------------------------------------------------------
header += "-------------------------------------------------------------
header += "-------------------------------------------------------------


def parse_config_file(config_file: str = "dnschef.toml"):
    log.debug("Parsing config file", path=config_file)
    with open(config_file, 'rb') as f:
        config = tomllib.load(f)

    for record, domains in config.items():
        if record not in RDMAP:
            log.warning(f"DNS record '{record}' is not supported. Contents will be ignored.")
            continue

        for domain, values in domains.items():
            if isinstance(values, dict):
                log.info("cooking file staging", section=record, domain=domain.lower(), file=values['file'])
            else:
                log.info("cooking replies", section=record, domain=domain.lower(), reply=values)

    return config
