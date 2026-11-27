#!/usr/bin/env python3
"""Entry program for make.fun news-image-20261127.

The front page image (entry.png, 1024x1024, drawn for Friday 27 November
2026) ships in this repository. This program copies it to the output
directory the grader provides, so both runs produce identical bytes.
"""
import argparse
import hashlib
import os
import shutil
import struct
import sys
from pathlib import Path

SOURCE = Path(__file__).resolve().parent / "entry.png"
TARGET_NAME = "entry.png"
MAX_BYTES = 1_048_576
MAX_SIDE = 1024
PNG_MAGIC = b"\x89PNG\r\n\x1a\n"


def png_dimensions(path: Path) -> tuple[int, int] | None:
    """Read width/height from a PNG IHDR chunk (stdlib only)."""
    with path.open("rb") as fh:
        header = fh.read(33)
    if len(header) < 33 or header[:8] != PNG_MAGIC:
        return None
    if header[12:16] != b"IHDR":
        return None
    width, height = struct.unpack(">II", header[16:24])
    return width, height


def output_dir() -> Path:
    return Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def verify(path: Path) -> list[str]:
    """Return a list of problems with the entry image (empty when fine)."""
    problems: list[str] = []
    if not path.is_file():
        return [f"missing: {path}"]
    size = path.stat().st_size
    if size > MAX_BYTES:
        problems.append(f"entry.png is {size} bytes, over the 1 MiB limit")
    if path.read_bytes()[:8] != PNG_MAGIC:
        problems.append("entry.png is not a PNG file")
        return problems
    dims = png_dimensions(path)
    if dims is None:
        problems.append("entry.png has no readable IHDR chunk")
    elif dims[0] > MAX_SIDE or dims[1] > MAX_SIDE:
        problems.append(
            f"entry.png is {dims[0]}x{dims[1]}, over the 1024x1024 limit")
    return problems


def run(dest: Path) -> int:
    problems = verify(SOURCE)
    if problems:
        for problem in problems:
            print(f"error: {problem}", file=sys.stderr)
        return 1
    dest.mkdir(parents=True, exist_ok=True)
    target = dest / TARGET_NAME
    shutil.copyfile(SOURCE, target)
    if sha256(target) != sha256(SOURCE):
        print("error: copied file differs from entry.png", file=sys.stderr)
        return 1
    problems = verify(target)
    if problems:
        for problem in problems:
            print(f"error: {problem}", file=sys.stderr)
        return 1
    print(f"wrote {target} ({target.stat().st_size} bytes, "
          f"sha256 {sha256(target)[:16]}...)")
    return 0


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(
        description="Copy the 27 November 2026 front page to the output dir.")
    parser.add_argument(
        "--verify-only", action="store_true",
        help="only check entry.png, do not write any output")
    args = parser.parse_args(argv)
    if args.verify_only:
        problems = verify(SOURCE)
        if problems:
            for problem in problems:
                print(f"error: {problem}", file=sys.stderr)
            return 1
        print(f"ok: entry.png ({SOURCE.stat().st_size} bytes, "
              f"sha256 {sha256(SOURCE)[:16]}...)")
        return 0
    return run(output_dir())


if __name__ == "__main__":
    raise SystemExit(main())
