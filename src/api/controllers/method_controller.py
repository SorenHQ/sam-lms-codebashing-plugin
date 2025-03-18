from typing import Dict, Any
from fastapi import HTTPException
from src.api.services.codebashing_api import (
    list_users,
    list_courses,
    get_course_lessons,
    create_team,
    get_team_info,
    list_teams,
    add_users_to_team,
    invite_user,
    assign_course,
    unassign_course,
)


class MethodExecutor:
    def __init__(self):
        self.method_handlers = {
            "list_users": self.handle_list_users,
            "list_courses": self.handle_list_courses,
            "get_course_lessons": self.handle_get_course_lessons,
            "create_team": self.handle_create_team,
            "list_teams": self.handle_list_teams,
            "get_team_info": self.handle_get_team_info,
            "add_users_to_team": self.handle_add_users_to_team,
            "invite_user": self.handle_invite_user,
            "assign_course": self.handle_assign_course,
            "unassign_course": self.handle_unassign_course,
        }

    async def execute(self, method_name: str, data: Dict[str, Any]):
        handler = self.method_handlers.get(method_name)
        if not handler:
            raise HTTPException(status_code=404, detail="Method not found")
        return await handler(data)

    async def handle_list_users(self, _):
        return list_users()

    async def handle_list_courses(self, data: Dict[str, Any]):
        params = data.get("params", [])
        course_type = (
            params[0].get("value", [])[0]
            if len(params) > 0 and len(params[0]["value"])
            else None
        )
        result = list_courses(course_type)
        return result

    async def handle_get_course_lessons(self, data: Dict[str, Any]):
        course_uuid = data.get("params", [])[0].get("value", [])[0]
        if not course_uuid:
            raise HTTPException(status_code=400, detail="Course UUID is required")
        return get_course_lessons(course_uuid)

    async def handle_create_team(self, data: Dict[str, Any]):
        try:
            params = data.get("params", [])
            param_dict = {param["key"]: param["value"] for param in params}

            # Extract and validate required parameters
            name_values = param_dict.get("name", [])
            description_values = param_dict.get("description", [])
            int_limit = int(param_dict.get("limit", [0])[0])
            users_values = param_dict.get("users", [])

            if not name_values or not name_values[0]:
                raise HTTPException(status_code=400, detail="Team name is required")
            if not description_values or not description_values[0]:
                raise HTTPException(
                    status_code=400, detail="Team description is required"
                )
            if not users_values or not users_values[0]:
                raise HTTPException(
                    status_code=400, detail="At least one user is required"
                )

            name = name_values[0]
            description = description_values[0]
            users = users_values

            result = create_team(
                name=name,
                description=description,
                limit=int_limit,
                users=users,
                managers=param_dict.get("managers", []),
            )

            return result
        except Exception as e:
            raise HTTPException(status_code=500, detail="Failed to create team") from e

    async def handle_list_teams(self, _):
        return list_teams()

    async def handle_get_team_info(self, data: Dict[str, Any]):
        team_uuid = data.get("params", [])[0].get("value", [])[0]
        if not team_uuid:
            raise HTTPException(status_code=400, detail="Team UUID is required")
        return get_team_info(team_uuid)

    async def handle_add_users_to_team(self, data: Dict[str, Any]):
        team_uuid = data.get("teamUuid")
        users = data.get("users")
        if not team_uuid or not users:
            raise HTTPException(
                status_code=400, detail="Team UUID and users are required"
            )
        return add_users_to_team(team_uuid, users)

    async def handle_invite_user(self, data: Dict[str, Any]):
        params = data.get("params", [])
        params_dict = {param["key"]: param["value"] for param in params}

        email = (
            params_dict.get("email", [])[0]
            if params_dict.get("email") and len(params_dict.get("email", [])) > 0
            else None
        )
        full_name = (
            params_dict.get("fullName", [])[0]
            if params_dict.get("fullName") and len(params_dict.get("fullName", [])) > 0
            else None
        )
        teams = (
            params_dict.get("teams", [])
            if params_dict.get("teams") and len(params_dict.get("teams", [])) > 0
            else None
        )
        cb_role = (
            params_dict.get("cbRole", [])[0]
            if params_dict.get("cbRole") and len(params_dict.get("cbRole", [])) > 0
            else None
        )
        primary_course_id = (
            params_dict.get("primaryCourseId", [])[0]
            if params_dict.get("primaryCourseId")
            and len(params_dict.get("primaryCourseId", [])) > 0
            else None
        )

        if not email or not teams:
            raise HTTPException(status_code=400, detail="Email and teams is required")
        result = invite_user(
            email=email,
            full_name=full_name,
            teams=teams,
            cb_role=cb_role,
            primary_course_id=primary_course_id,
        )

        return result

    async def handle_assign_course(self, data: Dict[str, Any]):
        try:
            params = data.get("params", [])
            params_dict = {param["key"]: param["value"] for param in params}

            course_id = params_dict.get("course_id")[0]
            users = params_dict.get("users")

            if not all([course_id, users]):
                raise HTTPException(
                    status_code=400, detail="Missing required parameters"
                )
            result = assign_course(course_id, users)
            print("\n\n Result of Request: ", result, "\n\n")
            return result
        except Exception as e:
            raise HTTPException(
                status_code=500, detail="Failed to assign course"
            ) from e

    async def handle_unassign_course(self, data: Dict[str, Any]):
        try:
            params = data.get("params", [])
            params_dict = {param["key"]: param["value"] for param in params}

            course_id = params_dict.get("course_id")[0]
            users = params_dict.get("users")

            if not all([course_id, users]):
                raise HTTPException(
                    status_code=400, detail="Missing required parameters"
                )
            result = unassign_course(course_id, users)
            print("\n\n Result of Request: ", result, "\n\n")
            return result
        except Exception as e:
            print("\n\n Error in unassign_course: ", e, "\n\n")
            raise HTTPException(
                status_code=500, detail="Failed to unassign the course"
            ) from e
