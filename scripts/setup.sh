#!/usr/bin/env bash
set -e

echo "🔧 Setting up Python services..."

SERVICES=(
  "airflow"
  "scraper-service"
  "trainer-service"
  "prediction-service"
  "ui-service"
)

for svc in "${SERVICES[@]}"; do
  echo ""
  echo "Setting up $svc"

  if [ ! -d "$svc" ]; then
    echo "ERROR: Folder $svc does not exist"
    exit 1
  fi

  cd "$svc"

  if [ ! -f Pipfile ]; then
    echo "ERROR: No Pipfile found in $svc"
    exit 1
  fi

  echo "Installing dependencies..."
  pipenv install --dev

  VENV=$(pipenv --venv)
  echo "Virtual environment created: $VENV"

  cd ..
done

echo ""
echo "All service environments are ready!"
