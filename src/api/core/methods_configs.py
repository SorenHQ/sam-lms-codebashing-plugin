methods_configs = [
    {
        "name": "list_users",
        "title": "List Users",
        "description": "Retrieve all users from the Codebashing platform",
        "params": [{}],
    },
    {
        "name": "get_team_info",
        "title": "Team Information",
        "description": "Retrieve detailed information about a specific team",
        "params": [
            {
                "attr": {
                    "regex_pattern": {
                        "pattern": "^[a-zA-Z0-9-]+$",
                        "message": "Invalid team UUID format",
                    },
                    "input_type": "string",
                    "secret": False,
                    "required": True,
                },
                "key": "uuid",
                "placeholder": "Enter team UUID",
                "value": [""],
                "title": "Team UUID",
                "description": "Unique identifier for the team",
            },
        ],
    },
    {
        "name": "list_courses",
        "title": "List of Courses",
        "description": "Retrieve all available courses in the learning management system",
        "params": [
            {
                "attr": {
                    "regex_pattern": None,
                    "input_type": "string",
                    "secret": False,
                    "required": False,
                },
                "options": [
                    {"value": "system", "title": "System Courses"},
                    {"value": "custom", "title": "Custom Courses"},
                ],
                "key": "type",
                "placeholder": "Filter courses by type",
                "value": [""],
                "title": "Course Type",
                "description": "Optional filter for course type",
            }
        ],
    },
    {
        "name": "get_course_lessons",
        "title": "Course Lessons",
        "description": "Retrieve all lessons for a specific course",
        "params": [
            {
                "attr": {
                    "regex_pattern": {
                        "pattern": "^[a-zA-Z0-9-]+$",
                        "message": "Invalid course UUID format",
                    },
                    "input_type": "string",
                    "secret": False,
                    "required": True,
                },
                "key": "uuid",
                "placeholder": "Enter course UUID",
                "value": [""],
                "title": "Course UUID",
                "description": "Unique identifier for the course",
            }
        ],
    },
    {
        "name": "create_team",
        "title": "Create Team",
        "description": "Create a new team in the learning management system",
        "params": [
            {
                "attr": {
                    "regex_pattern": {
                        "pattern": "^[a-zA-Z0-9 ]{3,50}$",
                        "message": "Team name must be 3-50 alphanumeric characters",
                    },
                    "input_type": "string",
                    "secret": False,
                    "required": True,
                },
                "key": "name",
                "placeholder": "Enter team name",
                "value": [""],
                "title": "Team Name",
                "description": "Name of the team to be created",
            },
            {
                "attr": {
                    "regex_pattern": None,
                    "input_type": "string",
                    "secret": False,
                    "required": False,
                },
                "key": "description",
                "placeholder": "Optional team description",
                "value": [""],
                "title": "Team Description",
                "description": "Optional description for the team",
            },
            {
                "attr": {
                    "regex_pattern": None,
                    "input_type": "number",
                    "secret": False,
                    "required": False,
                },
                "key": "limit",
                "placeholder": "Maximum number of users",
                "value": [0],
                "title": "User Limit",
                "description": "Maximum number of users in the team",
            },
            {
                "attr": {
                    "regex_pattern": None,
                    "input_type": "string[]",
                    "secret": False,
                    "required": True,
                },
                "key": "users",
                "placeholder": "Enter user emails",
                "value": [],
                "title": "Users",
                "description": "List of user emails to add to the team",
            },
            {
                "attr": {
                    "regex_pattern": None,
                    "input_type": "string[]",
                    "secret": False,
                    "required": False,
                },
                "key": "managers",
                "placeholder": "Enter manager emails",
                "value": [],
                "title": "Managers",
                "description": "List of manager emails to add to the team",
            },
        ],
    },
    {
        "name": "add_users_to_team",
        "title": "Add Users to Team",
        "description": "Add multiple users to a specific team",
        "params": [
            {
                "attr": {
                    "regex_pattern": {
                        "pattern": "^[a-zA-Z0-9-]+$",
                        "message": "Invalid team UUID format",
                    },
                    "input_type": "string",
                    "secret": False,
                    "required": True,
                },
                "key": "teamUuid",
                "placeholder": "Enter team UUID",
                "value": [""],
                "title": "Team UUID",
                "description": "Unique identifier for the target team",
            },
            {
                "attr": {
                    "regex_pattern": None,
                    "input_type": "string[]",
                    "secret": False,
                    "required": True,
                },
                "key": "users",
                "placeholder": "Enter user emails",
                "value": [],
                "title": "User Emails",
                "description": "List of user emails to be added to the team",
            },
        ],
    },
    {
        "name": "invite_user",
        "title": "Invite User",
        "description": "Send an invitation to a user to join the platform",
        "params": [
            {
                "attr": {
                    "regex_pattern": {
                        "pattern": "^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\\.[a-zA-Z]{2,}$",
                        "message": "Invalid email format",
                    },
                    "input_type": "string",
                    "secret": False,
                    "required": True,
                },
                "key": "email",
                "placeholder": "Enter user email",
                "value": [""],
                "title": "User Email",
                "description": "Email address of the user to invite",
            },
            {
                "attr": {
                    "regex_pattern": None,
                    "input_type": "string",
                    "secret": False,
                    "required": False,
                },
                "key": "fullName",
                "placeholder": "Enter full name",
                "value": [""],
                "title": "Full Name",
                "description": "Full name of the user to invite",
            },
            {
                "attr": {
                    "regex_pattern": None,
                    "input_type": "string[]",
                    "secret": False,
                    "required": False,
                },
                "key": "teams",
                "placeholder": "Enter team IDs",
                "value": [],
                "title": "Teams",
                "description": "List of team IDs to assign the invitee to",
            },
            {
                "attr": {
                    "regex_pattern": None,
                    "input_type": "string",
                    "secret": False,
                    "required": False,
                },
                "options": [
                    {"value": "student", "title": "Student"},
                    {"value": "instructor", "title": "Instructor"},
                    {"value": "admin", "title": "Administrator"},
                ],
                "key": "cbRole",
                "placeholder": "Select user role",
                "value": ["student"],
                "title": "User Role",
                "description": "Role of the invited user",
            },
            {
                "attr": {
                    "regex_pattern": {
                        "pattern": "^[a-zA-Z0-9-]+$",
                        "message": "Invalid course ID format",
                    },
                    "input_type": "string",
                    "secret": False,
                    "required": False,
                },
                "key": "primaryCourseId",
                "placeholder": "Enter primary course ID",
                "value": [""],
                "title": "Primary Course ID",
                "description": "ID of the primary course (optional)",
            },
        ],
    },
    {
        "name": "list_teams",
        "title": "List Teams",
        "description": "Retrieve a list of teams in the organization",
        "params": [
            {
                "attr": {
                    "regex_pattern": {
                        "pattern": "^[0-9]+$",
                        "message": "Page must be a positive integer",
                    },
                    "input_type": "number",
                    "secret": False,
                    "required": False,
                },
                "key": "page",
                "placeholder": "Page number",
                "value": [1],
                "title": "Page Number",
                "description": "Page number for paginated results",
            },
            {
                "attr": {
                    "regex_pattern": {
                        "pattern": "^[0-9]+$",
                        "message": "Limit must be a positive integer",
                    },
                    "input_type": "number",
                    "secret": False,
                    "required": False,
                },
                "key": "limit",
                "placeholder": "Results per page",
                "value": [10],
                "title": "Results Limit",
                "description": "Number of results per page",
            },
        ],
    },
    {
        "name": "assign_course",
        "title": "Assign Course",
        "description": "Assign a course to a list of users",
        "params": [
            {
                "attr": {
                    "regex_pattern": {
                        "pattern": "^[a-zA-Z0-9-]+$",
                        "message": "Invalid course ID format",
                    },
                    "input_type": "string",
                    "secret": False,
                    "required": True,
                },
                "key": "course_id",
                "placeholder": "Enter course UUID",
                "value": [""],
                "title": "Course UUID",
                "description": "Unique identifier of the course for assignment",
            },
            {
                "attr": {
                    "regex_pattern": {
                        "pattern": "^[\\w\\.-]+@[\\w\\.-]+\\.\\w+$",
                        "message": "Invalid email format",
                    },
                    "input_type": "string",
                    "secret": False,
                    "required": True,
                },
                "key": "users",
                "placeholder": "Enter users email address",
                "value": [""],
                "title": "Users Emails",
                "description": "Email addresses of users to assign the course to",
            },
        ],
    },
    {
        "name": "unassign_course",
        "title": "Unassign Course",
        "description": "Unassign users from a course",
        "params": [
            {
                "attr": {
                    "regex_pattern": {
                        "pattern": "^[a-zA-Z0-9-]+$",
                        "message": "Invalid course ID format",
                    },
                    "input_type": "string",
                    "secret": False,
                    "required": True,
                },
                "key": "course_id",
                "placeholder": "Enter course UUID",
                "value": [""],
                "title": "Course UUID",
                "description": "Unique identifier of the course to be unassigned",
            },
            {
                "attr": {
                    "regex_pattern": {
                        "pattern": "^[\\w\\.-]+@[\\w\\.-]+\\.\\w+$",
                        "message": "Invalid email format",
                    },
                    "input_type": "string",
                    "secret": False,
                    "required": True,
                },
                "key": "users",
                "placeholder": "Enter users email address",
                "value": [""],
                "title": "Users Emails",
                "description": "Email addresses of users to unassign the course to",
            },
        ],
    },
]
