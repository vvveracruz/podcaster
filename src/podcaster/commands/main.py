import json
from datetime import datetime
from typing import Optional

import click
from feedparser import parse


@click.group()
def cli():
    pass


@click.command()
@click.option(
    "-u",
    "--feed-url",
    help="RSS feed URL.",
    required=True,
)
@click.option(
    "-f",
    "--filename",
    help="Target filename where the resulting json will be saved.",
    required=False,
)
def feed_to_file(feed_url: str, filename: Optional[str] = None) -> None:
    d = parse(feed_url)
    if filename is None:
        filename = f"feed_exported_at_{datetime.now()}.json"
    with open(filename, "w") as f:
        json.dump(d, f)


cli.add_command(feed_to_file)

if __name__ == "__main__":
    cli()
