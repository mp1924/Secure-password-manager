"""
Entry point for the Secure Password Manager.
"""

import logging
import sys

from gui.app import run_app


def main() -> None:
    """
    Start the Secure Password Manager application.
    """
    logging.basicConfig(
        level=logging.INFO,
        format="%(asctime)s | %(levelname)s | %(name)s | %(message)s",
    )

    try:
        run_app()
    except KeyboardInterrupt:
        logging.info("Application closed by the user.")
    except Exception:
        logging.exception("An unexpected error occurred.")
        sys.exit(1)


if __name__ == "__main__":
    main()