# Load in PREFECT_API_KEY and PREFECT_API_URL
prefect profile inspect default > prefect_config.env

# Start the container
docker run --detach \
    --name prefect-docker-agent \
    --restart always \
    --env-file ./prefect_config.env \
    prefecthq/prefect:2-latest \
    prefect agent start -q default

# Kill the container and delete it
docker kill prefect-docker-agent
docker rm prefect-docker-agent