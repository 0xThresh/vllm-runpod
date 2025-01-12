import pulumi
import runpod

# Get Pulumi config values
config = pulumi.Config()
model_name = config.require("model:name")

runpod_endpoint = runpod.Endpoint(f"vllm-endpoint-{model_name}",
    name=f"vllm-endpoint-{model_name}",
    gpu_ids="NVIDIA RTX A4000,NVIDIA RTX A4500"
)

pulumi.export("endpoint_id", runpod_endpoint.id)
