#!/usr/bin/python3
"""Generate invitation letters for a list of people"""
from os.path import exists


def generate_invitations(template, attendees):
    """Generate an invitation letter"""

    if not exists("template.txt"):
        raise FileNotFoundError("template.txt not found")

    if not attendees:
        return {'message': "No data provided, no output files generated."}

    if not template.strip():
        return {'error': "Template is empty, no output files generated."}

    if not isinstance(template, str):
        raise TypeError("Template should be a string.")
    if not isinstance(attendees, list):
        raise TypeError("Attendees should be a list.")

    for i, attendee in enumerate(attendees, start=1):

        if not isinstance(attendee, dict):
            raise TypeError("attendees should be a list of dictionaries")

        invit = template  # Copy of template

        attendee = {key: (value if value is not None else "{}: N/A"
                          .format(key)) for key, value in attendee.items()}

        invit = invit.replace("{name}", attendee.get("name", "name: N/A"))
        invit = invit.replace(
            "{event_date}", attendee.get("event_date", "event_date: N/A"))
        invit = invit.replace(
            "{event_location}",
            attendee.get("event_location", "event_location: N/A"))
        invit = invit.replace(
            "{event_title}", attendee.get("event_title", "event_title: N/A"))

        filename = "output_{}.txt".format(i)

        try:
            with open(filename, "w", encoding="utf-8") as f:
                f.write(invit)
        except Exception as e:
            return {'error': str(e)}
