#!/usr/bin/env python3
# Copyright 2019 Pants project contributors (see CONTRIBUTORS.md).
# Licensed under the Apache License, Version 2.0 (see LICENSE).

import shutil
import subprocess
from glob import glob

from common import die, green


def main() -> None:
  ensure_shellcheck_installed()
  run_shellcheck()


def ensure_shellcheck_installed() -> None:
  if shutil.which("shellcheck") is None:
    die("`shellcheck` not installed! You may download this your operating system's package manager, "
        "such as brew, apt, or yum. See https://github.com/koalaman/shellcheck#installing.")


def run_shellcheck() -> None:
  targets = glob("./**/*.sh", recursive=True) + ["./pants"]
  command = ["shellcheck", "--shell=bash"] + targets
  try:
    subprocess.run(command, check=True)
  except subprocess.CalledProcessError:
    die("Please fix the above errors and run again.")
  else:
    green("./pants passed the shellcheck!")


if __name__ == "__main__":
  main()