# encoding: utf-8
# Copyright (C) 2012-2021 jrnl contributors
# License: https://www.gnu.org/licenses/gpl-3.0.html

import os
import re
import unicodedata

from jrnl.color import ERROR_COLOR
from jrnl.color import RESET_COLOR

from .text_exporter import TextExporter

ledger_known = [
        "asset",
        "expense",
        "liability",
        ]

class LedgerExporter(TextExporter):
    """This Exporter can convert entries and journals into ledger files."""

    names = ["ledger", "ldg"]
    extension = "ldg"

    @classmethod
    def export_entry(cls, entry):
        """Returns a string representation of a single entry."""

        date_str = entry.date.strftime(entry.journal.config["timeformat"])
        title = "{} {}".format(date_str, entry.title.rstrip("\n"))

        body = entry.body.rstrip("\n")

        only_ledger = ""
        for line in body.split("\n"):
            keyline = line.strip().lower()
            for key in ledger_known:
                if keyline.startswith(key):
                    only_ledger += " "  + line.strip().rstrip("\n") + "\n"
                    break

        return "{title}{sep}{body}".format(
                title=title,
                sep="\n",
                body=only_ledger.rstrip("\n"),
                )
