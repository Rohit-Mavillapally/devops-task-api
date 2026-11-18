
#!/bin/bash

echo "Checking application health..."

curl -fsS http://127.0.0.1:8001/health

echo ""
echo "Health check completed"
