
from app.agents.meeting_planner import planner_graph


# Information required for a meeting
FIELD_PROMPTS = {
    "meeting_title": "Enter meeting title: ",
    "purpose": "Enter meeting purpose: ",
    "participants": "Enter participants (separate names with commas): ",
    "preferred_date": "Enter preferred date: ",
    "preferred_time": "Enter preferred time: ",
    "duration": "Enter duration in minutes: ",
}


def main():
    print("\n====================================")
    print("    MEETING PLANNING AGENT")
    print("====================================")

    print("\nDescribe your meeting request.")
    print("You can leave details blank if you are unsure.\n")

    details = {}

    for field, prompt in FIELD_PROMPTS.items():
        details[field] = input(prompt).strip()

    while True:

        # Send information to the LangGraph agent
        result = planner_graph.invoke({
            "details": details
        })

        # Check whether information is missing
        if result.get("missing_fields"):

            print("\nAGENT NEEDS MORE INFORMATION")
            print(result["clarification_message"])

            for field in result["missing_fields"]:
                details[field] = input(
                    f"Please provide {REQUIRED_LABEL(field)}: "
                ).strip()

            continue

        # Display the generated meeting plan
        print("\nAGENT GENERATED THIS PLAN:")
        print(result["plan"])

        # Allow the scheduler to revise the plan
        choice = input(
            "\nWould you like to revise any information? (yes/no): "
        ).strip().lower()

        if choice not in ("yes", "y"):
            print("\nMeeting plan prepared successfully.")
            print("Remember: This is a draft, not an approved meeting.")
            break

        print("\nWhich information would you like to revise?")

        fields = list(FIELD_PROMPTS.keys())

        for number, field in enumerate(fields, start=1):
            print(f"{number}. {FIELD_LABEL(field)}")

        try:
            selected = int(input("\nEnter the number: "))
            if selected < 1 or selected > len(fields):
                print("Invalid selection. Try again.")
                continue

            field = fields[selected - 1]
            details[field] = input(
                f"Enter the updated {FIELD_LABEL(field)}: "
            ).strip()

        except ValueError:
            print("Please enter a valid number.")


def FIELD_LABEL(field):
    return FIELD_PROMPTS[field].split("(")[0].replace("Enter ", "").replace(": ", "").strip()


def REQUIRED_LABEL(field):
    return FIELD_LABEL(field)


if __name__ == "__main__":
    main()
