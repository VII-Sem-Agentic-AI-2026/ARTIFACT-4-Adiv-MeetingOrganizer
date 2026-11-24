from app.memory.meeting_memory import (
    save_meeting,
    search_meetings,
    get_recent_meetings,
)


def main():

    print("\n========================================")
    print("       MEETING MEMORY DEMONSTRATION")
    print("========================================")

    # Step 1: Store a previous meeting
    print("\n1. SAVING MEETING TO LONG-TERM MEMORY")

    meeting_id = save_meeting(
        meeting_title="Faculty Coordination Meeting",
        purpose="Discuss semester planning",
        meeting_date="2026-11-13",
        participants="Dr. Ravi, Dr. Priya",
        decisions="Semester planning review will be completed.",
        notes="Faculty discussed the upcoming semester schedule.",
    )

    print(f"Meeting saved successfully. ID: {meeting_id}")

    # Step 2: Retrieve information using a keyword
    print("\n2. SEARCHING PREVIOUS MEETINGS")

    results = search_meetings("semester")

    if results:

        for meeting in results:

            print("\nMeeting found:")
            print("Title:", meeting["meeting_title"])
            print("Purpose:", meeting["purpose"])
            print("Date:", meeting["meeting_date"])
            print("Participants:", meeting["participants"])
            print("Decisions:", meeting["decisions"])

    else:
        print("No matching meetings found.")

    # Step 3: Retrieve recent meetings
    print("\n3. RETRIEVING RECENT MEETINGS")

    recent_meetings = get_recent_meetings()

    print(f"Total records retrieved: {len(recent_meetings)}")

    for meeting in recent_meetings:
        print("-", meeting["meeting_title"])

    print("\nMemory demonstration completed.")


if __name__ == "__main__":
    main()