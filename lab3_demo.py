from app.skills.meeting_validation import validate_meeting
from app.skills.agenda_preparation import prepare_agenda
from app.skills.meeting_formatting import format_meeting_plan


def main():

    print("\n========================================")
    print("       MEETING SKILLS DEMONSTRATION")
    print("========================================")

    # Sample meeting request
    details = {
        "meeting_title": "Faculty Coordination Meeting",
        "purpose": "Discuss semester planning",
        "participants": "Dr. Ravi, Dr. Priya",
        "preferred_date": "Next Monday",
        "preferred_time": "11:00 AM",
        "duration": "60",
    }

    # Skill 1: Validate meeting information
    validation = validate_meeting(details)

    print("\nVALIDATION RESULT:")

    if not validation["valid"]:
        for error in validation["errors"]:
            print("-", error)

        print("\nMeeting preparation stopped.")
        return

    print("Meeting information is valid.")

    # Skill 2: Prepare meeting agenda
    agenda = prepare_agenda(
        details["purpose"],
        validation["duration"],
    )

    print("\nAGENDA PREPARED SUCCESSFULLY.")

    # Skill 3: Format meeting plan
    meeting_plan = format_meeting_plan(
        details,
        validation["participants"],
        agenda,
    )

    print(meeting_plan)


if __name__ == "__main__":
    main()