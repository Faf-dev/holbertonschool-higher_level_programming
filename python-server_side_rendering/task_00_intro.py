#!/usr/bin/python3
"""Generate invitation letters for a list of people"""
from os.path import exists


def generate_invitations(template, attendees):
    """Generate an invitation letter"""

    if not exists("template.txt"):
        raise FileNotFoundError("template.txt not found")

    if not attendees:
        print("Error: No data provided, no output files generated.")
        return

    if not template:
        raise ValueError("Template is empty, no output files generated.")

    if not isinstance(template, str):
        print("Error: Template should be a string.")
        return
    if not isinstance(attendees, list):
        print("Error: Attendees should be a list.")
        return

    for i, attendee in enumerate(attendees, start=1):

        if not isinstance(attendee, dict):
            raise TypeError("attendees should be a list of dictionaries")

        invit = template  # Copy of template

        invit = invit.replace("{name}", attendee.get("name", "{name}"))
        invit = template.format(
            name=attendee.get("name", "N/A"),
            event_title=attendee.get("event_title", "N/A"),
            event_date=attendee.get("event_date", "N/A"),
            event_location=attendee.get("event_location", "N/A"),
        )

        filename = "output_{}.txt".format(i)

        with open(filename, "w", encoding="utf-8") as f:
            f.write(invit)
