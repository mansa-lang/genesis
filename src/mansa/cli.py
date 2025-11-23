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

from . import __version__

def build_argparser():
    import argparse

    parser = argparse.ArgumentParser(
        prog="mansa",
        description="Mansa: Building the PERFECT systems language.",
        epilog=": Embryonic Bootstrapper for Building the PERFECT systems language.",
    )

    parser.add_argument(
        "--version",
        action="version",
        version=f"Mansa Genesis {__version__}",
    )

    return parser

def main():
    args = build_argparser().parse_args()
    
    print("Commands not implemented yet. Empire still rising.")
    return 1