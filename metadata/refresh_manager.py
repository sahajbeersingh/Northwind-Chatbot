import time

from metadata.schema_manager import refresh_metadata
from metadata.parser import parse_metadata
from metadata.generator import generate_context

last_refresh = 0

REFRESH_INTERVAL = 300


def refresh_if_needed():
    global last_refresh

    current_time = time.time()

    if current_time - last_refresh >= REFRESH_INTERVAL:
        refresh_metadata()
        parse_metadata()
        generate_context()
        last_refresh = current_time