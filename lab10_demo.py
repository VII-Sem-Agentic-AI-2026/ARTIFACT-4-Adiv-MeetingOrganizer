from app.agents.resilient_agent import execute_with_retry


# TEST TASK 1: Immediate success

def successful_task():

    return {
        "meeting_status": "Availability checked",
        "available": True,
    }


# TEST TASK 2: Fail twice, then succeed

temporary_failure_count = 0


def temporary_failure_task():

    global temporary_failure_count

    temporary_failure_count += 1

    if temporary_failure_count < 3:
        raise ConnectionError(
            "Temporary calendar service failure."
        )

    return {
        "meeting_status": "Availability checked",
        "available": True,
    }


# TEST TASK 3: Always fail

def permanent_failure_task():

    raise ConnectionError(
        "Calendar service is unavailable."
    )


def main():

    print("\n========================================")
    print("       RESILIENT MEETING AGENT")
    print("========================================")

    # Test 1
    print("\nTEST 1: SUCCESSFUL TASK")

    result = execute_with_retry(
        successful_task,
        max_attempts=3
    )

    print("Final result:", result)

    # Test 2
    print("\n----------------------------------------")
    print("TEST 2: TEMPORARY FAILURE")

    result = execute_with_retry(
        temporary_failure_task,
        max_attempts=3
    )

    print("Final result:", result)

    # Test 3
    print("\n----------------------------------------")
    print("TEST 3: PERMANENT FAILURE")

    result = execute_with_retry(
        permanent_failure_task,
        max_attempts=3
    )

    print("Final result:", result)

    print("\n========================================")
    print("       RESILIENCE TESTS COMPLETED")
    print("========================================")


if __name__ == "__main__":
    main()