import docker
import logging
import argparse

# Configure logging
logging.basicConfig(
    filename='docker_health_check.log', 
    level=logging.INFO, 
    format='%(asctime)s - %(levelname)s - %(message)s'
)

def restart_unhealthy_containers(dry_run=False):
    # Initialize the Docker client
    client = docker.from_env()

    try:
        # Get all running containers
        containers = client.containers.list()

        if not containers:
            print("No running containers found.")
            logging.info("No running containers found.")
            return

        # Loop through all containers
        for container in containers:
            # Inspect the container to check its health status
            container_info = container.attrs
            if 'State' in container_info and 'Health' in container_info['State']:
                health_status = container_info['State']['Health']['Status']
                if health_status == 'unhealthy':
                    print(f"Unhealthy container found: {container.name}")
                    logging.info(f"Unhealthy container found: {container.name}")

                    if not dry_run:
                        print(f"Restarting unhealthy container: {container.name}")
                        try:
                            container.restart()
                            print(f"Successfully restarted container: {container.name}")
                            logging.info(f"Successfully restarted container: {container.name}")
                        except Exception as e:
                            print(f"Failed to restart container {container.name}: {e}")
                            logging.error(f"Failed to restart container {container.name}: {e}")
                    else:
                        print(f"[Dry Run] Would restart container: {container.name}")
                        logging.info(f"[Dry Run] Would restart container: {container.name}")
                else:
                    print(f"Container {container.name} is healthy.")
                    logging.info(f"Container {container.name} is healthy.")
            else:
                print(f"Container {container.name} does not have a health check configured.")
                logging.info(f"Container {container.name} does not have a health check configured.")

    except docker.errors.DockerException as e:
        print(f"An error occurred interacting with Docker: {e}")
        logging.error(f"An error occurred interacting with Docker: {e}")

if __name__ == "__main__":
    # Argument parser for handling dry-run option
    parser = argparse.ArgumentParser(description="Check and restart unhealthy Docker containers.")
    parser.add_argument('--dry-run', action='store_true', help="Show which containers are unhealthy without restarting them.")
    
    args = parser.parse_args()

    # Call the function with dry_run flag
    restart_unhealthy_containers(dry_run=args.dry_run)
