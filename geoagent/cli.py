"""GeoAgent CLI.

Commands:
  geoagent ui        Launch the Solara UI
  geoagent --help    Show help
"""

from __future__ import annotations

import argparse


def _run_solara_ui() -> int:
    try:
        from geoagent.ui import launch_ui
    except Exception as e:
        print(f"Failed to locate UI app: {e}")
        return 1

    try:
        return launch_ui()
    except RuntimeError as e:
        print(f"{e}\nInstall with `pip install geoagent[ui]`.\n")
        return 1


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(
        prog="geoagent",
        description="GeoAgent command line interface",
    )
    subparsers = parser.add_subparsers(dest="command", metavar="command")

    subparsers.add_parser("ui", help="Launch the Solara UI")

    args = parser.parse_args(argv)

    if args.command == "ui":
        return _run_solara_ui()

    # No command: show help
    parser.print_help()
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
