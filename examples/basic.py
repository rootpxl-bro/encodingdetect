"""Minimal example for EncodingDetect."""

from encodingdetect import encodingdetect


def main():
 runner = encodingdetect({"name": "EncodingDetect", "dry_run": False})
 result = runner.execute()
 print(result)


if __name__ == "__main__":
 main()