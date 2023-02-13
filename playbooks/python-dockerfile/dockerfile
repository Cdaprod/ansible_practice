name: Inventory

on:
  push:
    branches:
      - main

jobs:
  run_inventory:
    runs-on: ubuntu-latest

    steps:
    - name: Checkout code
      uses: actions/checkout@v2

    - name: Build Docker image
      run: docker build -t image-with-inventory-script .

    - name: Run inventory script
      run: docker run image-with-inventory-script
