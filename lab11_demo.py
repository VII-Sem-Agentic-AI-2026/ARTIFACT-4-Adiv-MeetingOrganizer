from app.agents.sdlc_agent import execute_sdlc_pipeline


def display_results(result):

    print("\nSPECIFICATION")
    print(result["specification"])

    print("\nGENERATED AGENDA")

    for item in result["output"]["agenda"]:
        print(
            f"- {item['topic']} "
            f"({item['minutes']} minutes)"
        )

    print("\nVALIDATION RESULTS")
    print(result["validation"])

    print("\nACCEPTANCE TEST RESULTS")

    for test, passed in result["testing"]["tests"].items():
        print(f"{test}: {passed}")

    print(
        f"\nTests passed: "
        f"{result['testing']['passed']}/"
        f"{result['testing']['total']}"
    )

    print("\nRELEASE DECISION")
    print(result["release_approved"])


def main():

    print("\n========================================")
    print("          MEETING SDLC FACTORY")
    print("========================================")

    # TEST 1: Valid meeting specification

    print("\nTEST 1: VALID MEETING REQUEST")

    result = execute_sdlc_pipeline(
        meeting_title="Faculty Coordination Meeting",
        purpose="Discuss semester planning",
        participants=["Dr. Ravi", "Dr. Priya"],
        duration=60,
    )

    display_results(result)

    # TEST 2: Invalid meeting specification

    print("\n----------------------------------------")
    print("TEST 2: INVALID MEETING REQUEST")

    result = execute_sdlc_pipeline(
        meeting_title="",
        purpose="Discuss semester planning",
        participants=[],
        duration=60,
    )

    display_results(result)

    print("\n========================================")
    print("          SDLC TESTS COMPLETED")
    print("========================================")


if __name__ == "__main__":
    main()