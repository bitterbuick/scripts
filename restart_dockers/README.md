# Docker Health Check and Restart Script

This Python script checks all running Docker containers for their health status and restarts any containers that are marked as "unhealthy." It also supports a `--dry-run` option to display unhealthy containers without performing any restarts. All actions and health statuses are logged for auditing purposes.

## Features

- Check the health of all running Docker containers.
- Automatically restart containers that are marked as "unhealthy."
- Supports a `--dry-run` mode to display unhealthy containers without restarting them.
- Logs all actions (container health statuses and restart attempts) to a log file.

## Requirements

- Python 3.x
- Docker SDK for Python (`docker-py`)

## Installation

1. Clone or download the script to your local environment.
2. Install the required Python dependencies using `pip`:

    ```bash
    pip install docker
    ```

3. Ensure that Docker is installed and running on your system.

## Usage

### Check and Restart Unhealthy Containers

By default, the script will check the health status of all running containers and restart any that are unhealthy. All actions will be logged to `docker_health_check.log`.

To run the script:

    ```bash
    python script_name.py
    ```

### Dry Run Mode

To run the script in "dry run" mode, where it will display which containers are unhealthy but will **not** restart them, use the `--dry-run` option:

    ```bash
    python script_name.py --dry-run
    ```

### Logging

All container health statuses, restart attempts, and any errors will be logged in the `docker_health_check.log` file in the same directory as the script.

## Example Output

### Without Dry Run

    ```bash
    Unhealthy container found: container_1
    Restarting unhealthy container: container_1
    Successfully restarted container: container_1
    Container container_2 is healthy.
    ```

### With Dry Run

    ```bash
    Unhealthy container found: container_1
    [Dry Run] Would restart container: container_1
    Container container_2 is healthy.
    ```

### Log File Example

The script logs all events to `docker_health_check.log`:

    ```
    2024-09-07 12:30:45,102 - INFO - Unhealthy container found: container_1
    2024-09-07 12:30:45,204 - INFO - Successfully restarted container: container_1
    2024-09-07 12:31:12,345 - INFO - Container container_2 is healthy.
    ```

## Notes

- Containers must have health checks configured for the script to determine their health status. If a container does not have a health check, the script will log that it lacks a health check.
- The script interacts with the Docker daemon. Ensure that your user has the necessary permissions to interact with Docker, or use `sudo` if required.

## License

This project is licensed under the MIT License. See the LICENSE file for details.
