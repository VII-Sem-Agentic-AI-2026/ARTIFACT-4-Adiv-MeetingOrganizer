
from app.runtime.runtime_manager import AgentRuntime


def main():

    print("\n========================================")
    print("       AGENT RUNTIME DEMONSTRATION")
    print("========================================")

    # Step 1: Initialize runtime
    print("\n1. INITIALIZING AGENT RUNTIME")

    runtime = AgentRuntime(max_steps=5)

    print("Runtime initialized.")
    print("Maximum execution steps:", runtime.max_steps)

    # Step 2: Execute workflow operations
    print("\n2. EXECUTING AGENT OPERATIONS")

    runtime.check_budget()
    runtime.record_activity(
        "Validate meeting request",
        "Meeting details validated",
    )
    runtime.save_checkpoint("request_validation")

    print("Step 1 completed: Meeting request validated.")

    runtime.check_budget()
    runtime.record_activity(
        "Retrieve previous meetings",
        "Previous meeting records retrieved",
    )
    runtime.save_checkpoint("memory_retrieval")

    print("Step 2 completed: Previous meetings retrieved.")

    # Step 3: Request human approval
    print("\n3. REQUESTING HUMAN APPROVAL")

    approval = runtime.request_approval(
        "Schedule the proposed faculty meeting"
    )

    print(approval)

    # Step 4: Get approval decision
    print("\n4. HUMAN APPROVAL")

    decision = input(
        "Approve this action? (yes/no): "
    ).strip().lower()

    if decision == "yes":

        runtime.record_approval(True)

        print("Approval granted.")

    else:

        runtime.record_approval(False)

        print("Approval rejected.")

    # Step 5: Display checkpoint
    print("\n5. CURRENT CHECKPOINT")

    print(runtime.show_checkpoint())

    # Step 6: Display audit history
    print("\n6. AUDIT LOG")

    print(runtime.show_audit_log())

    # Step 7: Test execution budget
    print("\n7. TESTING EXECUTION BUDGET")

    budget_test = AgentRuntime(max_steps=2)

    for step in range(1, 4):

        try:
            budget_test.check_budget()
            print(f"Execution step {step}: Allowed.")

        except RuntimeError as error:
            print(f"Execution step {step}: Blocked.")
            print("Reason:", error)

    print("\nRUNTIME DEMONSTRATION COMPLETED.")


if __name__ == "__main__":
    main()
