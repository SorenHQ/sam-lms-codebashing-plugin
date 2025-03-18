import json
import os
from typing import Dict, Any
from src.plugin_configs import plugin_config


class ConfigManager:
    _instance = None
    _config_file = "plugin_runtime_config.json"

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(ConfigManager, cls).__new__(cls)
        return cls._instance

    def __init__(self):
        self.config = self._load_config()

    def _load_config(self) -> Dict[str, Any]:
        try:
            if os.path.exists(self._config_file):
                with open(self._config_file, "r") as f:
                    return json.load(f)
        except Exception:
            pass
        return plugin_config.copy()

    def save_config(self, new_config: Dict[str, Any]) -> bool:
        try:
            with open(self._config_file, "w") as f:
                json.dump(new_config, f, indent=2)
            self.config = new_config
            return True
        except Exception:
            return False

    def get_api_credentials(self) -> Dict[str, str]:
        try:
            global_configs = next(
                (
                    cfg
                    for cfg in self.config["init_config"]
                    if cfg["name"] == "global_configs"
                ),
                None,
            )
            if global_configs:
                params = {
                    param["key"]: param["value"][0] if param["value"] else ""
                    for param in global_configs["params"]
                }
                return {
                    "X-Api-Key": params.get("x_api_key", ""),
                    "Authorization": f"Bearer {params.get('token', '')}",
                }
        except Exception:
            pass
        return {}

    def get_config(self) -> Dict[str, Any]:
        return self.config
