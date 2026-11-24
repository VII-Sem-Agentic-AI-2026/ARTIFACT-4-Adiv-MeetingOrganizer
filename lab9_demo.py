from app.agents.grounding_agent import (
    generate_grounded_response
)


def main():

    print("\n========================================")
    print("       EVIDENCE-BASED MEETING AGENT")
    print("========================================")

    query = "semester planning"

    # Test 1: A claim supported by stored records
    supported_claim = (
        "Semester planning review will be completed."
    )

    print("\nTEST 1: SUPPORTED CLAIM")

    result = generate_grounded_response(
        query,
        supported_claim
    )

    print("\nClaim:")
    print(supported_claim)

    print("\nValidation:")
    print(result["validation"])

    print("\nAgent Answer:")
    print(result["answer"])

    # Test 2: A claim not supported by stored records
    unsupported_claim = (
        "The examination timetable was finalized "
        "and approved by all faculty members."
    )

    print("\n----------------------------------------")
    print("TEST 2: UNSUPPORTED CLAIM")

    result = generate_grounded_response(
        query,
        unsupported_claim
    )

    print("\nClaim:")
    print(unsupported_claim)

    print("\nValidation:")
    print(result["validation"])

    print("\nAgent Answer:")
    print(result["answer"])

    print("\n========================================")
    print("       GROUNDING TESTS COMPLETED")
    print("========================================")


if __name__ == "__main__":
    main()