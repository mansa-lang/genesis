# Copyright [2025] Rufai Limantawa <rufailimantawa@gmail.com>

# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at

#     http://www.apache.org/licenses/LICENSE-2.0

# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import argparse
from . import __version__


def build_argparser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        prog="mansa",
        description="Mansa: Building the PERFECT systems language.",
        epilog=": Embryonic Bootstrapper for Building the PERFECT systems language.",
        add_help=False,
    )

    parser.add_argument(
        "-V",
        "--version",
        action="version",
        version=f"Mansa Genesis {__version__}",
        help="Show the version number and exit.",
    )

    parser.add_argument(
        "-h",
        "--help",
        action="help",
        default=argparse.SUPPRESS,
        help="Show this help message and exit.",
    )

    return parser


def main() -> int:
    parser = build_argparser()
    args, argv = parser.parse_known_args()

    if argv:
        print(f"Command: '{argv[0]}' not yet implemented.")
        print("Empire still rising. Patience, citizen.")
        return 1
    if getattr(args, "command", None) is not None:
        if args.command == "help" or args.command is None:
            parser.print_help()
            return 0

    parser.print_help()
    return 1
