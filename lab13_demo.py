
from app.agents.specialists.academic_agents import (
    AcademicMeetingCoordinator
)


coordinator = AcademicMeetingCoordinator()


# --------------------------------------------------
# TEST 1: Faculty Meeting
# --------------------------------------------------

print("\n1. FACULTY MEETING")

faculty_result = coordinator.organize_meeting(
    meeting_type="faculty",
    purpose="Discuss semester academic planning"
)

print("Specialist:", faculty_result["agent"])
print("Meeting type:", faculty_result["meeting_type"])
print("Purpose:", faculty_result["purpose"])

for number, topic in enumerate(faculty_result["agenda"], start=1):
    print(f"{number}. {topic}")


# --------------------------------------------------
# TEST 2: Examination Committee Meeting
# --------------------------------------------------

print("\n2. EXAMINATION COMMITTEE MEETING")

exam_result = coordinator.organize_meeting(
    meeting_type="examination",
    purpose="Discuss the upcoming semester examinations"
)

print("Specialist:", exam_result["agent"])

for number, topic in enumerate(exam_result["agenda"], start=1):
    print(f"{number}. {topic}")


# --------------------------------------------------
# TEST 3: Research Review Meeting
# --------------------------------------------------

print("\n3. RESEARCH REVIEW MEETING")

research_result = coordinator.organize_meeting(
    meeting_type="research",
    purpose="Review ongoing faculty research projects"
)

print("Specialist:", research_result["agent"])

for number, topic in enumerate(research_result["agenda"], start=1):
    print(f"{number}. {topic}")


# --------------------------------------------------
# TEST 4: Invalid Meeting Type
# --------------------------------------------------

print("\n4. TESTING INVALID MEETING TYPE")

try:
    coordinator.organize_meeting(
        meeting_type="sports",
        purpose="Discuss sports activities"
    )
except ValueError as error:
    print("VALIDATION BLOCKED:", error)


# --------------------------------------------------
# TEST 5: Missing Purpose
# --------------------------------------------------

print("\n5. TESTING MISSING PURPOSE")

try:
    coordinator.organize_meeting(
        meeting_type="faculty",
        purpose=""
    )
except ValueError as error:
    print("VALIDATION BLOCKED:", error)
