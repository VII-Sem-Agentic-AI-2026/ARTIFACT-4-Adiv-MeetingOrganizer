from app.agents.meeting_assistant import meeting_assistant


def main():

    print("\n========================================")
    print("     MEETING ASSISTANT AGENT")
    print("========================================")

    participants = input(
        "\nEnter participants (separate names with commas): "
    )

    preferred_time = input(
        "Enter proposed meeting start time (e.g. 10:00 AM): "
    )

    duration = int(
        input("Enter meeting duration in minutes: ")
    )

    result = meeting_assistant.invoke({
        "participants_input": participants,
        "preferred_time": preferred_time,
        "duration": duration,
    })

    print(result["report"])

    print("Analysis completed successfully.")
    print("This is an availability report, not a confirmed booking.")


if __name__ == "__main__":
    main()