from app.agents.parallel_meeting_workflow import (
    parallel_meeting_workflow
)


def main():

    print("\n========================================")
    print("       PARALLEL MEETING AGENT SWARM")
    print("========================================")

    # Meeting request shared by all specialists
    meeting_request = {

        "meeting_title": "Faculty Coordination Meeting",

        "purpose": "Discuss semester planning",

        "participants": [
            "Dr. Ravi",
            "Dr. Priya"
        ],

        "preferred_time": "12:00 PM",

        "duration": 60,
    }

    print("\nINITIAL MEETING REQUEST")
    print(meeting_request)

    print("\nSTARTING PARALLEL AGENTS...")

    # Execute the parallel workflow
    result = parallel_meeting_workflow.invoke(
        meeting_request
    )

    print("\n========================================")
    print("       COMBINED WORKFLOW RESULTS")
    print("========================================")

    print("\n1. Scheduling Results")

    print(result.get("availability"))

    print("\n2. Previous Meetings Retrieved")

    previous_meetings = result.get(
        "previous_meetings", []
    )

    print("Total meetings:", len(previous_meetings))

    for meeting in previous_meetings:
        print(meeting)

    print("\n3. Prepared Agenda")

    for item in result.get("agenda", []):
        print(
            f"- {item['topic']} "
            f"({item['minutes']} minutes)"
        )

    print("\nPARALLEL WORKFLOW COMPLETED.")


if __name__ == "__main__":
    main()