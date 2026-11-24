
from app.agents.meeting_workflow import meeting_workflow


def main():

    print("\n========================================")
    print("       AGENTIC MEETING WORKFLOW")
    print("========================================")

    # Initial meeting request
    meeting_request = {
        "meeting_title": "Faculty Coordination Meeting",
        "purpose": "Discuss semester planning",
        "participants": ["Dr. Ravi", "Dr. Priya"],
        "preferred_date": "2026-11-16",
        "preferred_time": "12:00 PM",
        "duration": 60,
    }

    print("\nINITIAL MEETING REQUEST")
    print(meeting_request)

    # Execute the LangGraph workflow
    print("\nSTARTING WORKFLOW...")

    result = meeting_workflow.invoke(meeting_request)

    # Display final workflow results
    print("\n========================================")
    print("       WORKFLOW RESULTS")
    print("========================================")

    print("\nValidation status:")
    print(result.get("request_valid"))

    print("\nAvailability:")
    print(result.get("availability"))

    print("\nPrevious meetings retrieved:")
    print(len(result.get("previous_meetings", [])))

    print("\nPrepared agenda:")

    for item in result.get("agenda", []):
        print(
            f"- {item['topic']} "
            f"({item['minutes']} minutes)"
        )

    print("\nApproval status:")
    print(result.get("approval_status"))

    print("\nWORKFLOW EXECUTION COMPLETED.")


if __name__ == "__main__":
    main()
