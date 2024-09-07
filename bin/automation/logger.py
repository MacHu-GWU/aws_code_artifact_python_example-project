# -*- coding: utf-8 -*-

import os
from rich.console import Console

from .vislog import VisLog

logger = VisLog(
    name="automation",
    log_format="%(message)s",
)
logger.block = logger.start_and_end

if "CI" in os.environ:
    logger._logger.handlers.clear()

console = Console()
