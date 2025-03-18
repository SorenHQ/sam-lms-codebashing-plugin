import requests
from fastapi import HTTPException
from src.api.middlewares.config_manager import ConfigManager

BASE_URL = "https://api.codebashing.com/api/v1"


def get_headers():
    config_manager = ConfigManager()
    credentials = config_manager.get_api_credentials()
    return {**credentials, "Content-Type": "application/json"}


# all available end-points for methods


def list_users():
    """Retrieve list of users from Codebashing."""
    params = {}
    response = requests.get(
        f"{BASE_URL}/users/details", headers=get_headers(), params=params, timeout=30
    )
    return response.json()


def list_courses(course_type=None):
    """Retrieve a list of courses from Codebashing."""
    try:
        params = {}
        if course_type:
            params["type"] = course_type
        response = requests.get(
            f"{BASE_URL}/courses/list", headers=get_headers(), params=params, timeout=30
        )

        # Check for HTTP errors
        response.raise_for_status()

        result = (
            response.json()
            if response.json()
            else {
                "status_code": response.status_code,
                "status": "error",
                "message": "No courses found",
            }
        )

        return result
    except Exception as e:
        raise HTTPException(status_code=500, detail="Failed to retrieve courses") from e


def get_course_lessons(course_uuid):
    """Retrieve lessons for a specific course."""
    response = requests.get(
        f"{BASE_URL}/courses/lessons_for_course/{course_uuid}",
        headers=get_headers(),
        timeout=30,
    )
    return response.json()


def add_users_to_team(team_uuid: str, users: list):
    """Add users to a specific team."""
    data = {"teamUuid": team_uuid, "users": [{"email": email} for email in users]}
    response = requests.post(
        f"{BASE_URL}/teams/add_users", headers=get_headers(), json=data, timeout=30
    )
    return response.json()


def invite_user(
    email: str,
    full_name: str = None,
    teams: list = None,
    cb_role: str = None,
    primary_course_id: str = None,
):
    """Send invitation to user(s) to join Codebashing."""
    data = {
        "invitations": [
            {
                "email": email,
                "fullName": full_name,
                "teams": [
                    {
                        "teamId": team_id,
                        "cbRole": cb_role,
                        "primaryCourseId": primary_course_id,
                    }
                    for team_id in (teams or [])
                ],
            }
        ]
    }
    response = requests.post(
        f"{BASE_URL}/invitations/invite", headers=get_headers(), json=data, timeout=30
    )
    return response.json()


def create_team(
    name,
    description,
    limit=None,
    users=None,
    managers=None,
    managerProgressIncluded=None,
):
    """Create a new team."""
    data = {
        "name": name,
        "description": description,
        "users": users or [],
    }

    if limit is not None:
        data["limit"] = limit
    if managers:
        data["managers"] = managers
    if managerProgressIncluded is not None:
        data["managerProgressIncluded"] = managerProgressIncluded

    # Remove any keys where the value is None
    data = {k: v for k, v in data.items() if v is not None}

    print("\n\n Data to be sent:", data, "\n\n")

    response = requests.post(
        f"{BASE_URL}/teams/create_team", headers=get_headers(), json=data, timeout=30
    )

    # Check for HTTP errors
    response.raise_for_status()
    return response.json()


def list_teams():
    """Retrieve list of Codebashing teams."""
    response = requests.get(f"{BASE_URL}/teams/list", headers=get_headers(), timeout=30)
    return response.json()


def get_team_info(team_uuid):
    """Retrieve lessons for a specific course."""
    response = requests.get(
        f"{BASE_URL}/teams/team_info?uuids={team_uuid}",
        headers=get_headers(),
        timeout=30,
    )
    return response.json()


def assign_course(course_id: str, users: list[str]):
    """Assign a course to user or team."""
    data = {
        "courseUuid": course_id,
        "users": users,
    }
    response = requests.post(
        f"{BASE_URL}/assignments/set_primary_course",
        headers=get_headers(),
        json=data,
        timeout=30,
    )
    return response.json()


def unassign_course(course_id: str, users: list[str]):
    """Unassign a course to user or team."""
    data = {
        "contentUuid": course_id,
        "users": users,
    }
    response = requests.delete(
        f"{BASE_URL}/assignments/unassigned",
        headers=get_headers(),
        json=data,
        timeout=30,
    )

    # Check for empty response
    if response.status_code == 204:
        return {
            "status_code": 204,
            "status": "success",
            "message": "No content, but operation was successful",
        }

    response.raise_for_status()
    return response.json()
