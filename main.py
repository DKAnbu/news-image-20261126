#!/usr/bin/env python3
"""
The Global Chronicle - 26 November 2026 Visual Summary Runner.
Pure Python 3.13 standard library entrypoint.
"""

from pathlib import Path
import shutil
import sys

def deploy_visual_entry() -> None:
    source_image = Path(__file__).resolve().parent / "entry.png"
    destination_directory = Path("/output")
    
    if not destination_directory.exists():
        destination_directory = Path(__file__).resolve().parent / "out"
    
    destination_directory.mkdir(parents=True, exist_ok=True)
    target_image = destination_directory / "entry.png"
    
    if not source_image.is_file():
        sys.stderr.write(f"Critical error: Source artifact {source_image} not found.\n")
        sys.exit(1)
        
    shutil.copyfile(source_image, target_image)
    image_bytes = target_image.stat().st_size
    print(f"Delivered {image_bytes:,} bytes -> {target_image}")

if __name__ == "__main__":
    deploy_visual_entry()
