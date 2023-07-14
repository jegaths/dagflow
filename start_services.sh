#!/bin/bash

# Start pyroscope
helm install pyroscope pyroscope-io/pyroscope

# Start the services
echo "Starting the services..."


# Define the manifest file
MANIFEST_FILE="custom-manifest.yml"

# Delete existing resources
echo "Deleting existing resources..."
kubectl delete -f $MANIFEST_FILE

# Apply the new manifest
echo "Applying new resources..."
kubectl apply -f $MANIFEST_FILE

# Wait for the resources to be ready
echo "Waiting for resources to be ready..."
sleep 5

# Port-forward the services
echo "Starting port forwarding..."
kubectl port-forward svc/pyroscope 4040:4040 &
kubectl port-forward svc/dagflow-ui-service 3000:80 &
kubectl port-forward svc/mongodb-service 27017:27017 &
kubectl port-forward svc/app-service 8000:8000 &

# Wait for port-forwarding processes
wait
