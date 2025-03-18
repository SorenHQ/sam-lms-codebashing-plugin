"""
The `plugin_config` dictionary defines the configuration for a plugin named "codebashing-plugin". It includes the following settings:

- `name`: The name of the plugin, "codebashing-plugin".
- `author`: The author of the plugin, "Sam Soofy".
- `version`: The version of the plugin, "v1.0.1".
- `proto`: The protocol version, "v0.0.1".
- `schema_version`: The schema version, "srn-schema-v1".
- `init_config`: A list of configuration parameters, including:
    - `name`: The name of the configuration, "global_configs".
    - `title`: The title of the configuration, "CodeBashing settings".
    - `description`: The description of the configuration, "Required parameters".
    - `params`: A list of configuration parameters, including:
        - `token`: The API token required to use the CodeBashing service. This is a required string parameter.
        - `x_api_key`: The X-API-Key required to use the CodeBashing service. This is a required string parameter.
"""

plugin_config = {
    "name": "LMS CodeBashing",
    "author": "Sam Soofy",
    "version": "v1.0.1",
    "proto": "v0.0.1",
    "schema_version": "srn-schema-v1",
    "init_config": [
        {
            "name": "global_configs",
            "title": "CodeBashing settings",
            "description": "Required parameters",
            "params": [
                {
                    "attr": {
                        "regex_pattern": {
                            "pattern": "^[pattern]$",
                            "message": "invalid value",
                        },
                        "input_type": "string",
                        "secret": False,
                        "required": True,
                    },
                    "options": [{"value": "", "title": ""}],
                    "key": "token",
                    "placeholder": "e.g. eylhdfgliolk34u598t5huj9ofg5uh",
                    "value": [],
                    "title": "Please enter X-Api-Key",
                    "description": "Get the token and key from https://codebashing.com/ and paste the Bearer Authorization Token here",
                },
                {
                    "attr": {
                        "regex_pattern": {
                            "pattern": "^[pattern]$",
                            "message": "invalid value",
                        },
                        "input_type": "string",
                        "secret": False,
                        "required": True,
                    },
                    "options": [{"value": "", "title": ""}],
                    "key": "x_api_key",
                    "placeholder": "e.g. iwe4uryf9483fho34y0f383",
                    "value": [],
                    "title": "Please enter X-Api-Key",
                    "description": "Get the token and key from https://codebashing.com/ and paste the X-Api-Key here",
                },
            ],
        }
    ],
}
