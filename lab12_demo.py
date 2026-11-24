
from app.agents.gov_agent import GovernanceManager


governance = GovernanceManager()

# --------------------------------------------------
# TEST 1: Scheduler submits a meeting invitation
# --------------------------------------------------

print("\n1. CREATING MEETING REQUEST")

print(
    governance.request_operation(
        request_id="REQ001",
        requester="scheduler_01",
        requester_role="scheduler",
        operation="Send meeting invitation"
    )
)

# --------------------------------------------------
# TEST 2: Execution before approval must be blocked
# --------------------------------------------------

print("\n2. TESTING APPROVAL GATE")

try:
    governance.execute_if_approved("REQ001")
except PermissionError as error:
    print("BLOCKED:", error)

# --------------------------------------------------
# TEST 3: Scheduler cannot approve the request
# --------------------------------------------------

print("\n3. TESTING ROLE-BASED ACCESS")

try:
    governance.decide(
        request_id="REQ001",
        approver="scheduler_02",
        approver_role="scheduler",
        decision="approved"
    )
except PermissionError as error:
    print("ACCESS DENIED:", error)

# --------------------------------------------------
# TEST 4: Faculty approves the request
# --------------------------------------------------

print("\n4. FACULTY APPROVAL")

print(
    governance.decide(
        request_id="REQ001",
        approver="faculty_01",
        approver_role="faculty",
        decision="approved"
    )
)

# --------------------------------------------------
# TEST 5: Execute after approval
# --------------------------------------------------

print("\n5. EXECUTING APPROVED OPERATION")

print(governance.execute_if_approved("REQ001"))

# --------------------------------------------------
# TEST 6: Rollback simulation
# --------------------------------------------------

print("\n6. TESTING ROLLBACK")

print(
    governance.rollback(
        request_id="REQ001",
        actor="faculty_01",
        actor_role="faculty"
    )
)

# --------------------------------------------------
# TEST 7: Rejected request cannot execute
# --------------------------------------------------

print("\n7. TESTING REJECTED REQUEST")

governance.request_operation(
    request_id="REQ002",
    requester="scheduler_01",
    requester_role="scheduler",
    operation="Book meeting room"
)

governance.decide(
    request_id="REQ002",
    approver="faculty_01",
    approver_role="faculty",
    decision="rejected"
)

try:
    governance.execute_if_approved("REQ002")
except PermissionError as error:
    print("BLOCKED:", error)

# --------------------------------------------------
# TEST 8: Confidentiality
# --------------------------------------------------

print("\n8. TESTING CONFIDENTIALITY")

meeting_details = {
    "title": "Faculty Coordination Meeting",
    "purpose": "Semester planning",
    "confidential_notes": "Internal faculty discussion"
}

scheduler_view = governance.get_meeting_details(
    user="scheduler_01",
    user_role="scheduler",
    details=meeting_details
)

faculty_view = governance.get_meeting_details(
    user="faculty_01",
    user_role="faculty",
    details=meeting_details
)

print("Scheduler view:", scheduler_view)
print("Faculty view:", faculty_view)

# --------------------------------------------------
# TEST 9: Display audit history
# --------------------------------------------------

print("\n9. AUDIT LOG")

for event in governance.show_audit_log():
    print(event)
