from fastapi import APIRouter, HTTPException, Request, Body
from src.plugin_configs import plugin_config
from .middlewares.config_manager import ConfigManager
from .controllers.method_controller import MethodExecutor
from .core.methods_list import methods_list
from .core.methods_configs import methods_configs
from .core.response_models import StandardResponse

router = APIRouter()
method_executor = MethodExecutor()


@router.get("/version")
async def get_version():
    """Return current version of the plugin"""
    return {**plugin_config}


@router.post("/version")
async def update_version(config: dict = Body(...)):
    """Update plugin configuration"""
    config_manager = ConfigManager()
    if config_manager.save_config(config):
        return {
            "status": "success",
            "message": "Configuration updated successfully",
            "data": config_manager.get_config(),
        }
    raise HTTPException(status_code=500, detail="Failed to update configuration")


@router.get("/methods", response_model=StandardResponse)
async def get_methods():
    """Return list of available methods"""
    return {
        "status": "success",
        "data": methods_list,
        "message": "Available methods retrieved successfully",
    }


@router.get("/method/{method_name}")
async def get_method_config(method_name: str):
    """Return configuration for specific method"""
    if not method_name:
        raise HTTPException(status_code=404, detail="Action not found")

    for method in methods_list:
        if method["method"] == method_name:
            method_config = next(
                (config for config in methods_configs if config["name"] == method_name),
                None,
            )
            return {
                "status": "success",
                "data": method_config,
                "message": f"Configuration for {method_name} retrieved successfully",
            }

    raise HTTPException(status_code=404, detail="Action not found")


@router.post("/method/{method_name}", response_model=StandardResponse)
async def execute_method(method_name: str, request: Request):
    """Execute a method based on its name"""
    try:
        data = await request.json() if await request.body() else {}
        result = await method_executor.execute(method_name, data)

        try:
            return {
                "status": "success" if result.get("success") else "error",
                "data": result,
                "message": (
                    f"Executed {method_name} successfully"
                    if result.get("success")
                    else "Execution failed"
                ),
            }
        except AttributeError:
            # Handle AttributeError
            return {
                "status": "success" if result else "error",
                "data": result,
                "message": (
                    f"Executed {method_name} successfully"
                    if result
                    else "Execution failed"
                ),
            }
    except ValueError:
        # Handle empty or invalid JSON body
        result = await method_executor.execute(method_name, {})
        print("\n Fetched Results : \n\n", result, "\n\n")
        return {
            "status": "success" if result.get("success") else "error",
            "data": result,
            "message": (
                f"Executed {method_name} successfully"
                if result.get("success")
                else "Execution failed"
            ),
        }
